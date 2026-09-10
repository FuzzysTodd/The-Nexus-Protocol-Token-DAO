from _typeshed import Incomplete
from holidays.calendars.gregorian import JUN as JUN, SEP as SEP
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, TUE_TO_PREV_FRI as TUE_TO_PREV_FRI, WED_TO_NEXT_FRI as WED_TO_NEXT_FRI, WORKDAY_TO_NEAREST_MON as WORKDAY_TO_NEAREST_MON

class Chile(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    References:
    - https://www.feriados.cl
    - http://www.feriadoschilenos.cl/ (excellent history)
    - https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Chile
    - Law 2.977 (established official Chile holidays in its current form)
    - Law 20.983 (Day after New Year's Day, if it's a Sunday)
    - Law 19.668 (floating Monday holiday)
    - Law 19.668 (Corpus Christi)
    - Law 2.200, (Labour Day)
    - Law 18.018 (Labour Day renamed)
    - Law 16.840, Law 18.432 (Saint Peter and Saint Paul)
    - Law 20.148 (Day of Virgin of Carmen)
    - Law 18.026 (Day of National Liberation)
    - Law 19.588, Law 19.793 (Day of National Unity)
    - Law 20.983 (National Holiday Friday preceding Independence Day)
    - Law 20.215 (National Holiday Monday preceding Independence Day)
    - Law 20.215 (National Holiday Friday following Army Day)
    - Decree-law 636, Law 8.223
    - Law 3.810 (Columbus Day)
    - Law 20.299 (National Day of the Evangelical and Protestant Churches)
    - Law 20.663 (Región de Arica y Parinacota)
    - Law 20.678 (Región de Ñuble)
    """
    country: str
    default_language: str
    subdivisions: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class CL(Chile): ...
class CHL(Chile): ...

class ChileStaticHolidays:
    special_holidays: Incomplete
