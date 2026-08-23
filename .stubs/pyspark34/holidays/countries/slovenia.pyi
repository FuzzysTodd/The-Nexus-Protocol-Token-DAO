from _typeshed import Incomplete
from holidays.calendars.gregorian import AUG as AUG
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Slovenia(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    Contains all work-free public holidays in Slovenia.
    No holidays are returned before year 1991 when Slovenia became independent
    country. Before that Slovenia was part of Socialist federal republic of
    Yugoslavia.

    List of holidays (including those that are not work-free:
    https://en.wikipedia.org/wiki/Public_holidays_in_Slovenia
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class SI(Slovenia): ...
class SVN(Slovenia): ...

class SloveniaStaticHolidays:
    special_holidays: Incomplete
