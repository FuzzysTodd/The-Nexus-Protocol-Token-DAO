from _typeshed import Incomplete
from holidays.calendars.gregorian import NOV as NOV
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Poland(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://pl.wikipedia.org/wiki/Dni_wolne_od_pracy_w_Polsce
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class PL(Poland): ...
class POL(Poland): ...

class PolandStaticHolidays:
    special_holidays: Incomplete
