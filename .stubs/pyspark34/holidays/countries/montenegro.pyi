from holidays.calendars.julian import JULIAN_CALENDAR as JULIAN_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE as SUN_TO_NEXT_TUE

class Montenegro(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Montenegro
      - https://me.usembassy.gov/holiday-calendar/
      - https://publicholidays.eu/montenegro/2023-dates/
      - https://www.officeholidays.com/countries/montenegro/2023
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class ME(Montenegro): ...
class MNE(Montenegro): ...
