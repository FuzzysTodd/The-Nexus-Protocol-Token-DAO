from _typeshed import Incomplete
from holidays.calendars.gregorian import AUG as AUG, MAY as MAY, SEP as SEP
from holidays.calendars.thai import KHMER_CALENDAR as KHMER_CALENDAR
from holidays.groups import InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays, ThaiCalendarHolidays as ThaiCalendarHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Cambodia(HolidayBase, InternationalHolidays, StaticHolidays, ThaiCalendarHolidays):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays in Cambodia.

    References:

    - Based on: https://www.nbc.gov.kh/english/news_and_events/official_holiday.php
                https://www.nbc.gov.kh/news_and_events/official_holiday.php
                https://en.wikipedia.org/wiki/Public_holidays_in_Cambodia

    - Checked with: https://asean.org/wp-content/uploads/2021/12/ASEAN-National-Holidays-2022.pdf
                    https://asean.org/wp-content/uploads/2022/12/ASEAN-Public-Holidays-2023.pdf
                    https://www.timeanddate.com/holidays/cambodia/

    Limitations:

    - Cambodian holidays only works from 1993 onwards.

    - Exact Public Holidays as per Cambodia's Official Gazette are only
      available from 2015 onwards.

    - Cambodian Lunar Calendar Holidays only work from 1941 (B.E. 2485) onwards until 2057
      (B.E. 2601) as we only have Thai year-type data for cross-checking until then.


    Country created by: `PPsyrius <https://github.com/PPsyrius>`__

    Country maintained by: `PPsyrius <https://github.com/PPsyrius>`__
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class KH(Cambodia): ...
class KHM(Cambodia): ...

class CameroonStaticHolidays:
    sangkranta_in_lieu_covid: Incomplete
    special_in_lieu_holidays: Incomplete
    special_holidays: Incomplete
