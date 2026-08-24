from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, JAN as JAN, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON

class SouthAfrica(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    http://www.gov.za/about-sa/public-holidays
    https://en.wikipedia.org/wiki/Public_holidays_in_South_Africa
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class ZA(SouthAfrica): ...
class ZAF(SouthAfrica): ...

class SouthAfricaStaticHolidays:
    special_holidays: Incomplete
