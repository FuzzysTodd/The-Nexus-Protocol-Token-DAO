from .. import Command as Command, errors as errors, namespaces as namespaces
from ..discovery import find_package_path as find_package_path
from ..dist import Distribution as Distribution
from ..warnings import InformationOnly as InformationOnly, SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning, SetuptoolsWarning as SetuptoolsWarning
from _typeshed import Incomplete
from enum import Enum
from pathlib import Path
from typing import Dict, List, Protocol
from wheel.wheelfile import WheelFile

class _EditableMode(Enum):
    """
    Possible editable installation modes:
    `lenient` (new files automatically added to the package - DEFAULT);
    `strict` (requires a new installation when files are added/removed); or
    `compat` (attempts to emulate `python setup.py develop` - DEPRECATED).
    """
    STRICT: str
    LENIENT: str
    COMPAT: str
    @classmethod
    def convert(cls, mode: str | None) -> _EditableMode: ...

class editable_wheel(Command):
    """Build 'editable' wheel for development.
    This command is private and reserved for internal use of setuptools,
    users should rely on ``setuptools.build_meta`` APIs.
    """
    description: str
    user_options: Incomplete
    dist_dir: Incomplete
    dist_info_dir: Incomplete
    project_dir: Incomplete
    mode: Incomplete
    def initialize_options(self) -> None: ...
    package_dir: Incomplete
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...

class EditableStrategy(Protocol):
    def __call__(self, wheel: WheelFile, files: List[str], mapping: Dict[str, str]): ...
    def __enter__(self): ...
    def __exit__(self, _exc_type: type[BaseException] | None, _exc_value: BaseException | None, _traceback: types.TracebackType | None): ...

class _StaticPth:
    dist: Incomplete
    name: Incomplete
    path_entries: Incomplete
    def __init__(self, dist: Distribution, name: str, path_entries: List[Path]) -> None: ...
    def __call__(self, wheel: WheelFile, files: List[str], mapping: Dict[str, str]): ...
    def __enter__(self): ...
    def __exit__(self, _exc_type: type[BaseException] | None, _exc_value: BaseException | None, _traceback: types.TracebackType | None) -> None: ...

class _LinkTree(_StaticPth):
    """
    Creates a ``.pth`` file that points to a link tree in the ``auxiliary_dir``.

    This strategy will only link files (not dirs), so it can be implemented in
    any OS, even if that means using hardlinks instead of symlinks.

    By collocating ``auxiliary_dir`` and the original source code, limitations
    with hardlinks should be avoided.
    """
    auxiliary_dir: Incomplete
    build_lib: Incomplete
    def __init__(self, dist: Distribution, name: str, auxiliary_dir: _Path, build_lib: _Path) -> None: ...
    def __call__(self, wheel: WheelFile, files: List[str], mapping: Dict[str, str]): ...
    def __enter__(self): ...
    def __exit__(self, _exc_type: type[BaseException] | None, _exc_value: BaseException | None, _traceback: types.TracebackType | None) -> None: ...

class _TopLevelFinder:
    dist: Incomplete
    name: Incomplete
    def __init__(self, dist: Distribution, name: str) -> None: ...
    def __call__(self, wheel: WheelFile, files: List[str], mapping: Dict[str, str]): ...
    def __enter__(self): ...
    def __exit__(self, _exc_type: type[BaseException] | None, _exc_value: BaseException | None, _traceback: types.TracebackType | None) -> None: ...

class _NamespaceInstaller(namespaces.Installer):
    distribution: Incomplete
    src_root: Incomplete
    installation_dir: Incomplete
    editable_name: Incomplete
    outputs: Incomplete
    dry_run: bool
    def __init__(self, distribution, installation_dir, editable_name, src_root) -> None: ...

class LinksNotSupported(errors.FileError):
    """File system does not seem to support either symlinks or hard links."""
class _DebuggingTips(SetuptoolsWarning): ...
