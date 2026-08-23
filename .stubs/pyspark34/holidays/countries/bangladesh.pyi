from holidays.groups import InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Bangladesh(HolidayBase, InternationalHolidays):
    """
    https://mopa.gov.bd/sites/default/files/files/mopa.gov.bd/public_holiday/61c35b73_e335_462a_9bcf_4695b23b6d82/reg4-2019-212.PDF
    https://en.wikipedia.org/wiki/Public_holidays_in_Bangladesh
    """
    country: str
    def __init__(self, *args, **kwargs) -> None: ...

class BD(Bangladesh): ...
class BGD(Bangladesh): ...
