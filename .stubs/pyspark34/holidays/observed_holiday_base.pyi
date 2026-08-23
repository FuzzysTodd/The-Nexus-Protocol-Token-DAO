from _typeshed import Incomplete
from holidays.calendars.gregorian import FRI as FRI, MON as MON, SAT as SAT, SUN as SUN, THU as THU, TUE as TUE, WED as WED
from holidays.holiday_base import DateArg as DateArg, HolidayBase as HolidayBase
from typing import Dict

class ObservedRule(Dict[int, int]):
    def __add__(self, other): ...

MON_TO_NEXT_TUE: Incomplete
TUE_TO_PREV_MON: Incomplete
TUE_TO_PREV_FRI: Incomplete
WED_TO_PREV_MON: Incomplete
WED_TO_NEXT_FRI: Incomplete
THU_TO_PREV_MON: Incomplete
THU_TO_PREV_WED: Incomplete
THU_TO_NEXT_MON: Incomplete
THU_TO_NEXT_FRI: Incomplete
FRI_TO_PREV_THU: Incomplete
FRI_TO_NEXT_MON: Incomplete
FRI_TO_NEXT_TUE: Incomplete
FRI_TO_NEXT_SAT: Incomplete
FRI_TO_NEXT_WORKDAY: Incomplete
SAT_TO_PREV_FRI: Incomplete
SAT_TO_PREV_WORKDAY: Incomplete
SAT_TO_NEXT_MON: Incomplete
SAT_TO_NEXT_TUE: Incomplete
SAT_TO_NEXT_SUN: Incomplete
SAT_TO_NEXT_WORKDAY: Incomplete
SUN_TO_NEXT_MON: Incomplete
SUN_TO_NEXT_TUE: Incomplete
SUN_TO_NEXT_WED: Incomplete
SUN_TO_NEXT_WORKDAY: Incomplete
ALL_TO_NEAREST_MON: Incomplete
ALL_TO_NEAREST_MON_LATAM: Incomplete
ALL_TO_NEXT_MON: Incomplete
ALL_TO_NEXT_SUN: Incomplete
WORKDAY_TO_NEAREST_MON: Incomplete
WORKDAY_TO_NEXT_MON: Incomplete
WORKDAY_TO_NEXT_WORKDAY: Incomplete
TUE_WED_TO_PREV_MON: Incomplete
TUE_WED_THU_TO_PREV_MON: Incomplete
WED_THU_TO_NEXT_FRI: Incomplete
THU_FRI_TO_NEXT_MON: Incomplete
THU_FRI_TO_NEXT_WORKDAY: Incomplete
THU_FRI_SUN_TO_NEXT_MON: Incomplete
FRI_SAT_TO_NEXT_WORKDAY: Incomplete
FRI_SUN_TO_NEXT_MON: Incomplete
FRI_SUN_TO_NEXT_SAT_MON: Incomplete
SAT_SUN_TO_PREV_FRI: Incomplete
SAT_SUN_TO_NEXT_MON: Incomplete
SAT_SUN_TO_NEXT_TUE: Incomplete
SAT_SUN_TO_NEXT_WED: Incomplete
SAT_SUN_TO_NEXT_MON_TUE: Incomplete
SAT_SUN_TO_NEXT_WORKDAY: Incomplete

class ObservedHolidayBase(HolidayBase):
    """Observed holidays implementation."""
    observed_label: str
    def __init__(self, observed_rule: ObservedRule, observed_since: int = None, *args, **kwargs) -> None: ...
