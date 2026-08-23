from _typeshed import Incomplete
from holidays.groups import ChristianHolidays as ChristianHolidays, InternationalHolidays as InternationalHolidays
from holidays.holiday_base import HolidayBase as HolidayBase

class Malta(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://www.gov.mt/en/About%20Malta/Pages/Public%20Holidays.aspx

    [Att 10 tal-1980]
        Oldest Maltese Holidays Law available online in full.
        https://legislation.mt/eli/act/1980/10/mlt
    [A.L. 40 tal-1987]
        Additional Holidays added.
        https://legislation.mt/eli/ln/1987/8/mlt
    [Att 8 tal-1989]
        Additional Holidays added.
        https://legislation.mt/eli/act/1989/8
    [Att 2 tal-2005]
        If fall on weekends then not observed in terms of vacation leave.
        https://legislation.mt/eli/act/2005/2/eng
    [Att 4 tal-2021]
        Revert Act II of 2005 changes for vacation leave.
        https://legislation.mt/eli/cap/252/20210212/mlt
    """
    country: str
    default_language: str
    supported_languages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class MT(Malta): ...
class MLT(Malta): ...
