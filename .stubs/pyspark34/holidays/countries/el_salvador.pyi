from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class ElSalvador(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
    - https://www.transparencia.gob.sv/institutions/gd-usulutan/documents/192280/download
    - https://www.timeanddate.com/holidays/el-salvador
    - https://www.officeholidays.com/countries/el-salvador
    """
    country: str
    subdivisions: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class SV(ElSalvador): ...
class SLV(ElSalvador): ...
