from _typeshed import Incomplete
from holidays.calendars.gregorian import JUL as JUL, MAY as MAY, SEP as SEP
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_MON as SAT_SUN_TO_NEXT_MON

class Latvia(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Latvia
    https://information.lv/
    https://likumi.lv/ta/id/72608-par-svetku-atceres-un-atzimejamam-dienam
    """
    country: str
    default_language: str
    observed_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class LV(Latvia): ...
class LVA(Latvia): ...

class LatviaStaticHolidays:
    song_and_dance_festival_closing_day: Incomplete
    pope_francis_pastoral_visit_day: Incomplete
    hockey_team_win_bronze_medal_day: Incomplete
    special_holidays: Incomplete
