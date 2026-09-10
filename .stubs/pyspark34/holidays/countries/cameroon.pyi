from _typeshed import Incomplete
from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, FEB as FEB, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_WORKDAY as SUN_TO_NEXT_WORKDAY

class Cameroon(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Cameroon
      - https://www.timeanddate.com/holidays/cameroon
      - https://www.officeholidays.com/countries/cameroon
    """
    country: str
    observed_label: str
    special_holidays: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class CM(Cameroon): ...
class CMR(Cameroon): ...

class CameroonIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES: Incomplete
    EID_AL_FITR_DATES: Incomplete
    MAWLID_DATES: Incomplete
