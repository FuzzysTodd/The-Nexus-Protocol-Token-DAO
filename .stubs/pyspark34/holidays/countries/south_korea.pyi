from _typeshed import Incomplete
from holidays.calendars import _CustomChineseHolidays
from holidays.calendars.gregorian import APR as APR, AUG as AUG, FEB as FEB, JAN as JAN, JUN as JUN, MAR as MAR, MAY as MAY, SAT as SAT, SEP as SEP, SUN as SUN
from holidays.constants import BANK as BANK, PUBLIC as PUBLIC
from holidays.groups import ChineseCalendarHolidays as ChineseCalendarHolidays, ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class SouthKorea(HolidayBase, ChineseCalendarHolidays, ChristianHolidays, InternationalHolidays):
    """
    1. https://publicholidays.co.kr/ko/2020-dates/
    2. https://en.wikipedia.org/wiki/Public_holidays_in_South_Korea
    3. https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EA%B4%80%EA%B3%B5%EC%84%9C%EC%9D%98%20%EA%B3%B5%ED%9C%B4%EC%9D%BC%EC%97%90%20%EA%B4%80%ED%95%9C%20%EA%B7%9C%EC%A0%95  # noqa

    According to (3), the alt holidays in Korea are as follows:
    The alt holiday means next first non holiday after the holiday.
    Independence movement day, Liberation day, National Foundation Day,
    Hangul Day, Children's Day, Birthday of the Buddha, Christmas Day have alt holiday if they fell on Saturday or Sunday.
    Lunar New Year's Day, Korean Mid Autumn Day have alt holiday if they fell
    on only sunday.

    """
    country: str
    supported_categories: Incomplete
    special_public_holidays: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class Korea(SouthKorea):
    def __init__(self, *args, **kwargs) -> None: ...

class KR(SouthKorea): ...
class KOR(SouthKorea): ...

class SouthKoreaLunisolarHolidays(_CustomChineseHolidays):
    BUDDHA_BIRTHDAY_DATES: Incomplete
    LUNAR_NEW_YEAR_DATES: Incomplete
    MID_AUTUMN_DATES: Incomplete
