from _typeshed import Incomplete
from holidays.calendars.gregorian import APR as APR, AUG as AUG, DEC as DEC, FEB as FEB, JAN as JAN, JUL as JUL, JUN as JUN, MAR as MAR, MAY as MAY, MON as MON, NOV as NOV, OCT as OCT, SEP as SEP
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays, StaticHolidays as StaticHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class NewYorkStockExchange(HolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    Official regulations:
    - https://www.nyse.com/publicdocs/nyse/regulation/nyse/NYSE_Rules.pdf
    - https://www.nyse.com/markets/hours-calendars
    Historical data:
    - s3.amazonaws.com/armstrongeconomics-wp/2013/07/NYSE-Closings.pdf
    - https://web.archive.org/web/20211101162021/https://www.nyse.com/markets/hours-calendars
    """
    market: str
    def __init__(self, *args, **kwargs) -> None: ...

class XNYS(NewYorkStockExchange): ...
class NYSE(NewYorkStockExchange): ...

class NewYorkStockExchangeStaticHolidays:
    special_holidays: Incomplete
