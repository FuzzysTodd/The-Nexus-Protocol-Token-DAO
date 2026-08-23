from _typeshed import Incomplete
from holidays.calendars.gregorian import GREGORIAN_CALENDAR as GREGORIAN_CALENDAR
from holidays.calendars.julian import JULIAN_CALENDAR as JULIAN_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Moldova(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Moldova
    https://www.legis.md/cautare/getResults?doc_id=133686
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class MD(Moldova): ...
class MDA(Moldova): ...
