from _typeshed import Incomplete
from holidays.calendars import _CustomBuddhistHolidays, _CustomChineseHolidays, _CustomIslamicHolidays
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, FEB as FEB, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP
from holidays.constants import GOVERNMENT as GOVERNMENT, PUBLIC as PUBLIC
from holidays.groups import BuddhistCalendarHolidays as BuddhistCalendarHolidays, ChineseCalendarHolidays as ChineseCalendarHolidays, ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Indonesia(HolidayBase, BuddhistCalendarHolidays, ChineseCalendarHolidays, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Indonesia
    - https://www.timeanddate.com/holidays/indonesia
    - https://www.officeholidays.com/countries/indonesia
    - https://en.wikipedia.org/wiki/Nyepi
    """
    country: str
    default_language: str
    estimated_label: Incomplete
    supported_languages: Incomplete
    supported_categories: Incomplete
    election_day: Incomplete
    eid_al_fitr_joint_holiday: Incomplete
    christmas_joint_holiday: Incomplete
    lunar_new_year_joint_holiday: Incomplete
    day_of_silence_joint_holiday: Incomplete
    special_public_holidays: Incomplete
    special_government_holidays: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class ID(Indonesia): ...
class IDN(Indonesia): ...

class IndonesiaBuddhistHolidays(_CustomBuddhistHolidays):
    VESAK_DATES: Incomplete

class IndonesiaChineseHolidays(_CustomChineseHolidays):
    LUNAR_NEW_YEAR_DATES: Incomplete

class IndonesiaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES: Incomplete
    EID_AL_FITR_DATES: Incomplete
    HIJRI_NEW_YEAR_DATES: Incomplete
    ISRA_AND_MIRAJ_DATES: Incomplete
    MAWLID_DATES: Incomplete
