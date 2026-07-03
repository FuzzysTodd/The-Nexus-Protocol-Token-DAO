from _typeshed import Incomplete
from holidays.calendars.gregorian import MAY as MAY
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Lesotho(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Lesotho
    - https://www.ilo.org/dyn/travail/docs/2093/Public%20Holidays%20Act%201995.pdf
    - https://www.timeanddate.com/holidays/lesotho/
    """
    country: str
    def __init__(self, *args, **kwargs) -> None: ...

class LS(Lesotho): ...
class LSO(Lesotho): ...

class LesothoStaticHolidays:
    special_holidays: Incomplete
