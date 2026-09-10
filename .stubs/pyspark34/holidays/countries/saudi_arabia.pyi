from _typeshed import Incomplete
from holidays.calendars.gregorian import FEB as FEB, FRI as FRI, NOV as NOV, SAT as SAT, SEP as SEP, THU as THU
from holidays.groups import IslamicHolidays as IslamicHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import FRI_SAT_TO_NEXT_WORKDAY as FRI_SAT_TO_NEXT_WORKDAY, FRI_TO_NEXT_SAT as FRI_TO_NEXT_SAT, FRI_TO_PREV_THU as FRI_TO_PREV_THU, ObservedHolidayBase as ObservedHolidayBase, SAT_TO_NEXT_SUN as SAT_TO_NEXT_SUN, THU_FRI_TO_NEXT_WORKDAY as THU_FRI_TO_NEXT_WORKDAY, THU_TO_PREV_WED as THU_TO_PREV_WED

class SaudiArabia(ObservedHolidayBase, IslamicHolidays, StaticHolidays):
    """
    There are only 4 official national holidays in Saudi:
    https://laboreducation.hrsd.gov.sa/en/gallery/274
    https://laboreducation.hrsd.gov.sa/en/labor-education/322
    https://english.alarabiya.net/News/gulf/2022/01/27/Saudi-Arabia-to-commemorate-Founding-Day-on-Feb-22-annually-Royal-order
    The national day and the founding day holidays are based on the
    Georgian calendar while the other two holidays are based on the
    Islamic Calendar, and they are estimates as they announced each
    year and based on moon sightings;
    they are:
        - Eid al-Fitr
        - Eid al-Adha
    """
    country: str
    default_language: str
    estimated_label: Incomplete
    observed_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class SA(SaudiArabia): ...
class SAU(SaudiArabia): ...

class SaudiArabiaStaticHolidays:
    special_holidays: Incomplete
