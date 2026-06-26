from _typeshed import Incomplete
from holidays.calendars.gregorian import FEB as FEB, JAN as JAN, MAY as MAY
from holidays.calendars.julian import JULIAN_CALENDAR as JULIAN_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Russia(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Russia
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class RU(Russia): ...
class RUS(Russia): ...

class RussiaStaticHolidays:
    special_holidays: Incomplete
