from _typeshed import Incomplete
from holidays.groups import IslamicHolidays as IslamicHolidays, PersianCalendarHolidays as PersianCalendarHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Iran(HolidayBase, IslamicHolidays, PersianCalendarHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Iran
    - https://fa.wikipedia.org/wiki/تعطیلات_عمومی_در_ایران
    """
    country: str
    default_language: str
    estimated_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class IR(Iran): ...
class IRN(Iran): ...
