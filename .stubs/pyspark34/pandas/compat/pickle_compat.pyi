import pickle as pkl
from pandas import Index as Index
from pandas._libs.arrays import NDArrayBacked as NDArrayBacked
from pandas._libs.tslibs import BaseOffset as BaseOffset
from pandas.core.arrays import DatetimeArray as DatetimeArray, PeriodArray as PeriodArray, TimedeltaArray as TimedeltaArray
from pandas.core.internals import BlockManager as BlockManager
from typing import Generator

def load_reduce(self) -> None: ...

class Unpickler(pkl._Unpickler):
    def find_class(self, module, name): ...

def load_newobj(self) -> None: ...
def load_newobj_ex(self) -> None: ...
def load(fh, encoding: str | None = None, is_verbose: bool = False):
    """
    Load a pickle, with a provided encoding,

    Parameters
    ----------
    fh : a filelike object
    encoding : an optional encoding
    is_verbose : show exception output
    """
def loads(bytes_object: bytes, *, fix_imports: bool = True, encoding: str = 'ASCII', errors: str = 'strict'):
    """
    Analogous to pickle._loads.
    """
def patch_pickle() -> Generator[None, None, None]:
    """
    Temporarily patch pickle to use our unpickler.
    """
