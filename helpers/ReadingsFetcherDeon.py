import requests
from bs4 import BeautifulSoup
import logging

from models.Readings import Readings


def get_bible_reading():
    ''' Pobiera czytanie z deon.pl'''
    headers = {
        'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    url = 'https://deon.pl/czytania'

    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        logging.error(f'Problem z połączeniem: {e}')
        return None

    if response.status_code != 200:
        logging.error(
            f'Nie można pobrać strony, kod odpowiedzi: {response.status_code}')
        return None

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        logging.error(f'Problem z analizą składni HTML: {e}')
        return None

    # Pobierz div z czytaniami
    readings_div = soup.find('div', class_='readings-module')
    if readings_div is None:
        logging.error('Nie znaleziono diva z czytaniami')
        return None

    # Found info
    info_div = readings_div.find('div', class_='info')
    if info_div is None:
        logging.warning('Info div not found!')

    # Found content
    content_div = readings_div.find('div', class_='element-content')
    if content_div is None:
        logging.error('Content div not found!')
        return None

    # Get all H4
    h4s = content_div.find_all('h4')
    # Get all paragraphs
    paragraphs = content_div.find_all('p')
    # Merge title with paragrahps as text only
    readings = [f'{h4.text.strip()} {p.text.strip()}' for h4,
                p in zip(h4s, paragraphs)]

    # Check : 4 readings or more
    if (len(readings) < 4):
        logging.error('Invalid readings amount!')
        return None

    # First reading is first element,
    first_reading = readings[0]
    # Psalm is second element
    psalm = readings[1]
    # Second reading is third element (only if 5 readings)
    second_reading = None
    if (len(readings) == 5):
        second_reading = readings[2]
    # Gospel is fourth element
    gospel = readings[-2]
    # Last is evangelium
    evangelium = readings[-1]

    return Readings(first_reading, psalm, second_reading, gospel, evangelium)


if __name__ == '__main__':
    bible_reading = get_bible_reading()
    if bible_reading:
        print('Czytanie pobrane pomyślnie.')
        print(bible_reading)
    else:
        print('Nie udało się pobrać czytania.')
