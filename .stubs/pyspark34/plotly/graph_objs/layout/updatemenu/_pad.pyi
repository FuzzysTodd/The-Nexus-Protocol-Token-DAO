from _typeshed import Incomplete
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Pad(_BaseLayoutHierarchyType):
    @property
    def b(self):
        """
        The amount of padding (in px) along the bottom of the
        component.

        The 'b' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
    @b.setter
    def b(self, val) -> None: ...
    @property
    def l(self):
        """
        The amount of padding (in px) on the left side of the
        component.

        The 'l' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
    @l.setter
    def l(self, val) -> None: ...
    @property
    def r(self):
        """
        The amount of padding (in px) on the right side of the
        component.

        The 'r' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
    @r.setter
    def r(self, val) -> None: ...
    @property
    def t(self):
        """
        The amount of padding (in px) along the top of the component.

        The 't' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
    @t.setter
    def t(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, b: Incomplete | None = None, l: Incomplete | None = None, r: Incomplete | None = None, t: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Pad object

        Sets the padding around the buttons or dropdown menu.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.updatemenu.Pad`
        b
            The amount of padding (in px) along the bottom of the
            component.
        l
            The amount of padding (in px) on the left side of the
            component.
        r
            The amount of padding (in px) on the right side of the
            component.
        t
            The amount of padding (in px) along the top of the
            component.

        Returns
        -------
        Pad
        """
