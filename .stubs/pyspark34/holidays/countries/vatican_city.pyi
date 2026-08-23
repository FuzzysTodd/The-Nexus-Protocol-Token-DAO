from holidays.groups import ChristianHolidays as ChristianHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class VaticanCity(HolidayBase, ChristianHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Vatican_City
      - https://www.ewtn.com/catholicism/library/solemnity-of-mary-mother-of-god-5826
      - https://www.franciscanmedia.org/saint-of-the-day/saint-joseph-the-worker/
    """
    country: str
    def __init__(self, *args, **kwargs) -> None: ...

class VA(VaticanCity): ...
class VAT(VaticanCity): ...
