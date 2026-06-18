from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, DEC as DEC, JAN as JAN, JUL as JUL, MAR as MAR, MAY as MAY, OCT as OCT
from holidays.calendars.thai import KHMER_CALENDAR as KHMER_CALENDAR
from holidays.constants import BANK as BANK, PUBLIC as PUBLIC, SCHOOL as SCHOOL, WORKDAY as WORKDAY
from holidays.groups import InternationalHolidays as InternationalHolidays, ThaiCalendarHolidays as ThaiCalendarHolidays
from holidays.observed_holiday_base import FRI_TO_NEXT_TUE as FRI_TO_NEXT_TUE, ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_MON as SAT_SUN_TO_NEXT_MON, SAT_SUN_TO_NEXT_WED as SAT_SUN_TO_NEXT_WED, SAT_TO_NEXT_TUE as SAT_TO_NEXT_TUE, THU_FRI_TO_NEXT_MON as THU_FRI_TO_NEXT_MON

class Laos(ObservedHolidayBase, InternationalHolidays, ThaiCalendarHolidays):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays in Laos.

    References:

    - Based on: https://en.wikipedia.org/wiki/Public_holidays_in_Laos
                Decree on Holidays No. 386 / Rev. 15.12.2017
                https://juristact.weebly.com/uploads/1/0/9/9/109947087/d17_386.pdf

    - Checked with: https://asean.org/wp-content/uploads/2021/12/ASEAN-National-Holidays-2022.pdf
                    https://asean.org/wp-content/uploads/2022/12/ASEAN-Public-Holidays-2023.pdf
                    https://www.timeanddate.com/holidays/laos/
                    https://www.bcel.com.la/bcel/bcel-calendar.html?y=2022
                    https://www.bcel.com.la/bcel/bcel-calendar.html?year=2023
                    http://www.lsx.com.la/cal/getStockCalendar.do?lang=lo (from 2011 onwards)

        !!! If Public Holiday falls on weekends, (in lieu) on workday !!!
        Despite the wording, this usually only applies to Monday only for holidays,
        consecutive holidays all have their own special in lieu declared separately.

        As featured in Decree on Holidays No. 386 / Rev. 15.12.2017;
        - Saturdays and Sundays shall be restdays each week.
        - In-Lieu holidays shall be given if it fall on the weekends.

    Limitations:

    - Laotian holidays only works from 1976 onwards, and are only 100% accurate from 2018 onwards.

    - Laotian Lunar Calendar Holidays only work from 1941 (B.E. 2485) onwards until 2057
      (B.E. 2601) as we only have Thai year-type data for cross-checking until then.


    Country created by: `PPsyrius <https://github.com/PPsyrius>`__

    Country maintained by: `PPsyrius <https://github.com/PPsyrius>`__
    """
    country: str
    supported_categories: Incomplete
    default_language: str
    observed_label: Incomplete
    special_bank_day_off: Incomplete
    new_year_day_in_lieu: Incomplete
    international_womens_rights_day_in_lieu: Incomplete
    lao_new_year_in_lieu: Incomplete
    lao_new_year_special: Incomplete
    labor_day_in_lieu: Incomplete
    lao_womens_union_in_lieu: Incomplete
    establishment_day_of_bol_in_lieu: Incomplete
    lao_national_day_in_lieu: Incomplete
    special_bank_holidays: Incomplete
    special_public_holidays: Incomplete
    special_workday_holidays: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class LA(Laos): ...
class LAO(Laos): ...
