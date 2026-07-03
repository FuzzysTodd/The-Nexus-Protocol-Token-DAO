from _typeshed import Incomplete
from isodate.isoerror import ISO8601Error as ISO8601Error
from isodate.tzinfo import FixedOffset as FixedOffset, UTC as UTC, ZERO as ZERO

TZ_REGEX: str
TZ_RE: Incomplete

def build_tzinfo(tzname, tzsign: str = '+', tzhour: int = 0, tzmin: int = 0):
    """
    create a tzinfo instance according to given parameters.

    tzname:
      'Z'       ... return UTC
      '' | None ... return None
      other     ... return FixedOffset
    """
def parse_tzinfo(tzstring):
    """
    Parses ISO 8601 time zone designators to tzinfo objecs.

    A time zone designator can be in the following format:
              no designator indicates local time zone
      Z       UTC
      +-hhmm  basic hours and minutes
      +-hh:mm extended hours and minutes
      +-hh    hours
    """
def tz_isoformat(dt, format: str = '%Z'):
    """
    return time zone offset ISO 8601 formatted.
    The various ISO formats can be chosen with the format parameter.

    if tzinfo is None returns ''
    if tzinfo is UTC returns 'Z'
    else the offset is rendered to the given format.
    format:
        %h ... +-HH
        %z ... +-HHMM
        %Z ... +-HH:MM
    """
