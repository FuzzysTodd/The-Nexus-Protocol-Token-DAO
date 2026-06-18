from .traitlets import *
import typing as _t
from . import traitlets as traitlets
from ._version import __version__ as __version__, version_info as version_info
from .utils.bunch import Bunch as Bunch
from .utils.decorators import signature_has_traits as signature_has_traits
from .utils.importstring import import_item as import_item

__all__ = ['traitlets', '__version__', 'version_info', 'Bunch', 'signature_has_traits', 'import_item', 'Sentinel']

class Sentinel(traitlets.Sentinel):
    def __init__(self, *args: _t.Any, **kwargs: _t.Any) -> None: ...
