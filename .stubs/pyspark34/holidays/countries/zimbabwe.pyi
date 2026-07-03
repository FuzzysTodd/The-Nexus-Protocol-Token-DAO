from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE as SUN_TO_NEXT_TUE

class Zimbabwe(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Zimbabwe
    https://en.wikipedia.org/wiki/Robert_Gabriel_Mugabe_National_Youth_Day
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class ZW(Zimbabwe): ...
class ZWE(Zimbabwe): ...
