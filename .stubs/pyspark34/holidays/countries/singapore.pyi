from _typeshed import Incomplete
from holidays.calendars import _CustomBuddhistHolidays, _CustomChineseHolidays, _CustomHinduHolidays, _CustomIslamicHolidays
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, FEB as FEB, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP
from holidays.groups import BuddhistCalendarHolidays as BuddhistCalendarHolidays, ChineseCalendarHolidays as ChineseCalendarHolidays, ChristianHolidays as ChristianHolidays, HinduCalendarHolidays as HinduCalendarHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_WORKDAY as SUN_TO_NEXT_WORKDAY

class Singapore(ObservedHolidayBase, BuddhistCalendarHolidays, ChineseCalendarHolidays, ChristianHolidays, HinduCalendarHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays):
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None:
        """
        A subclass of :py:class:`HolidayBase` representing public holidays in
        Singapore.

        Limitations:

        - Prior to 1969: holidays are estimated.
        - Prior to 2000: holidays may not be accurate.
        - 2024 and later: the following four moving date holidays (whose exact
          date is announced yearly) are estimated, and so denoted:

          - Hari Raya Puasa
          - Hari Raya Haji
          - Vesak Day
          - Deepavali

        Sources:

        - `Holidays Act <https://sso.agc.gov.sg/Act/HA1998>`__ (Act 24 of
          1968—Holidays (Amendment) Act 1968)
        - `Ministry of Manpower
          <https://www.mom.gov.sg/employment-practices/public-holidays>`__

        References:

        - `Wikipedia
          <https://en.wikipedia.org/wiki/Public_holidays_in_Singapore>`__

        Country created and maintained by: `Mike Borsetti
        <https://github.com/mborsetti>`__

        See parameters and usage in :py:class:`HolidayBase`.
        """

class SG(Singapore): ...
class SGP(Singapore): ...

class SingaporeBuddhistHolidays(_CustomBuddhistHolidays):
    VESAK_DATES: Incomplete

class SingaporeChineseHolidays(_CustomChineseHolidays):
    LUNAR_NEW_YEAR_DATES: Incomplete

class SingaporeHinduHolidays(_CustomHinduHolidays):
    DIWALI_DATES: Incomplete

class SingaporeIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES: Incomplete
    EID_AL_FITR_DATES: Incomplete

class SingaporeStaticHolidays:
    special_holidays: Incomplete
