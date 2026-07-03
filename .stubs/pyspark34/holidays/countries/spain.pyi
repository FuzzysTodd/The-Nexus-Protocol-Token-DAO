from _typeshed import Incomplete
from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import APR as APR, AUG as AUG, JUL as JUL, JUN as JUN, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON

class Spain(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    Holidays checked with official sources for 2010-2023 only.

    References:
     - https://administracion.gob.es/pag_Home/atencionCiudadana/calendarios.html

     Labor Holidays:
     2010: https://www.boe.es/buscar/doc.php?id=BOE-A-2009-18477
     2011: https://www.boe.es/buscar/doc.php?id=BOE-A-2010-15722
     2012: https://www.boe.es/buscar/doc.php?id=BOE-A-2011-16116
     2013: https://www.boe.es/buscar/doc.php?id=BOE-A-2012-13644
     2014: https://www.boe.es/buscar/doc.php?id=BOE-A-2013-12147
     2015: https://www.boe.es/buscar/doc.php?id=BOE-A-2014-10823
     2016: https://www.boe.es/buscar/doc.php?id=BOE-A-2015-11348
     2017: https://www.boe.es/buscar/doc.php?id=BOE-A-2016-9244
     2018: https://www.boe.es/buscar/doc.php?id=BOE-A-2017-11639
     2019: https://www.boe.es/buscar/doc.php?id=BOE-A-2018-14369
     2020: https://www.boe.es/buscar/doc.php?id=BOE-A-2019-14552
     2021: https://www.boe.es/buscar/doc.php?id=BOE-A-2020-13343
     2022: https://www.boe.es/buscar/doc.php?id=BOE-A-2021-17113
     2023: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2022-16755
    """
    country: str
    observed_label: str
    subdivisions: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class ES(Spain): ...
class ESP(Spain): ...

class SpainIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES: Incomplete
    EID_AL_FITR_DATES: Incomplete
