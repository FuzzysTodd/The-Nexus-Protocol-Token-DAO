from _typeshed import Incomplete
from collections.abc import Callable as Callable
from urllib.parse import quote as quote, unquote as unquote, urlparse as urlparse, urlunparse as urlunparse

RECODE_HOSTNAME_FOR: Incomplete

def normalizeLink(url: str) -> str:
    """Normalize destination URLs in links

    ::

        [label]:   destination   'title'
                ^^^^^^^^^^^
    """
def normalizeLinkText(url: str) -> str:
    """Normalize autolink content

    ::

        <destination>
         ~~~~~~~~~~~
    """

BAD_PROTO_RE: Incomplete
GOOD_DATA_RE: Incomplete

def validateLink(url: str, validator: Callable[[str], bool] | None = None) -> bool:
    """Validate URL link is allowed in output.

    This validator can prohibit more than really needed to prevent XSS.
    It's a tradeoff to keep code simple and to be secure by default.

    Note: url should be normalized at this point, and existing entities decoded.
    """
