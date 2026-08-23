from _typeshed import Incomplete
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Projection(_BaseLayoutHierarchyType):
    @property
    def type(self):
        '''
        Sets the projection type. The projection type could be either
        "perspective" or "orthographic". The default is "perspective".

        The \'type\' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [\'perspective\', \'orthographic\']

        Returns
        -------
        Any
        '''
    @type.setter
    def type(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, type: Incomplete | None = None, **kwargs) -> None:
        '''
        Construct a new Projection object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.scene.c
            amera.Projection`
        type
            Sets the projection type. The projection type could be
            either "perspective" or "orthographic". The default is
            "perspective".

        Returns
        -------
        Projection
        '''
