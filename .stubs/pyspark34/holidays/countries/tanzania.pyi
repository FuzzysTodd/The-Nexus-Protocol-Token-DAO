from _typeshed import Incomplete
from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP
from holidays.constants import BANK as BANK, PUBLIC as PUBLIC
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, IslamicHolidays as IslamicHolidays, StaticHolidays as StaticHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Tanzania(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays):
    """
    References:
    - https://old.tanzlii.org/tz/legislation/act/1962/48/  # 1962
    - https://old.tanzlii.org/tz/legislation/act/1964/52/  # 1964
    - https://old.tanzlii.org/tz/legislation/act/1966/39/  # 1966
    - https://www.parliament.go.tz/polis/uploads/bills/acts/1566639469-The%20Written%20Laws%20(Miscellaneous%20Amendments)%20Act,%201993.pdf  # 1993  # noqa: E501
    - https://www.parliament.go.tz/polis/uploads/bills/acts/1566638051-The%20Written%20Laws%20(Miscellaneous%20Amendments)%20(No.%202)%20Act,%201994.pdf  # 1994  # noqa: E501
    - http://parliament.go.tz/polis/uploads/bills/acts/1454076376-ActNo-25-2002.pdf  # 2002
    - https://en.wikipedia.org/wiki/Public_holidays_in_Tanzania
    - http://mytanzaniatimes.blogspot.com/2014/08/holiday-nane-nane-farmers-day-in.html
    - https://www.theeastafrican.co.ke/tea/business/tanzania-declares-public-holiday-on-census-day-3918836  # noqa: E501
    - https://www.dw.com/en/samia-suluhu-hassan-who-is-tanzanias-new-president/a-56932264

    Checked With:
    - https://www.bot.go.tz/webdocs/Other/2023%20public%20holidays.pdf  # 2023
    - https://www.bot.go.tz/webdocs/Other/PUBLIC%20HOLIDAYS%202022.pdf  # 2022
    - https://www.bot.go.tz/webdocs/Other/PUBLIC%20HOLIDAYS%202021.pdf  # 2021
    - https://www.bot.go.tz/webdocs/Other/PUBLIC%20HOLIDAYS%202020.pdf  # 2020
    - https://issamichuzi.blogspot.com/2017/11/sikukuu-za-kitaifa-zenye-mapumziko-kwa.html  # 2018
    - https://www.timeanddate.com/holidays/tanzania/ (from 2013 onwards)

    Limitations:

    - Only works from 1994 onwards due to the lack of sources for certain legislation:
        Government Notices No. 79 of 1977
        Government Notices No. 300 of 1985
        Government Notices No. 296 of 1994

    - Exact Islamic holidays dates are only available for 2013-2023; the rest are estimates.
    """
    country: str
    supported_categories: Incomplete
    default_language: str
    estimated_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class TZ(Tanzania): ...
class TZA(Tanzania): ...

class TanzaniaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES: Incomplete
    EID_AL_FITR_DATES: Incomplete
    MAWLID_DATES: Incomplete

class TanzaniaStaticHolidays:
    john_magufuli_inauguration: Incomplete
    tz_election_day: Incomplete
    phc_census_day: Incomplete
    john_magufuli_funeral: Incomplete
    special_public_holidays: Incomplete
