from _typeshed import Incomplete
from datetime import tzinfo

ZERO: Incomplete

class Utc(tzinfo):
    """UTC

    Universal time coordinated time zone.
    """
    def utcoffset(self, dt):
        """
        Return offset from UTC in minutes east of UTC, which is ZERO for UTC.
        """
    def tzname(self, dt):
        """
        Return the time zone name corresponding to the datetime object dt,
        as a string.
        """
    def dst(self, dt):
        """
        Return the daylight saving time (DST) adjustment, in minutes east
        of UTC.
        """
    def __reduce__(self):
        """
        When unpickling a Utc object, return the default instance below, UTC.
        """

UTC: Incomplete

class FixedOffset(tzinfo):
    '''
    A class building tzinfo objects for fixed-offset time zones.

    Note that FixedOffset(0, 0, "UTC") or FixedOffset() is a different way to
    build a UTC tzinfo object.
    '''
    def __init__(self, offset_hours: int = 0, offset_minutes: int = 0, name: str = 'UTC') -> None:
        """
        Initialise an instance with time offset and name.
        The time offset should be positive for time zones east of UTC
        and negate for time zones west of UTC.
        """
    def utcoffset(self, dt):
        """
        Return offset from UTC in minutes of UTC.
        """
    def tzname(self, dt):
        """
        Return the time zone name corresponding to the datetime object dt, as a
        string.
        """
    def dst(self, dt):
        """
        Return the daylight saving time (DST) adjustment, in minutes east of
        UTC.
        """

STDOFFSET: Incomplete
DSTOFFSET: Incomplete
DSTOFFSET = STDOFFSET
DSTDIFF: Incomplete

class LocalTimezone(tzinfo):
    """
    A class capturing the platform's idea of local time.
    """
    def utcoffset(self, dt):
        """
        Return offset from UTC in minutes of UTC.
        """
    def dst(self, dt):
        """
        Return daylight saving offset.
        """
    def tzname(self, dt):
        """
        Return the time zone name corresponding to the datetime object dt, as a
        string.
        """

LOCAL: Incomplete
