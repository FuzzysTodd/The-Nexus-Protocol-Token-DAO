from typing import Tuple
from zmq.backend import zmq_version_info as zmq_version_info

__all__ = ['zmq_version', 'zmq_version_info', 'pyzmq_version', 'pyzmq_version_info', '__version__', '__revision__']

__version__: str
__revision__: str

def pyzmq_version() -> str:
    """return the version of pyzmq as a string"""
def pyzmq_version_info() -> Tuple[int, int, int] | Tuple[int, int, int, float]:
    """return the pyzmq version as a tuple of at least three numbers

    If pyzmq is a development version, `inf` will be appended after the third integer.
    """
def zmq_version() -> str:
    """return the version of libzmq as a string"""
