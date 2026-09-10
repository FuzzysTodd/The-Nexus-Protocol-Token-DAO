from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON

class Panama(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Panama
      - https://publicholidays.com.pa/
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class PA(Panama): ...
class PAN(Panama): ...
