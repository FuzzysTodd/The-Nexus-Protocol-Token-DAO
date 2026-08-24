from _typeshed import Incomplete
from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, FEB as FEB, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Gabon(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Gabon
      - https://www.timeanddate.com/holidays/gabon
      - https://www.officeholidays.com/countries/gabon
      - http://www.travail.gouv.ga/402-evenements/489-liste-des-jours-feries/
    """
    country: str
    def __init__(self, *args, **kwargs) -> None: ...

class GA(Gabon): ...
class GAB(Gabon): ...

class GabonIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES: Incomplete
    EID_AL_FITR_DATES: Incomplete
