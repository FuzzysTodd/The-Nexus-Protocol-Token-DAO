from holidays.calendars.gregorian import DEC as DEC
from holidays.groups import ChineseCalendarHolidays as ChineseCalendarHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_TO_PREV_WORKDAY as SAT_TO_PREV_WORKDAY, SUN_TO_NEXT_WORKDAY as SUN_TO_NEXT_WORKDAY

class Taiwan(ObservedHolidayBase, ChineseCalendarHolidays, InternationalHolidays):
    '''
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Taiwan
    - https://www.officeholidays.com/countries/taiwan

    If a public holiday falls on Tuesday or Thursday, government establishes an "extended holiday",
    although this will be compensated by making Saturday a working day.
    It\'s not supported yet.
    '''
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class TW(Taiwan): ...
class TWN(Taiwan): ...
