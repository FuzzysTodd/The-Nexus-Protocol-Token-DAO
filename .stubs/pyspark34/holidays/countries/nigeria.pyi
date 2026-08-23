from _typeshed import Incomplete
from holidays.calendars.gregorian import FEB as FEB, MAY as MAY
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY as SAT_SUN_TO_NEXT_WORKDAY

class Nigeria(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Nigeria
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class NG(Nigeria): ...
class NGA(Nigeria): ...

class NigeriaStaticHolidays:
    special_holidays: Incomplete
