from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, JUL as JUL, JUN as JUN, MAR as MAR
from holidays.constants import GOVERNMENT as GOVERNMENT, OPTIONAL as OPTIONAL, PUBLIC as PUBLIC
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ALL_TO_NEAREST_MON as ALL_TO_NEAREST_MON, ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_MON as SAT_SUN_TO_NEXT_MON, SAT_SUN_TO_NEXT_MON_TUE as SAT_SUN_TO_NEXT_MON_TUE, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE as SUN_TO_NEXT_TUE

class Canada(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Canada
    - https://web.archive.org/web/20130703014214/http://www.hrsdc.gc.ca/eng/labour/overviews/employment_standards/holidays.shtml  # noqa: E501
    - https://www.alberta.ca/alberta-general-holidays
    - https://www2.gov.bc.ca/gov/content/employment-business/employment-standards-advice/employment-standards/statutory-holidays  # noqa: E501
    - http://web2.gov.mb.ca/laws/statutes/ccsm/r120e.php
    - https://www2.gnb.ca/content/gnb/en/departments/elg/local_government/content/governance/content/days_of_rest_act.html  # noqa: E501
    - https://www.ontario.ca/document/your-guide-employment-standards-act-0/public-holidays
    - https://www.officeholidays.com/countries/canada/
    - https://www.timeanddate.com/holidays/canada/
    """
    country: str
    default_language: str
    observed_label: Incomplete
    supported_categories: Incomplete
    subdivisions: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class CA(Canada): ...
class CAN(Canada): ...
