from ..exceptions import UnrewindableBodyError as UnrewindableBodyError
from _typeshed import Incomplete

SKIP_HEADER: str
SKIPPABLE_HEADERS: Incomplete
ACCEPT_ENCODING: str

def make_headers(keep_alive: Incomplete | None = None, accept_encoding: Incomplete | None = None, user_agent: Incomplete | None = None, basic_auth: Incomplete | None = None, proxy_basic_auth: Incomplete | None = None, disable_cache: Incomplete | None = None):
    '''
    Shortcuts for generating request headers.

    :param keep_alive:
        If ``True``, adds \'connection: keep-alive\' header.

    :param accept_encoding:
        Can be a boolean, list, or string.
        ``True`` translates to \'gzip,deflate\'.
        List will get joined by comma.
        String will be used as provided.

    :param user_agent:
        String representing the user-agent you want, such as
        "python-urllib3/0.6"

    :param basic_auth:
        Colon-separated username:password string for \'authorization: basic ...\'
        auth header.

    :param proxy_basic_auth:
        Colon-separated username:password string for \'proxy-authorization: basic ...\'
        auth header.

    :param disable_cache:
        If ``True``, adds \'cache-control: no-cache\' header.

    Example::

        >>> make_headers(keep_alive=True, user_agent="Batman/1.0")
        {\'connection\': \'keep-alive\', \'user-agent\': \'Batman/1.0\'}
        >>> make_headers(accept_encoding=True)
        {\'accept-encoding\': \'gzip,deflate\'}
    '''
def set_file_position(body, pos):
    """
    If a position is provided, move file to that point.
    Otherwise, we'll attempt to record a position for future use.
    """
def rewind_body(body, body_pos) -> None:
    """
    Attempt to rewind body to a certain position.
    Primarily used for request redirects and retries.

    :param body:
        File-like object that supports seek.

    :param int pos:
        Position to seek to in file.
    """
