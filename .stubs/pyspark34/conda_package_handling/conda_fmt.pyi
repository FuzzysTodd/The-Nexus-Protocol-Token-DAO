import zstandard
from . import utils as utils
from .interface import AbstractBaseFormat as AbstractBaseFormat
from _typeshed import Incomplete
from typing import Callable

CONDA_PACKAGE_FORMAT_VERSION: int
DEFAULT_COMPRESSION_TUPLE: Incomplete
ZSTD_COMPRESS_LEVEL: int
ZSTD_COMPRESS_THREADS: int

class CondaFormat_v2(AbstractBaseFormat):
    """If there's another conda format or breaking changes, please create a new class and keep this
    one, so that handling of v2 stays working."""
    @staticmethod
    def supported(fn): ...
    @staticmethod
    def extract(fn, dest_dir, **kw) -> None: ...
    @staticmethod
    def extract_info(fn, dest_dir: Incomplete | None = None): ...
    size: int
    @staticmethod
    def create(prefix, file_list, out_fn, out_folder=..., compressor: Callable[[], zstandard.ZstdCompressor] | None = None, compression_tuple=(None, None, None)): ...
    @staticmethod
    def get_pkg_details(in_file): ...
