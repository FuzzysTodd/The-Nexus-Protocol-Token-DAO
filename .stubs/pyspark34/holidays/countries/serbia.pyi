from _typeshed import Incomplete
from holidays.calendars.julian import JULIAN_CALENDAR as JULIAN_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE as SUN_TO_NEXT_TUE

class Serbia(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Serbia holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Serbia
    """
    country: str
    default_language: str
    observed_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class RS(Serbia): ...
class SRB(Serbia): ...
