from _typeshed import Incomplete
from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, FEB as FEB, GREGORIAN_CALENDAR as GREGORIAN_CALENDAR, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP
from holidays.calendars.julian import JULIAN_CALENDAR as JULIAN_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_MON_TUE as SAT_SUN_TO_NEXT_MON_TUE, SAT_TO_NEXT_MON as SAT_TO_NEXT_MON, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE as SUN_TO_NEXT_TUE

class BosniaAndHerzegovina(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Bosnia_and_Herzegovina
    https://www.paragraf.ba/neradni-dani-fbih.html
    https://www.paragraf.ba/neradni-dani-republike-srpske.html
    https://www.paragraf.ba/neradni-dani-brcko.html

    Observed holidays rules:
    - BIH: if first day of New Year's Day and Labor Day fall on Sunday, observed on Tuesday.
    - BRC: if holiday fall on Sunday, observed on next working day.
    - SRP: if second day of New Year's Day and Labor Day fall on Sunday, observed on Monday.
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    observed_label: Incomplete
    subdivisions: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class BA(BosniaAndHerzegovina): ...
class BIH(BosniaAndHerzegovina): ...

class BosniaAndHerzegovinaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES: Incomplete
    EID_AL_FITR_DATES: Incomplete
