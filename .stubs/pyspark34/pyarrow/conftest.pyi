from _typeshed import Incomplete
from collections.abc import Generator
from pyarrow import Codec as Codec, fs as fs
from pyarrow.fs import GcsFileSystem as GcsFileSystem, HadoopFileSystem as HadoopFileSystem, S3FileSystem as S3FileSystem

groups: Incomplete
defaults: Incomplete

def pytest_ignore_collect(path, config): ...
def add_fs(doctest_namespace, request, tmp_path) -> Generator[None, None, None]: ...
def unary_func_fixture():
    """
    Register a unary scalar function.
    """
