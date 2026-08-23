from _typeshed import Incomplete
from holidays.calendars.julian import JULIAN_CALENDAR as JULIAN_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Georgia(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Georgia holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Georgia_(country)
     - https://matsne.gov.ge/en/document/view/1155567?publication=24
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class GE(Georgia): ...
class GEO(Georgia): ...
