from _typeshed import Incomplete
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Center(_BaseLayoutHierarchyType):
    @property
    def lat(self):
        """
        Sets the latitude of the map's center. For all projection
        types, the map's latitude center lies at the middle of the
        latitude range by default.

        The 'lat' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
    @lat.setter
    def lat(self, val) -> None: ...
    @property
    def lon(self):
        """
        Sets the longitude of the map's center. By default, the map's
        longitude center lies at the middle of the longitude range for
        scoped projection and above `projection.rotation.lon`
        otherwise.

        The 'lon' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
    @lon.setter
    def lon(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, lat: Incomplete | None = None, lon: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Center object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.geo.Center`
        lat
            Sets the latitude of the map's center. For all
            projection types, the map's latitude center lies at the
            middle of the latitude range by default.
        lon
            Sets the longitude of the map's center. By default, the
            map's longitude center lies at the middle of the
            longitude range for scoped projection and above
            `projection.rotation.lon` otherwise.

        Returns
        -------
        Center
        """
