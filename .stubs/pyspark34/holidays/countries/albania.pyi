from _typeshed import Incomplete
from holidays.calendars.gregorian import MAR as MAR
from holidays.calendars.julian import JULIAN_CALENDAR as JULIAN_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY as SAT_SUN_TO_NEXT_WORKDAY

class Albania(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Albania
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class AL(Albania): ...
class ALB(Albania): ...

class AlbaniaStaticHolidays:
    special_holidays: Incomplete
