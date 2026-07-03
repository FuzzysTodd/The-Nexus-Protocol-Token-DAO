from _typeshed import Incomplete
from holidays.calendars.gregorian import JUN as JUN
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, THU_FRI_SUN_TO_NEXT_MON as THU_FRI_SUN_TO_NEXT_MON, THU_FRI_TO_NEXT_MON as THU_FRI_TO_NEXT_MON, TUE_WED_TO_PREV_MON as TUE_WED_TO_PREV_MON

class DominicanRepublic(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    http://ojd.org.do/Normativas/LABORAL/Leyes/Ley%20No.%20%20139-97.pdf
    https://es.wikipedia.org/wiki/Rep%C3%BAblica_Dominicana#D%C3%ADas_festivos_nacionales
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class DO(DominicanRepublic): ...
class DOM(DominicanRepublic): ...
