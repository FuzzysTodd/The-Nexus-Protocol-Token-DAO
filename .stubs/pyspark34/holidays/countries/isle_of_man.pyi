from _typeshed import Incomplete
from holidays.calendars.gregorian import JUL as JUL
from holidays.countries.united_kingdom import UnitedKingdom as UnitedKingdom, UnitedKingdomStaticHolidays as UnitedKingdomStaticHolidays
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_MON as SAT_SUN_TO_NEXT_MON

class IsleOfMan(UnitedKingdom):
    """Using existing code in UnitedKingdom for now."""
    country: str
    subdivisions: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class IM(IsleOfMan): ...
class IMN(IsleOfMan): ...
