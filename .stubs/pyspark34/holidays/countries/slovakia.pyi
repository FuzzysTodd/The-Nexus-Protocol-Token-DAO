from _typeshed import Incomplete
from holidays.calendars.gregorian import OCT as OCT
from holidays.constants import PUBLIC as PUBLIC, WORKDAY as WORKDAY
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Slovakia(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Slovakia
    https://sk.wikipedia.org/wiki/Zoznam_sviatkov_na_Slovensku
    https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/1993/241/
    """
    country: str
    default_language: str
    special_public_holidays: Incomplete
    supported_categories: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class SK(Slovakia): ...
class SVK(Slovakia): ...
