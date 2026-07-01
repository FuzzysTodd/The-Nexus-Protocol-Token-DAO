from _pytest.recwarn import WarningsChecker
from _typeshed import Incomplete
from typing import Tuple, Type

__all__ = ['pytest_warns']

class NoWarningsChecker:
    cw: Incomplete
    rec: Incomplete
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def pytest_warns(warning: Type[Warning] | Tuple[Type[Warning], ...] | None) -> WarningsChecker | NoWarningsChecker:
    """

    Parameters
    ----------
    warning : {None, Warning, Tuple[Warning]}
        None if no warning is produced, or a single or multiple Warnings

    Returns
    -------
    cm

    """
