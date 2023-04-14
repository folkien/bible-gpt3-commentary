
'''
    Bible readings dataclass

'''

from dataclasses import dataclass


@dataclass
class Readings:
    ''' Bible readings dataclass.'''
    url: str = ''
    first_reading: str = None
    psalm: str = None
    second_reading: str = None
    gospel: str = None
    evangelium: str = None

    def __post_init__(self):
        ''' At least evangelium must be not None '''
        if (self.evangelium is None):
            raise ValueError('Evangelium is None!')
