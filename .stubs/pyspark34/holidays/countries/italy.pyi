from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Italy(HolidayBase, ChristianHolidays, InternationalHolidays):
    country: str
    subdivisions: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class IT(Italy): ...
class ITA(Italy): ...
