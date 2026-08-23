from .testing import tools as tools
from _typeshed import Incomplete
from collections.abc import Generator

def pytest_collection_modifyitems(items) -> None:
    """This function is automatically run by pytest passing all collected test
    functions.

    We use it to add asyncio marker to all async tests and assert we don't use
    test functions that are async generators which wouldn't make sense.
    """
def get_ipython(): ...
def work_path() -> Generator[None, None, None]: ...
def nopage(strng, start: int = 0, screen_lines: int = 0, pager_cmd: Incomplete | None = None) -> None: ...
def xsys(self, cmd) -> None:
    """Replace the default system call with a capturing one for doctest.
    """
def inject() -> None: ...
