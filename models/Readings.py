
'''
    Bible readings dataclass

'''

from dataclasses import dataclass, field
from datetime import date


def CompactString(string: str) -> str:
    ''' Compact string '''
    if (string is None):
        return None

    return string.replace('  ', '')\
                 .replace('\n', '')\
                 .replace('\t', '')\
                 .replace('\r', '')\
                 .replace('  ', ' ').strip()


@dataclass
class Readings:
    ''' Bible readings dataclass.'''
    # Url of readings
    url: str = ''
    # Date of readings
    creationDate: date = field(init=True, default_factory=date.today)
    # Livery color
    livery_color: str = None
    # Liturgical year
    liturgical_year: str = None
    # liturgical week
    liturgical_week: str = None
    # First reading
    first_reading: str = None
    # Psalm
    psalm: str = None
    # Second reading
    second_reading: str = None
    # Gospel
    gospel: str = None
    # Evangelium
    evangelium: str = None

    def __post_init__(self):
        ''' At least evangelium must be not None '''
        if (self.evangelium is None):
            raise ValueError('Evangelium is None!')

        if (isinstance(self.creationDate, str)):
            self.creationDate = date.fromisoformat(self.creationDate)

        # Compact first reading
        self.first_reading = CompactString(self.first_reading)

        # Compact psalm
        self.psalm = CompactString(self.psalm)

        # Compact second reading
        self.second_reading = CompactString(self.second_reading)

        # Compact gospel
        self.gospel = CompactString(self.gospel)

        # Compacted version of evangelium
        self.evangelium = CompactString(self.evangelium)

    @property
    def liturgical_info(self):
        ''' Returns liturgical info '''
        return f'{self.liturgical_week}, {self.liturgical_year}'


if __name__ == '__main__':
    # Test compact string code
    text = 'Ewangelia\n                                \n                                                                    (J 21, 1-14) Jezus znowu ukazał się nad Morzem Tyberiadzkim. A ukazał się w ten sposób:Byli razem Szymon Piotr, Tomasz, zwany Didymos, Natanael z Kany Galilejskiej, synowie Zebedeusza oraz dwaj inni z Jego uczniów. Szymon Piotr powiedział do nich: „Idę łowić ryby”. Odpowiedzieli mu: „Idziemy i my z tobą”. Wyszli więc i wsiedli do łodzi, ale tej nocy nic nie złowili.A gdy ranek zaświtał, Jezus stanął na brzegu. Jednakże uczniowie nie wiedzieli, że to był Jezus.A Jezus rzekł do nich: „Dzieci, czy nie macie nic do jedzenia?”Odpowiedzieli Mu: „Nie”.On rzekł do nich: „Zarzućcie sieć po prawej stronie łodzi, a znajdziecie”. Zarzucili więc i z powodu mnóstwa ryb nie mogli jej wyciągnąć.Powiedział więc do Piotra ów uczeń, którego Jezus miłował: „To jest Pan!” Szymon Piotr usłyszawszy, że to jest Pan, przywdział na siebie wierzchnią szatę, był bowiem prawie nagi, i rzucił się w morze. Reszta uczniów dobiła łodzią, ciągnąc za sobą sieć z rybami. Od brzegu bowiem nie było daleko, tylko około dwustu łokci.A kiedy zeszli na ląd, ujrzeli żarzące się na ziemi węgle, a na nich ułożoną rybę oraz chleb. Rzekł do nich Jezus: „Przynieście jeszcze ryb, któreście teraz ułowili”. Poszedł Szymon Piotr i wyciągnął na brzeg sieć pełną wielkich ryb w liczbie stu pięćdziesięciu trzech. A pomimo tak wielkiej ilości sieć się nie rozerwała. Rzekł do nich Jezus: „Chodźcie, posilcie się!” Żaden z uczniów nie odważył się zadać Mu pytania: „Kto Ty jesteś?”, bo wiedzieli, że to jest Pan. A Jezus przyszedł, wziął chleb i podał im, podobnie i rybę.To już trzeci raz, jak Jezus ukazał się uczniom od chwili, gdy zmartwychwstał.'
    compacted = CompactString(text)
    print(compacted)
    print('Length before: ', len(text))
    print('Length after: ', len(compacted))
