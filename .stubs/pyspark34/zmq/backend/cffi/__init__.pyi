from ._poll import *
from .context import *
from .devices import *
from .error import *
from .message import *
from .socket import *
from .utils import *

__all__ = ['zmq_version_info']

def zmq_version_info():
    """Get libzmq version as tuple of ints"""
