from helpers.CommentaryGPT import get_gpt4_commentary
from helpers.LoggingSetup import loggingSetup
from helpers.ReadingsFetcherDeon import get_bible_reading


def SetupLogging():
    ''' Setup logging during application.'''
    loggingSetup(console_log_output='stdout', console_log_level='debug', console_log_color=True,
                 logfile_file='trace.log', logfile_log_level='debug', logfile_log_color=False,
                 log_line_template='%(color_on)s %(asctime)s [%(threadName)s] [%(levelname)-8s] %(message)s%(color_off)s')


SetupLogging()

text = get_bible_reading()
print(text)

commentary = get_gpt4_commentary(text)
print(commentary)
