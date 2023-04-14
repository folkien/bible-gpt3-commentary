from dataclasses import asdict
from datetime import date
import json
import logging
import sys
from helpers.Ayrshare import post_to_social_media
from helpers.CommentaryGPT import get_gpt_commentary, get_gpt_test
from helpers.Database import PostDatabase
from helpers.LoggingSetup import loggingSetup
from helpers.ReadingsFetcherDeon import get_bible_reading
from models.Post import Post
from views.ViewPost import ViewPost


def SetupLogging():
    ''' Setup logging during application.'''
    loggingSetup(console_log_output='stdout', console_log_level='debug', console_log_color=True,
                 logfile_file='trace.log', logfile_log_level='debug', logfile_log_color=False,
                 log_line_template='%(color_on)s %(asctime)s [%(threadName)s] [%(levelname)-8s] %(message)s%(color_off)s')


def PostCreate(database: PostDatabase):
    ''' Create post.'''
    # Get daily readings from website
    readings = get_bible_reading()
    if (readings is None):
        logging.fatal('Readings : Cannot get readings!')
        sys.exit(-1)

    # Save temporary object (developer debuging)
    json.dump(asdict(readings), open('temp/readings.json', 'w'),
              indent=4, ensure_ascii=False)

    # Comment only evangelium
    commentary = get_gpt_commentary(readings.evangelium)
    if (commentary is None):
        logging.fatal('Commentary : Cannot get commentary!')
        sys.exit(-1)

    # Save temporary object (developer debuging)
    json.dump(asdict(commentary), open('temp/commentary.json', 'w'),
              indent=4, ensure_ascii=False)

    # Create media post
    post = Post(readings=readings, commentary=commentary)
    # Database : Save created post
    database.AddCreated(post)

    return post


def PostUpload(database: PostDatabase, post: Post):
    ''' Upload post. '''
    # Create post text/view
    postText = ViewPost.View(post)

    # Save media post view as temporary object
    with open('temp/post.txt', 'w') as fileObject:
        fileObject.write(postText)

    result = post_to_social_media(postText)

    # Database : Save posted post
    if (result):
        database.AddPosted(post)


if __name__ == '__main__':
    SetupLogging()
    database = PostDatabase()

    # Check : if post exists then read it
    post = database.GetPost(date.today())
    # Create post if not exists
    if (not database.IsCreated(date.today())):
        post = PostCreate(database)

    # Check : Post is posted, do nothing.
    if (database.IsPosted(date.today())):
        logging.info('Post is already posted!')
        sys.exit(0)

    # Upload post.
    PostUpload(database, post)
