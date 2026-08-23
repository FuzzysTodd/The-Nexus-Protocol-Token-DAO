from _typeshed import Incomplete
from holidays.calendars import _CustomBuddhistHolidays, _CustomChineseHolidays, _CustomHinduHolidays, _CustomIslamicHolidays
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, FEB as FEB, FRI as FRI, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SAT as SAT, SEP as SEP
from holidays.groups import BuddhistCalendarHolidays as BuddhistCalendarHolidays, ChineseCalendarHolidays as ChineseCalendarHolidays, ChristianHolidays as ChristianHolidays, HinduCalendarHolidays as HinduCalendarHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import FRI_TO_NEXT_WORKDAY as FRI_TO_NEXT_WORKDAY, ObservedHolidayBase as ObservedHolidayBase, SAT_TO_NEXT_WORKDAY as SAT_TO_NEXT_WORKDAY, SUN_TO_NEXT_WORKDAY as SUN_TO_NEXT_WORKDAY

class Malaysia(ObservedHolidayBase, BuddhistCalendarHolidays, ChineseCalendarHolidays, ChristianHolidays, HinduCalendarHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays):
    country: str
    observed_label: str
    subdivisions: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        '''
        An subclass of :py:class:`HolidayBase` representing public holidays in
        Malaysia.

        If ``subdiv`` for a state is not supplied, only nationwide holidays are
        returned. The following ``subdiv`` state codes are used (ISO 3166-2
        subdivision codes are not yet supported):

        - JHR: Johor
        - KDH: Kedah
        - KTN: Kelantan
        - MLK: Melaka
        - NSN: Negeri Sembilan
        - PHG: Pahang
        - PRK: Perak
        - PLS: Perlis
        - PNG: Pulau Pinang
        - SBH: Sabah
        - SWK: Sarawak
        - SGR: Selangor
        - TRG: Terengganu
        - KUL: FT Kuala Lumpur
        - LBN: FT Labuan
        - PJY: FT Putrajaya

        Limitations:

        - Prior to 2021: holidays are not accurate.
        - 2027 and later: Thaipusam dates are are estimated, and so denoted.

        Section 3 of Malaysian Holidays Act:
        "If any day specified in the Schedule falls on Sunday then the day following shall be
        a public holiday and if such day is already a public holiday, then the day following
        shall be a public holiday".
        In Johor and Kedah it\'s Friday -> Sunday,
        in Kelantan and Terengganu it\'s Saturday -> Sunday

        Reference: `Wikipedia
        <https://en.wikipedia.org/wiki/Public_holidays_in_Malaysia>`__

        Country created by: `Eden <https://github.com/jusce17>`__

        Country maintained by: `Mike Borsetti <https://github.com/mborsetti>`__

        See parameters and usage in :py:class:`HolidayBase`.
        '''

class MY(Malaysia): ...
class MYS(Malaysia): ...

class MalaysiaBuddhistHolidays(_CustomBuddhistHolidays):
    VESAK_MAY_DATES: Incomplete

class MalaysiaChineseHolidays(_CustomChineseHolidays):
    LUNAR_NEW_YEAR_DATES: Incomplete

class MalaysiaHinduHolidays(_CustomHinduHolidays):
    DIWALI_DATES: Incomplete
    THAIPUSAM_DATES: Incomplete

class MalaysiaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES: Incomplete
    EID_AL_FITR_DATES: Incomplete
    HARI_HOL_JOHOR_DATES: Incomplete
    HIJRI_NEW_YEAR_DATES: Incomplete
    ISRA_AND_MIRAJ_DATES: Incomplete
    MAWLID_DATES: Incomplete
    NUZUL_AL_QURAN_DATES: Incomplete
    RAMADAN_BEGINNING_DATES: Incomplete

class MalaysiaStaticHolidays:
    special_holidays: Incomplete
