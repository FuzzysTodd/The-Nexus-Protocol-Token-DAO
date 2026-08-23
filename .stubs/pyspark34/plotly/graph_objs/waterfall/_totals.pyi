from _typeshed import Incomplete
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Totals(_BaseTraceHierarchyType):
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.waterfall.totals.Marker`
          - A dict of string/value properties that will be passed
            to the Marker constructor

            Supported dict properties:

                color
                    Sets the marker color of all intermediate sums
                    and total values.
                line
                    :class:`plotly.graph_objects.waterfall.totals.m
                    arker.Line` instance or dict with compatible
                    properties

        Returns
        -------
        plotly.graph_objs.waterfall.totals.Marker
        """
    @marker.setter
    def marker(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, marker: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Totals object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.waterfall.Totals`
        marker
            :class:`plotly.graph_objects.waterfall.totals.Marker`
            instance or dict with compatible properties

        Returns
        -------
        Totals
        """
