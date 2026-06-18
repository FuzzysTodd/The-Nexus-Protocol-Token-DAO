from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Lithuania(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Lithuania holidays.

    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Lithuania
    - https://www.kalendorius.today/
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class LT(Lithuania): ...
class LTU(Lithuania): ...
