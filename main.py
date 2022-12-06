import logging
import os
import openai
import sys
from helpers.LoggingSetup import loggingSetup

# @TODO Get Ewangelia from https://deon.pl/czytania


def SetupLogging():
    ''' Setup logging during application.'''
    loggingSetup(console_log_output='stdout', console_log_level='debug', console_log_color=True,
                 logfile_file='trace.log', logfile_log_level='debug', logfile_log_color=False,
                 log_line_template='%(color_on)s %(asctime)s [%(threadName)s] [%(levelname)-8s] %(message)s%(color_off)s')


SetupLogging()

# Open AI prompt message creation
header = f'Napisz w 3 akapitach, komentarz do poniższego fragmentu Słowa Bożego. Użyj w tekście 3 cytatów świętych Kościoła. Fragment:'
bibletext = f'Tak bowiem Bóg umiłował świat, że Syna swego Jednorodzonego dał, aby każdy, kto w Niego wierzy, nie zginął, ale miał życie wieczne.(J3, 16)'
message = f'In:{header}{bibletext}\n Out:'

# Get Open AI key from env
openai.api_key = os.environ.get('OPENAI_API_KEY', None)
# Get open API key from file
if (openai.api_key is None) and (os.path.exists('openai.key')):
    logging.debug('(OpenAI) Reading key from file.')
    with open('openai.key', 'r') as f:
        openai.api_key = f.read().strip()

# Call Open AI to handle response.
response = openai.Completion.create(
    model='text-davinci-003',
    prompt=message,
    temperature=0,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=['In:', 'Out:']
)

# Response failed
if (response is None):
    logging.fatal('(OpenAI) No response!')
    sys.exit(-1)

# Extract response text
resultText = ''
for choice in response.choices:
    resultText += choice.text

# Missing response text
if len(resultText) == 0:
    logging.error('(OpenAI) Empty response!')
    sys.exit(-1)

# Save results
with open('response.txt', 'w') as f:
    f.write(resultText)
