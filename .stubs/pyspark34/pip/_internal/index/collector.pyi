from .sources import CandidatesFromPage as CandidatesFromPage, LinkSource as LinkSource, build_source as build_source
from _typeshed import Incomplete
from html.parser import HTMLParser
from optparse import Values
from pip._internal.exceptions import NetworkConnectionError as NetworkConnectionError
from pip._internal.models.link import Link as Link
from pip._internal.models.search_scope import SearchScope as SearchScope
from pip._internal.network.session import PipSession as PipSession
from pip._internal.network.utils import raise_for_status as raise_for_status
from pip._internal.utils.filetypes import is_archive_file as is_archive_file
from pip._internal.utils.misc import redact_auth_from_url as redact_auth_from_url
from pip._internal.vcs import vcs as vcs
from pip._vendor import requests as requests
from pip._vendor.requests import Response as Response
from pip._vendor.requests.exceptions import RetryError as RetryError, SSLError as SSLError
from typing import Iterable, List, MutableMapping, NamedTuple, Protocol, Sequence, Tuple

logger: Incomplete
ResponseHeaders = MutableMapping[str, str]

class _NotAPIContent(Exception):
    content_type: Incomplete
    request_desc: Incomplete
    def __init__(self, content_type: str, request_desc: str) -> None: ...

class _NotHTTP(Exception): ...

class CacheablePageContent:
    page: Incomplete
    def __init__(self, page: IndexContent) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class ParseLinks(Protocol):
    def __call__(self, page: IndexContent) -> Iterable[Link]: ...

def with_cached_index_content(fn: ParseLinks) -> ParseLinks:
    """
    Given a function that parses an Iterable[Link] from an IndexContent, cache the
    function's result (keyed by CacheablePageContent), unless the IndexContent
    `page` has `page.cache_link_parsing == False`.
    """
def parse_links(page: IndexContent) -> Iterable[Link]:
    """
    Parse a Simple API's Index Content, and yield its anchor elements as Link objects.
    """

class IndexContent:
    """Represents one response (or page), along with its URL"""
    content: Incomplete
    content_type: Incomplete
    encoding: Incomplete
    url: Incomplete
    cache_link_parsing: Incomplete
    def __init__(self, content: bytes, content_type: str, encoding: str | None, url: str, cache_link_parsing: bool = True) -> None:
        """
        :param encoding: the encoding to decode the given content.
        :param url: the URL from which the HTML was downloaded.
        :param cache_link_parsing: whether links parsed from this page's url
                                   should be cached. PyPI index urls should
                                   have this set to False, for example.
        """

class HTMLLinkParser(HTMLParser):
    """
    HTMLParser that keeps the first base HREF and a list of all anchor
    elements' attributes.
    """
    url: Incomplete
    base_url: Incomplete
    anchors: Incomplete
    def __init__(self, url: str) -> None: ...
    def handle_starttag(self, tag: str, attrs: List[Tuple[str, str | None]]) -> None: ...
    def get_href(self, attrs: List[Tuple[str, str | None]]) -> str | None: ...

class CollectedSources(NamedTuple):
    find_links: Sequence[LinkSource | None]
    index_urls: Sequence[LinkSource | None]

class LinkCollector:
    """
    Responsible for collecting Link objects from all configured locations,
    making network requests as needed.

    The class's main method is its collect_sources() method.
    """
    search_scope: Incomplete
    session: Incomplete
    def __init__(self, session: PipSession, search_scope: SearchScope) -> None: ...
    @classmethod
    def create(cls, session: PipSession, options: Values, suppress_no_index: bool = False) -> LinkCollector:
        """
        :param session: The Session to use to make requests.
        :param suppress_no_index: Whether to ignore the --no-index option
            when constructing the SearchScope object.
        """
    @property
    def find_links(self) -> List[str]: ...
    def fetch_response(self, location: Link) -> IndexContent | None:
        """
        Fetch an HTML page containing package links.
        """
    def collect_sources(self, project_name: str, candidates_from_page: CandidatesFromPage) -> CollectedSources: ...
