from _typeshed import Incomplete
from holidays.calendars.gregorian import MAY as MAY, SUN as SUN
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Madagascar(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://www.officeholidays.com/countries/madagascar
    https://www.timeanddate.com/holidays/madagascar/
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class MG(Madagascar): ...
class MDG(Madagascar): ...
