import argparse
from dataclasses import asdict, dataclass, is_dataclass
from datetime import date, datetime, timedelta
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

# App version.
__version__ = '1.0.0'


class EnhancedJSONEncoder(json.JSONEncoder):
    '''Enhanced JSON encoder with dataclasses support.'''

    def default(self, o):
        ''' Method to default dataclass.'''
        # Set : Json
        if (isinstance(o, (set))):
            return list(o)

        # Dataclass : Json.
        if is_dataclass(o):
            return asdict(o)

        # Datetime : Json
        if (isinstance(o, (datetime, date))):
            return o.isoformat()

        # Timedelta : Json
        if (isinstance(o, timedelta)):
            return str(o.total_seconds())

        return super().default(o)


def SetupLogging():
    ''' Setup logging during application.'''
    loggingSetup(console_log_output='stdout', console_log_level='debug', console_log_color=True,
                 logfile_file='trace.log', logfile_log_level='debug', logfile_log_color=False,
                 log_line_template='%(color_on)s %(asctime)s [%(threadName)s] [%(levelname)-8s] %(message)s%(color_off)s')


def SetupArgparse():
    ''' Setup argparse during application. '''
    parser = argparse.ArgumentParser(
        description='Script for creating and posting media post.')
    parser.add_argument('-f', '--force', action='store_true',
                        help='Force to create post again.')
    parser.add_argument('-np', '--nopost', action='store_true',
                        help='No posting on social media.')
    parser.add_argument('-ve', '--verbose', action='store_true',
                        help='Verbose operating.')
    parser.add_argument('-v', '--version', action='version',
                        version=f'{__version__}', help='Show version.')
    return parser.parse_args()


def PostCreate(database: PostDatabase):
    ''' Create post.'''
    # Get daily readings from website
    readings = get_bible_reading()
    if (readings is None):
        logging.fatal('Readings : Cannot get readings!')
        sys.exit(-1)

    # Save temporary object (developer debuging)
    json.dump(asdict(readings), open('temp/readings.json', 'w'),
              indent=4, ensure_ascii=False, cls=EnhancedJSONEncoder)

    # Comment only evangelium
    commentary = get_gpt_commentary(readings)
    if (commentary is None):
        logging.fatal('Commentary : Cannot get commentary!')
        sys.exit(-1)

    # Save temporary object (developer debuging)
    json.dump(asdict(commentary), open('temp/commentary.json', 'w'),
              indent=4, ensure_ascii=False, cls=EnhancedJSONEncoder)

    # Create media post
    post = Post(readings=readings, commentary=commentary)
    # Database : Save created post
    database.AddCreated(post)

    return post


def PostView(post: Post) -> str:
    ''' Upload post. '''
    # Create post text/view
    postText = ViewPost.View(post)

    # Save media post view as temporary object
    with open('temp/post.txt', 'w') as fileObject:
        fileObject.write(postText)

    return postText


def PostUpload(database: PostDatabase, postText: str):
    ''' Upload post. '''
    result = post_to_social_media(postText)

    # Database : Save posted post
    if (result):
        database.AddPosted(post)

    return result


if __name__ == '__main__':
    SetupLogging()
    args = SetupArgparse()
    database = PostDatabase()

    # Check : if post exists then read it
    post = database.GetPost(date.today())
    # Create post if not exists
    if (args.force) or (not database.IsCreated(date.today())):
        post = PostCreate(database)

    # Create post View/text
    postText = PostView(post)

    # Show post if verbose or nopost.
    if (args.nopost) or (args.verbose):
        logging.info(f'\n{postText}')

    # Check : Post is posted, do nothing.
    if (args.nopost) or (database.IsPosted(date.today())):
        logging.warning('Post is already posted!')
        sys.exit(0)

    # Upload post.
    PostUpload(database, postText)
