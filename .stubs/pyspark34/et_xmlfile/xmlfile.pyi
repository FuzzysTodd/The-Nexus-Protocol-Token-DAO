from _typeshed import Incomplete
from collections.abc import Generator

class LxmlSyntaxError(Exception): ...

class _FakeIncrementalFileWriter:
    """Replacement for _IncrementalFileWriter of lxml.
       Uses ElementTree to build xml in memory."""
    def __init__(self, output_file) -> None: ...
    def element(self, tag, attrib: Incomplete | None = None, nsmap: Incomplete | None = None, **_extra) -> Generator[None, None, None]:
        """Create a new xml element using a context manager.
        The elements are written when the top level context is left.

        This is for code compatibility only as it is quite slow.
        """
    def write(self, arg) -> None:
        """Write a string or subelement."""
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class xmlfile:
    """Context manager that can replace lxml.etree.xmlfile."""
    def __init__(self, output_file, buffered: bool = False, encoding: Incomplete | None = None, close: bool = False) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
