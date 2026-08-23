from _typeshed import Incomplete
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Domain(_BaseLayoutHierarchyType):
    @property
    def x(self):
        """
            Sets the horizontal domain of this grid subplot (in plot
            fraction). The first and last cells end exactly at the domain
            edges, with no grout around the edges.

            The 'x' property is an info array that may be specified as:

            * a list or tuple of 2 elements where:
        (0) The 'x[0]' property is a number and may be specified as:
              - An int or float in the interval [0, 1]
        (1) The 'x[1]' property is a number and may be specified as:
              - An int or float in the interval [0, 1]

            Returns
            -------
            list
        """
    @x.setter
    def x(self, val) -> None: ...
    @property
    def y(self):
        """
            Sets the vertical domain of this grid subplot (in plot
            fraction). The first and last cells end exactly at the domain
            edges, with no grout around the edges.

            The 'y' property is an info array that may be specified as:

            * a list or tuple of 2 elements where:
        (0) The 'y[0]' property is a number and may be specified as:
              - An int or float in the interval [0, 1]
        (1) The 'y[1]' property is a number and may be specified as:
              - An int or float in the interval [0, 1]

            Returns
            -------
            list
        """
    @y.setter
    def y(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, x: Incomplete | None = None, y: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Domain object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.grid.Domain`
        x
            Sets the horizontal domain of this grid subplot (in
            plot fraction). The first and last cells end exactly at
            the domain edges, with no grout around the edges.
        y
            Sets the vertical domain of this grid subplot (in plot
            fraction). The first and last cells end exactly at the
            domain edges, with no grout around the edges.

        Returns
        -------
        Domain
        """
