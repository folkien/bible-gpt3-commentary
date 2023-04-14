
import logging
import os
import openai

# Get Open AI key from env
openai.api_key = os.environ.get('OPENAI_API_KEY', None)
# Get open API key from file
if (openai.api_key is None) and (os.path.exists('openai.key')):
    logging.debug('(OpenAI) Reading key from file.')
    with open('openai.key', 'r') as f:
        openai.api_key = f.read().strip()


def get_gpt4_commentary(text, engine='gpt-4', temperature=0.7):
    prompt = (f'{text}\n\nKomentarz do czytania:\n\n'
              '3 najważniejsze myśli z czytania:\n\n'
              'Cytat świętego Kościoła Katolickiego:\n\n'
              'Najważniejsza myśl czytania:')
    response = openai.Completion.create(engine=engine,
                                        prompt=prompt,
                                        max_tokens=200,
                                        n=1,
                                        stop=None,
                                        temperature=temperature)
    return response.choices[0].text.strip()


if __name__ == '__main__':
    text = 'Tak bowiem Bóg umiłował świat, że Syna swego Jednorodzonego dał, aby każdy, kto w Niego wierzy, nie zginął, ale miał życie wieczne.(J3, 16)'
    print(get_gpt4_commentary(text))
