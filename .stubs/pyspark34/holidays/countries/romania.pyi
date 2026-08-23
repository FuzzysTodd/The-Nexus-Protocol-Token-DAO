from _typeshed import Incomplete
from holidays.calendars.julian_revised import JULIAN_REVISED_CALENDAR as JULIAN_REVISED_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Romania(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Romania
    http://www.dreptonline.ro/legislatie/codul_muncii.php
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class RO(Romania): ...
class ROU(Romania): ...
