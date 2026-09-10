import ipywidgets as widgets
from .basedatatypes import BaseFigure as BaseFigure, BasePlotlyType as BasePlotlyType
from .callbacks import BoxSelector as BoxSelector, InputDeviceState as InputDeviceState, LassoSelector as LassoSelector, Points as Points
from .serializers import custom_serializers as custom_serializers
from .version import __frontend_version__ as __frontend_version__
from _typeshed import Incomplete
from importlib import import_module as import_module
from urlparse import urlparse as parse

class BaseFigureWidget(BaseFigure, widgets.DOMWidget):
    """
    Base class for FigureWidget. The FigureWidget class is code-generated as a
    subclass
    """
    def __init__(self, data: Incomplete | None = None, layout: Incomplete | None = None, frames: Incomplete | None = None, skip_invalid: bool = False, **kwargs) -> None: ...
    def on_edits_completed(self, fn) -> None:
        """
        Register a function to be called after all pending trace and layout
        edit operations have completed

        If there are no pending edit operations then function is called
        immediately

        Parameters
        ----------
        fn : callable
            Function of zero arguments to be called when all pending edit
            operations have completed
        """
    @property
    def frames(self): ...
    @frames.setter
    def frames(self, new_frames) -> None: ...
