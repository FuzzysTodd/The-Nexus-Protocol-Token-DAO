from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Mexico(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Mexico
    - https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_festivos_en_M%C3%A9xico
    - https://www.gob.mx/cms/uploads/attachment/file/156203/1044_Ley_Federal_del_Trabajo.pdf
    - http://www.diputados.gob.mx/LeyesBiblio/ref/lft/LFT_orig_01abr70_ima.pdf
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class MX(Mexico): ...
class MEX(Mexico): ...
