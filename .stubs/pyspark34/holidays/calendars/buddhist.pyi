from _typeshed import Incomplete
from datetime import date
from holidays.calendars.custom import _CustomCalendar
from holidays.calendars.gregorian import JUN as JUN, MAY as MAY
from typing import Tuple

VESAK: str
VESAK_MAY: str

class _BuddhistLunisolar:
    VESAK_DATES: Incomplete
    VESAK_MAY_DATES: Incomplete
    def vesak_date(self, year: int) -> Tuple[date | None, bool]: ...
    def vesak_may_date(self, year: int) -> Tuple[date | None, bool]: ...

class _CustomBuddhistHolidays(_CustomCalendar, _BuddhistLunisolar): ...
