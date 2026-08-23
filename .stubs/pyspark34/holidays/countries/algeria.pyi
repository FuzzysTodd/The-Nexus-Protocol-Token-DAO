from _typeshed import Incomplete
from holidays.groups import InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Algeria(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Algeria
    """
    country: str
    default_language: str
    estimated_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class DZ(Algeria): ...
class DZA(Algeria): ...
