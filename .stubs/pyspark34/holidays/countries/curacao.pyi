from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, MAY as MAY
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Curacao(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://loketdigital.gobiernu.cw/Loket/product/571960bbe1e5fe8712b10a1323630e70
    https://en.wikipedia.org/wiki/Public_holidays_in_Cura%C3%A7ao

    New Year's Eve (Vispu di Aña Nobo) is a half-day public holiday, though
    this isn't supported by Python Holidays so it won't be implemented.
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class CW(Curacao): ...
class CUW(Curacao): ...
