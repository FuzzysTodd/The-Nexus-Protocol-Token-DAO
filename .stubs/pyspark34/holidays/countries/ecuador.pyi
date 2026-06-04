from _typeshed import Incomplete
from holidays.calendars.gregorian import DEC as DEC
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_TO_PREV_FRI as SAT_TO_PREV_FRI, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON, TUE_TO_PREV_MON as TUE_TO_PREV_MON, WED_THU_TO_NEXT_FRI as WED_THU_TO_NEXT_FRI, WED_TO_NEXT_FRI as WED_TO_NEXT_FRI

class Ecuador(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Ecuador
      - http://tiny.cc/ec_co_tr
    """
    country: str
    default_language: str
    observed_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class EC(Ecuador): ...
class ECU(Ecuador): ...
