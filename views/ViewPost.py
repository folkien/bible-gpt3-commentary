'''
    View of media post for readings and commentary.

'''
from models.Post import Post


class ViewPost:

    @staticmethod
    def View(post: Post) -> str:
        ''' View creates string/markdown representation of media post. '''

        content = ''
        content += f'# Tytuł : {post.commentary.title}\n\n'
        content += f"'''{post.commentary.quote}'''\n\n"
        content += f'# Główne myśli\n\n'
        for index, point in enumerate(post.commentary.points):
            content += f'{index + 1}. {point}\n'
        content += f'\n\n'
        content += f'# Ewangelia na dziś\n\n {post.readings.evangelium}\n\n'
        content += f'# Komentarz\n\n {post.commentary.comment}\n\n'
        content += f'Zapamiętaj : \n\n {post.commentary.summary}\n\n'

        # Add Disclaimer
        content += f'------------------------\n\n'
        content += f'Czytania z dnia pobrano ze strony : {post.readings.url} \n'
        content += f'Uwaga! Powyższy tekst został wygenerowany automatycznie przy użyciu modelu GPT firmy OpenAI. '
        content += f'Komentarz nie jest w żaden sposób oficjalną wypowiedzią Kościoła Katolickiego, ani komentarzem bilisty, '
        content += f'ani nie posiada żadnego autorytetu teologicznego. Jest to jedynie demo technologiczne próbujące '
        content += f'pokazać możliwości sztucznej inteligencji. Autorzy projektu nie ponoszą żadnej odpowiedzialności za treść komentarza '
        content += f'oraz za ewentualne błędy w nim zawarte.\n\n'
        content += f'Repozytorium projektu https://github.com/folkien/bible-gpt3-commentary \n'
        content += f'Projekt Bible-Gpt3-Commentary jest projektem nonprofit open source! Zapraszamy do współpracy!'

        return content
