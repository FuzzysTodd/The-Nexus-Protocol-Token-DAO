from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Portugal(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays
    in Portugal.

    References:

    - Based on:
        https://en.wikipedia.org/wiki/Public_holidays_in_Portugal

    National Level:
    - [Labour Day]
        https://www.e-konomista.pt/dia-do-trabalhador/
    - [Portugal Day]
        Decreto 17.171
    - [Restoration of Independence Day]
        Gazeta de Lisboa, 8 de Dezembro de 1823 (n.º 290), pp. 1789 e 1790

    Regional Level:
    - [Azores]
        https://files.dre.pt/1s/1980/08/19200/23052305.pdf
    - [Madeira]
        https://files.dre.pt/1s/1979/11/25900/28782878.pdf
        https://files.dre.pt/1s/1989/02/02800/04360436.pdf
        https://files.dre.pt/1s/2002/11/258a00/71837183.pdf

    """
    country: str
    default_language: str
    subdivisions: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class PT(Portugal): ...
class PRT(Portugal): ...
