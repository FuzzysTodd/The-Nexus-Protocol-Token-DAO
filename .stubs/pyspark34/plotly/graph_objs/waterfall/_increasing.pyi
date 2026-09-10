from _typeshed import Incomplete
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Increasing(_BaseTraceHierarchyType):
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.waterfall.increasing.Marker`
          - A dict of string/value properties that will be passed
            to the Marker constructor

            Supported dict properties:

                color
                    Sets the marker color of all increasing values.
                line
                    :class:`plotly.graph_objects.waterfall.increasi
                    ng.marker.Line` instance or dict with
                    compatible properties

        Returns
        -------
        plotly.graph_objs.waterfall.increasing.Marker
        """
    @marker.setter
    def marker(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, marker: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Increasing object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.waterfall.Increasing`
        marker
            :class:`plotly.graph_objects.waterfall.increasing.Marke
            r` instance or dict with compatible properties

        Returns
        -------
        Increasing
        """
