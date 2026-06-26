from _typeshed import Incomplete
from geographiclib.geodesiccapability import GeodesicCapability as GeodesicCapability
from geographiclib.geomath import Math as Math

class GeodesicLine:
    """Points on a geodesic path"""
    a: Incomplete
    f: Incomplete
    caps: Incomplete
    lat1: Incomplete
    lon1: Incomplete
    azi1: Incomplete
    salp1: Incomplete
    calp1: Incomplete
    s13: Incomplete
    a13: Incomplete
    def __init__(self, geod, lat1, lon1, azi1, caps=..., salp1=..., calp1=...) -> None:
        """Construct a GeodesicLine object

    :param geod: a :class:`~geographiclib.geodesic.Geodesic` object
    :param lat1: latitude of the first point in degrees
    :param lon1: longitude of the first point in degrees
    :param azi1: azimuth at the first point in degrees
    :param caps: the :ref:`capabilities <outmask>`

    This creates an object allowing points along a geodesic starting at
    (*lat1*, *lon1*), with azimuth *azi1* to be found.  The default
    value of *caps* is STANDARD | DISTANCE_IN.  The optional parameters
    *salp1* and *calp1* should not be supplied; they are part of the
    private interface.

    """
    def Position(self, s12, outmask=...):
        """Find the position on the line given *s12*

    :param s12: the distance from the first point to the second in
      meters
    :param outmask: the :ref:`output mask <outmask>`
    :return: a :ref:`dict`

    The default value of *outmask* is STANDARD, i.e., the *lat1*,
    *lon1*, *azi1*, *lat2*, *lon2*, *azi2*, *s12*, *a12* entries are
    returned.  The :class:`~geographiclib.geodesicline.GeodesicLine`
    object must have been constructed with the DISTANCE_IN capability.

    """
    def ArcPosition(self, a12, outmask=...):
        """Find the position on the line given *a12*

    :param a12: spherical arc length from the first point to the second
      in degrees
    :param outmask: the :ref:`output mask <outmask>`
    :return: a :ref:`dict`

    The default value of *outmask* is STANDARD, i.e., the *lat1*,
    *lon1*, *azi1*, *lat2*, *lon2*, *azi2*, *s12*, *a12* entries are
    returned.

    """
    def SetDistance(self, s13) -> None:
        """Specify the position of point 3 in terms of distance

    :param s13: distance from point 1 to point 3 in meters

    """
    def SetArc(self, a13) -> None:
        """Specify the position of point 3 in terms of arc length

    :param a13: spherical arc length from point 1 to point 3 in degrees

    """
