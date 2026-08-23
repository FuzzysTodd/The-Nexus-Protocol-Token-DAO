from _typeshed import Incomplete
from pip._internal.models.index import PyPI as PyPI
from pip._internal.utils.compat import has_tls as has_tls
from pip._internal.utils.misc import normalize_path as normalize_path, redact_auth_from_url as redact_auth_from_url
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name
from typing import List

logger: Incomplete

class SearchScope:
    """
    Encapsulates the locations that pip is configured to search.
    """
    @classmethod
    def create(cls, find_links: List[str], index_urls: List[str], no_index: bool) -> SearchScope:
        """
        Create a SearchScope object after normalizing the `find_links`.
        """
    find_links: Incomplete
    index_urls: Incomplete
    no_index: Incomplete
    def __init__(self, find_links: List[str], index_urls: List[str], no_index: bool) -> None: ...
    def get_formatted_locations(self) -> str: ...
    def get_index_urls_locations(self, project_name: str) -> List[str]:
        """Returns the locations found via self.index_urls

        Checks the url_name on the main (first in the list) index and
        use this url_name to produce all locations
        """
