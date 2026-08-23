from _typeshed import Incomplete
from holidays.calendars.gregorian import JUL as JUL, OCT as OCT
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import MON_TO_NEXT_TUE as MON_TO_NEXT_TUE, ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON

class Vanuatu(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Vanuatu
    https://www.timeanddate.com/holidays/vanuatu/
    https://www.gov.vu/index.php/events/holidays
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class VU(Vanuatu): ...
class VTU(Vanuatu): ...

class VanatuStaticHolidays:
    independence_anniversary: str
    special_holidays: Incomplete
