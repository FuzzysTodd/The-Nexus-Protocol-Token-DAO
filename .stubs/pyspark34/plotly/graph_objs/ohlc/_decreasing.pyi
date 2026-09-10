from _typeshed import Incomplete
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Decreasing(_BaseTraceHierarchyType):
    @property
    def line(self):
        '''
        The \'line\' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.ohlc.decreasing.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

            Supported dict properties:

                color
                    Sets the line color.
                dash
                    Sets the dash style of lines. Set to a dash
                    type string ("solid", "dot", "dash",
                    "longdash", "dashdot", or "longdashdot") or a
                    dash length list in px (eg "5px,10px,2px,2px").
                width
                    Sets the line width (in px).

        Returns
        -------
        plotly.graph_objs.ohlc.decreasing.Line
        '''
    @line.setter
    def line(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, line: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Decreasing object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.ohlc.Decreasing`
        line
            :class:`plotly.graph_objects.ohlc.decreasing.Line`
            instance or dict with compatible properties

        Returns
        -------
        Decreasing
        """
