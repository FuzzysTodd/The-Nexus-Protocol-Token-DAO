from _typeshed import Incomplete
from datetime import date
from holidays.calendars.custom import _CustomCalendar
from holidays.calendars.gregorian import APR as APR, FEB as FEB, JAN as JAN, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP
from typing import Tuple

BUDDHA_BIRTHDAY: str
DOUBLE_NINTH: str
DRAGON_BOAT: str
HUNG_KINGS: str
LUNAR_NEW_YEAR: str
MID_AUTUMN: str

class _ChineseLunisolar:
    BUDDHA_BIRTHDAY_DATES: Incomplete
    DOUBLE_NINTH_DATES: Incomplete
    DRAGON_BOAT_DATES: Incomplete
    HUNG_KINGS_DATES: Incomplete
    LUNAR_NEW_YEAR_DATES: Incomplete
    MID_AUTUMN_DATES: Incomplete
    def buddha_birthday_date(self, year: int) -> Tuple[date | None, bool]: ...
    def double_ninth_date(self, year: int) -> Tuple[date | None, bool]: ...
    def dragon_boat_date(self, year: int) -> Tuple[date | None, bool]: ...
    def hung_kings_date(self, year: int) -> Tuple[date | None, bool]: ...
    def lunar_new_year_date(self, year: int) -> Tuple[date | None, bool]: ...
    def mid_autumn_date(self, year: int) -> Tuple[date | None, bool]: ...

class _CustomChineseHolidays(_CustomCalendar, _ChineseLunisolar): ...
