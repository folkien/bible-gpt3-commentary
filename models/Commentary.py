'''
    Bible readings commentary dataclass

'''

from dataclasses import dataclass


@dataclass
class Commentary:
    ''' Bible readings commentary dataclass'''
    # OpenAI model used to generate commentary
    aimodel: str = None
    # Commentary title
    title: str = None
    # Location name
    location: str = None
    # List of people names
    people: list = None
    # Commentary single day quote
    quote: str = None
    # Quote author
    quote_author: str = None
    # Commentary main points
    points: list = None
    # Commentary comment
    comment: str = None
    # Conculsions
    conclusions: list = None
    # Commentary summary
    summary: str = None

    @property
    def action_place(self):
        ''' Returns action place as string '''
        if (self.location is None):
            return ''

        return self.location

    @property
    def people_names(self):
        ''' Returns people names as string '''
        return ', '.join(self.people)

    @property
    def quote_with_author(self):
        ''' Returns quote with author '''
        if (self.quote_author is None):
            return self.quote

        return f'{self.quote} ({self.quote_author})'

    def __post_init__(self):
        ''' Checks if all fields are not None '''
        if (self.title is None):
            raise ValueError('Title is None!')

        if (self.quote is None):
            raise ValueError('Quote is None!')

        if (self.points is None):
            raise ValueError('Points is None!')

        if (self.comment is None):
            raise ValueError('Comment is None!')

        if (self.conclusions is None):
            raise ValueError('Conclusions is None!')

        if (self.summary is None):
            raise ValueError('Summary is None!')
