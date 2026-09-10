from arrow import locales as locales
from arrow.constants import DEFAULT_LOCALE as DEFAULT_LOCALE
from arrow.util import next_weekday as next_weekday, normalize_timestamp as normalize_timestamp
from datetime import datetime, tzinfo as dt_tzinfo
from typing import ClassVar, List, Literal, Tuple, TypedDict

class ParserError(ValueError): ...
class ParserMatchError(ParserError): ...

class _Parts(TypedDict, total=False):
    year: int
    month: int
    day_of_year: int
    day: int
    hour: int
    minute: int
    second: int
    microsecond: int
    timestamp: float
    expanded_timestamp: int
    tzinfo: dt_tzinfo
    am_pm: Literal['am', 'pm']
    day_of_week: int
    weekdate: Tuple[_WEEKDATE_ELEMENT, _WEEKDATE_ELEMENT, _WEEKDATE_ELEMENT | None]

class DateTimeParser:
    SEPARATORS: ClassVar[List[str]]
    locale: locales.Locale
    def __init__(self, locale: str = ..., cache_size: int = 0) -> None: ...
    def parse_iso(self, datetime_string: str, normalize_whitespace: bool = False) -> datetime: ...
    def parse(self, datetime_string: str, fmt: List[str] | str, normalize_whitespace: bool = False) -> datetime: ...

class TzinfoParser:
    @classmethod
    def parse(cls, tzinfo_string: str) -> dt_tzinfo: ...
