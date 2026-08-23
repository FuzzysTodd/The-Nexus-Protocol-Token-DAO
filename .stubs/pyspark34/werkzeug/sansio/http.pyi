from .. import datastructures as ds
from ..http import generate_etag as generate_etag, parse_date as parse_date, parse_etags as parse_etags, parse_if_range_header as parse_if_range_header, unquote_etag as unquote_etag
from datetime import datetime

def is_resource_modified(http_range: str | None = None, http_if_range: str | None = None, http_if_modified_since: str | None = None, http_if_none_match: str | None = None, http_if_match: str | None = None, etag: str | None = None, data: bytes | None = None, last_modified: datetime | str | None = None, ignore_if_range: bool = True) -> bool:
    """Convenience method for conditional requests.
    :param http_range: Range HTTP header
    :param http_if_range: If-Range HTTP header
    :param http_if_modified_since: If-Modified-Since HTTP header
    :param http_if_none_match: If-None-Match HTTP header
    :param http_if_match: If-Match HTTP header
    :param etag: the etag for the response for comparison.
    :param data: or alternatively the data of the response to automatically
                 generate an etag using :func:`generate_etag`.
    :param last_modified: an optional date of the last modification.
    :param ignore_if_range: If `False`, `If-Range` header will be taken into
                            account.
    :return: `True` if the resource was modified, otherwise `False`.

    .. versionadded:: 2.2
    """
def parse_cookie(cookie: str | None = None, cls: type[ds.MultiDict] | None = None) -> ds.MultiDict[str, str]:
    """Parse a cookie from a string.

    The same key can be provided multiple times, the values are stored
    in-order. The default :class:`MultiDict` will have the first value
    first, and all values can be retrieved with
    :meth:`MultiDict.getlist`.

    :param cookie: The cookie header as a string.
    :param cls: A dict-like class to store the parsed cookies in.
        Defaults to :class:`MultiDict`.

    .. versionchanged:: 3.0
        Passing bytes, and the ``charset`` and ``errors`` parameters, were removed.

    .. versionadded:: 2.2
    """
