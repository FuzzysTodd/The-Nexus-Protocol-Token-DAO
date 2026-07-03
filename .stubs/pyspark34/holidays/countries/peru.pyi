from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Peru(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Peru holidays.

    References:
    - https://www.gob.pe/feriados
    - https://es.wikipedia.org/wiki/Anexo:Días_feriados_en_el_Perú
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class PE(Peru): ...
class PER(Peru): ...
