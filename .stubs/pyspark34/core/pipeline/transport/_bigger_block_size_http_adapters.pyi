from _typeshed import Incomplete
from requests.adapters import HTTPAdapter

class BiggerBlockSizeHTTPAdapter(HTTPAdapter):
    def get_connection(self, url, proxies: Incomplete | None = None):
        """Returns a urllib3 connection for the given URL. This should not be
        called from user code, and is only exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param str url: The URL to connect to.
        :param dict proxies: (optional) A Requests-style dictionary of proxies used on this request.
        :rtype: urllib3.ConnectionPool
        :returns: The urllib3 ConnectionPool for the given URL.
        """
