from .importer import Importer as Importer, ObjMismatchError as ObjMismatchError, ObjNotFoundError as ObjNotFoundError, sys_importer as sys_importer
from _typeshed import Incomplete
from pickle import _Pickler

class PackagePickler(_Pickler):
    """Package-aware pickler.

    This behaves the same as a normal pickler, except it uses an `Importer`
    to find objects and modules to save.
    """
    importer: Incomplete
    dispatch: Incomplete
    def __init__(self, importer: Importer, *args, **kwargs) -> None: ...
    def save_global(self, obj, name: Incomplete | None = None) -> None: ...

def create_pickler(data_buf, importer, protocol: int = 4): ...
