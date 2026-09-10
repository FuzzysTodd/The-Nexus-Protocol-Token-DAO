from _typeshed import Incomplete
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Marker(_BaseTraceHierarchyType):
    @property
    def color(self):
        """
        Sets the aggregation data.

        The 'color' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
    @color.setter
    def color(self, val) -> None: ...
    @property
    def colorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `color`.

        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
    @colorsrc.setter
    def colorsrc(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, color: Incomplete | None = None, colorsrc: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Marker object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.histogram2d.Marker`
        color
            Sets the aggregation data.
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.

        Returns
        -------
        Marker
        """
