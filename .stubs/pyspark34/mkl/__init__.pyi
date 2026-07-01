from ._py_mkl_service import *
from _typeshed import Incomplete

class RTLD_for_MKL:
    saved_rtld: Incomplete
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...

__version__: str
