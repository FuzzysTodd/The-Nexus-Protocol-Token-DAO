from _typeshed import Incomplete
from holidays.calendars.gregorian import DEC as DEC, JAN as JAN
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE as SUN_TO_NEXT_TUE

class Eswatini(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://swazilii.org/sz/legislation/act/1938/71
    https://www.officeholidays.com/countries/swaziland
    """
    country: str
    observed_label: str
    special_holidays: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class Swaziland(Eswatini):
    def __init__(self, *args, **kwargs) -> None: ...

class SZ(Eswatini): ...
class SZW(Eswatini): ...
