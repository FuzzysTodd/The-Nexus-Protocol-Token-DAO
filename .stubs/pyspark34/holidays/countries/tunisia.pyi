from _typeshed import Incomplete
from holidays.groups import InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Tunisia(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    Holidays here are estimates, it is common for the day to be pushed
    if falls in a weekend, although not a rule that can be implemented.
    Holidays after 2020: the following four moving date holidays whose exact
    date is announced yearly are estimated (and so denoted):
    - Eid El Fetr
    - Eid El Adha
    - Arafat Day
    - Moulad El Naby
    """
    country: str
    default_language: str
    estimated_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class TN(Tunisia): ...
class TUN(Tunisia): ...
