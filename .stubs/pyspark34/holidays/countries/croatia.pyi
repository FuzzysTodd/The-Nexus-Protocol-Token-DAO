from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Croatia(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Updated with act 022-03 / 19-01 / 219 of 14 November 2019
    https://narodne-novine.nn.hr/clanci/sluzbeni/2019_11_110_2212.html
    https://en.wikipedia.org/wiki/Public_holidays_in_Croatia
    https://hr.wikipedia.org/wiki/Blagdani_i_spomendani_u_Hrvatskoj
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class HR(Croatia): ...
class HRV(Croatia): ...
