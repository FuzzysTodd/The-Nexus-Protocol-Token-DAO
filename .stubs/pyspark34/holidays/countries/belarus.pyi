from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, DEC as DEC, GREGORIAN_CALENDAR as GREGORIAN_CALENDAR, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, NOV as NOV
from holidays.calendars.julian import JULIAN_CALENDAR as JULIAN_CALENDAR
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Belarus(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    Belarus holidays.

    References:
     - http://president.gov.by/en/holidays_en/
     - http://www.belarus.by/en/about-belarus/national-holidays
     - http://laws.newsby.org/documents/ukazp/pos05/ukaz05806.htm
     - http://president.gov.by/uploads/documents/2019/464uk.pdf
     - https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B0%D0%B7%D0%B4%D0%BD%D0%B8%D0%BA%D0%B8_%D0%91%D0%B5%D0%BB%D0%BE%D1%80%D1%83%D1%81%D1%81%D0%B8%D0%B8  # noqa: E501
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class BY(Belarus): ...
class BLR(Belarus): ...

class BelarusStaticHolidays:
    substituted_date_format: Incomplete
    substituted_label: Incomplete
    substituted_holidays: Incomplete
