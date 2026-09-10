from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, FEB as FEB, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, OCT as OCT, SEP as SEP
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Paraguay(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://www.ghp.com.py/news/feriados-nacionales-del-ano-2019-en-paraguay
    https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Paraguay
    http://www.calendarioparaguay.com/
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class PY(Paraguay): ...
class PRY(Paraguay): ...

class ParaguayStaticHolidays:
    public_holiday: Incomplete
    public_sector_holiday: Incomplete
    special_holidays: Incomplete
