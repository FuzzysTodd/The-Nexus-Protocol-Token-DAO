from _typeshed import Incomplete
from geographiclib.accumulator import Accumulator as Accumulator
from geographiclib.geomath import Math as Math

class PolygonArea:
    """Area of a geodesic polygon"""
    earth: Incomplete
    polyline: Incomplete
    area0: Incomplete
    num: int
    lat1: Incomplete
    lon1: Incomplete
    def __init__(self, earth, polyline: bool = False) -> None:
        """Construct a PolygonArea object

    :param earth: a :class:`~geographiclib.geodesic.Geodesic` object
    :param polyline: if true, treat object as a polyline instead of a polygon

    Initially the polygon has no vertices.
    """
    def Clear(self) -> None:
        """Reset to empty polygon."""
    def AddPoint(self, lat, lon) -> None:
        """Add the next vertex to the polygon

    :param lat: the latitude of the point in degrees
    :param lon: the longitude of the point in degrees

    This adds an edge from the current vertex to the new vertex.
    """
    def AddEdge(self, azi, s) -> None:
        """Add the next edge to the polygon

    :param azi: the azimuth at the current the point in degrees
    :param s: the length of the edge in meters

    This specifies the new vertex in terms of the edge from the current
    vertex.

    """
    def Compute(self, reverse: bool = False, sign: bool = True):
        '''Compute the properties of the polygon

    :param reverse: if true then clockwise (instead of
      counter-clockwise) traversal counts as a positive area
    :param sign: if true then return a signed result for the area if the
      polygon is traversed in the "wrong" direction instead of returning
      the area for the rest of the earth
    :return: a tuple of number, perimeter (meters), area (meters^2)

    Arbitrarily complex polygons are allowed.  In the case of
    self-intersecting polygons the area is accumulated "algebraically",
    e.g., the areas of the 2 loops in a figure-8 polygon will partially
    cancel.

    If the object is a polygon (and not a polyline), the perimeter
    includes the length of a final edge connecting the current point to
    the initial point.  If the object is a polyline, then area is nan.

    More points can be added to the polygon after this call.

    '''
    def TestPoint(self, lat, lon, reverse: bool = False, sign: bool = True):
        '''Compute the properties for a tentative additional vertex

    :param lat: the latitude of the point in degrees
    :param lon: the longitude of the point in degrees
    :param reverse: if true then clockwise (instead of
      counter-clockwise) traversal counts as a positive area
    :param sign: if true then return a signed result for the area if the
      polygon is traversed in the "wrong" direction instead of returning
      the area for the rest of the earth
    :return: a tuple of number, perimeter (meters), area (meters^2)

    '''
    def TestEdge(self, azi, s, reverse: bool = False, sign: bool = True):
        '''Compute the properties for a tentative additional edge

    :param azi: the azimuth at the current the point in degrees
    :param s: the length of the edge in meters
    :param reverse: if true then clockwise (instead of
      counter-clockwise) traversal counts as a positive area
    :param sign: if true then return a signed result for the area if the
      polygon is traversed in the "wrong" direction instead of returning
      the area for the rest of the earth
    :return: a tuple of number, perimeter (meters), area (meters^2)

    '''
