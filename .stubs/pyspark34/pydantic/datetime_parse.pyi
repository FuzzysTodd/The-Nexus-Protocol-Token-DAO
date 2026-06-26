from . import errors as errors
from _typeshed import Incomplete
from datetime import date, datetime, time, timedelta

date_expr: str
time_expr: str
date_re: Incomplete
time_re: Incomplete
datetime_re: Incomplete
standard_duration_re: Incomplete
iso8601_duration_re: Incomplete
EPOCH: Incomplete
MS_WATERSHED: Incomplete
MAX_NUMBER: Incomplete
StrBytesIntFloat = str | bytes | int | float

def get_numeric(value: StrBytesIntFloat, native_expected_type: str) -> None | int | float: ...
def from_unix_seconds(seconds: int | float) -> datetime: ...
def parse_date(value: date | StrBytesIntFloat) -> date:
    """
    Parse a date/int/float/string and return a datetime.date.

    Raise ValueError if the input is well formatted but not a valid date.
    Raise ValueError if the input isn't well formatted.
    """
def parse_time(value: time | StrBytesIntFloat) -> time:
    """
    Parse a time/string and return a datetime.time.

    Raise ValueError if the input is well formatted but not a valid time.
    Raise ValueError if the input isn't well formatted, in particular if it contains an offset.
    """
def parse_datetime(value: datetime | StrBytesIntFloat) -> datetime:
    """
    Parse a datetime/int/float/string and return a datetime.datetime.

    This function supports time zone offsets. When the input contains one,
    the output uses a timezone with a fixed offset from UTC.

    Raise ValueError if the input is well formatted but not a valid datetime.
    Raise ValueError if the input isn't well formatted.
    """
def parse_duration(value: StrBytesIntFloat) -> timedelta:
    """
    Parse a duration int/float/string and return a datetime.timedelta.

    The preferred format for durations in Django is '%d %H:%M:%S.%f'.

    Also supports ISO 8601 representation.
    """
