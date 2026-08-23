from _typeshed import Incomplete
from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, FEB as FEB, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP
from holidays.groups import ChineseCalendarHolidays as ChineseCalendarHolidays, ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays
from holidays.observed_holiday_base import FRI_SUN_TO_NEXT_SAT_MON as FRI_SUN_TO_NEXT_SAT_MON, FRI_TO_NEXT_MON as FRI_TO_NEXT_MON, FRI_TO_NEXT_SAT as FRI_TO_NEXT_SAT, ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_TUE as SUN_TO_NEXT_TUE, SUN_TO_NEXT_WED as SUN_TO_NEXT_WED

class Brunei(ObservedHolidayBase, ChineseCalendarHolidays, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays in Brunei Darussalam.

    References:

    - Based on: http://www.labour.gov.bn/Lists/Upcomming%20events/AllItems.aspx
                http://www.labour.gov.bn/Download/GUIDE%20TO%20BRUNEI%20EMPLOYMENT%20LAWS%20-%20english%20version-3.pdf  # noqa: E501
    - Checked with: https://asean.org/wp-content/uploads/2021/12/ASEAN-National-Holidays-2022.pdf
                    https://asean.org/wp-content/uploads/2022/12/ASEAN-Public-Holidays-2023.pdf
                    https://www.timeanddate.com/holidays/brunei/
    - [Jubli Emas Sultan Hassanal Bolkiah]
        https://www.brudirect.com/news.php?id=28316

    If Public Holiday falls on either Friday or Sunday, in-lieu observance is given out
    on the following Saturday or Monday.

    Limitations:

    - Brunei Darussalam holidays only works from 1984 onwards
    - Islamic holidays


    Country created by: `PPsyrius <https://github.com/PPsyrius>`__

    Country maintained by: `PPsyrius <https://github.com/PPsyrius>`__
    """
    country: str
    default_language: str
    estimated_label: Incomplete
    observed_label: Incomplete
    supported_languages: Incomplete
    special_holidays: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class BN(Brunei): ...
class BRN(Brunei): ...

class BruneiIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES: Incomplete
    EID_AL_FITR_DATES: Incomplete
    HIJRI_NEW_YEAR_DATES: Incomplete
    ISRA_AND_MIRAJ_DATES: Incomplete
    MAWLID_DATES: Incomplete
    NUZUL_AL_QURAN_DATES: Incomplete
    RAMADAN_BEGINNING_DATES: Incomplete
