from _typeshed import Incomplete
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Margin(_BaseLayoutHierarchyType):
    @property
    def autoexpand(self):
        """
        Turns on/off margin expansion computations. Legends, colorbars,
        updatemenus, sliders, axis rangeselector and rangeslider are
        allowed to push the margins by defaults.

        The 'autoexpand' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
    @autoexpand.setter
    def autoexpand(self, val) -> None: ...
    @property
    def b(self):
        """
        Sets the bottom margin (in px).

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
        Sets the left margin (in px).

        The 'l' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
    @l.setter
    def l(self, val) -> None: ...
    @property
    def pad(self):
        """
        Sets the amount of padding (in px) between the plotting area
        and the axis lines

        The 'pad' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
    @pad.setter
    def pad(self, val) -> None: ...
    @property
    def r(self):
        """
        Sets the right margin (in px).

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
        Sets the top margin (in px).

        The 't' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
    @t.setter
    def t(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, autoexpand: Incomplete | None = None, b: Incomplete | None = None, l: Incomplete | None = None, pad: Incomplete | None = None, r: Incomplete | None = None, t: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Margin object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.Margin`
        autoexpand
            Turns on/off margin expansion computations. Legends,
            colorbars, updatemenus, sliders, axis rangeselector and
            rangeslider are allowed to push the margins by
            defaults.
        b
            Sets the bottom margin (in px).
        l
            Sets the left margin (in px).
        pad
            Sets the amount of padding (in px) between the plotting
            area and the axis lines
        r
            Sets the right margin (in px).
        t
            Sets the top margin (in px).

        Returns
        -------
        Margin
        """
