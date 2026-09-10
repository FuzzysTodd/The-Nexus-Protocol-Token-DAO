from . import sysinfo as sysinfo
from _typeshed import Incomplete

def default_get_open_files(pipes: bool = False, **_kwargs): ...
def default_get_number_open_files(): ...
lsof_get_open_files = default_get_open_files
get_open_files = default_get_open_files
get_number_open_files = default_get_number_open_files

class _TrivialOpenFile:
    fd: Incomplete
    def __init__(self, fd) -> None: ...

class DoesNotLeakFilesMixin:
    """
    A test case mixin that helps find a method that's leaking an
    open file.

    Only mix this in when needed to debug, it slows tests down.
    """
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
