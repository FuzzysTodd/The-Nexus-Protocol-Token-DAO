from _typeshed import Incomplete
from datetime import date, datetime
from gettext import gettext
from typing import Any, Dict, Iterable, List, Set, Tuple

__all__ = ['DateLike', 'HolidayBase', 'HolidaySum']

DateArg = date | Tuple[int, int]
DateLike = date | datetime | str | float | int
SpecialHoliday = Tuple[int, int, str] | Tuple[Tuple[int, int, str], ...]
SubstitutedHoliday = Tuple[int, int, int, int] | Tuple[int, int, int, int, int] | Tuple[Tuple[int, int, int, int] | Tuple[int, int, int, int, int], ...]
gettext = gettext

class HolidayBase(Dict[date, str]):
    '''
    A dict-like object containing the holidays for a specific country (and
    province or state if so initiated); inherits the dict class (so behaves
    similarly to a dict). Dates without a key in the Holiday object are not
    holidays.

    The key of the object is the date of the holiday and the value is the name
    of the holiday itself. When passing the date as a key, the date can be
    expressed as one of the following formats:

    * datetime.datetime type;
    * datetime.date types;
    * a float representing a Unix timestamp;
    * or a string of any format (recognized by datetime.parse).

    The key is always returned as a `datetime.date` object.

    To maximize speed, the list of holidays is built as needed on the fly, one
    calendar year at a time. When you instantiate the object, it is empty, but
    the moment a key is accessed it will build that entire year\'s list of
    holidays. To pre-populate holidays, instantiate the class with the years
    argument:

    us_holidays = holidays.US(years=2020)

    It is generally instantiated using the :func:`country_holidays` function.

    The key of the :class:`dict`-like :class:`HolidayBase` object is the
    `date` of the holiday, and the value is the name of the holiday itself.
    Dates where a key is not present are not public holidays (or, if
    **observed** is False, days when a public holiday is observed).

    When passing the `date` as a key, the `date` can be expressed in one of the
    following types:

    * :class:`datetime.date`,
    * :class:`datetime.datetime`,
    * a :class:`str` of any format recognized by :func:`dateutil.parser.parse`,
    * or a :class:`float` or :class:`int` representing a POSIX timestamp.

    The key is always returned as a :class:`datetime.date` object.

    To maximize speed, the list of public holidays is built on the fly as
    needed, one calendar year at a time. When the object is instantiated
    without a **years** parameter, it is empty, but, unless **expand** is set
    to False, as soon as a key is accessed the class will calculate that entire
    year\'s list of holidays and set the keys with them.

    If you need to list the holidays as opposed to querying individual dates,
    instantiate the class with the **years** parameter.

    Example usage:

    >>> from holidays import country_holidays
    >>> us_holidays = country_holidays(\'US\')
    # For a specific subdivisions (e.g. state or province):
    >>> california_holidays = country_holidays(\'US\', subdiv=\'CA\')

    The below will cause 2015 holidays to be calculated on the fly:

    >>> from datetime import date
    >>> assert date(2015, 1, 1) in us_holidays

    This will be faster because 2015 holidays are already calculated:

    >>> assert date(2015, 1, 2) not in us_holidays

    The :class:`HolidayBase` class also recognizes strings of many formats
    and numbers representing a POSIX timestamp:

    >>> assert \'2014-01-01\' in us_holidays
    >>> assert \'1/1/2014\' in us_holidays
    >>> assert 1388597445 in us_holidays

    Show the holiday\'s name:

    >>> us_holidays.get(\'2014-01-01\')
    "New Year\'s Day"

    Check a range:

    >>> us_holidays[\'2014-01-01\': \'2014-01-03\']
    [datetime.date(2014, 1, 1)]

    List all 2020 holidays:

    >>> us_holidays = country_holidays(\'US\', years=2020)
    >>> for day in us_holidays.items():
    ...     print(day)
    (datetime.date(2020, 1, 1), "New Year\'s Day")
    (datetime.date(2020, 1, 20), \'Martin Luther King Jr. Day\')
    (datetime.date(2020, 2, 17), "Washington\'s Birthday")
    (datetime.date(2020, 5, 25), \'Memorial Day\')
    (datetime.date(2020, 7, 4), \'Independence Day\')
    (datetime.date(2020, 7, 3), \'Independence Day (Observed)\')
    (datetime.date(2020, 9, 7), \'Labor Day\')
    (datetime.date(2020, 10, 12), \'Columbus Day\')
    (datetime.date(2020, 11, 11), \'Veterans Day\')
    (datetime.date(2020, 11, 26), \'Thanksgiving\')
    (datetime.date(2020, 12, 25), \'Christmas Day\')

    Some holidays are only present in parts of a country:

    >>> us_pr_holidays = country_holidays(\'US\', subdiv=\'PR\')
    >>> assert \'2018-01-06\' not in us_holidays
    >>> assert \'2018-01-06\' in us_pr_holidays

    Append custom holiday dates by passing one of:

    * a :class:`dict` with date/name key/value pairs (e.g.
      ``{\'2010-07-10\': \'My birthday!\'}``),
    * a list of dates (as a :class:`datetime.date`, :class:`datetime.datetime`,
      :class:`str`, :class:`int`, or :class:`float`); ``\'Holiday\'`` will be
      used as a description,
    * or a single date item (of one of the types above); ``\'Holiday\'`` will be
      used as a description:

    >>> custom_holidays = country_holidays(\'US\', years=2015)
    >>> custom_holidays.update({\'2015-01-01\': "New Year\'s Day"})
    >>> custom_holidays.update([\'2015-07-01\', \'07/04/2015\'])
    >>> custom_holidays.update(date(2015, 12, 25))
    >>> assert date(2015, 1, 1) in custom_holidays
    >>> assert date(2015, 1, 2) not in custom_holidays
    >>> assert \'12/25/2015\' in custom_holidays

    For special (one-off) country-wide holidays handling use
    :attr:`special_holidays`:

    .. code-block:: python

        special_holidays = {
            1977: ((JUN, 7, "Silver Jubilee of Elizabeth II"),),
            1981: ((JUL, 29, "Wedding of Charles and Diana"),),
            1999: ((DEC, 31, "Millennium Celebrations"),),
            2002: ((JUN, 3, "Golden Jubilee of Elizabeth II"),),
            2011: ((APR, 29, "Wedding of William and Catherine"),),
            2012: ((JUN, 5, "Diamond Jubilee of Elizabeth II"),),
            2022: (
                (JUN, 3, "Platinum Jubilee of Elizabeth II"),
                (SEP, 19, "State Funeral of Queen Elizabeth II"),
            ),
        }

        def _populate(self, year):
            super()._populate(year)

            ...

    For more complex logic, like 4th Monday of January, you can inherit the
    :class:`HolidayBase` class and define your own :meth:`_populate` method.
    See documentation for examples.
    '''
    country: str
    market: str
    subdivisions: Tuple[str, ...]
    years: Set[int]
    expand: bool
    observed: bool
    subdiv: str | None
    special_holidays: Dict[int, SpecialHoliday]
    substituted_holidays: Dict[int, SubstitutedHoliday]
    weekend: Set[int]
    default_language: str | None
    categories: Set[str] | None
    supported_categories: Set[str]
    supported_languages: Tuple[str, ...]
    language: Incomplete
    tr: Incomplete
    def __init__(self, years: int | Iterable[int] | None = None, expand: bool = True, observed: bool = True, subdiv: str | None = None, prov: str | None = None, state: str | None = None, language: str | None = None, categories: Tuple[str] | None = None) -> None:
        """
        :param years:
            The year(s) to pre-calculate public holidays for at instantiation.

        :param expand:
            Whether the entire year is calculated when one date from that year
            is requested.

        :param observed:
            Whether to include the dates when public holiday are observed
            (e.g. a holiday falling on a Sunday being observed the
            following Monday). This doesn't work for all countries.

        :param subdiv:
            The subdivision (e.g. state or province); not implemented for all
            countries (see documentation).

        :param prov:
            *deprecated* use subdiv instead.

        :param state:
            *deprecated* use subdiv instead.

        :param language:
            The language which the returned holiday names will be translated
            into. It must be an ISO 639-1 (2-letter) language code. If the
            language translation is not supported the original holiday names
            will be used.

        :param categories:
            Requested holiday categories.

        :return:
            A :class:`HolidayBase` object matching the **country**.
        """
    def __add__(self, other: int | HolidayBase | HolidaySum) -> HolidayBase:
        """Add another dictionary of public holidays creating a
        :class:`HolidaySum` object.

        :param other:
            The dictionary of public holiday to be added.

        :return:
            A :class:`HolidaySum` object unless the other object cannot be
            added, then :class:`self`.
        """
    def __bool__(self) -> bool: ...
    def __contains__(self, key: object) -> bool:
        """Return true if date is in self, false otherwise. Accepts a date in
        the following types:

        * :class:`datetime.date`,
        * :class:`datetime.datetime`,
        * a :class:`str` of any format recognized by
          :func:`dateutil.parser.parse`,
        * or a :class:`float` or :class:`int` representing a POSIX timestamp.
        """
    def __eq__(self, other: object) -> bool: ...
    def __getattr__(self, name): ...
    def __getitem__(self, key: DateLike) -> Any: ...
    def __keytransform__(self, key: DateLike) -> date:
        """Transforms the date from one of the following types:

        * :class:`datetime.date`,
        * :class:`datetime.datetime`,
        * a :class:`str` of any format recognized by
          :func:`dateutil.parser.parse`,
        * or a :class:`float` or :class:`int` representing a POSIX timestamp

        to :class:`datetime.date`, which is how it's stored by the class."""
    def __ne__(self, other: object) -> bool: ...
    def __radd__(self, other: Any) -> HolidayBase: ...
    def __reduce__(self) -> str | Tuple[Any, ...]: ...
    def __setattr__(self, key: str, value: Any) -> None: ...
    def __setitem__(self, key: DateLike, value: str) -> None: ...
    def append(self, *args: Dict[DateLike, str] | List[DateLike] | DateLike) -> None:
        """Alias for :meth:`update` to mimic list type."""
    def copy(self):
        """Return a copy of the object."""
    def get(self, key: DateLike, default: str | Any = None) -> str | Any:
        """Return the holiday name for a date if date is a holiday, else
        default. If default is not given, it defaults to None, so that this
        method never raises a KeyError. If more than one holiday is present,
        they are separated by a comma.

        :param key:
            The date expressed in one of the following types:

            * :class:`datetime.date`,
            * :class:`datetime.datetime`,
            * a :class:`str` of any format recognized by
              :func:`dateutil.parser.parse`,
            * or a :class:`float` or :class:`int` representing a POSIX
              timestamp.

        :param default:
            The default value to return if no value is found.
        """
    def get_list(self, key: DateLike) -> List[str]:
        """Return a list of all holiday names for a date if date is a holiday,
        else empty string.

        :param key:
            The date expressed in one of the following types:

            * :class:`datetime.date`,
            * :class:`datetime.datetime`,
            * a :class:`str` of any format recognized by
              :func:`dateutil.parser.parse`,
            * or a :class:`float` or :class:`int` representing a POSIX
              timestamp.
        """
    def get_named(self, holiday_name: str, lookup: str = 'icontains', split_multiple_names: bool = True) -> List[date]:
        """Return a list of all holiday dates matching the provided holiday
        name. The match will be made case insensitively and partial matches
        will be included by default.

        :param holiday_name:
            The holiday's name to try to match.
        :param lookup:
            The holiday name lookup type:
                contains - case sensitive contains match;
                exact - case sensitive exact match;
                startswith - case sensitive starts with match;
                icontains - case insensitive contains match;
                iexact - case insensitive exact match;
                istartswith - case insensitive starts with match;
        :param split_multiple_names:
            Either use the exact name for each date or split it by holiday
            name delimiter.

        :return:
            A list of all holiday dates matching the provided holiday name.
        """
    def pop(self, key: DateLike, default: str | Any = None) -> str | Any:
        """If date is a holiday, remove it and return its date, else return
        default.

        :param key:
            The date expressed in one of the following types:

            * :class:`datetime.date`,
            * :class:`datetime.datetime`,
            * a :class:`str` of any format recognized by
              :func:`dateutil.parser.parse`,
            * or a :class:`float` or :class:`int` representing a POSIX
              timestamp.

        :param default:
            The default value to return if no match is found.

        :return:
            The date removed.

        :raise:
            KeyError if date is not a holiday and default is not given.
        """
    def pop_named(self, name: str) -> List[date]:
        """Remove (no longer treat at as holiday) all dates matching the
        provided holiday name. The match will be made case insensitively and
        partial matches will be removed.

        :param name:
            The holiday's name to try to match.

        :param default:
            The default value to return if no match is found.

        :return:
            A list of dates removed.

        :raise:
            KeyError if date is not a holiday and default is not given.
        """
    def update(self, *args: Dict[DateLike, str] | List[DateLike] | DateLike) -> None:
        '''Update the object, overwriting existing dates.

        :param:
            Either another dictionary object where keys are dates and values
            are holiday names, or a single date (or a list of dates) for which
            the value will be set to "Holiday".

            Dates can be expressed in one or more of the following types:

            * :class:`datetime.date`,
            * :class:`datetime.datetime`,
            * a :class:`str` of any format recognized by
              :func:`dateutil.parser.parse`,
            * or a :class:`float` or :class:`int` representing a POSIX
              timestamp.
        '''

class HolidaySum(HolidayBase):
    """
    Returns a :class:`dict`-like object resulting from the addition of two or
    more individual dictionaries of public holidays. The original dictionaries
    are available as a :class:`list` in the attribute :attr:`holidays,` and
    :attr:`country` and :attr:`subdiv` attributes are added
    together and could become :class:`list` s. Holiday names, when different,
    are merged. All years are calculated (expanded) for all operands.
    """
    country: str | List[str]
    market: str | List[str]
    subdiv: str | List[str] | None
    holidays: List[HolidayBase]
    years: Set[int]
    def __init__(self, h1: HolidayBase | HolidaySum, h2: HolidayBase | HolidaySum) -> None:
        '''
        :param h1:
            The first HolidayBase object to add.

        :param h2:
            The other HolidayBase object to add.

        Example:

        >>> from holidays import country_holidays
        >>> nafta_holidays = country_holidays(\'US\', years=2020) + country_holidays(\'CA\') + country_holidays(\'MX\')
        >>> dates = sorted(nafta_holidays.items(), key=lambda x: x[0])
        >>> from pprint import pprint
        >>> pprint(dates[:10], width=72)
        [(datetime.date(2020, 1, 1), "Año Nuevo"),
         (datetime.date(2020, 1, 20), \'Martin Luther King Jr. Day\'),
         (datetime.date(2020, 2, 3),
          \'Día de la Constitución\'),
         (datetime.date(2020, 2, 17), "Washington\'s Birthday, Family Day"),
         (datetime.date(2020, 3, 16),
          "Natalicio de Benito Juárez"),
         (datetime.date(2020, 4, 10), \'Good Friday\'),
         (datetime.date(2020, 5, 1), \'Día del Trabajo\'),
         (datetime.date(2020, 5, 18), \'Victoria Day\')]
        '''
