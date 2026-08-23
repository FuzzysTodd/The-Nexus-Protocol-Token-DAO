from .constants import ENDPOINT as ENDPOINT, HF_HUB_ENABLE_HF_TRANSFER as HF_HUB_ENABLE_HF_TRANSFER
from .hf_api import RepoFile as RepoFile
from .lfs import UploadInfo as UploadInfo, lfs_upload as lfs_upload, post_lfs_batch_info as post_lfs_batch_info
from .utils import EntryNotFoundError as EntryNotFoundError, build_hf_headers as build_hf_headers, chunk_iterable as chunk_iterable, hf_raise_for_status as hf_raise_for_status, logging as logging, tqdm_stream_file as tqdm_stream_file, validate_hf_hub_args as validate_hf_hub_args
from _typeshed import Incomplete
from dataclasses import dataclass
from huggingface_hub import get_session as get_session
from pathlib import Path
from typing import BinaryIO, Iterator, Literal

logger: Incomplete
UploadMode: Incomplete
FETCH_LFS_BATCH_SIZE: int

@dataclass
class CommitOperationDelete:
    '''
    Data structure holding necessary info to delete a file or a folder from a repository
    on the Hub.

    Args:
        path_in_repo (`str`):
            Relative filepath in the repo, for example: `"checkpoints/1fec34a/weights.bin"`
            for a file or `"checkpoints/1fec34a/"` for a folder.
        is_folder (`bool` or `Literal["auto"]`, *optional*)
            Whether the Delete Operation applies to a folder or not. If "auto", the path
            type (file or folder) is guessed automatically by looking if path ends with
            a "/" (folder) or not (file). To explicitly set the path type, you can set
            `is_folder=True` or `is_folder=False`.
    '''
    path_in_repo: str
    is_folder: bool | Literal['auto'] = ...
    def __post_init__(self) -> None: ...
    def __init__(self, path_in_repo, is_folder) -> None: ...

@dataclass
class CommitOperationCopy:
    '''
    Data structure holding necessary info to copy a file in a repository on the Hub.

    Limitations:
      - Only LFS files can be copied. To copy a regular file, you need to download it locally and re-upload it
      - Cross-repository copies are not supported.

    Note: you can combine a [`CommitOperationCopy`] and a [`CommitOperationDelete`] to rename an LFS file on the Hub.

    Args:
        src_path_in_repo (`str`):
            Relative filepath in the repo of the file to be copied, e.g. `"checkpoints/1fec34a/weights.bin"`.
        path_in_repo (`str`):
            Relative filepath in the repo where to copy the file, e.g. `"checkpoints/1fec34a/weights_copy.bin"`.
        src_revision (`str`, *optional*):
            The git revision of the file to be copied. Can be any valid git revision.
            Default to the target commit revision.
    '''
    src_path_in_repo: str
    path_in_repo: str
    src_revision: str | None = ...
    def __post_init__(self) -> None: ...
    def __init__(self, src_path_in_repo, path_in_repo, src_revision) -> None: ...

@dataclass
class CommitOperationAdd:
    '''
    Data structure holding necessary info to upload a file to a repository on the Hub.

    Args:
        path_in_repo (`str`):
            Relative filepath in the repo, for example: `"checkpoints/1fec34a/weights.bin"`
        path_or_fileobj (`str`, `Path`, `bytes`, or `BinaryIO`):
            Either:
            - a path to a local file (as `str` or `pathlib.Path`) to upload
            - a buffer of bytes (`bytes`) holding the content of the file to upload
            - a "file object" (subclass of `io.BufferedIOBase`), typically obtained
                with `open(path, "rb")`. It must support `seek()` and `tell()` methods.

    Raises:
        [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
            If `path_or_fileobj` is not one of `str`, `Path`, `bytes` or `io.BufferedIOBase`.
        [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
            If `path_or_fileobj` is a `str` or `Path` but not a path to an existing file.
        [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
            If `path_or_fileobj` is a `io.BufferedIOBase` but it doesn\'t support both
            `seek()` and `tell()`.
    '''
    path_in_repo: str
    path_or_fileobj: str | Path | bytes | BinaryIO
    upload_info: UploadInfo = ...
    def __post_init__(self) -> None:
        """Validates `path_or_fileobj` and compute `upload_info`."""
    def as_file(self, with_tqdm: bool = False) -> Iterator[BinaryIO]:
        '''
        A context manager that yields a file-like object allowing to read the underlying
        data behind `path_or_fileobj`.

        Args:
            with_tqdm (`bool`, *optional*, defaults to `False`):
                If True, iterating over the file object will display a progress bar. Only
                works if the file-like object is a path to a file. Pure bytes and buffers
                are not supported.

        Example:

        ```python
        >>> operation = CommitOperationAdd(
        ...        path_in_repo="remote/dir/weights.h5",
        ...        path_or_fileobj="./local/weights.h5",
        ... )
        CommitOperationAdd(path_in_repo=\'remote/dir/weights.h5\', path_or_fileobj=\'./local/weights.h5\')

        >>> with operation.as_file() as file:
        ...     content = file.read()

        >>> with operation.as_file(with_tqdm=True) as file:
        ...     while True:
        ...         data = file.read(1024)
        ...         if not data:
        ...              break
        config.json: 100%|█████████████████████████| 8.19k/8.19k [00:02<00:00, 3.72kB/s]

        >>> with operation.as_file(with_tqdm=True) as file:
        ...     requests.put(..., data=file)
        config.json: 100%|█████████████████████████| 8.19k/8.19k [00:02<00:00, 3.72kB/s]
        ```
        '''
    def b64content(self) -> bytes:
        """
        The base64-encoded content of `path_or_fileobj`

        Returns: `bytes`
        """
    def __init__(self, path_in_repo, path_or_fileobj) -> None: ...
CommitOperation = CommitOperationAdd | CommitOperationCopy | CommitOperationDelete
