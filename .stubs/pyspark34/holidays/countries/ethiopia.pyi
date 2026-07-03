from _typeshed import Incomplete
from holidays.calendars.gregorian import SEP as SEP
from holidays.calendars.julian import JULIAN_CALENDAR as JULIAN_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Ethiopia(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    country: str
    default_language: str
    estimated_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class ET(Ethiopia): ...
class ETH(Ethiopia): ...
