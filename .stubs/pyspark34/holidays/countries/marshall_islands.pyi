from _typeshed import Incomplete
from holidays.calendars.gregorian import NOV as NOV
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON

class HolidaysMH(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://rmiparliament.org/cms/component/content/article/14-pressrelease/49-important-public-holidays.html?Itemid=101
    https://www.rmiembassyus.org/country-profile#:~:text=national%20holidays
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class MH(HolidaysMH): ...
class MHL(HolidaysMH): ...
class MarshallIslands(HolidaysMH): ...

class MarshalIslandsStaticHolidays:
    election_day: str
    special_holidays: Incomplete
