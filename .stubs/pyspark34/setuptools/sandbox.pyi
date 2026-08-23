from _typeshed import Incomplete
from distutils.errors import DistutilsError

__all__ = ['AbstractSandbox', 'DirectorySandbox', 'SandboxViolation', 'run_setup']

class UnpickleableException(Exception):
    """
    An exception representing another Exception that could not be pickled.
    """
    @staticmethod
    def dump(type, exc):
        """
        Always return a dumped (pickled) type and exc. If exc can't be pickled,
        wrap it in UnpickleableException first.
        """

class ExceptionSaver:
    """
    A Context Manager that will save an exception, serialized, and restore it
    later.
    """
    def __enter__(self): ...
    def __exit__(self, type: type[BaseException] | None, exc: BaseException | None, tb: types.TracebackType | None): ...
    def resume(self) -> None:
        """restore and re-raise any exception"""

def run_setup(setup_script, args):
    """Run a distutils setup script, sandboxed in its directory"""

class AbstractSandbox:
    """Wrap 'os' module and 'open()' builtin for virtualizing setup scripts"""
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def run(self, func):
        """Run 'func' under os sandboxing"""

class DirectorySandbox(AbstractSandbox):
    """Restrict operations to a single subdirectory - pseudo-chroot"""
    write_ops: Incomplete
    def __init__(self, sandbox, exceptions=...) -> None: ...
    def tmpnam(self) -> None: ...
    def open(self, file, flags, mode: int = 511, *args, **kw):
        """Called for low-level os.open()"""

class SandboxViolation(DistutilsError):
    """A setup script attempted to modify the filesystem outside the sandbox"""
    tmpl: Incomplete
