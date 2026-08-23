from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ALL_TO_NEAREST_MON_LATAM as ALL_TO_NEAREST_MON_LATAM, ALL_TO_NEXT_SUN as ALL_TO_NEXT_SUN, ObservedHolidayBase as ObservedHolidayBase, WORKDAY_TO_NEXT_MON as WORKDAY_TO_NEXT_MON

class CostaRica(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Costa_Rica
    - Law #8442 from 19.04.2005
    - Law #8604 from 17.09.2007
    - Law #8753 from 25.07.2009
    - Law #8886 from 01.11.2010
    - Law #9803 from 19.05.2020
    - Law #10050 from 25.10.2021
    """
    country: str
    default_language: str
    observed_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class CR(CostaRica): ...
class CRI(CostaRica): ...
