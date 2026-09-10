from _typeshed import Incomplete
from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP
from holidays.groups import InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY as SAT_SUN_TO_NEXT_WORKDAY, WORKDAY_TO_NEXT_WORKDAY as WORKDAY_TO_NEXT_WORKDAY

class Azerbaijan(ObservedHolidayBase, InternationalHolidays, IslamicHolidays):
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class AZ(Azerbaijan): ...
class AZE(Azerbaijan): ...

class AzerbaijanIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES: Incomplete
    EID_AL_FITR_DATES: Incomplete
