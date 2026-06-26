from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, THU as THU
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Switzerland(HolidayBase, ChristianHolidays, InternationalHolidays):
    country: str
    default_language: str
    subdivisions: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class CH(Switzerland): ...
class CHE(Switzerland): ...
