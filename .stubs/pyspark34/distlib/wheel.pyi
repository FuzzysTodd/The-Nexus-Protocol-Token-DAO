from . import DistlibException as DistlibException, __version__ as __version__
from .compat import ZipFile as ZipFile, filter as filter, fsdecode as fsdecode, sysconfig as sysconfig, text_type as text_type
from .database import InstalledDistribution as InstalledDistribution
from .metadata import LEGACY_METADATA_FILENAME as LEGACY_METADATA_FILENAME, METADATA_FILENAME as METADATA_FILENAME, Metadata as Metadata, WHEEL_METADATA_FILENAME as WHEEL_METADATA_FILENAME
from .util import CSVReader as CSVReader, CSVWriter as CSVWriter, Cache as Cache, FileOperator as FileOperator, cached_property as cached_property, convert_path as convert_path, get_cache_base as get_cache_base, get_platform as get_platform, read_exports as read_exports, tempdir as tempdir
from .version import NormalizedVersion as NormalizedVersion, UnsupportedVersionError as UnsupportedVersionError
from _typeshed import Incomplete
from collections.abc import Generator

logger: Incomplete
cache: Incomplete
IMP_PREFIX: str
VER_SUFFIX: Incomplete
PYVER: Incomplete
IMPVER: Incomplete
ARCH: Incomplete
ABI: Incomplete
FILENAME_RE: Incomplete
NAME_VERSION_RE: Incomplete
SHEBANG_RE: Incomplete
SHEBANG_DETAIL_RE: Incomplete
SHEBANG_PYTHON: bytes
SHEBANG_PYTHONW: bytes
to_posix: Incomplete
imp: Incomplete

class Mounter:
    impure_wheels: Incomplete
    libs: Incomplete
    def __init__(self) -> None: ...
    def add(self, pathname, extensions) -> None: ...
    def remove(self, pathname) -> None: ...
    def find_module(self, fullname, path: Incomplete | None = None): ...
    def load_module(self, fullname): ...

class Wheel:
    """
    Class to build and install from Wheel files (PEP 427).
    """
    wheel_version: Incomplete
    hash_kind: str
    sign: Incomplete
    should_verify: Incomplete
    buildver: str
    pyver: Incomplete
    abi: Incomplete
    arch: Incomplete
    dirname: Incomplete
    name: str
    version: str
    def __init__(self, filename: Incomplete | None = None, sign: bool = False, verify: bool = False) -> None:
        """
        Initialise an instance using a (valid) filename.
        """
    @property
    def filename(self):
        """
        Build and return a filename from the various components.
        """
    @property
    def exists(self): ...
    @property
    def tags(self) -> Generator[Incomplete, None, None]: ...
    def metadata(self): ...
    def get_wheel_metadata(self, zf): ...
    def info(self): ...
    def process_shebang(self, data): ...
    def get_hash(self, data, hash_kind: Incomplete | None = None): ...
    def write_record(self, records, record_path, archive_record_path) -> None: ...
    def write_records(self, info, libdir, archive_paths) -> None: ...
    def build_zip(self, pathname, archive_paths) -> None: ...
    def build(self, paths, tags: Incomplete | None = None, wheel_version: Incomplete | None = None):
        """
        Build a wheel from files in specified paths, and use any specified tags
        when determining the name of the wheel.
        """
    def skip_entry(self, arcname):
        """
        Determine whether an archive entry should be skipped when verifying
        or installing.
        """
    def install(self, paths, maker, **kwargs):
        """
        Install a wheel to the specified paths. If kwarg ``warner`` is
        specified, it should be a callable, which will be called with two
        tuples indicating the wheel version of this software and the wheel
        version in the file, if there is a discrepancy in the versions.
        This can be used to issue any warnings to raise any exceptions.
        If kwarg ``lib_only`` is True, only the purelib/platlib files are
        installed, and the headers, scripts, data and dist-info metadata are
        not written. If kwarg ``bytecode_hashed_invalidation`` is True, written
        bytecode will try to use file-hash based invalidation (PEP-552) on
        supported interpreter versions (CPython 2.7+).

        The return value is a :class:`InstalledDistribution` instance unless
        ``options.lib_only`` is True, in which case the return value is ``None``.
        """
    def is_compatible(self):
        """
        Determine if a wheel is compatible with the running system.
        """
    def is_mountable(self):
        """
        Determine if a wheel is asserted as mountable by its metadata.
        """
    def mount(self, append: bool = False) -> None: ...
    def unmount(self) -> None: ...
    def verify(self) -> None: ...
    def update(self, modifier, dest_dir: Incomplete | None = None, **kwargs):
        """
        Update the contents of a wheel in a generic way. The modifier should
        be a callable which expects a dictionary argument: its keys are
        archive-entry paths, and its values are absolute filesystem paths
        where the contents the corresponding archive entries can be found. The
        modifier is free to change the contents of the files pointed to, add
        new entries and remove entries, before returning. This method will
        extract the entire contents of the wheel to a temporary location, call
        the modifier, and then use the passed (and possibly updated)
        dictionary to write a new wheel. If ``dest_dir`` is specified, the new
        wheel is written there -- otherwise, the original wheel is overwritten.

        The modifier should return True if it updated the wheel, else False.
        This method returns the same value the modifier returns.
        """

def compatible_tags():
    """
    Return (pyver, abi, arch) tuples compatible with this Python.
    """

COMPATIBLE_TAGS: Incomplete

def is_compatible(wheel, tags: Incomplete | None = None): ...
