from _typeshed import Incomplete
from holidays.calendars.gregorian import MAR as MAR, NOV as NOV, OCT as OCT
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class India(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    https://www.india.gov.in/calendar
    https://www.india.gov.in/state-and-ut-holiday-calendar
    https://en.wikipedia.org/wiki/Public_holidays_in_India
    https://www.calendarlabs.com/holidays/india/2021
    https://slusi.dacnet.nic.in/watershedatlas/list_of_state_abbreviation.htm
    https://vahan.parivahan.gov.in/vahan4dashboard/
    """
    country: str
    subdivisions: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class IN(India): ...
class IND(India): ...
