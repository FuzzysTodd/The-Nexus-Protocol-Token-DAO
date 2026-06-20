from _typeshed import Incomplete
from holidays.constants import BANK as BANK, PUBLIC as PUBLIC
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Liechtenstein(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Liechtenstein holidays.
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Liechtenstein
    - https://www.llb.li/en/contact/bank-holidays
    """
    country: str
    default_language: str
    supported_categories: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class LI(Liechtenstein): ...
class LIE(Liechtenstein): ...
