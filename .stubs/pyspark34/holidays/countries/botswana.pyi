from _typeshed import Incomplete
from holidays.calendars.gregorian import JUL as JUL
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE as SUN_TO_NEXT_TUE

class Botswana(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://www.gov.bw/public-holidays
    https://publicholidays.africa/botswana/2021-dates/
    https://www.timeanddate.com/holidays/botswana/
    http://www.ilo.org/dyn/travail/docs/1766/Public%20Holidays%20Act.pdf
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class BW(Botswana): ...
class BWA(Botswana): ...

class BotswanaStaticHolidays:
    special_holidays: Incomplete
