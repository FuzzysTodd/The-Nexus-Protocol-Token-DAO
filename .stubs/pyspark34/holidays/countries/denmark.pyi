from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Denmark(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Denmark holidays.

    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Denmark
    - https://www.ft.dk/samling/20222/lovforslag/l13/index.htm
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class DK(Denmark): ...
class DNK(Denmark): ...
