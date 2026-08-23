from _typeshed import Incomplete

class HttpClient:
    """This describes a minimal http request interface used by this package."""
    def post(self, url, params: Incomplete | None = None, data: Incomplete | None = None, headers: Incomplete | None = None, **kwargs):
        """HTTP post.

        :param dict params: A dict to be url-encoded and sent as query-string.
        :param dict headers: A dict representing headers to be sent via request.
        :param data:
            Implementation needs to support 2 types.

            * A dict, which will need to be urlencode() before being sent.
            * (Recommended) A string, which will be sent in request as-is.

        It returns an :class:`~Response`-like object.

        Note: In its async counterpart, this method would be defined as async.
        """
    def get(self, url, params: Incomplete | None = None, headers: Incomplete | None = None, **kwargs):
        """HTTP get.

        :param dict params: A dict to be url-encoded and sent as query-string.
        :param dict headers: A dict representing headers to be sent via request.

        It returns an :class:`~Response`-like object.

        Note: In its async counterpart, this method would be defined as async.
        """

class Response:
    '''This describes a minimal http response interface used by this package.

    :var int status_code:
        The status code of this http response.

        Our async code path would also accept an alias as "status".

    :var string text:
        The body of this http response.

        Our async code path would also accept an awaitable with the same name.
    '''
    status_code: int
    text: str
    headers: Incomplete
    def raise_for_status(self) -> None:
        """Raise an exception when http response status contains error"""
