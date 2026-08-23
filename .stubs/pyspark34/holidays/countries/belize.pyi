from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import FRI_SUN_TO_NEXT_MON as FRI_SUN_TO_NEXT_MON, ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON, TUE_WED_THU_TO_PREV_MON as TUE_WED_THU_TO_PREV_MON

class Belize(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Belize
      - http://www.belizelaw.org/web/lawadmin/PDF%20files/cap289.pdf
      - https://www.pressoffice.gov.bz/public-and-bank-holidays-2022-updated/
      - https://www.pressoffice.gov.bz/government-of-belize-establishes-new-public-and-bank-holidays/  # noqa: E501
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class BZ(Belize): ...
class BLZ(Belize): ...
