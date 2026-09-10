from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, DEC as DEC, JUL as JUL, JUN as JUN, MAY as MAY, SEP as SEP
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import MON_TO_NEXT_TUE as MON_TO_NEXT_TUE, ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_MON as SAT_SUN_TO_NEXT_MON, SAT_SUN_TO_NEXT_MON_TUE as SAT_SUN_TO_NEXT_MON_TUE
from typing import Tuple

class UnitedKingdom(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_the_United_Kingdom
    - https://www.gov.uk/bank-holidays
    - https://www.timeanddate.com/holidays/uk/
    """
    country: str
    observed_label: str
    subdivisions: Tuple | Tuple[str, ...]
    def __init__(self, *args, **kwargs) -> None: ...

class UK(UnitedKingdom): ...
class GB(UnitedKingdom): ...
class GBR(UnitedKingdom): ...

class UnitedKingdomStaticHolidays:
    special_holidays: Incomplete
