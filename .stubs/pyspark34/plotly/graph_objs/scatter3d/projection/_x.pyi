from _typeshed import Incomplete
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class X(_BaseTraceHierarchyType):
    @property
    def opacity(self):
        """
        Sets the projection color.

        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
    @opacity.setter
    def opacity(self, val) -> None: ...
    @property
    def scale(self):
        """
        Sets the scale factor determining the size of the projection
        marker points.

        The 'scale' property is a number and may be specified as:
          - An int or float in the interval [0, 10]

        Returns
        -------
        int|float
        """
    @scale.setter
    def scale(self, val) -> None: ...
    @property
    def show(self):
        """
        Sets whether or not projections are shown along the x axis.

        The 'show' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
    @show.setter
    def show(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, opacity: Incomplete | None = None, scale: Incomplete | None = None, show: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new X object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.scatter3d.projection.X`
        opacity
            Sets the projection color.
        scale
            Sets the scale factor determining the size of the
            projection marker points.
        show
            Sets whether or not projections are shown along the x
            axis.

        Returns
        -------
        X
        """
