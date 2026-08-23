from _typeshed import Incomplete
from numba.core.config import PYVERSION as PYVERSION

logger: Incomplete

def init_all() -> None:
    """Execute all `numba_extensions` entry points with the name `init`

    If extensions have already been initialized, this function does nothing.
    """
