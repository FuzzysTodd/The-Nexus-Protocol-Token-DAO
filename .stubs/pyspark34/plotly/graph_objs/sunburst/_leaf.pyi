from _typeshed import Incomplete
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Leaf(_BaseTraceHierarchyType):
    @property
    def opacity(self):
        """
        Sets the opacity of the leaves. With colorscale it is defaulted
        to 1; otherwise it is defaulted to 0.7

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
        Construct a new Leaf object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.sunburst.Leaf`
        opacity
            Sets the opacity of the leaves. With colorscale it is
            defaulted to 1; otherwise it is defaulted to 0.7

        Returns
        -------
        Leaf
        """
