![title](doc/title.png)

# Bible readings GPT commentary!

A OpenAI GPT powered commentary to the daily readings of Bible.

* Polish version commentary website with all publications https://www.facebook.com/gptczytania

Example published commentary

```text
# Tytuł : Ziarno pszenicy / 24 April, III Tydzień Wielkanocny, Rok A, I
    '''Jeżeli ziarno pszenicy wpadłszy w ziemię nie obumrze, zostanie tylko samo, ale jeżeli obumrze, przynosi plon obfity. (Jezus)'''
# Streszczenie
Miejsce akcji :
Osoby : Jezus
1. Jeśli chcemy osiągnąć coś wartościowego, musimy być gotowi zaryzykować i poświęcić coś z siebie
2. Miłość do siebie może prowadzić do utraty życia wiecznego
3. Służba Jezusowi jest kluczem do uzyskania uznania Ojca
# Ewangelia na dziś (pobrano ze strony https://ayr.app/l/2UPn)
    Ewangelia(J 12, 24-26) Jezus powiedział do swoich uczniów: «Zaprawdę, zaprawdę, powiadam wam: Jeżeli ziarno pszenicy wpadłszy w ziemię nie obumrze, zostanie tylko samo, ale jeżeli obumrze, przynosi plon obfity.Ten, kto miłuje swoje życie, traci je, a kto nienawidzi swego życia na tym świecie, zachowa je na życie wieczne.A kto by chciał Mi służyć, niech idzie za Mną, a gdzie Ja jestem, tam będzie i mój sługa. A jeśli ktoś Mi służy, uczci go mój Ojciec».
# Komentarz
    Słowa Jezusa zachęcają nas do poświęcenia i służby, aby osiągnąć życie wieczne. Ziarno pszenicy, które umiera, aby przynieść obfity plon, jest metaforą naszej gotowości do poświęcenia i ryzyka w służbie dla Boga.
# Wnioski
 -  Musimy być gotowi poświęcić coś z siebie, aby osiągnąć coś wartościowego
 -  Miłość do siebie może nas odciąć od życia wiecznego
 -  Służba Jezusowi jest kluczem do uzyskania uznania Ojca i osiągnięcia życia wiecznego
# Zapamiętaj
    Słowa Jezusa zachęcają nas do poświęcenia i służby, aby osiągnąć życie wieczne.
#ewangelia #wiara #komentarz #ChatGPT #gpt3 #ai #bible #biblia #komentarz
------------------------
Czytania z dnia pobrano ze strony https://deon.pl/czytania
Komentarz wygenerowano przy użyciu modelu gpt-3.5-turbo.
Uwaga! Poza tekstem czytań, pozostały tekst został wygenerowany automatycznie przy użyciu modelu GPT firmy OpenAI. Komentarz nie jest w żaden sposób oficjalną wypowiedzią Kościoła Katolickiego, ani komentarzem biblisty, ani nie posiada żadnego autorytetu teologicznego oraz nie jest wiarygodnym źródłem danych/cytatów. Jest to jedynie demo technologiczne próbujące pokazać możliwości sztucznej inteligencji. Autorzy projektu nie ponoszą żadnej odpowiedzialności za treść komentarza oraz za ewentualne błędy w nim zawarte.
Link do repozytorium projektu oraz wiecęi informacji w opisie strony. Projekt Bible-Gpt3-Commentary jest projektem nonprofit open source. Zapraszam do współpracy! via #Ayrshare

```


# Installation

1. Install requirements

```bash
pip install -r requirements.txt
```

2. Use env template to create your own env file.

```bash
cp .env.template .env
```

3. Add OpenAI API key to the `.env` file.

# Usage - Run the script

```bash
source .env
python main.py
```

# How it works?

1. The script will fetch the daily readings from [Polish] Deon.pl
2. Text of readings will be passed to OpenAI GPT API
3. The response will be saved to the file
4. The file will be uploaded to the Facebook site.

# How to contribute?

Fork the repo and create a pull request.
