from _typeshed import Incomplete
from datetime import date
from holidays.calendars.gregorian import APR as APR, DEC as DEC, FEB as FEB, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP

class _HebrewLunisolar:
    HANUKKAH_DATES: Incomplete
    LAG_BAOMER_DATES: Incomplete
    MEMORIAL_DAY_DATES: Incomplete
    PASSOVER_DATES: Incomplete
    PURIM_DATES: Incomplete
    ROSH_HASHANAH_DATES: Incomplete
    SHAVUOT_DATES: Incomplete
    SUKKOT_DATES: Incomplete
    YOM_KIPPUR_DATES: Incomplete
    @staticmethod
    def hebrew_holiday_date(year: int, hol_type: str) -> date | None: ...
