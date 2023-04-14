from dataclasses import asdict
import json
import logging
import sys
from helpers.CommentaryGPT import get_gpt_commentary, get_gpt_test
from helpers.LoggingSetup import loggingSetup
from helpers.ReadingsFetcherDeon import get_bible_reading


def SetupLogging():
    ''' Setup logging during application.'''
    loggingSetup(console_log_output='stdout', console_log_level='debug', console_log_color=True,
                 logfile_file='trace.log', logfile_log_level='debug', logfile_log_color=False,
                 log_line_template='%(color_on)s %(asctime)s [%(threadName)s] [%(levelname)-8s] %(message)s%(color_off)s')


if __name__ == '__main__':
    SetupLogging()

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
