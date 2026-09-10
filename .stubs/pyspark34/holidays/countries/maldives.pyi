from _typeshed import Incomplete
from holidays.calendars.gregorian import FRI as FRI, SAT as SAT
from holidays.groups import InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Maldives(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_the_Maldives
    - https://www.timeanddate.com/holidays/maldives/
    - http://www.mma.gov.mv/#/about/bankholidays
    """
    country: str
    weekend: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class MV(Maldives): ...
class MDV(Maldives): ...
