from _typeshed import Incomplete
from datetime import date
from holidays.calendars.custom import _CustomCalendar
from holidays.calendars.gregorian import FEB as FEB, JAN as JAN, MAR as MAR, NOV as NOV, OCT as OCT
from typing import Tuple

DIWALI: str
THAIPUSAM: str

class _HinduLunisolar:
    DIWALI_DATES: Incomplete
    THAIPUSAM_DATES: Incomplete
    def diwali_date(self, year: int) -> Tuple[date | None, bool]: ...
    def thaipusam_date(self, year: int) -> Tuple[date | None, bool]: ...

class _CustomHinduHolidays(_CustomCalendar, _HinduLunisolar): ...
