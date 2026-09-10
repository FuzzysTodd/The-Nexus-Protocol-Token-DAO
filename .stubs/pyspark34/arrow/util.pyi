import datetime
from typing import Any

__all__ = ['next_weekday', 'is_timestamp', 'validate_ordinal', 'iso_to_gregorian']

def next_weekday(start_date: datetime.date | None, weekday: int) -> datetime.datetime:
    """Get next weekday from the specified start date.

    :param start_date: Datetime object representing the start date.
    :param weekday: Next weekday to obtain. Can be a value between 0 (Monday) and 6 (Sunday).
    :return: Datetime object corresponding to the next weekday after start_date.

    Usage::

        # Get first Monday after epoch
        >>> next_weekday(datetime(1970, 1, 1), 0)
        1970-01-05 00:00:00

        # Get first Thursday after epoch
        >>> next_weekday(datetime(1970, 1, 1), 3)
        1970-01-01 00:00:00

        # Get first Sunday after epoch
        >>> next_weekday(datetime(1970, 1, 1), 6)
        1970-01-04 00:00:00
    """
def is_timestamp(value: Any) -> bool:
    """Check if value is a valid timestamp."""
def validate_ordinal(value: Any) -> None:
    """Raise an exception if value is an invalid Gregorian ordinal.

    :param value: the input to be checked

    """
def iso_to_gregorian(iso_year: int, iso_week: int, iso_day: int) -> datetime.date:
    """Converts an ISO week date into a datetime object.

    :param iso_year: the year
    :param iso_week: the week number, each year has either 52 or 53 weeks
    :param iso_day: the day numbered 1 through 7, beginning with Monday

    """
