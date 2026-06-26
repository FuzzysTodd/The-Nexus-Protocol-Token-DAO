from _typeshed import Incomplete
from holidays.calendars.gregorian import FEB as FEB, MAR as MAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_MON as SAT_SUN_TO_NEXT_MON, SAT_SUN_TO_NEXT_MON_TUE as SAT_SUN_TO_NEXT_MON_TUE

class Ireland(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    Official holidays in Ireland, as declared in the Citizen's Information
    bulletin:
    https://www.citizensinformation.ie/en/employment/employment_rights_and_conditions/leave_and_holidays/public_holidays_in_ireland.html
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class IE(Ireland): ...
class IRL(Ireland): ...

class IrelandStaticHolidays:
    special_holidays: Incomplete
