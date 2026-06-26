from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Nicaragua(HolidayBase, ChristianHolidays, InternationalHolidays):
    country: str
    default_language: str
    subdivisions: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class NI(Nicaragua): ...
class NIC(Nicaragua): ...
