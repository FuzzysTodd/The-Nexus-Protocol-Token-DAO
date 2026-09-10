from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['Baidu', 'BaiduV3']

class Baidu(Geocoder):
    """Geocoder using the Baidu Maps v2 API.

    Documentation at:
        http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding

    .. attention::
        Newly registered API keys will not work with v2 API,
        use :class:`.BaiduV3` instead.
    """
    api_path: str
    reverse_path: str
    api_key: Incomplete
    api: Incomplete
    reverse_api: Incomplete
    security_key: Incomplete
    def __init__(self, api_key, *, scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None, security_key: Incomplete | None = None) -> None:
        """

        :param str api_key: The API key (AK) required by Baidu Map to perform
            geocoding requests. API keys are managed through the Baidu APIs
            console (http://lbsyun.baidu.com/apiconsole/key).

        :param str scheme:
            See :attr:`geopy.geocoders.options.default_scheme`.

        :param int timeout:
            See :attr:`geopy.geocoders.options.default_timeout`.

        :param dict proxies:
            See :attr:`geopy.geocoders.options.default_proxies`.

        :param str user_agent:
            See :attr:`geopy.geocoders.options.default_user_agent`.

        :type ssl_context: :class:`ssl.SSLContext`
        :param ssl_context:
            See :attr:`geopy.geocoders.options.default_ssl_context`.

        :param callable adapter_factory:
            See :attr:`geopy.geocoders.options.default_adapter_factory`.

            .. versionadded:: 2.0

        :param str security_key: The security key (SK) to calculate
            the SN parameter in request if authentication setting requires
            (http://lbsyun.baidu.com/index.php?title=lbscloud/api/appendix).
        """
    def geocode(self, query, *, exactly_one: bool = True, timeout=...):
        """
        Return a location point by address.

        :param str query: The address or query you wish to geocode.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder's initialization.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.

        """
    def reverse(self, query, *, exactly_one: bool = True, timeout=...):
        '''
        Return an address by location point.

        :param query: The coordinates for which you wish to obtain the
            closest human-readable addresses.
        :type query: :class:`geopy.point.Point`, list or tuple of ``(latitude,
            longitude)``, or string as ``"%(latitude)s, %(longitude)s"``.

        :param bool exactly_one: Return one result or a list of results, if
            available. Baidu\'s API will always return at most one result.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.

        '''

class BaiduV3(Baidu):
    """Geocoder using the Baidu Maps v3 API.

    Documentation at:
        http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding
    """
    api_path: str
    reverse_path: str
