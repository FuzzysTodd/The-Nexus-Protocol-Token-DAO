from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, AUG as AUG, FEB as FEB, SEP as SEP
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE as SUN_TO_NEXT_TUE

class Kenya(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Kenya
    http://kenyaembassyberlin.de/Public-Holidays-in-Kenya.48.0.html
    https://www.officeholidays.com/holidays/kenya/moi-day
    """
    country: str
    observed_label: str
    special_holidays: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class KE(Kenya): ...
class KEN(Kenya): ...
