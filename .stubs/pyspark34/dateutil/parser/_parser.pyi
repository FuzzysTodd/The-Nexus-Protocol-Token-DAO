from _typeshed import Incomplete

__all__ = ['parse', 'parserinfo', 'ParserError']

class _timelex:
    instream: Incomplete
    charstack: Incomplete
    tokenstack: Incomplete
    eof: bool
    def __init__(self, instream) -> None: ...
    def get_token(self):
        '''
        This function breaks the time string into lexical units (tokens), which
        can be parsed by the parser. Lexical units are demarcated by changes in
        the character set, so any continuous string of letters is considered
        one unit, any continuous string of numbers is considered one unit.

        The main complication arises from the fact that dots (\'.\') can be used
        both as separators (e.g. "Sep.20.2009") or decimal points (e.g.
        "4:30:21.447"). As such, it is necessary to read the full context of
        any dot-separated strings before breaking it into tokens; as such, this
        function maintains a "token stack", for when the ambiguous context
        demands that multiple tokens be parsed at once.
        '''
    def __iter__(self): ...
    def __next__(self): ...
    def next(self): ...
    @classmethod
    def split(cls, s): ...
    @classmethod
    def isword(cls, nextchar):
        """ Whether or not the next character is part of a word """
    @classmethod
    def isnum(cls, nextchar):
        """ Whether the next character is part of a number """
    @classmethod
    def isspace(cls, nextchar):
        """ Whether the next character is whitespace """

class _resultbase:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...

class parserinfo:
    """
    Class which handles what inputs are accepted. Subclass this to customize
    the language and acceptable values for each parameter.

    :param dayfirst:
        Whether to interpret the first value in an ambiguous 3-integer date
        (e.g. 01/05/09) as the day (``True``) or month (``False``). If
        ``yearfirst`` is set to ``True``, this distinguishes between YDM
        and YMD. Default is ``False``.

    :param yearfirst:
        Whether to interpret the first value in an ambiguous 3-integer date
        (e.g. 01/05/09) as the year. If ``True``, the first number is taken
        to be the year, otherwise the last number is taken to be the year.
        Default is ``False``.
    """
    JUMP: Incomplete
    WEEKDAYS: Incomplete
    MONTHS: Incomplete
    HMS: Incomplete
    AMPM: Incomplete
    UTCZONE: Incomplete
    PERTAIN: Incomplete
    TZOFFSET: Incomplete
    dayfirst: Incomplete
    yearfirst: Incomplete
    def __init__(self, dayfirst: bool = False, yearfirst: bool = False) -> None: ...
    def jump(self, name): ...
    def weekday(self, name): ...
    def month(self, name): ...
    def hms(self, name): ...
    def ampm(self, name): ...
    def pertain(self, name): ...
    def utczone(self, name): ...
    def tzoffset(self, name): ...
    def convertyear(self, year, century_specified: bool = False):
        """
        Converts two-digit years to year within [-50, 49]
        range of self._year (current local time)
        """
    def validate(self, res): ...

class _ymd(list):
    century_specified: bool
    dstridx: Incomplete
    mstridx: Incomplete
    ystridx: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def has_year(self): ...
    @property
    def has_month(self): ...
    @property
    def has_day(self): ...
    def could_be_day(self, value): ...
    def append(self, val, label: Incomplete | None = None) -> None: ...
    def resolve_ymd(self, yearfirst, dayfirst): ...

class parser:
    info: Incomplete
    def __init__(self, info: Incomplete | None = None) -> None: ...
    def parse(self, timestr, default: Incomplete | None = None, ignoretz: bool = False, tzinfos: Incomplete | None = None, **kwargs):
        '''
        Parse the date/time string into a :class:`datetime.datetime` object.

        :param timestr:
            Any date/time string using the supported formats.

        :param default:
            The default datetime object, if this is a datetime object and not
            ``None``, elements specified in ``timestr`` replace elements in the
            default object.

        :param ignoretz:
            If set ``True``, time zones in parsed strings are ignored and a
            naive :class:`datetime.datetime` object is returned.

        :param tzinfos:
            Additional time zone names / aliases which may be present in the
            string. This argument maps time zone names (and optionally offsets
            from those time zones) to time zones. This parameter can be a
            dictionary with timezone aliases mapping time zone names to time
            zones or a function taking two parameters (``tzname`` and
            ``tzoffset``) and returning a time zone.

            The timezones to which the names are mapped can be an integer
            offset from UTC in seconds or a :class:`tzinfo` object.

            .. doctest::
               :options: +NORMALIZE_WHITESPACE

                >>> from dateutil.parser import parse
                >>> from dateutil.tz import gettz
                >>> tzinfos = {"BRST": -7200, "CST": gettz("America/Chicago")}
                >>> parse("2012-01-19 17:21:00 BRST", tzinfos=tzinfos)
                datetime.datetime(2012, 1, 19, 17, 21, tzinfo=tzoffset(u\'BRST\', -7200))
                >>> parse("2012-01-19 17:21:00 CST", tzinfos=tzinfos)
                datetime.datetime(2012, 1, 19, 17, 21,
                                  tzinfo=tzfile(\'/usr/share/zoneinfo/America/Chicago\'))

            This parameter is ignored if ``ignoretz`` is set.

        :param \\*\\*kwargs:
            Keyword arguments as passed to ``_parse()``.

        :return:
            Returns a :class:`datetime.datetime` object or, if the
            ``fuzzy_with_tokens`` option is ``True``, returns a tuple, the
            first element being a :class:`datetime.datetime` object, the second
            a tuple containing the fuzzy tokens.

        :raises ParserError:
            Raised for invalid or unknown string format, if the provided
            :class:`tzinfo` is not in a valid format, or if an invalid date
            would be created.

        :raises TypeError:
            Raised for non-string or character stream input.

        :raises OverflowError:
            Raised if the parsed date exceeds the largest valid C integer on
            your system.
        '''
    class _result(_resultbase): ...

def parse(timestr, parserinfo: Incomplete | None = None, **kwargs):
    '''

    Parse a string in one of the supported formats, using the
    ``parserinfo`` parameters.

    :param timestr:
        A string containing a date/time stamp.

    :param parserinfo:
        A :class:`parserinfo` object containing parameters for the parser.
        If ``None``, the default arguments to the :class:`parserinfo`
        constructor are used.

    The ``**kwargs`` parameter takes the following keyword arguments:

    :param default:
        The default datetime object, if this is a datetime object and not
        ``None``, elements specified in ``timestr`` replace elements in the
        default object.

    :param ignoretz:
        If set ``True``, time zones in parsed strings are ignored and a naive
        :class:`datetime` object is returned.

    :param tzinfos:
        Additional time zone names / aliases which may be present in the
        string. This argument maps time zone names (and optionally offsets
        from those time zones) to time zones. This parameter can be a
        dictionary with timezone aliases mapping time zone names to time
        zones or a function taking two parameters (``tzname`` and
        ``tzoffset``) and returning a time zone.

        The timezones to which the names are mapped can be an integer
        offset from UTC in seconds or a :class:`tzinfo` object.

        .. doctest::
           :options: +NORMALIZE_WHITESPACE

            >>> from dateutil.parser import parse
            >>> from dateutil.tz import gettz
            >>> tzinfos = {"BRST": -7200, "CST": gettz("America/Chicago")}
            >>> parse("2012-01-19 17:21:00 BRST", tzinfos=tzinfos)
            datetime.datetime(2012, 1, 19, 17, 21, tzinfo=tzoffset(u\'BRST\', -7200))
            >>> parse("2012-01-19 17:21:00 CST", tzinfos=tzinfos)
            datetime.datetime(2012, 1, 19, 17, 21,
                              tzinfo=tzfile(\'/usr/share/zoneinfo/America/Chicago\'))

        This parameter is ignored if ``ignoretz`` is set.

    :param dayfirst:
        Whether to interpret the first value in an ambiguous 3-integer date
        (e.g. 01/05/09) as the day (``True``) or month (``False``). If
        ``yearfirst`` is set to ``True``, this distinguishes between YDM and
        YMD. If set to ``None``, this value is retrieved from the current
        :class:`parserinfo` object (which itself defaults to ``False``).

    :param yearfirst:
        Whether to interpret the first value in an ambiguous 3-integer date
        (e.g. 01/05/09) as the year. If ``True``, the first number is taken to
        be the year, otherwise the last number is taken to be the year. If
        this is set to ``None``, the value is retrieved from the current
        :class:`parserinfo` object (which itself defaults to ``False``).

    :param fuzzy:
        Whether to allow fuzzy parsing, allowing for string like "Today is
        January 1, 2047 at 8:21:00AM".

    :param fuzzy_with_tokens:
        If ``True``, ``fuzzy`` is automatically set to True, and the parser
        will return a tuple where the first element is the parsed
        :class:`datetime.datetime` datetimestamp and the second element is
        a tuple containing the portions of the string which were ignored:

        .. doctest::

            >>> from dateutil.parser import parse
            >>> parse("Today is January 1, 2047 at 8:21:00AM", fuzzy_with_tokens=True)
            (datetime.datetime(2047, 1, 1, 8, 21), (u\'Today is \', u\' \', u\'at \'))

    :return:
        Returns a :class:`datetime.datetime` object or, if the
        ``fuzzy_with_tokens`` option is ``True``, returns a tuple, the
        first element being a :class:`datetime.datetime` object, the second
        a tuple containing the fuzzy tokens.

    :raises ParserError:
        Raised for invalid or unknown string formats, if the provided
        :class:`tzinfo` is not in a valid format, or if an invalid date would
        be created.

    :raises OverflowError:
        Raised if the parsed date exceeds the largest valid C integer on
        your system.
    '''

class _tzparser:
    class _result(_resultbase):
        class _attr(_resultbase): ...
        start: Incomplete
        end: Incomplete
        def __init__(self) -> None: ...
    def parse(self, tzstr): ...

class ParserError(ValueError):
    """Exception subclass used for any failure to parse a datetime string.

    This is a subclass of :py:exc:`ValueError`, and should be raised any time
    earlier versions of ``dateutil`` would have raised ``ValueError``.

    .. versionadded:: 2.8.1
    """
class UnknownTimezoneWarning(RuntimeWarning):
    """Raised when the parser finds a timezone it cannot parse into a tzinfo.

    .. versionadded:: 2.7.0
    """
