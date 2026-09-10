from _typeshed import Incomplete
from holidays.calendars.julian import JULIAN_CALENDAR as JULIAN_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Armenia(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Armenia holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Armenia
     - http://www.parliament.am/legislation.php?sel=show&ID=1274&lang=arm&enc=utf8
     - https://www.arlis.am/documentview.aspx?docid=259
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class AM(Armenia): ...
class ARM(Armenia): ...
