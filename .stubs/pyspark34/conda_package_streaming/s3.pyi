from _typeshed import Incomplete
from collections.abc import Generator
from mypy_boto3_s3 import Client
from mypy_boto3_s3.type_defs import GetObjectOutputTypeDef

__all__ = ['stream_conda_info', 'conda_reader_for_s3']

class ResponseFacade:
    response: Incomplete
    raw: Incomplete
    def __init__(self, response: GetObjectOutputTypeDef) -> None: ...
    def raise_for_status(self) -> None: ...
    @property
    def status_code(self): ...
    @property
    def headers(self): ...
    def iter_content(self, n: int): ...

class SessionFacade:
    """
    Make s3 client look just enough like a requests.session for LazyZipOverHTTP
    """
    client: Incomplete
    bucket: Incomplete
    key: Incomplete
    def __init__(self, client: Client, bucket: str, key: str) -> None: ...
    def get(self, url, *, headers: dict | None = None, stream: bool = True): ...

def stream_conda_info(client, bucket, key) -> Generator[Incomplete, Incomplete, None]:
    '''
    Yield (tar, member) for conda package.

    Just "info/" for .conda, all members for tar.
    '''
def conda_reader_for_s3(client: Client, bucket: str, key: str):
    """
    Return (name, file_like) suitable for package_streaming APIs
    """
