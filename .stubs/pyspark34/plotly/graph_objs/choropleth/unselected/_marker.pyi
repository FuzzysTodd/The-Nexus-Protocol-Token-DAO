from _typeshed import Incomplete
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Marker(_BaseTraceHierarchyType):
    @property
    def opacity(self):
        """
        Sets the marker opacity of unselected points, applied only when
        a selection exists.

        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
    @opacity.setter
    def opacity(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, opacity: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Marker object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.choropleth.unselected.Marker`
        opacity
            Sets the marker opacity of unselected points, applied
            only when a selection exists.

        Returns
        -------
        Marker
        """
