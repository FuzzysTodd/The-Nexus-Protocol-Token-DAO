from ._commit_api import CommitOperationAdd as CommitOperationAdd
from .utils import get_token_to_send as get_token_to_send, hf_raise_for_status as hf_raise_for_status, http_backoff as http_backoff, logging as logging, validate_hf_hub_args as validate_hf_hub_args
from .utils.sha import sha256 as sha256, sha_fileobj as sha_fileobj
from _typeshed import Incomplete
from contextlib import AbstractContextManager
from dataclasses import dataclass
from huggingface_hub.constants import ENDPOINT as ENDPOINT, HF_HUB_ENABLE_HF_TRANSFER as HF_HUB_ENABLE_HF_TRANSFER, REPO_TYPES_URL_PREFIXES as REPO_TYPES_URL_PREFIXES
from huggingface_hub.utils import get_session as get_session
from typing import BinaryIO, Dict, Iterable, List, Tuple, TypedDict

logger: Incomplete
OID_REGEX: Incomplete
LFS_MULTIPART_UPLOAD_COMMAND: str
LFS_HEADERS: Incomplete

@dataclass
class UploadInfo:
    """
    Dataclass holding required information to determine whether a blob
    should be uploaded to the hub using the LFS protocol or the regular protocol

    Args:
        sha256 (`bytes`):
            SHA256 hash of the blob
        size (`int`):
            Size in bytes of the blob
        sample (`bytes`):
            First 512 bytes of the blob
    """
    sha256: bytes
    size: int
    sample: bytes
    @classmethod
    def from_path(cls, path: str): ...
    @classmethod
    def from_bytes(cls, data: bytes): ...
    @classmethod
    def from_fileobj(cls, fileobj: BinaryIO): ...
    def __init__(self, sha256, size, sample) -> None: ...

def post_lfs_batch_info(upload_infos: Iterable[UploadInfo], token: str | None, repo_type: str, repo_id: str, endpoint: str | None = None) -> Tuple[List[dict], List[dict]]:
    '''
    Requests the LFS batch endpoint to retrieve upload instructions

    Learn more: https://github.com/git-lfs/git-lfs/blob/main/docs/api/batch.md

    Args:
        upload_infos (`Iterable` of `UploadInfo`):
            `UploadInfo` for the files that are being uploaded, typically obtained
            from `CommitOperationAdd.upload_info`
        repo_type (`str`):
            Type of the repo to upload to: `"model"`, `"dataset"` or `"space"`.
        repo_id (`str`):
            A namespace (user or an organization) and a repo name separated
            by a `/`.
        token (`str`, *optional*):
            An authentication token ( See https://huggingface.co/settings/tokens )

    Returns:
        `LfsBatchInfo`: 2-tuple:
            - First element is the list of upload instructions from the server
            - Second element is an list of errors, if any

    Raises:
        `ValueError`: If an argument is invalid or the server response is malformed

        `HTTPError`: If the server returned an error
    '''

class PayloadPartT(TypedDict):
    partNumber: int
    etag: str

class CompletionPayloadT(TypedDict):
    """Payload that will be sent to the Hub when uploading multi-part."""
    oid: str
    parts: List[PayloadPartT]

def lfs_upload(operation: CommitOperationAdd, lfs_batch_action: Dict, token: str | None) -> None:
    """
    Handles uploading a given object to the Hub with the LFS protocol.

    Can be a No-op if the content of the file is already present on the hub large file storage.

    Args:
        operation (`CommitOperationAdd`):
            The add operation triggering this upload.
        lfs_batch_action (`dict`):
            Upload instructions from the LFS batch endpoint for this object. See [`~utils.lfs.post_lfs_batch_info`] for
            more details.
        token (`str`, *optional*):
            A [user access token](https://hf.co/settings/tokens) to authenticate requests against the Hub

    Raises:
        - `ValueError` if `lfs_batch_action` is improperly formatted
        - `HTTPError` if the upload resulted in an error
    """

class SliceFileObj(AbstractContextManager):
    '''
    Utility context manager to read a *slice* of a seekable file-like object as a seekable, file-like object.

    This is NOT thread safe

    Inspired by stackoverflow.com/a/29838711/593036

    Credits to @julien-c

    Args:
        fileobj (`BinaryIO`):
            A file-like object to slice. MUST implement `tell()` and `seek()` (and `read()` of course).
            `fileobj` will be reset to its original position when exiting the context manager.
        seek_from (`int`):
            The start of the slice (offset from position 0 in bytes).
        read_limit (`int`):
            The maximum number of bytes to read from the slice.

    Attributes:
        previous_position (`int`):
            The previous position

    Examples:

    Reading 200 bytes with an offset of 128 bytes from a file (ie bytes 128 to 327):
    ```python
    >>> with open("path/to/file", "rb") as file:
    ...     with SliceFileObj(file, seek_from=128, read_limit=200) as fslice:
    ...         fslice.read(...)
    ```

    Reading a file in chunks of 512 bytes
    ```python
    >>> import os
    >>> chunk_size = 512
    >>> file_size = os.getsize("path/to/file")
    >>> with open("path/to/file", "rb") as file:
    ...     for chunk_idx in range(ceil(file_size / chunk_size)):
    ...         with SliceFileObj(file, seek_from=chunk_idx * chunk_size, read_limit=chunk_size) as fslice:
    ...             chunk = fslice.read(...)

    ```
    '''
    fileobj: Incomplete
    seek_from: Incomplete
    read_limit: Incomplete
    def __init__(self, fileobj: BinaryIO, seek_from: int, read_limit: int) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def read(self, n: int = -1): ...
    def tell(self) -> int: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def __iter__(self): ...
