from _typeshed import Incomplete
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Circle(_BaseLayoutHierarchyType):
    @property
    def radius(self):
        '''
        Sets the circle radius (mapbox.layer.paint.circle-radius). Has
        an effect only when `type` is set to "circle".

        The \'radius\' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        '''
    @radius.setter
    def radius(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, radius: Incomplete | None = None, **kwargs) -> None:
        '''
        Construct a new Circle object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.mapbox.layer.Circle`
        radius
            Sets the circle radius (mapbox.layer.paint.circle-
            radius). Has an effect only when `type` is set to
            "circle".

        Returns
        -------
        Circle
        '''
