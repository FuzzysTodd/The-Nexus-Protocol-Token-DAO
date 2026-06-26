import zstandard
from .package_streaming import CondaComponent as CondaComponent, stream_conda_component as stream_conda_component
from pathlib import Path
from typing import Callable

ZSTD_COMPRESS_LEVEL: int
ZSTD_COMPRESS_THREADS: int
CONDA_PACKAGE_FORMAT_VERSION: int

def transmute(package, path, *, compressor: Callable[[], zstandard.ZstdCompressor] = ..., is_info: Callable[[str], bool] = ...) -> Path:
    """
    Convert .tar.bz2 conda :package to .conda-format under path.

    :param package: path to .tar.bz2 conda package
    :param path: destination path for transmuted .conda package
    :param compressor: A function that creates instances of
        ``zstandard.ZstdCompressor()`` to override defaults.
    :param is_info: A function that returns True if a file belongs in the
        ``info`` component of a `.conda` package.  ``conda-package-handling``
        (not this package ``conda-package-streaming``) uses a set of regular
        expressions to keep expected items in the info- component, while other
        items starting with ``info/`` wind up in the pkg- component.

    :return: Path to transmuted package.
    """
def transmute_tar_bz2(package: str, path) -> Path:
    """
    Convert .conda :package to .tar.bz2 format under path.

    Can recompress .tar.bz2 packages.

    :param package: path to `.conda` or `.tar.bz2` package.
    :param path: destination path for transmuted package.

    :return: Path to transmuted package.
    """
