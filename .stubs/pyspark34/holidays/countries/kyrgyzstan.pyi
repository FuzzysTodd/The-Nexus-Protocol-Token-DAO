from holidays.calendars.julian import JULIAN_CALENDAR as JULIAN_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Kyrgyzstan(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    Kyrgyzstan holidays.

    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Kyrgyzstan
    """
    country: str
    def __init__(self, *args, **kwargs) -> None: ...

class KG(Kyrgyzstan): ...
class KGZ(Kyrgyzstan): ...
