from .conda_fmt import ZSTD_COMPRESS_LEVEL as ZSTD_COMPRESS_LEVEL, ZSTD_COMPRESS_THREADS as ZSTD_COMPRESS_THREADS
from .exceptions import ConversionError as ConversionError, InvalidArchiveError as InvalidArchiveError
from .interface import AbstractBaseFormat as AbstractBaseFormat
from .utils import filter_info_files as filter_info_files
from _typeshed import Incomplete

SUPPORTED_EXTENSIONS: dict[str, type[AbstractBaseFormat]]
libarchive_enabled: bool
THREADSAFE_EXTRACT: bool

def get_default_extracted_folder(in_file, abspath: bool = True): ...
def extract(fn, dest_dir: Incomplete | None = None, components: Incomplete | None = None, prefix: Incomplete | None = None) -> None: ...
def create(prefix, file_list, out_fn, out_folder: Incomplete | None = None, **kw): ...
def transmute(in_file, out_ext, out_folder: Incomplete | None = None, processes: int = 1, **kw): ...
def get_pkg_details(in_file):
    """For the new pkg format, we return the size and hashes of the inner pkg part of the file"""
