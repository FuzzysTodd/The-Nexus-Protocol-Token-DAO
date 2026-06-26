from _typeshed import Incomplete
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Lightposition(_BaseTraceHierarchyType):
    @property
    def x(self):
        """
        Numeric vector, representing the X coordinate for each vertex.

        The 'x' property is a number and may be specified as:
          - An int or float in the interval [-100000, 100000]

        Returns
        -------
        int|float
        """
    @x.setter
    def x(self, val) -> None: ...
    @property
    def y(self):
        """
        Numeric vector, representing the Y coordinate for each vertex.

        The 'y' property is a number and may be specified as:
          - An int or float in the interval [-100000, 100000]

        Returns
        -------
        int|float
        """
    @y.setter
    def y(self, val) -> None: ...
    @property
    def z(self):
        """
        Numeric vector, representing the Z coordinate for each vertex.

        The 'z' property is a number and may be specified as:
          - An int or float in the interval [-100000, 100000]

        Returns
        -------
        int|float
        """
    @z.setter
    def z(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, x: Incomplete | None = None, y: Incomplete | None = None, z: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Lightposition object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.streamtube.Lightposition`
        x
            Numeric vector, representing the X coordinate for each
            vertex.
        y
            Numeric vector, representing the Y coordinate for each
            vertex.
        z
            Numeric vector, representing the Z coordinate for each
            vertex.

        Returns
        -------
        Lightposition
        """
