from _typeshed import Incomplete
from holidays.calendars.julian_revised import JULIAN_REVISED_CALENDAR as JULIAN_REVISED_CALENDAR
from holidays.constants import HALF_DAY as HALF_DAY, PUBLIC as PUBLIC
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY as SAT_SUN_TO_NEXT_WORKDAY

class Greece(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Greece holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Greece
    """
    country: str
    default_language: str
    observed_label: Incomplete
    supported_categories: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class GR(Greece): ...
class GRC(Greece): ...
