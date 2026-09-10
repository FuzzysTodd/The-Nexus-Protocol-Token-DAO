from .widgets import *
from ._version import __jupyter_widgets_base_version__ as __jupyter_widgets_base_version__, __jupyter_widgets_controls_version__ as __jupyter_widgets_controls_version__, __protocol_version__ as __protocol_version__, __version__ as __version__
from _typeshed import Incomplete
from traitlets import dlink as dlink, link as link

def load_ipython_extension(ip) -> None:
    """Set up Jupyter to work with widgets"""
def register_comm_target(kernel: Incomplete | None = None) -> None:
    """Register the jupyter.widget comm target"""
