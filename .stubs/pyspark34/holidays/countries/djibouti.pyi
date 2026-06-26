from _typeshed import Incomplete
from holidays.calendars.gregorian import FRI as FRI, SAT as SAT
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Djibouti(HolidayBase, ChristianHolidays, IslamicHolidays, InternationalHolidays):
    country: str
    default_language: str
    estimated_label: Incomplete
    supported_languages: Incomplete
    weekend: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class DJ(Djibouti): ...
class DJI(Djibouti): ...
