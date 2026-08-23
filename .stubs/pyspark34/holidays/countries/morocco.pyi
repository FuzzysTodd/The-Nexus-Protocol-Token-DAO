from _typeshed import Incomplete
from holidays.groups import InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Morocco(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    Morocco holidays.

    Primary sources:
    - https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Maroc
    - https://www.mmsp.gov.ma/fr/pratiques.aspx?id=38
    """
    country: str
    default_language: str
    estimated_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class MA(Morocco): ...
class MOR(Morocco): ...
