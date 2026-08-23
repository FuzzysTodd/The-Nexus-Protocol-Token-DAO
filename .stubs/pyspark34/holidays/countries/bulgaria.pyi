from _typeshed import Incomplete
from holidays.calendars.julian_revised import JULIAN_REVISED_CALENDAR as JULIAN_REVISED_CALENDAR
from holidays.constants import PUBLIC as PUBLIC, SCHOOL as SCHOOL
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY as SAT_SUN_TO_NEXT_WORKDAY

class Bulgaria(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Official holidays in Bulgaria in their current form. This class does not
    any return holidays before 1990, as holidays in the People's Republic of
    Bulgaria and earlier were different.

    Since 2017, it has been accepted that public holidays in Bulgaria that fall on a Saturday
    or Sunday are to be taken on the first working day after them. If there are both Saturday
    and Sunday holidays, Monday and Tuesday are rested respectively.
    The exceptions are:
    1) the Easter holidays, which are always a consecutive Friday, Saturday, and Sunday;
    2) National Awakening Day which, while an official holiday and a non-attendance day for
    schools, is still a working day.

    Sources (Bulgarian):
    - http://lex.bg/laws/ldoc/1594373121
    - https://www.parliament.bg/bg/24
    - https://kik-info.com/spravochnik/calendar/2021/

    Sources (English):
    - https://en.wikipedia.org/wiki/Public_holidays_in_Bulgaria
    """
    country: str
    default_language: str
    observed_label: Incomplete
    supported_categories: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class BG(Bulgaria): ...
class BLG(Bulgaria): ...
