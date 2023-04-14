
from dataclasses import asdict
import ast
import logging
import os
import openai
from models.Commentary import Commentary

# Get Open AI key from env
openai.api_key = os.environ.get('OPENAI_API_KEY', None)
if (openai.api_key is None):
    raise ValueError('Open AI key not found in env.')


def get_gpt_test(text: str, model: str = 'gpt-3.5-turbo', temperature: float = 0.7):
    # Chat GPT messages content
    messages = [
        {'role': 'system', 'content': 'Jesteś katolickim teologiem, biblistą, który komentuje biblię. Szuka głębi w tekście, alegorii, duchowych odniesień.'},
        {'role': 'user', 'content': f'Napisz komentarz do tekstu : ' +
                                    f'Albowiem tak Bóg umiłościł świat, że dał jedynego Syna swojego, aby każdy, kto w Niego wierzy, nie zginął, lecz miał wieczne życie.'},
    ]

    # Send request to Open AI
    response = openai.ChatCompletion.create(model=model,
                                            messages=messages,
                                            temperature=temperature)

    print(response)
    return response


def get_gpt_commentary(text: str, model: str = 'gpt-3.5-turbo', temperature: float = 0.5):
    # Chat GPT messages content
    messages = [
        {'role': 'system', 'content': 'Jesteś kreatywnym, katolickim teologiem i biblistą. Szukasz duchowości, serca, poruszenia, charyzmatów, alegorii, drugiego znaczenia, historii ludzi i postaci. Tłumaczysz pisma.'},
        {'role': 'user', 'content': f'Odpowiedz w formie jsona gdzie pola to :\n' +
                                    f'- title : kreatywny tytuł nie wprost,\n' +
                                    f'- quote : twój pasujący cytat świętej osoby i nazwa autora,\n' +
                                    f'- points : 3 najwazniejsze myśli z czytania,\n' +
                                    f'- comment: akapit z twoim komentarzem,\n' +
                                    f'- summary: niewprost, najważniejsze zdanie podsumowujące.\n' +
                                    f'Skomentuj czytanie: ${text}'},
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
