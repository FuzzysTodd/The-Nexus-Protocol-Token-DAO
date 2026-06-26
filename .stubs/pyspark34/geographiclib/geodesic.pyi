from _typeshed import Incomplete
from geographiclib.constants import Constants as Constants
from geographiclib.geodesiccapability import GeodesicCapability as GeodesicCapability
from geographiclib.geomath import Math as Math

class Geodesic:
    """Solve geodesic problems"""
    GEOGRAPHICLIB_GEODESIC_ORDER: int
    nA1_ = GEOGRAPHICLIB_GEODESIC_ORDER
    nC1_ = GEOGRAPHICLIB_GEODESIC_ORDER
    nC1p_ = GEOGRAPHICLIB_GEODESIC_ORDER
    nA2_ = GEOGRAPHICLIB_GEODESIC_ORDER
    nC2_ = GEOGRAPHICLIB_GEODESIC_ORDER
    nA3_ = GEOGRAPHICLIB_GEODESIC_ORDER
    nA3x_ = nA3_
    nC3_ = GEOGRAPHICLIB_GEODESIC_ORDER
    nC3x_: Incomplete
    nC4_ = GEOGRAPHICLIB_GEODESIC_ORDER
    nC4x_: Incomplete
    maxit1_: int
    maxit2_: Incomplete
    tiny_: Incomplete
    tol0_: Incomplete
    tol1_: Incomplete
    tol2_: Incomplete
    tolb_: Incomplete
    xthresh_: Incomplete
    CAP_NONE: Incomplete
    CAP_C1: Incomplete
    CAP_C1p: Incomplete
    CAP_C2: Incomplete
    CAP_C3: Incomplete
    CAP_C4: Incomplete
    CAP_ALL: Incomplete
    CAP_MASK: Incomplete
    OUT_ALL: Incomplete
    OUT_MASK: Incomplete
    a: Incomplete
    f: Incomplete
    def __init__(self, a, f) -> None:
        """Construct a Geodesic object

    :param a: the equatorial radius of the ellipsoid in meters
    :param f: the flattening of the ellipsoid

    An exception is thrown if *a* or the polar semi-axis *b* = *a* (1 -
    *f*) is not a finite positive quantity.

    """
    def Inverse(self, lat1, lon1, lat2, lon2, outmask=...):
        """Solve the inverse geodesic problem

    :param lat1: latitude of the first point in degrees
    :param lon1: longitude of the first point in degrees
    :param lat2: latitude of the second point in degrees
    :param lon2: longitude of the second point in degrees
    :param outmask: the :ref:`output mask <outmask>`
    :return: a :ref:`dict`

    Compute geodesic between (*lat1*, *lon1*) and (*lat2*, *lon2*).
    The default value of *outmask* is STANDARD, i.e., the *lat1*,
    *lon1*, *azi1*, *lat2*, *lon2*, *azi2*, *s12*, *a12* entries are
    returned.

    """
    def Direct(self, lat1, lon1, azi1, s12, outmask=...):
        """Solve the direct geodesic problem

    :param lat1: latitude of the first point in degrees
    :param lon1: longitude of the first point in degrees
    :param azi1: azimuth at the first point in degrees
    :param s12: the distance from the first point to the second in
      meters
    :param outmask: the :ref:`output mask <outmask>`
    :return: a :ref:`dict`

    Compute geodesic starting at (*lat1*, *lon1*) with azimuth *azi1*
    and length *s12*.  The default value of *outmask* is STANDARD, i.e.,
    the *lat1*, *lon1*, *azi1*, *lat2*, *lon2*, *azi2*, *s12*, *a12*
    entries are returned.

    """
    def ArcDirect(self, lat1, lon1, azi1, a12, outmask=...):
        """Solve the direct geodesic problem in terms of spherical arc length

    :param lat1: latitude of the first point in degrees
    :param lon1: longitude of the first point in degrees
    :param azi1: azimuth at the first point in degrees
    :param a12: spherical arc length from the first point to the second
      in degrees
    :param outmask: the :ref:`output mask <outmask>`
    :return: a :ref:`dict`

    Compute geodesic starting at (*lat1*, *lon1*) with azimuth *azi1*
    and arc length *a12*.  The default value of *outmask* is STANDARD,
    i.e., the *lat1*, *lon1*, *azi1*, *lat2*, *lon2*, *azi2*, *s12*,
    *a12* entries are returned.

    """
    def Line(self, lat1, lon1, azi1, caps=...):
        """Return a GeodesicLine object

    :param lat1: latitude of the first point in degrees
    :param lon1: longitude of the first point in degrees
    :param azi1: azimuth at the first point in degrees
    :param caps: the :ref:`capabilities <outmask>`
    :return: a :class:`~geographiclib.geodesicline.GeodesicLine`

    This allows points along a geodesic starting at (*lat1*, *lon1*),
    with azimuth *azi1* to be found.  The default value of *caps* is
    STANDARD | DISTANCE_IN, allowing direct geodesic problem to be
    solved.

    """
    def DirectLine(self, lat1, lon1, azi1, s12, caps=...):
        """Define a GeodesicLine object in terms of the direct geodesic
    problem specified in terms of spherical arc length

    :param lat1: latitude of the first point in degrees
    :param lon1: longitude of the first point in degrees
    :param azi1: azimuth at the first point in degrees
    :param s12: the distance from the first point to the second in
      meters
    :param caps: the :ref:`capabilities <outmask>`
    :return: a :class:`~geographiclib.geodesicline.GeodesicLine`

    This function sets point 3 of the GeodesicLine to correspond to
    point 2 of the direct geodesic problem.  The default value of *caps*
    is STANDARD | DISTANCE_IN, allowing direct geodesic problem to be
    solved.

    """
    def ArcDirectLine(self, lat1, lon1, azi1, a12, caps=...):
        """Define a GeodesicLine object in terms of the direct geodesic
    problem specified in terms of spherical arc length

    :param lat1: latitude of the first point in degrees
    :param lon1: longitude of the first point in degrees
    :param azi1: azimuth at the first point in degrees
    :param a12: spherical arc length from the first point to the second
      in degrees
    :param caps: the :ref:`capabilities <outmask>`
    :return: a :class:`~geographiclib.geodesicline.GeodesicLine`

    This function sets point 3 of the GeodesicLine to correspond to
    point 2 of the direct geodesic problem.  The default value of *caps*
    is STANDARD | DISTANCE_IN, allowing direct geodesic problem to be
    solved.

    """
    def InverseLine(self, lat1, lon1, lat2, lon2, caps=...):
        """Define a GeodesicLine object in terms of the invese geodesic problem

    :param lat1: latitude of the first point in degrees
    :param lon1: longitude of the first point in degrees
    :param lat2: latitude of the second point in degrees
    :param lon2: longitude of the second point in degrees
    :param caps: the :ref:`capabilities <outmask>`
    :return: a :class:`~geographiclib.geodesicline.GeodesicLine`

    This function sets point 3 of the GeodesicLine to correspond to
    point 2 of the inverse geodesic problem.  The default value of *caps*
    is STANDARD | DISTANCE_IN, allowing direct geodesic problem to be
    solved.

    """
    def Polygon(self, polyline: bool = False):
        """Return a PolygonArea object

    :param polyline: if True then the object describes a polyline
      instead of a polygon
    :return: a :class:`~geographiclib.polygonarea.PolygonArea`

    """
    EMPTY: Incomplete
    LATITUDE: Incomplete
    LONGITUDE: Incomplete
    AZIMUTH: Incomplete
    DISTANCE: Incomplete
    STANDARD: Incomplete
    DISTANCE_IN: Incomplete
    REDUCEDLENGTH: Incomplete
    GEODESICSCALE: Incomplete
    AREA: Incomplete
    ALL: Incomplete
    LONG_UNROLL: Incomplete
