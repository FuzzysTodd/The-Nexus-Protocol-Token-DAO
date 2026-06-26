from holidays.calendars.gregorian import DEC as DEC
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import FRI_TO_PREV_THU as FRI_TO_PREV_THU, MON_TO_NEXT_TUE as MON_TO_NEXT_TUE, ObservedHolidayBase as ObservedHolidayBase, SAT_SUN_TO_NEXT_MON as SAT_SUN_TO_NEXT_MON, SAT_SUN_TO_PREV_FRI as SAT_SUN_TO_PREV_FRI, SAT_TO_PREV_FRI as SAT_TO_PREV_FRI, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON
from typing import Tuple

class UnitedStates(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_the_United_States

    For Northern Mariana Islands (subdivision MP):
    - https://governor.gov.mp/archived-news/executive-actions-archive/memorandum-2022-legal-holidays/  # noqa: E501
    - https://webcache.googleusercontent.com/search?q=cache:C17_7FBgPtQJ:https://governor.gov.mp/archived-news/executive-actions-archive/memorandum-2022-legal-holidays/&hl=en&gl=sg&strip=1&vwsrc=0  # noqa: E501

    Columbus Day / Indigenous Peoples' Day history:
    - https://www.pewresearch.org/short-reads/2023/10/05/working-on-columbus-day-or-indigenous-peoples-day-it-depends-on-where-your-job-is/  # noqa: E501
    - https://www.officeholidays.com/holidays/usa/columbus-day-state-guide
    - https://en.wikipedia.org/wiki/Indigenous_Peoples%27_Day_(United_States)
    - https://www.sos.ri.gov/divisions/civics-and-education/reference-desk/ri-state-holidays
    - https://web.archive.org/web/20080831103521/http://www.dpa.ca.gov/personnel-policies/holidays.htm  # noqa: E501

    """
    country: str
    observed_label: str
    subdivisions: Tuple | Tuple[str, ...]
    def __init__(self, *args, **kwargs) -> None: ...

class US(UnitedStates): ...
class USA(UnitedStates): ...
