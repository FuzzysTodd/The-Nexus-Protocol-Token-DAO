import linecache
from _typeshed import Incomplete

getline = linecache.getline

def getlines(filename, module_globals: Incomplete | None = None):
    """
    Deprecated since IPython 6.0
    """
