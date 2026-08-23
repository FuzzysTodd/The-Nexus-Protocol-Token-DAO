from _typeshed import Incomplete
from isodate.duration import Duration as Duration
from isodate.isotzinfo import tz_isoformat as tz_isoformat

DATE_BAS_COMPLETE: str
DATE_EXT_COMPLETE: str
DATE_BAS_WEEK_COMPLETE: str
DATE_EXT_WEEK_COMPLETE: str
DATE_BAS_ORD_COMPLETE: str
DATE_EXT_ORD_COMPLETE: str
DATE_BAS_WEEK: str
DATE_EXT_WEEK: str
DATE_BAS_MONTH: str
DATE_EXT_MONTH: str
DATE_YEAR: str
DATE_CENTURY: str
TIME_BAS_COMPLETE: str
TIME_EXT_COMPLETE: str
TIME_BAS_MINUTE: str
TIME_EXT_MINUTE: str
TIME_HOUR: str
TZ_BAS: str
TZ_EXT: str
TZ_HOUR: str
DT_EXT_COMPLETE: Incomplete
DT_BAS_COMPLETE: Incomplete
DT_EXT_ORD_COMPLETE: Incomplete
DT_BAS_ORD_COMPLETE: Incomplete
DT_EXT_WEEK_COMPLETE: Incomplete
DT_BAS_WEEK_COMPLETE: Incomplete
D_DEFAULT: str
D_WEEK: str
D_ALT_EXT: Incomplete
D_ALT_BAS: Incomplete
D_ALT_EXT_ORD: Incomplete
D_ALT_BAS_ORD: Incomplete
STRF_DT_MAP: Incomplete
STRF_D_MAP: Incomplete

def strftime(tdt, format, yeardigits: int = 4):
    """Directive    Meaning    Notes
    %d    Day of the month as a decimal number [01,31].
    %f    Microsecond as a decimal number [0,999999], zero-padded
          on the left (1)
    %H    Hour (24-hour clock) as a decimal number [00,23].
    %j    Day of the year as a decimal number [001,366].
    %m    Month as a decimal number [01,12].
    %M    Minute as a decimal number [00,59].
    %S    Second as a decimal number [00,61].    (3)
    %w    Weekday as a decimal number [0(Monday),6].
    %W    Week number of the year (Monday as the first day of the week)
          as a decimal number [00,53]. All days in a new year preceding the
          first Monday are considered to be in week 0.  (4)
    %Y    Year with century as a decimal number. [0000,9999]
    %C    Century as a decimal number. [00,99]
    %z    UTC offset in the form +HHMM or -HHMM (empty string if the
          object is naive).    (5)
    %Z    Time zone name (empty string if the object is naive).
    %P    ISO8601 duration format.
    %p    ISO8601 duration format in weeks.
    %%    A literal '%' character.

    """
