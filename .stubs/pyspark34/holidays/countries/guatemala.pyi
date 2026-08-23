from _typeshed import Incomplete
from holidays.calendars.gregorian import OCT as OCT
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ALL_TO_NEAREST_MON_LATAM as ALL_TO_NEAREST_MON_LATAM, ObservedHolidayBase as ObservedHolidayBase

class Guatemala(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
    - http://www.bvnsa.com.gt/bvnsa/calendario_dias_festivos.php
    - https://www.minfin.gob.gt/images/downloads/leyes_acuerdos/decretocong19_101018.pdf

    Moving holidays:
        law 19-2018 start 18 oct 2018
        https://www.minfin.gob.gt/images/downloads/leyes_acuerdos/decretocong19_101018.pdf

        EXPEDIENTE 5536-2018 (CC) start 17 abr 2020
        https://leyes.infile.com/index.php?id=181&id_publicacion=81051
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class GT(Guatemala): ...
class GUA(Guatemala): ...
