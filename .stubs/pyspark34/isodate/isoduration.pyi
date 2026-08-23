from _typeshed import Incomplete
from isodate.duration import Duration as Duration
from isodate.isodatetime import parse_datetime as parse_datetime
from isodate.isoerror import ISO8601Error as ISO8601Error
from isodate.isostrf import D_DEFAULT as D_DEFAULT, strftime as strftime

ISO8601_PERIOD_REGEX: Incomplete

def parse_duration(datestring):
    """
    Parses an ISO 8601 durations into datetime.timedelta or Duration objects.

    If the ISO date string does not contain years or months, a timedelta
    instance is returned, else a Duration instance is returned.

    The following duration formats are supported:
      -PnnW                  duration in weeks
      -PnnYnnMnnDTnnHnnMnnS  complete duration specification
      -PYYYYMMDDThhmmss      basic alternative complete date format
      -PYYYY-MM-DDThh:mm:ss  extended alternative complete date format
      -PYYYYDDDThhmmss       basic alternative ordinal date format
      -PYYYY-DDDThh:mm:ss    extended alternative ordinal date format

    The '-' is optional.

    Limitations:  ISO standard defines some restrictions about where to use
      fractional numbers and which component and format combinations are
      allowed. This parser implementation ignores all those restrictions and
      returns something when it is able to find all necessary components.
      In detail:
        it does not check, whether only the last component has fractions.
        it allows weeks specified with all other combinations

      The alternative format does not support durations with years, months or
      days set to 0.
    """
def duration_isoformat(tduration, format=...):
    """
    Format duration strings.

    This method is just a wrapper around isodate.isostrf.strftime and uses
    P%P (D_DEFAULT) as default format.
    """
