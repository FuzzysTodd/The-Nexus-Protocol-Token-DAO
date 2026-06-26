from . import detect as detect, session as session, source as source, temp as temp
from ._dill import CONTENTS_FMODE as CONTENTS_FMODE, DEFAULT_PROTOCOL as DEFAULT_PROTOCOL, FILE_FMODE as FILE_FMODE, HANDLE_FMODE as HANDLE_FMODE, HIGHEST_PROTOCOL as HIGHEST_PROTOCOL, PickleError as PickleError, PickleWarning as PickleWarning, Pickler as Pickler, PicklingError as PicklingError, PicklingWarning as PicklingWarning, Unpickler as Unpickler, UnpicklingError as UnpicklingError, UnpicklingWarning as UnpicklingWarning, check as check, copy as copy, dump as dump, dumps as dumps, load as load, loads as loads, pickle as pickle, pickles as pickles, register as register
from .session import dump_module as dump_module, dump_session as dump_session, load_module as load_module, load_module_asdict as load_module_asdict, load_session as load_session
from .settings import settings as settings
from _typeshed import Incomplete
from version import __version__ as __version__

parent: Incomplete
objects: Incomplete

def load_types(pickleable: bool = True, unpickleable: bool = True) -> None:
    """load pickleable and/or unpickleable types to ``dill.types``

    ``dill.types`` is meant to mimic the ``types`` module, providing a
    registry of object types.  By default, the module is empty (for import
    speed purposes). Use the ``load_types`` function to load selected object
    types to the ``dill.types`` module.

    Args:
        pickleable (bool, default=True): if True, load pickleable types.
        unpickleable (bool, default=True): if True, load unpickleable types.

    Returns:
        None
    """
def extend(use_dill: bool = True) -> None:
    """add (or remove) dill types to/from the pickle registry

    by default, ``dill`` populates its types to ``pickle.Pickler.dispatch``.
    Thus, all ``dill`` types are available upon calling ``'import pickle'``.
    To drop all ``dill`` types from the ``pickle`` dispatch, *use_dill=False*.

    Args:
        use_dill (bool, default=True): if True, extend the dispatch table.

    Returns:
        None
    """
def license() -> None:
    """print license"""
def citation() -> None:
    """print citation"""
