from _typeshed import Incomplete
from geopy import units as units, util as util
from geopy.point import Point as Point
from geopy.units import radians as radians

EARTH_RADIUS: float
ELLIPSOIDS: Incomplete

def cmp(a, b): ...
def lonlat(x, y, z: int = 0):
    """
    ``geopy.distance.distance`` accepts coordinates in ``(y, x)``/``(lat, lon)``
    order, while some other libraries and systems might use
    ``(x, y)``/``(lon, lat)``.

    This function provides a convenient way to convert coordinates of the
    ``(x, y)``/``(lon, lat)`` format to a :class:`geopy.point.Point` instance.

    Example::

        >>> from geopy.distance import lonlat, distance
        >>> newport_ri_xy = (-71.312796, 41.49008)
        >>> cleveland_oh_xy = (-81.695391, 41.499498)
        >>> print(distance(lonlat(*newport_ri_xy), lonlat(*cleveland_oh_xy)).miles)
        538.3904453677203

    :param x: longitude
    :param y: latitude
    :param z: (optional) altitude
    :return: Point(latitude, longitude, altitude)
    """

class Distance:
    """
    Base class for other distance algorithms. Represents a distance.

    Can be used for units conversion::

        >>> from geopy.distance import Distance
        >>> Distance(miles=10).km
        16.09344

    Distance instances have all *distance* properties from :mod:`geopy.units`,
    e.g.: ``km``, ``m``, ``meters``, ``miles`` and so on.

    Distance instances are immutable.

    They support comparison::

        >>> from geopy.distance import Distance
        >>> Distance(kilometers=2) == Distance(meters=2000)
        True
        >>> Distance(kilometers=2) > Distance(miles=1)
        True

    String representation::

        >>> from geopy.distance import Distance
        >>> repr(Distance(kilometers=2))
        'Distance(2.0)'
        >>> str(Distance(kilometers=2))
        '2.0 km'
        >>> repr(Distance(miles=2))
        'Distance(3.218688)'
        >>> str(Distance(miles=2))
        '3.218688 km'

    Arithmetics::

        >>> from geopy.distance import Distance
        >>> -Distance(miles=2)
        Distance(-3.218688)
        >>> Distance(miles=2) + Distance(kilometers=1)
        Distance(4.218688)
        >>> Distance(miles=2) - Distance(kilometers=1)
        Distance(2.218688)
        >>> Distance(kilometers=6) * 5
        Distance(30.0)
        >>> Distance(kilometers=6) / 5
        Distance(1.2)
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        There are 3 ways to create a distance:

        - From kilometers::

            >>> from geopy.distance import Distance
            >>> Distance(1.42)
            Distance(1.42)

        - From units::

            >>> from geopy.distance import Distance
            >>> Distance(kilometers=1.42)
            Distance(1.42)
            >>> Distance(miles=1)
            Distance(1.609344)

        - From points (for non-abstract distances only),
          calculated as a sum of distances between all points::

            >>> from geopy.distance import geodesic
            >>> geodesic((40, 160), (40.1, 160.1))
            Distance(14.003702498106215)
            >>> geodesic((40, 160), (40.1, 160.1), (40.2, 160.2))
            Distance(27.999954644813478)
        """
    def __add__(self, other): ...
    def __neg__(self): ...
    def __sub__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __truediv__(self, other): ...
    def __floordiv__(self, other): ...
    def __abs__(self): ...
    def __bool__(self) -> bool: ...
    def measure(self, a, b) -> None: ...
    def destination(self, point, bearing, distance: Incomplete | None = None) -> None:
        '''
        Calculate destination point using a starting point, bearing
        and a distance. This method works for non-abstract distances only.

        Example: a point 10 miles east from ``(34, 148)``::

            >>> import geopy.distance
            >>> geopy.distance.distance(miles=10).destination((34, 148), bearing=90)
            Point(33.99987666492774, 148.17419994321995, 0.0)

        :param point: Starting point.
        :type point: :class:`geopy.point.Point`, list or tuple of ``(latitude,
            longitude)``, or string as ``"%(latitude)s, %(longitude)s"``.

        :param float bearing: Bearing in degrees: 0 -- North, 90 -- East,
            180 -- South, 270 or -90 -- West.

        :param distance: Distance, can be used to override
            this instance::

                >>> from geopy.distance import distance, Distance
                >>> distance(miles=10).destination((34, 148), bearing=90, distance=Distance(100))
                Point(33.995238229104764, 149.08238904409637, 0.0)

        :type distance: :class:`.Distance`

        :rtype: :class:`geopy.point.Point`
        '''
    def __cmp__(self, other): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __gt__(self, other): ...
    def __lt__(self, other): ...
    def __ge__(self, other): ...
    def __le__(self, other): ...
    @property
    def feet(self): ...
    @property
    def ft(self): ...
    @property
    def kilometers(self): ...
    @property
    def km(self): ...
    @property
    def m(self): ...
    @property
    def meters(self): ...
    @property
    def mi(self): ...
    @property
    def miles(self): ...
    @property
    def nautical(self): ...
    @property
    def nm(self): ...

class great_circle(Distance):
    """
    Use spherical geometry to calculate the surface distance between
    points.

    Set which radius of the earth to use by specifying a ``radius`` keyword
    argument. It must be in kilometers. The default is to use the module
    constant `EARTH_RADIUS`, which uses the average great-circle radius.

    Example::

        >>> from geopy.distance import great_circle
        >>> newport_ri = (41.49008, -71.312796)
        >>> cleveland_oh = (41.499498, -81.695391)
        >>> print(great_circle(newport_ri, cleveland_oh).miles)
        536.997990696

    """
    RADIUS: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def measure(self, a, b): ...
    def destination(self, point, bearing, distance: Incomplete | None = None): ...
GreatCircleDistance = great_circle

class geodesic(Distance):
    """
    Calculate the geodesic distance between points.

    Set which ellipsoidal model of the earth to use by specifying an
    ``ellipsoid`` keyword argument. The default is 'WGS-84', which is the
    most globally accurate model.  If ``ellipsoid`` is a string, it is
    looked up in the `ELLIPSOIDS` dictionary to obtain the major and minor
    semiaxes and the flattening. Otherwise, it should be a tuple with those
    values.  See the comments above the `ELLIPSOIDS` dictionary for
    more information.

    Example::

        >>> from geopy.distance import geodesic
        >>> newport_ri = (41.49008, -71.312796)
        >>> cleveland_oh = (41.499498, -81.695391)
        >>> print(geodesic(newport_ri, cleveland_oh).miles)
        538.390445368

    """
    ellipsoid_key: Incomplete
    ELLIPSOID: Incomplete
    geod: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def set_ellipsoid(self, ellipsoid) -> None: ...
    def measure(self, a, b): ...
    def destination(self, point, bearing, distance: Incomplete | None = None): ...
GeodesicDistance = geodesic
distance = GeodesicDistance
