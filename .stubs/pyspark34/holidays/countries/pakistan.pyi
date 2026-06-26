from _typeshed import Incomplete
from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, FEB as FEB, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP
from holidays.groups import InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Pakistan(HolidayBase, InternationalHolidays, IslamicHolidays):
    country: str
    def __init__(self, *args, **kwargs) -> None: ...

class PK(Pakistan): ...
class PAK(Pakistan): ...

class PakistanIslamicHolidays(_CustomIslamicHolidays):
    ASHURA_DATES: Incomplete
    EID_AL_ADHA_DATES: Incomplete
    EID_AL_FITR_DATES: Incomplete
    MAWLID_DATES: Incomplete
