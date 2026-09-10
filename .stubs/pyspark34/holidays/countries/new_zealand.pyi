from _typeshed import Incomplete
from holidays.calendars.gregorian import DEC as DEC, FEB as FEB, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, NOV as NOV, SEP as SEP
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ALL_TO_NEAREST_MON as ALL_TO_NEAREST_MON, ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_MON as SAT_SUN_TO_NEXT_MON, SAT_SUN_TO_NEXT_MON_TUE as SAT_SUN_TO_NEXT_MON_TUE

class NewZealand(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    country: str
    observed_label: str
    subdivisions: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class NZ(NewZealand): ...
class NZL(NewZealand): ...

class NewZelandStaticHolidays:
    special_holidays: Incomplete
