from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, AUG as AUG, FRI as FRI, OCT as OCT, SEP as SEP
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_MON as SAT_SUN_TO_NEXT_MON, SAT_SUN_TO_NEXT_MON_TUE as SAT_SUN_TO_NEXT_MON_TUE, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON

class Australia(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    References:
      - https://www.qld.gov.au/recreation/travel/holidays
    """
    country: str
    observed_label: str
    subdivisions: Incomplete
    @property
    def sovereign_birthday(self) -> str:
        """Sovereign's birthday holiday name."""
    def __init__(self, *args, **kwargs) -> None: ...

class AU(Australia): ...
class AUS(Australia): ...

class AustraliaStaticHolidays:
    special_holidays: Incomplete
