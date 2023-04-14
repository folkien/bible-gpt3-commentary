'''
    Bible readings commentary dataclass

'''

from dataclasses import dataclass


@dataclass
class Commentary:
    ''' Bible readings commentary dataclass'''
    title: str = None
    quote: str = None
    points: list = None
    comment: str = None
    summary: str = None

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

        if (self.summary is None):
            raise ValueError('Summary is None!')
