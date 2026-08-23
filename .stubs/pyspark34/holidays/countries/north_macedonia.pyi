from holidays.calendars.julian import JULIAN_CALENDAR as JULIAN_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class NorthMacedonia(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_North_Macedonia
    """
    country: str
    def __init__(self, *args, **kwargs) -> None: ...

class MK(NorthMacedonia): ...
class MKD(NorthMacedonia): ...
