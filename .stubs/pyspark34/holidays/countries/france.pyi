from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class France(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Official French holidays.

    Some provinces have specific holidays, only those are included in the
    PROVINCES, because these provinces have different administrative status,
    which makes it difficult to enumerate.

    For religious holidays usually happening on Sundays (Easter, Pentecost),
    only the following Monday is considered a holiday.

    Primary sources:
        https://fr.wikipedia.org/wiki/Fêtes_et_jours_fériés_en_France
        https://www.service-public.fr/particuliers/vosdroits/F2405
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    subdivisions: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class FR(France):
    """FR is also used by dateutil (Friday), so be careful with this one."""
class FRA(France): ...
