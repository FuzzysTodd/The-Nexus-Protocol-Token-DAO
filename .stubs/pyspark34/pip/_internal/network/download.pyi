from _typeshed import Incomplete
from pip._internal.cli.progress_bars import get_download_progress_renderer as get_download_progress_renderer
from pip._internal.exceptions import NetworkConnectionError as NetworkConnectionError
from pip._internal.models.index import PyPI as PyPI
from pip._internal.models.link import Link as Link
from pip._internal.network.cache import is_from_cache as is_from_cache
from pip._internal.network.session import PipSession as PipSession
from pip._internal.network.utils import HEADERS as HEADERS, raise_for_status as raise_for_status, response_chunks as response_chunks
from pip._internal.utils.misc import format_size as format_size, redact_auth_from_url as redact_auth_from_url, splitext as splitext
from pip._vendor.requests.models import CONTENT_CHUNK_SIZE as CONTENT_CHUNK_SIZE, Response as Response
from typing import Iterable, Tuple

logger: Incomplete

def sanitize_content_filename(filename: str) -> str:
    '''
    Sanitize the "filename" value from a Content-Disposition header.
    '''
def parse_content_disposition(content_disposition: str, default_filename: str) -> str:
    '''
    Parse the "filename" value from a Content-Disposition header, and
    return the default filename if the result is empty.
    '''

class Downloader:
    def __init__(self, session: PipSession, progress_bar: str) -> None: ...
    def __call__(self, link: Link, location: str) -> Tuple[str, str]:
        """Download the file given by link into location."""

class BatchDownloader:
    def __init__(self, session: PipSession, progress_bar: str) -> None: ...
    def __call__(self, links: Iterable[Link], location: str) -> Iterable[Tuple[Link, Tuple[str, str]]]:
        """Download the files given by links into location."""
