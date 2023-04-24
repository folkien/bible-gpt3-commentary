'''
    View of media post for readings and commentary.

'''
from helpers.git import GetGitBranchRev
from models.Post import Post
from datetime import date


class ViewPost:

    @staticmethod
    def View(post: Post) -> str:
        ''' View creates string/markdown representation of media post. '''

        content = ''
        content += f'# Tytuł : {post.commentary.title} / {post.readings.creationDate.strftime("%d %B")}, {post.readings.liturgical_info}\n\n'
        content += f"    '''{post.commentary.quote_with_author}'''\n\n"
        content += f'# Streszczenie \n\n'
        content += f'Miejsce akcji : {post.commentary.action_place}\n'
        content += f'Osoby : {post.commentary.people_names}\n\n'
        for index, point in enumerate(post.commentary.points):
            content += f'{index + 1}. {point}\n'
        content += f'\n\n'
        content += f'# Ewangelia na dziś (pobrano ze strony {post.readings.url})\n\n    {post.readings.evangelium}\n\n'
        content += f'# Komentarz\n\n    {post.commentary.comment}\n\n'
        content += f'# Wnioski\n\n'
        for index, point in enumerate(post.commentary.conclusions):
            content += f' -  {point}\n'
        content += f'\n\n'
        content += f'# Zapamiętaj\n\n    {post.commentary.summary}\n\n'

        # Add tags
        content += f'#ewangelia #wiara #komentarz #ChatGPT #gpt3 #ai #bible #biblia #komentarz\n\n'

        # Add Disclaimer
        content += f'------------------------\n\n'
        content += f'Czytania z dnia pobrano ze strony {post.readings.url}\n'
        content += f'Komentarz wygenerowano przy użyciu modelu {post.commentary.aimodel}.\n'
        content += f'Użyto bible-gpt-commentary w rewizji {GetGitBranchRev()}.\n'
        content += f'Uwaga! Poza tekstem czytań, pozostały tekst został wygenerowany automatycznie przy użyciu modelu GPT firmy OpenAI. '
        content += f'Komentarz nie jest w żaden sposób oficjalną wypowiedzią Kościoła Katolickiego, ani komentarzem biblisty, '
        content += f'ani nie posiada żadnego autorytetu teologicznego oraz nie jest wiarygodnym źródłem danych/cytatów. Jest to jedynie demo technologiczne próbujące '
        content += f'pokazać możliwości sztucznej inteligencji. Autorzy projektu nie ponoszą żadnej odpowiedzialności za treść komentarza '
        content += f'oraz za ewentualne błędy w nim zawarte.\n\n'
        content += f'Link do repozytorium projektu oraz wiecęi informacji w opisie strony. '
        content += f'Projekt Bible-Gpt3-Commentary jest projektem nonprofit open source. Zapraszam do współpracy!'

        return content
