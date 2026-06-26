from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_MON as SAT_SUN_TO_NEXT_MON, SAT_SUN_TO_NEXT_MON_TUE as SAT_SUN_TO_NEXT_MON_TUE

class Malawi(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://www.officeholidays.com/countries/malawi
    https://www.timeanddate.com/holidays/malawi/
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class MW(Malawi): ...
class MWI(Malawi): ...
