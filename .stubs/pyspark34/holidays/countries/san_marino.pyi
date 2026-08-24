from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class SanMarino(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_San_Marino
    """
    country: str
    def __init__(self, *args, **kwargs) -> None: ...

class SM(SanMarino): ...
class SMR(SanMarino): ...
