from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON, THU_TO_NEXT_FRI as THU_TO_NEXT_FRI, TUE_TO_PREV_MON as TUE_TO_PREV_MON

class Bolivia(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
    - [Supreme Decree #14260] https://bolivia.infoleyes.com/norma/1141/decreto-supremo-14260
    - [Supreme Decree #21060] https://bolivia.infoleyes.com/norma/1211/decreto-supremo-21060
    - [Supreme Decree #22352] https://bolivia.infoleyes.com/norma/1310/decreto-supremo-22352
    - [Supreme Decree #0173] https://bolivia.infoleyes.com/norma/829/decreto-supremo-0173
    - [Supreme Decree #0405] https://bolivia.infoleyes.com/norma/1252/decreto-supremo-0405
    - [Supreme Decree #1210] https://bolivia.infoleyes.com/norma/3756/decreto-supremo-1210
    - [Supreme Decree #2750] https://bolivia.infoleyes.com/norma/6023/decreto-supremo-2750
    - https://en.wikipedia.org/wiki/Public_holidays_in_Bolivia
    - https://www.officeholidays.com/countries/bolivia
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    observed_label: Incomplete
    subdivisions: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class BO(Bolivia): ...
class BOL(Bolivia): ...
