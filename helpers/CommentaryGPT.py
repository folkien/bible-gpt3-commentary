
import logging
import os
import openai

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
        {'role': 'user', 'content': f'Napisz komentarz do poniższego tekstu czytania w formacie : ' +
                                    f'Tytuł komentarza, cytat świętego kościoła, 3 najwazniejsze myśli z czytania, ' +
                                    f'akapit z komentarzem, myśl podsumowująca. Oto tekst : ${text}'},
    ]

    # Debugging
    logging.debug('Messagees list : ')
#    logging.debug(messages)
    logging.debug('Used open ai key %s', openai.api_key)

    # Send request to Open AI
    response = openai.ChatCompletion.create(model=model,
                                            messages=messages,
                                            temperature=temperature)
    return response


if __name__ == '__main__':
    text = 'Tak bowiem Bóg umiłował świat, że Syna swego Jednorodzonego dał, aby każdy, kto w Niego wierzy, nie zginął, ale miał życie wieczne.(J3, 16)'
    print(get_gpt_commentary(text))
