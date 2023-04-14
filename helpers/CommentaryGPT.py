
from dataclasses import asdict
import ast
import logging
import os
import openai
from helpers.Commentary import Commentary

# Get Open AI key from env
openai.api_key = os.environ.get('OPENAI_API_KEY', None)
if (openai.api_key is None):
    raise ValueError('Open AI key not found in env.')


def get_gpt_test(text: str, model: str = 'gpt-3.5-turbo', temperature: float = 0.7):
    # Chat GPT messages content
    messages = [
        {'role': 'system', 'content': 'Komentujesz czytania biblijne. Jesteś katolickim teologiem i biblistą.'},
        {'role': 'user', 'content': f'Napisz komentarz do tekstu : ' +
                                    f'Albowiem tak Bóg umiłościł świat, że dał jedynego Syna swojego, aby każdy, kto w Niego wierzy, nie zginął, lecz miał wieczne życie.'},
    ]

    # Send request to Open AI
    response = openai.ChatCompletion.create(model=model,
                                            messages=messages,
                                            temperature=temperature)

    print(response)
    return response


def get_gpt_commentary(text: str, model: str = 'gpt-3.5-turbo', temperature: float = 0.7):
    # Chat GPT messages content
    messages = [
        {'role': 'system', 'content': 'Komentujesz czytania biblijne. Jesteś katolickim teologiem i biblistą.'},
        {'role': 'user', 'content': f'Skomentuj tekst czytania jako json gdzie pola to (w nawiasie nazwa pola)  : ' +
                                    f'1.(title) Tytuł komentarza, 2.(quote) cytat świętego kościoła, 3. (points) Trzy najwazniejsze myśli z czytania, ' +
                                    f'4. (comment) akapit z komentarzem, 5. (summary) myśl podsumowująca.\n Oto czytanie: ${text}'},
    ]

    # Debugging
    logging.debug('Messagees list : ')
#    logging.debug(messages)
    logging.debug('Used open ai key %s', openai.api_key)

    # Send request to Open AI
    response = openai.ChatCompletion.create(model=model,
                                            messages=messages,
                                            temperature=temperature)

    # Check : Invalid response
    if (response is None) or ('choices' not in response) or (len(response['choices']) == 0):
        logging.error('Open AI response is invalid!')
        return None

    # Check : Message field exists
    if ('message' not in response['choices'][0]):
        logging.error('Open AI response has no message!')
        return None

    # Get first choice message.
    message = response['choices'][0]['message']

    # Convert response text '{}' to python dict.
    jsonCommentary = ast.literal_eval(message['content'])

    # Convert jsonCommentary to Commentary dataclass from json.
    commentary = Commentary(**jsonCommentary)

    return commentary


if __name__ == '__main__':
    text = u'Tak bowiem Bóg umiłował świat, że Syna swego Jednorodzonego dał, aby każdy, kto w Niego wierzy, nie zginął, ale miał życie wieczne.(J3, 16)'
    print(get_gpt_commentary(text))
