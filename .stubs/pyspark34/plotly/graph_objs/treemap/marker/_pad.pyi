from _typeshed import Incomplete
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Pad(_BaseTraceHierarchyType):
    @property
    def b(self):
        """
        Sets the padding form the bottom (in px).

        The 'b' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
    @b.setter
    def b(self, val) -> None: ...
    @property
    def l(self):
        """
        Sets the padding form the left (in px).

        The 'l' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
    @l.setter
    def l(self, val) -> None: ...
    @property
    def r(self):
        """
        Sets the padding form the right (in px).

        The 'r' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
    @r.setter
    def r(self, val) -> None: ...
    @property
    def t(self):
        """
        Sets the padding form the top (in px).

        The 't' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
    @t.setter
    def t(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, b: Incomplete | None = None, l: Incomplete | None = None, r: Incomplete | None = None, t: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Pad object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.treemap.marker.Pad`
        b
            Sets the padding form the bottom (in px).
        l
            Sets the padding form the left (in px).
        r
            Sets the padding form the right (in px).
        t
            Sets the padding form the top (in px).

        Returns
        -------
        Pad
        """
