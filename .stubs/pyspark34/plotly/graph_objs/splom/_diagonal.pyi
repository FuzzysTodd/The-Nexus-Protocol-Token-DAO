from _typeshed import Incomplete
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Diagonal(_BaseTraceHierarchyType):
    @property
    def visible(self):
        """
        Determines whether or not subplots on the diagonal are
        displayed.

        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
    @visible.setter
    def visible(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, visible: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Diagonal object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.splom.Diagonal`
        visible
            Determines whether or not subplots on the diagonal are
            displayed.

        Returns
        -------
        Diagonal
        """
