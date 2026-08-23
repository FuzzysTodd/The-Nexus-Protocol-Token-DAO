from _typeshed import Incomplete
from isodate.isoerror import ISO8601Error as ISO8601Error
from isodate.isostrf import TIME_EXT_COMPLETE as TIME_EXT_COMPLETE, TZ_EXT as TZ_EXT, strftime as strftime
from isodate.isotzinfo import TZ_REGEX as TZ_REGEX, build_tzinfo as build_tzinfo

TIME_REGEX_CACHE: Incomplete

def build_time_regexps():
    """
    Build regular expressions to parse ISO time string.

    The regular expressions are compiled and stored in TIME_REGEX_CACHE
    for later reuse.
    """
def parse_time(timestring):
    """
    Parses ISO 8601 times into datetime.time objects.

    Following ISO 8601 formats are supported:
      (as decimal separator a ',' or a '.' is allowed)
      hhmmss.ssTZD    basic complete time
      hh:mm:ss.ssTZD  extended compelte time
      hhmm.mmTZD      basic reduced accuracy time
      hh:mm.mmTZD     extended reduced accuracy time
      hh.hhTZD        basic reduced accuracy time
    TZD is the time zone designator which can be in the following format:
              no designator indicates local time zone
      Z       UTC
      +-hhmm  basic hours and minutes
      +-hh:mm extended hours and minutes
      +-hh    hours
    """
def time_isoformat(ttime, format=...):
    """
    Format time strings.

    This method is just a wrapper around isodate.isostrf.strftime and uses
    Time-Extended-Complete with extended time zone as default format.
    """
