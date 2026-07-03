from .shutils import env as env, find as find, homedir as homedir, minpath as minpath, mkdir as mkdir, rmtree as rmtree, rootdir as rootdir, sep as sep, shellsub as shellsub, shelltype as shelltype, username as username, walk as walk, where as where, whereis as whereis, which as which
from .utils import convert as convert, disk_used as disk_used, expandvars as expandvars, findpackage as findpackage, getvars as getvars, index_join as index_join, index_slice as index_slice, kbytes as kbytes, parse_remote as parse_remote, pattern as pattern, remote as remote, replace as replace, select as select, selectdict as selectdict, wait_for as wait_for, which_python as which_python
from _typeshed import Incomplete
from version import __version__ as __version__

parent: Incomplete

def license() -> None:
    """print the license"""
def citation() -> None:
    """print the citation"""
