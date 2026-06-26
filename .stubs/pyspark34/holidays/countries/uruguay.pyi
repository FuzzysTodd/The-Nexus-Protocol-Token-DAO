from _typeshed import Incomplete
from holidays.calendars.gregorian import MAR as MAR
from holidays.constants import BANK as BANK, PUBLIC as PUBLIC
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, THU_FRI_TO_NEXT_MON as THU_FRI_TO_NEXT_MON, TUE_WED_TO_PREV_MON as TUE_WED_TO_PREV_MON

class Uruguay(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Uruguay
    - [Law #6997] https://www.impo.com.uy/diariooficial/1919/10/25/2
    - [Decree Law #9000] https://www.impo.com.uy/bases/decretos-ley/9000-1933
    - [Decree Law #14977] https://www.impo.com.uy/bases/decretos-ley/14977-1979
    - [Decree Law #15535] https://www.impo.com.uy/bases/decretos-ley/15535-1984
    - [Law #16805] http://www.parlamento.gub.uy/leyes/AccesoTextoLey.asp?Ley=16805
    - [Law #17414] http://www.parlamento.gub.uy/leyes/AccesoTextoLey.asp?Ley=17414
    """
    country: str
    default_language: str
    supported_categories: Incomplete
    supported_languages: Incomplete
    presidential_inauguration_day: Incomplete
    special_public_holidays: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class UY(Uruguay): ...
class URY(Uruguay): ...
