from _typeshed import Incomplete
from holidays.constants import BANK as BANK, PUBLIC as PUBLIC
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Austria(HolidayBase, ChristianHolidays, InternationalHolidays):
    country: str
    default_language: str
    supported_categories: Incomplete
    supported_languages: Incomplete
    subdivisions: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class AT(Austria): ...
class AUT(Austria): ...
