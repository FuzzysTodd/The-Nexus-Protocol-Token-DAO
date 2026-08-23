from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, FEB as FEB, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV, OCT as OCT, SEP as SEP
from holidays.constants import ARMED_FORCES as ARMED_FORCES, BANK as BANK, GOVERNMENT as GOVERNMENT, PUBLIC as PUBLIC, SCHOOL as SCHOOL, WORKDAY as WORKDAY
from holidays.groups import InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays, ThaiCalendarHolidays as ThaiCalendarHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_MON as SAT_SUN_TO_NEXT_MON, SAT_SUN_TO_NEXT_MON_TUE as SAT_SUN_TO_NEXT_MON_TUE, SAT_SUN_TO_NEXT_TUE as SAT_SUN_TO_NEXT_TUE, SAT_TO_NEXT_MON as SAT_TO_NEXT_MON, SAT_TO_NEXT_TUE as SAT_TO_NEXT_TUE, THU_FRI_TO_NEXT_MON as THU_FRI_TO_NEXT_MON

class Thailand(ObservedHolidayBase, InternationalHolidays, StaticHolidays, ThaiCalendarHolidays):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays in Thailand.

    References:

    - Based on: https://en.wikipedia.org/wiki/Public_holidays_in_Thailand
    - Checked with: (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_2023
    - [In Lieus]
        (isranews.org 's wbm) http://tiny.cc/wa_isranews_inlieu_hist
        https://resolution.soc.go.th/?prep_id=99159317
        https://resolution.soc.go.th/?prep_id=196007
        https://github.com/dr-prodigy/python-holidays/pull/929
    - [New Year's Day]
        (wikisource.org 's wbm) http://tiny.cc/wa_wiki_thai_newyear_2483
    - [National Children's Day]
        https://thainews.prd.go.th/banner/th/children'sday/
    - [Chakri Memorial Day]
        (ocac.got.th 's wbm) http://tiny.cc/wa_ocac_chakri
    - [Songkran Festival]
        (museumsiam.org 's wbm) http://tiny.cc/wa_museumsiam_songkran
        https://resolution.soc.go.th/?prep_id=123659
    - [National Labour Day]
        https://www.thairath.co.th/lifestyle/culture/1832869
    - [National Day (24 June: Defunct)]
        (Ministry of Culture 's wbm) http://tiny.cc/wa_mincul_nat_day
    - [Coronation Day]
        https://www.matichon.co.th/politics/news_526200
        https://workpointtoday.com/news1-5/
    - [HM Queen Suthida's Birthday]
        https://www.thairath.co.th/news/politic/1567418
    - [HM Maha Vajiralongkorn's Birthday]
        https://www.matichon.co.th/politics/news_526200
    - [HM Queen Sirikit the Queen Mother's Birthday]
        https://hilight.kapook.com/view/14164
    - [National Mother's Day]
        https://www.brh.go.th/index.php/2019-02-27-04-11-52/542-12-2564
    - [HM King Bhumibol Adulyadej Memorial Day]
        https://www.matichon.co.th/politics/news_526200
    - [HM King Chulalongkorn Memorial Day]
        https://th.wikipedia.org/wiki/วันปิยมหาราช
    - [HM King Bhumibol Adulyadej's Birthday]
        (Ministry of Culture 's wbm) http://tiny.cc/wa_mincul_nat_day
        https://hilight.kapook.com/view/148862
    - [National Father's Day]
        https://www.brh.go.th/index.php/2019-02-27-04-12-21/594-5-5
    - [Constitution Day]
        https://hilight.kapook.com/view/18208
        (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_1992
        https://www.myhora.com/ปฏิทิน/ปฏิทิน-พ.ศ.2475.aspx
    - [New Year's Eve]
        (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_1992
        https://resolution.soc.go.th/?prep_id=205799
        https://resolution.soc.go.th/?prep_id=210744
    - [Makha Bucha]
        https://www.onab.go.th/th/content/category/detail/id/73/iid/3403
    - [Visakha Bucha]
        https://www.onab.go.th/th/content/category/detail/id/73/iid/3401
    - [Asarnha Bucha]
        https://www.onab.go.th/th/content/category/detail/id/73/iid/3397
    - [Buddhist Lent Day]
        https://www.onab.go.th/th/content/category/detail/id/73/iid/3395
    - [Royal Ploughing Ceremony]
        https://en.wikipedia.org/wiki/Royal_Ploughing_Ceremony
        https://www.lib.ru.ac.th/journal/may/may_phauchmongkol.html
        https://www.myhora.com/ปฏิทิน/ปฏิทิน-พ.ศ.2540.aspx
    - [Royal Thai Armed Forces Day]
        https://th.wikipedia.org/wiki/วันกองทัพไทย
    - [Teacher's Day]
        https://www.cabinet.soc.go.th/doc_image/2500/718941.pdf

        !!! If Public Holiday falls on weekends, (in lieu) on workday !!!
        Despite the wording, this usually only applies to Monday only for
        holidays, consecutive holidays all have their own special in lieu
        declared separately.
        Data from 1992-1994 and 1998-2000 are declared discretely in
        special_holidays declarations above.
        Applied Automatically for Monday if on Weekends: 1961-1973
         **NOTE: No New Year's Eve (in lieu) for this period
        No In Lieu days available: 1974-1988
        Case-by-Case application for Workday if on Weekends: 1989-1994
        Applied Automatically for Workday if on Weekends: 1995-1997
        Case-by-Case application for Workday if on Weekends: 1998-2000
        Applied Automatically for Workday if on Weekends: 2001-Present

    Limitations:

    - This is only 100% accurate for 1997-2023; any future dates are up to the
      Royal Thai Government Gazette which updates on a year-by-year basis.

    - Approx. date only goes as far back as 1941 (B.E. 2484) as the Thai
      calendar for B.E. 2483 as we only have nine months from switching
      New Year Date (April 1st to January 1st).

    - Thai Lunar Calendar Holidays only work from 1941 (B.E. 2484) onwards
      until 2057 (B.E. 2600) as we only have Thai year-type data for
      cross-checking until then.

    - Royal Ploughing Ceremony Day is date is announced on an annual basis
      by the Court Astrologers, thus need an annual update to the library here

    - This doesn't cover Thai regional public holidays yet, only stubs added


    Country created by: `arkid15r <https://github.com/arkid15r>`__

    Country maintained by: `PPsyrius <https://github.com/PPsyrius>`__
    """
    country: str
    supported_categories: Incomplete
    default_language: str
    observed_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class TH(Thailand): ...
class THA(Thailand): ...

class ThailandStaticHolidays:
    thai_special_in_lieu_holidays: Incomplete
    thai_election: Incomplete
    thai_election_in_lieu: Incomplete
    thai_bridge_public_holiday: Incomplete
    rama_ix_golden_jubilee: Incomplete
    rama_ix_sixty_accession: Incomplete
    thai_military_emergency_lockdown: Incomplete
    thai_political_emergency_lockdown: Incomplete
    thai_flood_2011_emergency_lockdown: Incomplete
    rama_ix_mourning: Incomplete
    rama_ix_cremation: Incomplete
    rama_x_coronation_celebrations: Incomplete
    songkran_festival_in_lieu_covid: Incomplete
    special_public_holidays: Incomplete
