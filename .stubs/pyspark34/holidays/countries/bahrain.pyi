from _typeshed import Incomplete
from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import AUG as AUG, FRI as FRI, JUL as JUL, MAY as MAY, OCT as OCT, SAT as SAT
from holidays.groups import InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Bahrain(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    Bahrain holidays.

    References:
      - https://www.cbb.gov.bh/official-bank-holidays/
      - https://www.officeholidays.com/countries/bahrain/
    """
    country: str
    default_language: str
    estimated_label: Incomplete
    supported_languages: Incomplete
    weekend: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class BH(Bahrain): ...
class BAH(Bahrain): ...

class BahrainIslamicHolidays(_CustomIslamicHolidays):
    ASHURA_DATES: Incomplete
    EID_AL_ADHA: Incomplete
    EID_AL_FITR_DATES: Incomplete
    HIJRI_NEW_YEAR_DATES: Incomplete
    MAWLID_DATES: Incomplete
