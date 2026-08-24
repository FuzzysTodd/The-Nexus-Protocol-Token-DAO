from _typeshed import Incomplete
from holidays.calendars.gregorian import DEC as DEC, JAN as JAN
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON

class Namibia(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://www.officeholidays.com/countries/namibia
    https://www.timeanddate.com/holidays/namibia/

    https://tinyurl.com/lacorg5835
    As of 1991/2/1, whenever a public holiday falls on a Sunday, it rolls over to the monday,
    unless that monday is already a public holiday.
    Since the interval from 1991/1/1 to 1991/2/1 includes only New Year's Day, and it's a Tuesday,
    we can assume that the beginning is 1991.
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class NA(Namibia): ...
class NAM(Namibia): ...

class NamibiaStaticHolidays:
    special_holidays: Incomplete
