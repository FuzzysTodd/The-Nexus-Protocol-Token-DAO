from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ALL_TO_NEXT_MON as ALL_TO_NEXT_MON, ObservedHolidayBase as ObservedHolidayBase

class Colombia(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    '''
    Colombia has 18 holidays. The establishing of these are by:
    Ley 35 de 1939 (DEC 4): https://bit.ly/3PJwk7B
    Decreto 2663 de 1950 (AUG 5): https://bit.ly/3PJcut8
    Decreto 3743 de 1950 (DEC 20): https://bit.ly/3B9Otr3
    Ley 51 de 1983 (DEC 6): https://bit.ly/3aSobiB

    On the 6th of December 1983, the government of Colombia declared which
    holidays are to take effect, and also clarified that a subset of them
    are to take place the next Monday if they do not fall on a Monday.
    This law is "Ley 51 de 1983" which translates to law 51 of 1983.
    Link: https://bit.ly/3PtPi2e
    A few links below to calendars from the 1980s to demonstrate this law
    change. In 1984 some calendars still use the old rules, presumably
    because they were printed prior to the declaration of law change.
    1981: https://bit.ly/3BbgKOc
    1982: https://bit.ly/3BdbhWW
    1984: https://bit.ly/3PqGxWU
    1984: https://bit.ly/3B7ogt8
    '''
    country: str
    default_language: str
    observed_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class CO(Colombia): ...
class COL(Colombia): ...
