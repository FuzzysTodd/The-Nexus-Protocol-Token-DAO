from _typeshed import Incomplete
from holidays.constants import BANK as BANK, PUBLIC as PUBLIC
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Belgium(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Belgium
    https://www.belgium.be/nl/over_belgie/land/belgie_in_een_notendop/feestdagen
    https://nl.wikipedia.org/wiki/Feestdagen_in_Belgi%C3%AB
    https://www.nbb.be/en/about-national-bank/national-bank-belgium/public-holidays
    """
    country: str
    default_language: str
    supported_categories: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class BE(Belgium): ...
class BEL(Belgium): ...
