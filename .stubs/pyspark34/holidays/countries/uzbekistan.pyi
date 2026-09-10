from holidays.groups import InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Uzbekistan(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    https://www.officeholidays.com/countries/uzbekistan
    """
    country: str
    def __init__(self, *args, **kwargs) -> None: ...

class UZ(Uzbekistan): ...
class UZB(Uzbekistan): ...
