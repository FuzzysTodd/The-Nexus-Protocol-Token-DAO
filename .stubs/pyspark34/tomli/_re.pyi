import re
from ._types import ParseFloat as ParseFloat
from _typeshed import Incomplete
from datetime import date, datetime, time, timezone
from typing import Any

RE_NUMBER: Incomplete
RE_LOCALTIME: Incomplete
RE_DATETIME: Incomplete

def match_to_datetime(match: re.Match) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
def cached_tz(hour_str: str, minute_str: str, sign_str: str) -> timezone: ...
def match_to_localtime(match: re.Match) -> time: ...
def match_to_number(match: re.Match, parse_float: ParseFloat) -> Any: ...
