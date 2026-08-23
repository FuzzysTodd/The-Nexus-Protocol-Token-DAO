from isodate.isodates import parse_date as parse_date
from isodate.isoerror import ISO8601Error as ISO8601Error
from isodate.isostrf import DATE_EXT_COMPLETE as DATE_EXT_COMPLETE, TIME_EXT_COMPLETE as TIME_EXT_COMPLETE, TZ_EXT as TZ_EXT, strftime as strftime
from isodate.isotime import parse_time as parse_time

def parse_datetime(datetimestring):
    """
    Parses ISO 8601 date-times into datetime.datetime objects.

    This function uses parse_date and parse_time to do the job, so it allows
    more combinations of date and time representations, than the actual
    ISO 8601:2004 standard allows.
    """
def datetime_isoformat(tdt, format=...):
    """
    Format datetime strings.

    This method is just a wrapper around isodate.isostrf.strftime and uses
    Extended-Complete as default format.
    """
