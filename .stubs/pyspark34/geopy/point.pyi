from _typeshed import Incomplete
from geopy import units as units, util as util
from geopy.format import DEGREE as DEGREE, DOUBLE_PRIME as DOUBLE_PRIME, PRIME as PRIME, format_degrees as format_degrees, format_distance as format_distance

POINT_PATTERN: Incomplete

class Point:
    '''
    A geodetic point with latitude, longitude, and altitude.

    Latitude and longitude are floating point values in degrees.
    Altitude is a floating point value in kilometers. The reference level
    is never considered and is thus application dependent, so be consistent!
    The default for all values is 0.

    Points can be created in a number of ways...

    With latitude, longitude, and altitude::

        >>> p1 = Point(41.5, -81, 0)
        >>> p2 = Point(latitude=41.5, longitude=-81)

    With a sequence of 2 to 3 values (latitude, longitude, altitude)::

        >>> p1 = Point([41.5, -81, 0])
        >>> p2 = Point((41.5, -81))

    Copy another `Point` instance::

        >>> p2 = Point(p1)
        >>> p2 == p1
        True
        >>> p2 is p1
        False

    Give a string containing at least latitude and longitude::

        >>> p = Point(\'41.5,-81.0\')
        >>> p = Point(\'+41.5 -81.0\')
        >>> p = Point(\'41.5 N -81.0 W\')
        >>> p = Point(\'-41.5 S, 81.0 E, 2.5km\')
        >>> p = Point(\'23 26m 22s N 23 27m 30s E 21.0mi\')
        >>> p = Point(\'\'\'3 26\' 22" N 23 27\' 30" E\'\'\')

    Point values can be accessed by name or by index::

        >>> p = Point(41.5, -81.0, 0)
        >>> p.latitude == p[0]
        True
        >>> p.longitude == p[1]
        True
        >>> p.altitude == p[2]
        True

    When unpacking (or iterating), a ``(latitude, longitude, altitude)`` tuple is
    returned::

        >>> latitude, longitude, altitude = p

    Textual representations::

        >>> p = Point(41.5, -81.0, 12.3)
        >>> str(p)  # same as `p.format()`
        \'41 30m 0s N, 81 0m 0s W, 12.3km\'
        >>> p.format_unicode()
        \'41° 30′ 0″ N, 81° 0′ 0″ W, 12.3km\'
        >>> repr(p)
        \'Point(41.5, -81.0, 12.3)\'
        >>> repr(tuple(p))
        \'(41.5, -81.0, 12.3)\'
    '''
    POINT_PATTERN = POINT_PATTERN
    latitude: Incomplete
    longitude: Incomplete
    altitude: Incomplete
    def __new__(cls, latitude: Incomplete | None = None, longitude: Incomplete | None = None, altitude: Incomplete | None = None):
        """
        :param float latitude: Latitude of point.
        :param float longitude: Longitude of point.
        :param float altitude: Altitude of point.
        """
    def __getitem__(self, index): ...
    def __setitem__(self, index, value) -> None: ...
    def __iter__(self): ...
    def format(self, altitude: Incomplete | None = None, deg_char: str = '', min_char: str = 'm', sec_char: str = 's'):
        """
        Format decimal degrees (DD) to degrees minutes seconds (DMS)::

            >>> p = Point(41.5, -81.0, 12.3)
            >>> p.format()
            '41 30m 0s N, 81 0m 0s W, 12.3km'
            >>> p = Point(41.5, 0, 0)
            >>> p.format()
            '41 30m 0s N, 0 0m 0s E'

        See also :meth:`.format_unicode`.

        :param bool altitude: Whether to include ``altitude`` value.
            By default it is automatically included if it is non-zero.
        """
    def format_unicode(self, altitude: Incomplete | None = None):
        """
        :meth:`.format` with pretty unicode chars for degrees,
        minutes and seconds::

            >>> p = Point(41.5, -81.0, 12.3)
            >>> p.format_unicode()
            '41° 30′ 0″ N, 81° 0′ 0″ W, 12.3km'

        :param bool altitude: Whether to include ``altitude`` value.
            By default it is automatically included if it is non-zero.
        """
    def format_decimal(self, altitude: Incomplete | None = None):
        """
        Format decimal degrees with altitude::

            >>> p = Point(41.5, -81.0, 12.3)
            >>> p.format_decimal()
            '41.5, -81.0, 12.3km'
            >>> p = Point(41.5, 0, 0)
            >>> p.format_decimal()
            '41.5, 0.0'

        :param bool altitude: Whether to include ``altitude`` value.
            By default it is automatically included if it is non-zero.
        """
    def format_altitude(self, unit: str = 'km'):
        """
        Format altitude with unit::

            >>> p = Point(41.5, -81.0, 12.3)
            >>> p.format_altitude()
            '12.3km'
            >>> p = Point(41.5, -81.0, 0)
            >>> p.format_altitude()
            '0.0km'

        :param str unit: Resulting altitude unit. Supported units
            are listed in :meth:`.from_string` doc.
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    @classmethod
    def parse_degrees(cls, degrees, arcminutes, arcseconds, direction: Incomplete | None = None):
        """
        Convert degrees, minutes, seconds and direction (N, S, E, W)
        to a single degrees number.

        :rtype: float
        """
    @classmethod
    def parse_altitude(cls, distance, unit):
        """
        Parse altitude managing units conversion::

            >>> Point.parse_altitude(712, 'm')
            0.712
            >>> Point.parse_altitude(712, 'km')
            712.0
            >>> Point.parse_altitude(712, 'mi')
            1145.852928

        :param float distance: Numeric value of altitude.
        :param str unit: ``distance`` unit. Supported units
            are listed in :meth:`.from_string` doc.
        """
    @classmethod
    def from_string(cls, string):
        '''
        Create and return a ``Point`` instance from a string containing
        latitude and longitude, and optionally, altitude.

        Latitude and longitude must be in degrees and may be in decimal form
        or indicate arcminutes and arcseconds (labeled with Unicode prime and
        double prime, ASCII quote and double quote or \'m\' and \'s\'). The degree
        symbol is optional and may be included after the decimal places (in
        decimal form) and before the arcminutes and arcseconds otherwise.
        Coordinates given from south and west (indicated by S and W suffixes)
        will be converted to north and east by switching their signs. If no
        (or partial) cardinal directions are given, north and east are the
        assumed directions. Latitude and longitude must be separated by at
        least whitespace, a comma, or a semicolon (each with optional
        surrounding whitespace).

        Altitude, if supplied, must be a decimal number with given units.
        The following unit abbrevations (case-insensitive) are supported:

            - ``km`` (kilometers)
            - ``m`` (meters)
            - ``mi`` (miles)
            - ``ft`` (feet)
            - ``nm``, ``nmi`` (nautical miles)

        Some example strings that will work include:

            - ``41.5;-81.0``
            - ``41.5,-81.0``
            - ``41.5 -81.0``
            - ``41.5 N -81.0 W``
            - ``-41.5 S;81.0 E``
            - ``23 26m 22s N 23 27m 30s E``
            - ``23 26\' 22" N 23 27\' 30" E``
            - ``UT: N 39°20\' 0\'\' / W 74°35\' 0\'\'``

        '''
    @classmethod
    def from_sequence(cls, seq):
        """
        Create and return a new ``Point`` instance from any iterable with 2 to
        3 elements.  The elements, if present, must be latitude, longitude,
        and altitude, respectively.
        """
    @classmethod
    def from_point(cls, point):
        """
        Create and return a new ``Point`` instance from another ``Point``
        instance.
        """
