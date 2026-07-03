import datetime
from _typeshed import Incomplete
from pytz.exceptions import AmbiguousTimeError as AmbiguousTimeError, InvalidTimeError as InvalidTimeError, NonExistentTimeError as NonExistentTimeError, UnknownTimeZoneError as UnknownTimeZoneError
from pytz.lazy import LazyDict
from pytz.tzinfo import BaseTzInfo as BaseTzInfo

__all__ = ['timezone', 'utc', 'country_timezones', 'country_names', 'AmbiguousTimeError', 'InvalidTimeError', 'NonExistentTimeError', 'UnknownTimeZoneError', 'all_timezones', 'all_timezones_set', 'common_timezones', 'common_timezones_set', 'BaseTzInfo', 'FixedOffset']

__version__ = VERSION
OLSEN_VERSION = OLSON_VERSION
unicode = str

def timezone(zone):
    """ Return a datetime.tzinfo implementation for the given timezone

    >>> from datetime import datetime, timedelta
    >>> utc = timezone('UTC')
    >>> eastern = timezone('US/Eastern')
    >>> eastern.zone
    'US/Eastern'
    >>> timezone(unicode('US/Eastern')) is eastern
    True
    >>> utc_dt = datetime(2002, 10, 27, 6, 0, 0, tzinfo=utc)
    >>> loc_dt = utc_dt.astimezone(eastern)
    >>> fmt = '%Y-%m-%d %H:%M:%S %Z (%z)'
    >>> loc_dt.strftime(fmt)
    '2002-10-27 01:00:00 EST (-0500)'
    >>> (loc_dt - timedelta(minutes=10)).strftime(fmt)
    '2002-10-27 00:50:00 EST (-0500)'
    >>> eastern.normalize(loc_dt - timedelta(minutes=10)).strftime(fmt)
    '2002-10-27 01:50:00 EDT (-0400)'
    >>> (loc_dt + timedelta(minutes=10)).strftime(fmt)
    '2002-10-27 01:10:00 EST (-0500)'

    Raises UnknownTimeZoneError if passed an unknown zone.

    >>> try:
    ...     timezone('Asia/Shangri-La')
    ... except UnknownTimeZoneError:
    ...     print('Unknown')
    Unknown

    >>> try:
    ...     timezone(unicode('\\N{TRADE MARK SIGN}'))
    ... except UnknownTimeZoneError:
    ...     print('Unknown')
    Unknown

    """

class UTC(BaseTzInfo):
    """UTC

    Optimized UTC implementation. It unpickles using the single module global
    instance defined beneath this class declaration.
    """
    zone: str
    def fromutc(self, dt): ...
    def utcoffset(self, dt): ...
    def tzname(self, dt): ...
    def dst(self, dt): ...
    def __reduce__(self): ...
    def localize(self, dt, is_dst: bool = False):
        """Convert naive time to local time"""
    def normalize(self, dt, is_dst: bool = False):
        """Correct the timezone information on the given datetime"""

utc: Incomplete

class _CountryTimezoneDict(LazyDict):
    """Map ISO 3166 country code to a list of timezone names commonly used
    in that country.

    iso3166_code is the two letter code used to identify the country.

    >>> def print_list(list_of_strings):
    ...     'We use a helper so doctests work under Python 2.3 -> 3.x'
    ...     for s in list_of_strings:
    ...         print(s)

    >>> print_list(country_timezones['nz'])
    Pacific/Auckland
    Pacific/Chatham
    >>> print_list(country_timezones['ch'])
    Europe/Zurich
    >>> print_list(country_timezones['CH'])
    Europe/Zurich
    >>> print_list(country_timezones[unicode('ch')])
    Europe/Zurich
    >>> print_list(country_timezones['XXX'])
    Traceback (most recent call last):
    ...
    KeyError: 'XXX'

    Previously, this information was exposed as a function rather than a
    dictionary. This is still supported::

    >>> print_list(country_timezones('nz'))
    Pacific/Auckland
    Pacific/Chatham
    """
    def __call__(self, iso3166_code):
        """Backwards compatibility."""

country_timezones: Incomplete

class _CountryNameDict(LazyDict):
    """Dictionary proving ISO3166 code -> English name.

    >>> print(country_names['au'])
    Australia
    """

country_names: Incomplete

class _FixedOffset(datetime.tzinfo):
    zone: Incomplete
    def __init__(self, minutes) -> None: ...
    def utcoffset(self, dt): ...
    def __reduce__(self): ...
    def dst(self, dt): ...
    def tzname(self, dt) -> None: ...
    def localize(self, dt, is_dst: bool = False):
        """Convert naive time to local time"""
    def normalize(self, dt, is_dst: bool = False):
        """Correct the timezone information on the given datetime"""

def FixedOffset(offset, _tzinfos={}):
    """return a fixed-offset timezone based off a number of minutes.

        >>> one = FixedOffset(-330)
        >>> one
        pytz.FixedOffset(-330)
        >>> str(one.utcoffset(datetime.datetime.now()))
        '-1 day, 18:30:00'
        >>> str(one.dst(datetime.datetime.now()))
        '0:00:00'

        >>> two = FixedOffset(1380)
        >>> two
        pytz.FixedOffset(1380)
        >>> str(two.utcoffset(datetime.datetime.now()))
        '23:00:00'
        >>> str(two.dst(datetime.datetime.now()))
        '0:00:00'

    The datetime.timedelta must be between the range of -1 and 1 day,
    non-inclusive.

        >>> FixedOffset(1440)
        Traceback (most recent call last):
        ...
        ValueError: ('absolute offset is too large', 1440)

        >>> FixedOffset(-1440)
        Traceback (most recent call last):
        ...
        ValueError: ('absolute offset is too large', -1440)

    An offset of 0 is special-cased to return UTC.

        >>> FixedOffset(0) is UTC
        True

    There should always be only one instance of a FixedOffset per timedelta.
    This should be true for multiple creation calls.

        >>> FixedOffset(-330) is one
        True
        >>> FixedOffset(1380) is two
        True

    It should also be true for pickling.

        >>> import pickle
        >>> pickle.loads(pickle.dumps(one)) is one
        True
        >>> pickle.loads(pickle.dumps(two)) is two
        True
    """

all_timezones: Incomplete
all_timezones_set: Incomplete
common_timezones: Incomplete
common_timezones_set: Incomplete
