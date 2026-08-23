from pip._internal.exceptions import NetworkConnectionError as NetworkConnectionError
from pip._vendor.requests.models import CONTENT_CHUNK_SIZE as CONTENT_CHUNK_SIZE, Response as Response
from typing import Dict, Generator

HEADERS: Dict[str, str]

def raise_for_status(resp: Response) -> None: ...
def response_chunks(response: Response, chunk_size: int = ...) -> Generator[bytes, None, None]:
    """Given a requests Response, provide the data chunks."""
