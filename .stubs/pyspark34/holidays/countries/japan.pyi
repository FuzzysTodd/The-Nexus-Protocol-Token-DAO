from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, AUG as AUG, FEB as FEB, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP
from holidays.constants import BANK as BANK, PUBLIC as PUBLIC
from holidays.groups import InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Japan(HolidayBase, InternationalHolidays):
    """
    References:

    - https://en.wikipedia.org/wiki/Public_holidays_in_Japan
    - https://www.boj.or.jp/en/about/outline/holi.htm
    """
    country: str
    default_language: str
    special_public_holidays: Incomplete
    supported_categories: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class JP(Japan): ...
class JPN(Japan): ...
