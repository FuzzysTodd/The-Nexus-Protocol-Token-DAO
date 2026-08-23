from _typeshed import Incomplete
from io import StringIO
from pathlib import Path
from pip._vendor.pyproject_hooks import BuildBackendHookCaller
from types import FunctionType, TracebackType
from typing import Any, Callable, ContextManager, Dict, Iterable, List, TextIO, Tuple, Type, TypeVar

__all__ = ['rmtree', 'display_path', 'backup_dir', 'ask', 'splitext', 'format_size', 'is_installable_dir', 'normalize_path', 'renames', 'get_prog', 'captured_stdout', 'ensure_dir', 'remove_auth_from_url', 'check_externally_managed', 'ConfiguredBuildBackendHookCaller']

T = TypeVar('T')
ExcInfo = Tuple[Type[BaseException], BaseException, TracebackType]
VersionInfo = Tuple[int, int, int]
NetlocTuple = Tuple[str, Tuple[str | None, str | None]]
OnExc = Callable[[FunctionType, Path, BaseException], Any]
OnErr = Callable[[FunctionType, Path, ExcInfo], Any]

def ensure_dir(path: str) -> None:
    """os.path.makedirs without EEXIST."""
def get_prog() -> str: ...
def rmtree(dir: str, ignore_errors: bool = False, onexc: OnExc | None = None) -> None: ...
def display_path(path: str) -> str:
    """Gives the display value for a given path, making it relative to cwd
    if possible."""
def backup_dir(dir: str, ext: str = '.bak') -> str:
    """Figure out the name of a directory to back up the given dir to
    (adding .bak, .bak2, etc)"""
def ask(message: str, options: Iterable[str]) -> str:
    """Ask the message interactively, with the given possible responses"""
def format_size(bytes: float) -> str: ...
def is_installable_dir(path: str) -> bool:
    """Is path is a directory containing pyproject.toml or setup.py?

    If pyproject.toml exists, this is a PEP 517 project. Otherwise we look for
    a legacy setuptools layout by identifying setup.py. We don't check for the
    setup.cfg because using it without setup.py is only available for PEP 517
    projects, which are already covered by the pyproject.toml check.
    """
def normalize_path(path: str, resolve_symlinks: bool = True) -> str:
    """
    Convert a path to its canonical, case-normalized, absolute version.

    """
def splitext(path: str) -> Tuple[str, str]:
    """Like os.path.splitext, but take off .tar too"""
def renames(old: str, new: str) -> None:
    """Like os.renames(), but handles renaming across devices."""

class StreamWrapper(StringIO):
    orig_stream: TextIO
    @classmethod
    def from_stream(cls, orig_stream: TextIO) -> StreamWrapper: ...
    @property
    def encoding(self) -> str: ...

def captured_stdout() -> ContextManager[StreamWrapper]:
    """Capture the output of sys.stdout:

       with captured_stdout() as stdout:
           print('hello')
       self.assertEqual(stdout.getvalue(), 'hello
')

    Taken from Lib/support/__init__.py in the CPython repo.
    """
def remove_auth_from_url(url: str) -> str:
    """Return a copy of url with 'username:password@' removed."""

class HiddenText:
    secret: Incomplete
    redacted: Incomplete
    def __init__(self, secret: str, redacted: str) -> None: ...
    def __eq__(self, other: Any) -> bool: ...

def check_externally_managed() -> None:
    """Check whether the current environment is externally managed.

    If the ``EXTERNALLY-MANAGED`` config file is found, the current environment
    is considered externally managed, and an ExternallyManagedEnvironment is
    raised.
    """

class ConfiguredBuildBackendHookCaller(BuildBackendHookCaller):
    config_holder: Incomplete
    def __init__(self, config_holder: Any, source_dir: str, build_backend: str, backend_path: str | None = None, runner: Callable[..., None] | None = None, python_executable: str | None = None) -> None: ...
    def build_wheel(self, wheel_directory: str, config_settings: Dict[str, str | List[str]] | None = None, metadata_directory: str | None = None) -> str: ...
    def build_sdist(self, sdist_directory: str, config_settings: Dict[str, str | List[str]] | None = None) -> str: ...
    def build_editable(self, wheel_directory: str, config_settings: Dict[str, str | List[str]] | None = None, metadata_directory: str | None = None) -> str: ...
    def get_requires_for_build_wheel(self, config_settings: Dict[str, str | List[str]] | None = None) -> List[str]: ...
    def get_requires_for_build_sdist(self, config_settings: Dict[str, str | List[str]] | None = None) -> List[str]: ...
    def get_requires_for_build_editable(self, config_settings: Dict[str, str | List[str]] | None = None) -> List[str]: ...
    def prepare_metadata_for_build_wheel(self, metadata_directory: str, config_settings: Dict[str, str | List[str]] | None = None, _allow_fallback: bool = True) -> str: ...
    def prepare_metadata_for_build_editable(self, metadata_directory: str, config_settings: Dict[str, str | List[str]] | None = None, _allow_fallback: bool = True) -> str: ...
