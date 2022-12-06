# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
#                                                                               -
#  Python dual-logging setup (console and log file),                            -
#  supporting different log levels and colorized output                         -
#                                                                               -
#  Created by Fonic <https://github.com/fonic>                                  -
#  Date: 04/05/20                                                               -
#                                                                               -
#  Based on:                                                                    -
#  https://stackoverflow.com/a/13733863/1976617                                 -
#  https://uran198.github.io/en/python/2016/07/12/colorful-python-logging.html  -
#  https://en.wikipedia.org/wiki/ANSI_escape_code#Colors                        -
#                                                                               -
# -------------------------------------------------------------------------------

# Imports
import sys
import logging
import logging.handlers

log_template1 = '%(color_on)s %(asctime)s [%(threadName)s] [%(levelname)-8s] %(message)s%(color_off)s'


class LogFormatter(logging.Formatter):
    ''' Logging formatter supporting colored output'''

    COLOR_CODES = {
        logging.CRITICAL: '\033[1;35m',  # bright/bold magenta
        logging.ERROR:    '\033[1;31m',  # bright/bold red
        logging.WARNING:  '\033[1;33m',  # bright/bold yellow
        logging.INFO:     '\033[0;37m',  # white / light gray
        logging.DEBUG:    '\033[1;30m'  # bright/bold black / dark gray
    }

    RESET_CODE = '\033[0m'

    def __init__(self, color, *args, **kwargs):
        super(LogFormatter, self).__init__(*args, **kwargs)
        self.color = color

    def format(self, record, *args, **kwargs):
        if (self.color is True and record.levelno in self.COLOR_CODES):
            record.color_on = self.COLOR_CODES[record.levelno]
            record.color_off = self.RESET_CODE
        else:
            record.color_on = ''
            record.color_off = ''
        return super(LogFormatter, self).format(record, *args, **kwargs)


def AddFileLogger(logfile_file, logfile_log_level='warning', logfile_log_color=False, log_line_template=log_template1, filemode='w'):
    ''' Method to add new logger which is a file logger.'''
    logger = logging.getLogger()

    # Create log file handler
    try:
        logfile_handler = logging.handlers.RotatingFileHandler(
            logfile_file, mode=filemode, maxBytes=25*1024*1024, backupCount=2)
    except Exception as exception:
        print('Failed to set up log file: %s' % str(exception))
        return None

    # Set log file log level
    try:
        # only accepts uppercase level names
        logfile_handler.setLevel(logfile_log_level.upper())
    except:
        print("Failed to set log file log level: invalid level: '%s'" %
              logfile_log_level)
        return None

    # Create and set formatter, add log file handler to logger
    logfile_formatter = LogFormatter(
        fmt=log_line_template, color=logfile_log_color)
    logfile_handler.setFormatter(logfile_formatter)
    logger.addHandler(logfile_handler)

    return logfile_handler


def AddConsoleLogger(console_log_output, console_log_level='warning', console_log_color=True, log_line_template=log_template1):
    ''' Method to add new console logger.'''
    logger = logging.getLogger()

    # Create console handler
    console_log_output = console_log_output.lower()
    if (console_log_output == 'stdout'):
        console_log_output = sys.stdout
    elif (console_log_output == 'stderr'):
        console_log_output = sys.stderr
    else:
        print("Failed to set console output: invalid output: '%s'" %
              console_log_output)
        return None
    console_handler = logging.StreamHandler(console_log_output)

    # Set console log level
    try:
        # only accepts uppercase level names
        console_handler.setLevel(console_log_level.upper())
    except:
        print("Failed to set console log level: invalid level: '%s'" %
              console_log_level)
        return None

    # Create and set formatter, add console handler to logger
    console_formatter = LogFormatter(
        fmt=log_line_template, color=console_log_color)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    return console_handler


def loggingSetup(console_log_output, console_log_level, console_log_color, logfile_file, logfile_log_level, logfile_log_color, log_line_template):

    # Create logger
    # For simplicity, we use the root logger, i.e. call 'logging.getLogger()'
    # without name argument. This way we can simply use module methods for
    # for logging throughout the script. An alternative would be exporting
    # the logger, i.e. 'global logger; logger = logging.getLogger("<name>")'
    logger = logging.getLogger()

    # Set global log level to 'debug' (required for handler levels to work)
    logger.setLevel(logging.DEBUG)

    # Create console handler
    console_log_output = console_log_output.lower()
    if (console_log_output == 'stdout'):
        console_log_output = sys.stdout
    elif (console_log_output == 'stderr'):
        console_log_output = sys.stderr
    else:
        print("Failed to set console output: invalid output: '%s'" %
              console_log_output)
        return False
    console_handler = logging.StreamHandler(console_log_output)

    # Set console log level
    try:
        # only accepts uppercase level names
        console_handler.setLevel(console_log_level.upper())
    except:
        print("Failed to set console log level: invalid level: '%s'" %
              console_log_level)
        return False

    # Create and set formatter, add console handler to logger
    console_formatter = LogFormatter(
        fmt=log_line_template, color=console_log_color)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Create log file handler
    try:
        logfile_handler = logging.handlers.RotatingFileHandler(
            logfile_file, mode='w', maxBytes=25*1024*1024, backupCount=2)
    except Exception as exception:
        print('Failed to set up log file: %s' % str(exception))
        return False

    # Set log file log level
    try:
        # only accepts uppercase level names
        logfile_handler.setLevel(logfile_log_level.upper())
    except:
        print("Failed to set log file log level: invalid level: '%s'" %
              logfile_log_level)
        return False

    # Create and set formatter, add log file handler to logger
    logfile_formatter = LogFormatter(
        fmt=log_line_template, color=logfile_log_color)
    logfile_handler.setFormatter(logfile_formatter)
    logger.addHandler(logfile_handler)

    # Success
    logging.debug('Logging enabled!')
    return True
    return True
