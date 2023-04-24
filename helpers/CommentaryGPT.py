
from dataclasses import asdict
import ast
import logging
import os
import helpers.GptChat as GptChat
from models.Commentary import Commentary
from models.Readings import Readings


def get_gpt_test(text: str, model: str = 'gpt-3.5-turbo', temperature: float = 0.7):
    # Chat GPT messages content
    messages = [
        {'role': 'system', 'content': 'Jesteś katolickim teologiem, biblistą, który komentuje biblię. Szuka głębi w tekście, alegorii, duchowych odniesień.'},
        {'role': 'user', 'content': f'Napisz komentarz do tekstu : ' +
                                    f'Albowiem tak Bóg umiłościł świat, że dał jedynego Syna swojego, aby każdy, kto w Niego wierzy, nie zginął, lecz miał wieczne życie.'},
    ]

    # Send request to Open AI
    response = GptChat.GptPrompt(model=model,
                                 messages=messages,
                                 temperature=temperature)

    print(response)
    return response


def get_gpt_commentary(readings: Readings, model: str = 'gpt-3.5-turbo', temperature: float = 0.5) -> Commentary:
    ''' Creates commentary for given text.'''
    # Create text analysis as json.
    messages = [
        {'role': 'system', 'content': 'Jesteś katolickim teologiem i biblistą.' +
                                      'Szukasz duchowości, charyzmatów, alegorii,' +
                                      'głębi znaczenia, kontekstu biblijnego, historii postaci oraz wyjaśnienia przykładów.' +
                                      'Skup się na postaciach, ich sytuacji, ich relacji, przesłaniu, ' +
                                      'wnioskach dla czytającego.'},
        {'role': 'user', 'content': f'Odpowiedz tylko jako json. Opis pól:\n' +
                                    f'- title : kreatywny tytuł nie wprost,\n' +
                                    f'- location : miejsce akcji (np dach, dom, las),\n' +
                                    f'- people : imiona postaci,\n' +
                                    f'- quote : pasujący cytat świętej osoby,\n' +
                                    f'- quote_author : autor powyższego cytatu,\n' +
                                    f'- points : 3 najwazniejsze punkty czytania,\n' +
                                    f'- comment: kilka zdań wyjaśnienia,\n' +
                                    f'- conclusions : 3 wnioski dla wierzącego,\n' +
                                    f'- summary: niewprost, najważniejsze zdanie podsumowujące.\n' +
                                    f'Tekst : {readings.evangelium}'},
    ]

    # Send request to Open AI
    response = GptChat.GptPrompt(model=model,
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

    # Send request to Open AI
    messages = [
        {'role': 'system', 'content': 'Jesteś katolickim teologiem i biblistą.' +
                                      'Szukasz duchowości, charyzmatów, alegorii,' +
                                      'głębi znaczenia, kontekstu biblijnego, historii postaci oraz wyjaśnienia przykładów.' +
                                      'Skup się na postaciach, ich sytuacji, ich relacji, przesłaniu, ' +
                                      'wnioskach dla czytającego.'},
        {'role': 'user', 'content': f'Napisz kilka akapitów komentarza do Ewangelii. Uwzględnij analogie między ewangelią, a czytaniami:\n' +
                                    f'Tekst ewangelii: {readings.evangelium}\n' +
                                    f'Tekst czytań: {readings.first_reading} {readings.second_reading} \n'
         },
    ]
    response = GptChat.GptPrompt(model=model,
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

    # Update basic commentary with more detailed
    jsonCommentary['comment'] = response['choices'][0]['message']['content']

    # Convert jsonCommentary to Commentary dataclass from json.
    commentary = Commentary(**jsonCommentary)
    commentary.aimodel = model
    return commentary


if __name__ == '__main__':
    text = u'Tak bowiem Bóg umiłował świat, że Syna swego Jednorodzonego dał, aby każdy, kto w Niego wierzy, nie zginął, ale miał życie wieczne.(J3, 16)'
    print(get_gpt_commentary(text))
