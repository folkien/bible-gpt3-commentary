import requests
from bs4 import BeautifulSoup
import logging

def get_bible_reading():
    headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}
    url = "https://deon.pl/czytania"

    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        logging.error(f"Problem z połączeniem: {e}")
        return None

    if response.status_code != 200:
        logging.error(f"Nie można pobrać strony, kod odpowiedzi: {response.status_code}")
        return None

    try:
        soup = BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        logging.error(f"Problem z analizą składni HTML: {e}")
        return None

    readings_div = soup.find("div", class_="readings-module")

    if readings_div is None:
        logging.error("Nie znaleziono diva z czytaniami")
        return None

    return readings_div.text.strip()

bible_reading = get_bible_reading()

if bible_reading:
    print("Czytanie pobrane pomyślnie.")
    print(bible_reading)
else:
    print("Nie udało się pobrać czytania.")
