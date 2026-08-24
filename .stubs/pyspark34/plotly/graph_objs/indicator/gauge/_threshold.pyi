from _typeshed import Incomplete
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Threshold(_BaseTraceHierarchyType):
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.indicator.gauge.threshold.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

            Supported dict properties:

                color
                    Sets the color of the threshold line.
                width
                    Sets the width (in px) of the threshold line.

        Returns
        -------
        plotly.graph_objs.indicator.gauge.threshold.Line
        """
    @line.setter
    def line(self, val) -> None: ...
    @property
    def thickness(self):
        """
        Sets the thickness of the threshold line as a fraction of the
        thickness of the gauge.

        The 'thickness' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
    @thickness.setter
    def thickness(self, val) -> None: ...
    @property
    def value(self):
        """
        Sets a treshold value drawn as a line.

        The 'value' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
    @value.setter
    def value(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, line: Incomplete | None = None, thickness: Incomplete | None = None, value: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Threshold object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.indicator.gauge.Threshold`
        line
            :class:`plotly.graph_objects.indicator.gauge.threshold.
            Line` instance or dict with compatible properties
        thickness
            Sets the thickness of the threshold line as a fraction
            of the thickness of the gauge.
        value
            Sets a treshold value drawn as a line.

        Returns
        -------
        Threshold
        """
