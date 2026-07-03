from _typeshed import Incomplete
from email.message import Message
from pip._internal.exceptions import InstallationError as InstallationError
from pip._internal.locations import get_major_minor_version as get_major_minor_version
from pip._internal.metadata import BaseDistribution as BaseDistribution, FilesystemWheel as FilesystemWheel, get_wheel_distribution as get_wheel_distribution
from pip._internal.models.direct_url import DIRECT_URL_METADATA_NAME as DIRECT_URL_METADATA_NAME, DirectUrl as DirectUrl
from pip._internal.models.scheme import SCHEME_KEYS as SCHEME_KEYS, Scheme as Scheme
from pip._internal.utils.filesystem import adjacent_tmp_file as adjacent_tmp_file, replace as replace
from pip._internal.utils.misc import captured_stdout as captured_stdout, ensure_dir as ensure_dir, hash_file as hash_file, partition as partition
from pip._internal.utils.unpacking import current_umask as current_umask, is_within_directory as is_within_directory, set_extracted_file_to_default_mode_plus_executable as set_extracted_file_to_default_mode_plus_executable, zip_item_is_executable as zip_item_is_executable
from pip._internal.utils.wheel import parse_wheel as parse_wheel
from pip._vendor.distlib.scripts import ScriptMaker as ScriptMaker
from pip._vendor.distlib.util import get_export_entry as get_export_entry
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name
from typing import Any, Dict, Generator, List, Protocol, Sequence, Set, Tuple
from zipfile import ZipFile

class File(Protocol):
    src_record_path: RecordPath
    dest_path: str
    changed: bool
    def save(self) -> None: ...

logger: Incomplete
RecordPath: Incomplete
InstalledCSVRow = Tuple[RecordPath, str, int | str]

def rehash(path: str, blocksize: int = ...) -> Tuple[str, str]:
    """Return (encoded_digest, length) for path using hashlib.sha256()"""
def csv_io_kwargs(mode: str) -> Dict[str, Any]:
    """Return keyword arguments to properly open a CSV file
    in the given mode.
    """
def fix_script(path: str) -> bool:
    """Replace #!python with #!/path/to/python
    Return True if file was changed.
    """
def wheel_root_is_purelib(metadata: Message) -> bool: ...
def get_entrypoints(dist: BaseDistribution) -> Tuple[Dict[str, str], Dict[str, str]]: ...
def message_about_scripts_not_on_PATH(scripts: Sequence[str]) -> str | None:
    """Determine if any scripts are not on PATH and format a warning.
    Returns a warning message if one or more scripts are not on PATH,
    otherwise None.
    """
def get_csv_rows_for_installed(old_csv_rows: List[List[str]], installed: Dict[RecordPath, RecordPath], changed: Set[RecordPath], generated: List[str], lib_dir: str) -> List[InstalledCSVRow]:
    """
    :param installed: A map from archive RECORD path to installation RECORD
        path.
    """
def get_console_script_specs(console: Dict[str, str]) -> List[str]:
    """
    Given the mapping from entrypoint name to callable, return the relevant
    console script specs.
    """

class ZipBackedFile:
    src_record_path: Incomplete
    dest_path: Incomplete
    changed: bool
    def __init__(self, src_record_path: RecordPath, dest_path: str, zip_file: ZipFile) -> None: ...
    def save(self) -> None: ...

class ScriptFile:
    src_record_path: Incomplete
    dest_path: Incomplete
    changed: bool
    def __init__(self, file: File) -> None: ...
    def save(self) -> None: ...

class MissingCallableSuffix(InstallationError):
    def __init__(self, entry_point: str) -> None: ...

class PipScriptMaker(ScriptMaker):
    def make(self, specification: str, options: Dict[str, Any] | None = None) -> List[str]: ...

def req_error_context(req_description: str) -> Generator[None, None, None]: ...
def install_wheel(name: str, wheel_path: str, scheme: Scheme, req_description: str, pycompile: bool = True, warn_script_location: bool = True, direct_url: DirectUrl | None = None, requested: bool = False) -> None: ...
