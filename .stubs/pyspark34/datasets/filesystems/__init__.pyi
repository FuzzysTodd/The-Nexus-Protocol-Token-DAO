import fsspec
from . import compression as compression
from .s3filesystem import S3FileSystem as S3FileSystem
from typing import List

COMPRESSION_FILESYSTEMS: List[compression.BaseCompressedFileFileSystem]

def extract_path_from_uri(dataset_path: str) -> str:
    """
    Preprocesses `dataset_path` and removes remote filesystem (e.g. removing `s3://`).

    Args:
        dataset_path (`str`):
            Path (e.g. `dataset/train`) or remote uri (e.g. `s3://my-bucket/dataset/train`) of the dataset directory.
    """
def is_remote_filesystem(fs: fsspec.AbstractFileSystem) -> bool:
    """
    Validates if filesystem has remote protocol.

    Args:
        fs (`fsspec.spec.AbstractFileSystem`):
            An abstract super-class for pythonic file-systems, e.g. `fsspec.filesystem('file')` or [`datasets.filesystems.S3FileSystem`].
    """
def rename(fs: fsspec.AbstractFileSystem, src: str, dst: str):
    """
    Renames the file `src` in `fs` to `dst`.
    """
