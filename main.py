import logging
import os
import openai

# Open AI prompt message creation
header = f'Napisz komentarz do poniższego fragmentu Słowa Bożego. Dodaj do komentarza, 2 lub 3 cytaty świętych katolickich. Komentarz napisz w formie wstęp, rozwinięcie, zakończenie. Fragment Słowa Bożego :'
bibletext = f'Trwajcie cierpliwie, bracia, aż do przyjścia Pana. Oto rolnik czeka wytrwale na cenny plon ziemi, dopóki nie spadnie deszcz wczesny i późny. Tak i wy bądźcie cierpliwi i umacniajcie serca wasze, bo przyjście Pana jest już bliskie. Nie uskarżajcie się, bracia, jeden na drugiego, byście nie popadli pod sąd. Oto sędzia stoi przed drzwiami. Za przykład wytrwałości i cierpliwości weźcie, bracia, proroków, którzy przemawiali w imię Pańskie. (Jk 5,7-10)'
message = f'{header}{bibletext}'

# Get Open AI key from env
openai.api_key = os.getenv('OPENAI_API_KEY')
# Get open API key from file
if (os.path.exists('openai.key')):
    with open('openai.key', 'r') as f:
        openai.api_key = f.read()

# Call Open AI to handle response.
response = openai.Completion.create(
    model='text-davinci-003',
    prompt=message,
    temperature=0,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=['\n']
)

# Save response
with open('response.txt', 'w') as f:
    f.write(response)
