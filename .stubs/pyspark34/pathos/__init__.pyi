from . import connection as connection, core as core, helpers as helpers, hosts as hosts, maps as maps, multiprocessing as multiprocessing, parallel, pools as pools, selector as selector, serial, server as server, threading as threading, util as util
from _typeshed import Incomplete
from version import __version__ as __version__

parent: Incomplete

def logger(level: Incomplete | None = None, handler: Incomplete | None = None, **kwds):
    """generate a logger instance for pathos

    Args:
        level (int, default=None): the logging level.
        handler (object, default=None): a ``logging`` handler instance.
        name (str, default='pathos'): name of the logger instance.
    Returns:
        configured logger instance.
    """
python = serial
pp = parallel

def license() -> None:
    """print license"""
def citation() -> None:
    """print citation"""
