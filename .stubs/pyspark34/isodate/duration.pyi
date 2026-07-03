from _typeshed import Incomplete

def fquotmod(val, low, high):
    """
    A divmod function with boundaries.

    """
def max_days_in_month(year, month):
    """
    Determines the number of days of a specific month in a specific year.
    """

class Duration:
    """
    A class which represents a duration.

    The difference to datetime.timedelta is, that this class handles also
    differences given in years and months.
    A Duration treats differences given in year, months separately from all
    other components.

    A Duration can be used almost like any timedelta object, however there
    are some restrictions:
      * It is not really possible to compare Durations, because it is unclear,
        whether a duration of 1 year is bigger than 365 days or not.
      * Equality is only tested between the two (year, month vs. timedelta)
        basic components.

    A Duration can also be converted into a datetime object, but this requires
    a start date or an end date.

    The algorithm to add a duration to a date is defined at
    http://www.w3.org/TR/xmlschema-2/#adding-durations-to-dateTimes
    """
    months: Incomplete
    years: Incomplete
    tdelta: Incomplete
    def __init__(self, days: int = 0, seconds: int = 0, microseconds: int = 0, milliseconds: int = 0, minutes: int = 0, hours: int = 0, weeks: int = 0, months: int = 0, years: int = 0) -> None:
        """
        Initialise this Duration instance with the given parameters.
        """
    def __getattr__(self, name):
        """
        Provide direct access to attributes of included timedelta instance.
        """
    def __hash__(self):
        """
        Return a hash of this instance so that it can be used in, for
        example, dicts and sets.
        """
    def __neg__(self):
        """
        A simple unary minus.

        Returns a new Duration instance with all it's negated.
        """
    def __add__(self, other):
        """
        Durations can be added with Duration, timedelta, date and datetime
        objects.
        """
    __radd__ = __add__
    def __mul__(self, other): ...
    __rmul__ = __mul__
    def __sub__(self, other):
        """
        It is possible to subtract Duration and timedelta objects from Duration
        objects.
        """
    def __rsub__(self, other):
        """
        It is possible to subtract Duration objecs from date, datetime and
        timedelta objects.

        TODO: there is some weird behaviour in date - timedelta ...
              if timedelta has seconds or microseconds set, then
              date - timedelta != date + (-timedelta)
              for now we follow this behaviour to avoid surprises when mixing
              timedeltas with Durations, but in case this ever changes in
              the stdlib we can just do:
                return -self + other
              instead of all the current code
        """
    def __eq__(self, other):
        """
        If the years, month part and the timedelta part are both equal, then
        the two Durations are considered equal.
        """
    def __ne__(self, other):
        """
        If the years, month part or the timedelta part is not equal, then
        the two Durations are considered not equal.
        """
    def totimedelta(self, start: Incomplete | None = None, end: Incomplete | None = None):
        """
        Convert this duration into a timedelta object.

        This method requires a start datetime or end datetimem, but raises
        an exception if both are given.
        """
