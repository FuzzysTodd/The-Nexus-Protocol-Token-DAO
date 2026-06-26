from holidays.groups import InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Turkey(HolidayBase, IslamicHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Turkey
    """
    country: str
    def __init__(self, *args, **kwargs) -> None: ...

class TR(Turkey): ...
class TUR(Turkey): ...
