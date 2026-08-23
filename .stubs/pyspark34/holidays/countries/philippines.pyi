from holidays.groups import ChineseCalendarHolidays as ChineseCalendarHolidays, ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Philippines(HolidayBase, ChineseCalendarHolidays, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    Philippines holidays.

    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_the_Philippines
    """
    country: str
    def __init__(self, *args, **kwargs) -> None: ...

class PH(Philippines): ...
class PHL(Philippines): ...
