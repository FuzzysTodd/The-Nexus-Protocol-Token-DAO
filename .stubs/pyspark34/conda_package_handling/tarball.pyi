from . import streaming as streaming, utils as utils
from .interface import AbstractBaseFormat as AbstractBaseFormat
from _typeshed import Incomplete

LOG: Incomplete

def create_compressed_tarball(prefix, files, tmpdir, basename, ext, compression_filter, filter_opts: str = ''): ...

class CondaTarBZ2(AbstractBaseFormat):
    @staticmethod
    def supported(fn): ...
    @staticmethod
    def extract(fn, dest_dir, **kw) -> None: ...
    @staticmethod
    def create(prefix, file_list, out_fn, out_folder=..., **kw): ...
    @staticmethod
    def get_pkg_details(in_file): ...
