from _typeshed import Incomplete
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Aspectratio(_BaseLayoutHierarchyType):
    @property
    def x(self):
        """
        The 'x' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
    @x.setter
    def x(self, val) -> None: ...
    @property
    def y(self):
        """
        The 'y' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
    @y.setter
    def y(self, val) -> None: ...
    @property
    def z(self):
        """
        The 'z' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
    @z.setter
    def z(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, x: Incomplete | None = None, y: Incomplete | None = None, z: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Aspectratio object

        Sets this scene's axis aspectratio.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.scene.Aspectratio`
        x

        y

        z


        Returns
        -------
        Aspectratio
        """
