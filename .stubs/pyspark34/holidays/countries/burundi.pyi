from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON

class Burundi(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    Burundian holidays
    Note that holidays falling on a sunday maybe observed
    on the following Monday.
    This depends on formal announcements by the government,
    which only happens close to the date of the holiday.

    Primary sources:
    https://www.officeholidays.com/countries/burundi
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class BI(Burundi): ...
class BDI(Burundi): ...
