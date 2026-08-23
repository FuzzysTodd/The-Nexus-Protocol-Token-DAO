from _typeshed import Incomplete
from holidays.calendars.gregorian import AUG as AUG, DEC as DEC, SEP as SEP
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase as ObservedHolidayBase, SUN_TO_NEXT_MON as SUN_TO_NEXT_MON, THU_TO_NEXT_FRI as THU_TO_NEXT_FRI, TUE_TO_PREV_MON as TUE_TO_PREV_MON

class Angola(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Angola
    - http://www.siac.gv.ao/downloads/181029-Lei-Feriados.pdf
    - [Decree #5/75] https://www.lexlink.eu/FileGet.aspx?FileId=3023486
    - [Decree #92/80] https://www.lexlink.eu/FileGet.aspx?FileId=3023473
    - [Decree #7/92] https://www.lexlink.eu/FileGet.aspx?FileId=3023485
    - [Law #16/96] https://www.lexlink.eu/FileGet.aspx?FileId=3037036
    - [Law #1/01] https://www.lexlink.eu/FileGet.aspx?FileId=3029035
    - [Law #7/03] https://www.lexlink.eu/FileGet.aspx?FileId=3002131
    - [Law #10/11] https://equadros.gov.ao/documents/40468/0/lei_10_11-1+%281%29.pdf
    - [Law #11/18] https://equadros.gov.ao/documents/40468/0/Lei_no_11-18+%281%29.pdf
    - https://www.officeholidays.com/countries/angola/
    - https://www.timeanddate.com/holidays/angola/
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    observed_label: Incomplete
    special_holidays: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class AO(Angola): ...
class AGO(Angola): ...
