from _typeshed import Incomplete
from holidays.calendars.gregorian import DEC as DEC, JAN as JAN
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON

class Monaco(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Monaco
    https://en.service-public-entreprises.gouv.mc/Employment-and-social-affairs/Employment-regulations/Leave/Public-Holidays  # noqa: E501
    """
    country: str
    default_language: str
    observed_label: Incomplete
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class MC(Monaco): ...
class MCO(Monaco): ...

class MonacoStaticHolidays:
    special_holidays: Incomplete
