from _typeshed import Incomplete
from holidays.calendars.gregorian import AUG as AUG, JUL as JUL, MAR as MAR, SEP as SEP
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON

class Zambia(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://www.officeholidays.com/countries/zambia/
    https://www.timeanddate.com/holidays/zambia/
    https://en.wikipedia.org/wiki/Public_holidays_in_Zambia
    https://www.parliament.gov.zm/sites/default/files/documents/acts/Public%20Holidays%20Act.pdf
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class ZM(Zambia): ...
class ZMB(Zambia): ...

class ZambiaStaticHolidays:
    special_holidays: Incomplete
