from holidays.calendars.julian import JULIAN_CALENDAR as JULIAN_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_WORKDAY as SAT_SUN_TO_NEXT_WORKDAY

class Kazakhstan(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    1. https://www.officeholidays.com/countries/kazakhstan/2020
    2. https://egov.kz/cms/en/articles/holidays-calend
    3. https://en.wikipedia.org/wiki/Public_holidays_in_Kazakhstan
    4. https://adilet.zan.kz/rus/docs/Z010000267_/history
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class KZ(Kazakhstan): ...
class KAZ(Kazakhstan): ...
