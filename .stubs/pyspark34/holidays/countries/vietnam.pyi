from holidays.groups import ChineseCalendarHolidays as ChineseCalendarHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY as SAT_SUN_TO_NEXT_WORKDAY

class Vietnam(ObservedHolidayBase, ChineseCalendarHolidays, InternationalHolidays):
    """
    https://publicholidays.vn/
    http://vbpl.vn/TW/Pages/vbpqen-toanvan.aspx?ItemID=11013 Article.115
    https://www.timeanddate.com/holidays/vietnam/
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class VN(Vietnam): ...
class VNM(Vietnam): ...
