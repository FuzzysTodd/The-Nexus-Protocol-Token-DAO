from _typeshed import Incomplete
from holidays.calendars.gregorian import AUG as AUG, JUL as JUL, MON as MON, SEP as SEP, SUN as SUN
from holidays.groups import ChineseCalendarHolidays as ChineseCalendarHolidays, ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import MON_TO_NEXT_TUE as MON_TO_NEXT_TUE, ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY as SAT_SUN_TO_NEXT_WORKDAY, SUN_TO_NEXT_WORKDAY as SUN_TO_NEXT_WORKDAY, WORKDAY_TO_NEXT_WORKDAY as WORKDAY_TO_NEXT_WORKDAY

class HongKong(ObservedHolidayBase, ChineseCalendarHolidays, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Hong_Kong
    Holidays for 2007–2023 (government source):
    https://www.gov.hk/en/about/abouthk/holiday/index.htm
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class HK(HongKong): ...
class HKG(HongKong): ...

class HongKongStaticHolidays:
    special_holidays: Incomplete
