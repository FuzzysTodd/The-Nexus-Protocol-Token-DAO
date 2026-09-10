from _typeshed import Incomplete
from holidays.calendars.gregorian import FRI as FRI, JAN as JAN, MAR as MAR, NOV as NOV, SEP as SEP
from holidays.constants import OPTIONAL as OPTIONAL, PUBLIC as PUBLIC
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Brazil(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
    - https://pt.wikipedia.org/wiki/Feriados_no_Brasil
    - Decreto n. 155-B, de 14.01.1890:
        https://www2.camara.leg.br/legin/fed/decret/1824-1899/decreto-155-b-14-janeiro-1890-517534-publicacaooriginal-1-pe.html
    - Decreto n. 19.488, de 15.12.1930:
        https://www2.camara.leg.br/legin/fed/decret/1930-1939/decreto-19488-15-dezembro-1930-508040-republicacao-85201-pe.html
    """
    country: str
    subdivisions: Incomplete
    supported_categories: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class BR(Brazil): ...
class BRA(Brazil): ...
