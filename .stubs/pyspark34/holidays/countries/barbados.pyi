from _typeshed import Incomplete
from holidays.calendars.gregorian import JAN as JAN, JUL as JUL
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.observed_holiday_base import MON_TO_NEXT_TUE as MON_TO_NEXT_TUE, ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON, SUN_TO_NEXT_TUE as SUN_TO_NEXT_TUE

class Barbados(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Barbados
    https://www.timeanddate.com/holidays/barbados/
    [Public Holidays Act Cap.352] http://barbadosparliament-laws.com/en/showdoc/cs/352
    https://labour.gov.bb/pdf/Library/Other%20Docs/Public%20Holidays%20for%20the%20Year%202018.pdf
    https://labour.gov.bb/wp-content/uploads/2020/04/Public-Holidays-for-the-Year-2021.pdf
    https://gisbarbados.gov.bb/download/public-holidays-for-2022/
    https://gisbarbados.gov.bb/download/public-holidays-for-2023/
    """
    country: str
    observed_label: str
    def __init__(self, *args, **kwargs) -> None: ...

class BB(Barbados): ...
class BRB(Barbados): ...

class BarbadosStaticHolidays:
    special_holidays: Incomplete
