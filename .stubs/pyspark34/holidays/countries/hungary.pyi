from _typeshed import Incomplete
from holidays.calendars.gregorian import DEC as DEC
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, THU_TO_NEXT_FRI as THU_TO_NEXT_FRI, TUE_TO_PREV_MON as TUE_TO_PREV_MON

class Hungary(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Hungary
    Codification dates:
      - https://hvg.hu/gazdasag/20170307_Megszavaztak_munkaszuneti_nap_lett_a_nagypentek  # noqa
      - https://www.tankonyvtar.hu/hu/tartalom/historia/92-10/ch01.html#id496839
    """
    country: str
    default_language: str
    observed_label_before: Incomplete
    observed_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class HU(Hungary): ...
class HUN(Hungary): ...
