from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Andorra(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Andorra
      - https://www.holsdb.com/public-holidays/ad
    """
    country: str
    subdivisions: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class AD(Andorra): ...
class AND(Andorra): ...
