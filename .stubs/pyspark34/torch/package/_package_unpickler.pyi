import pickle
from .importer import Importer as Importer

class PackageUnpickler(pickle._Unpickler):
    """Package-aware unpickler.

    This behaves the same as a normal unpickler, except it uses `importer` to
    find any global names that it encounters while unpickling.
    """
    def __init__(self, importer: Importer, *args, **kwargs) -> None: ...
    def find_class(self, module, name): ...
