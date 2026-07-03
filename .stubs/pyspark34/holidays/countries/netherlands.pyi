from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, AUG as AUG
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Netherlands(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_the_Netherlands
    http://www.iamsterdam.com/en/plan-your-trip/practical-info/public-holidays
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class NL(Netherlands): ...
class NLD(Netherlands): ...
