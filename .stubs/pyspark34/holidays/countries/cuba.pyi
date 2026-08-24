from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON

class Cuba(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Overview: https://en.wikipedia.org/wiki/Public_holidays_in_Cuba
    1984 (DEC 28): https://bit.ly/3okNBbt
    2007 (NOV 19): https://bit.ly/3oFbhaZ
    2013 (DEC 20): https://bit.ly/3zoO3vC
    Note: for holidays that can be moved to a Monday if they fall on a
            Sunday, between 1984 and 2013, the State Committee of Work and
            Social Security would determine if they would be moved to the
            Monday, or if they would stay on the Sunday, presumably depending
            on quotas. After 2013, they always move to Monday. I could not
            find any records of this, so I implemented this making it always
            go to the next Monday.
    """
    country: str
    default_language: str
    observed_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class CU(Cuba): ...
class CUB(Cuba): ...
