from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['What3Words', 'What3WordsV3']

class What3Words(Geocoder):
    """What3Words geocoder using the legacy V2 API.

    Documentation at:
        https://docs.what3words.com/api/v2/

    .. attention::
        Consider using :class:`.What3WordsV3` instead.
    """
    geocode_path: str
    reverse_path: str
    api_key: Incomplete
    geocode_api: Incomplete
    reverse_api: Incomplete
    def __init__(self, api_key, *, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """

        :param str api_key: Key provided by What3Words
            (https://accounts.what3words.com/register).

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
        """
    def geocode(self, query, *, lang: str = 'en', exactly_one: bool = True, timeout=...):
        """
        Return a location point for a `3 words` query. If the `3 words` address
        doesn't exist, a :class:`geopy.exc.GeocoderQueryError` exception will be
        thrown.

        :param str query: The 3-word address you wish to geocode.

        :param str lang: two character language code as supported by
            the API (https://docs.what3words.com/api/v2/#lang).

        :param bool exactly_one: Return one result or a list of results, if
            available. Due to the address scheme there is always exactly one
            result for each `3 words` address, so this parameter is rather
            useless for this geocoder.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder's initialization.

        :rtype: :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        """
    def reverse(self, query, *, lang: str = 'en', exactly_one: bool = True, timeout=...):
        '''
        Return a `3 words` address by location point. Each point on surface has
        a `3 words` address, so there\'s always a non-empty response.

        :param query: The coordinates for which you wish to obtain the 3 word
            address.
        :type query: :class:`geopy.point.Point`, list or tuple of ``(latitude,
            longitude)``, or string as ``"%(latitude)s, %(longitude)s"``.

        :param str lang: two character language code as supported by the
            API (https://docs.what3words.com/api/v2/#lang).

        :param bool exactly_one: Return one result or a list of results, if
            available. Due to the address scheme there is always exactly one
            result for each `3 words` address, so this parameter is rather
            useless for this geocoder.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :rtype: :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.

        '''

class What3WordsV3(Geocoder):
    """What3Words geocoder using the V3 API.

    Documentation at:
        https://developer.what3words.com/public-api/docs

    .. versionadded:: 2.2
    """
    geocode_path: str
    reverse_path: str
    api_key: Incomplete
    geocode_api: Incomplete
    reverse_api: Incomplete
    def __init__(self, api_key, *, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """

        :param str api_key: Key provided by What3Words
            (https://accounts.what3words.com/register).

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
        """
    def geocode(self, query, *, exactly_one: bool = True, timeout=...):
        """
        Return a location point for a `3 words` query. If the `3 words` address
        doesn't exist, a :class:`geopy.exc.GeocoderQueryError` exception will be
        thrown.

        :param str query: The 3-word address you wish to geocode.

        :param bool exactly_one: Return one result or a list of results, if
            available. Due to the address scheme there is always exactly one
            result for each `3 words` address, so this parameter is rather
            useless for this geocoder.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder's initialization.

        :rtype: :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        """
    def reverse(self, query, *, lang: str = 'en', exactly_one: bool = True, timeout=...):
        '''
        Return a `3 words` address by location point. Each point on surface has
        a `3 words` address, so there\'s always a non-empty response.

        :param query: The coordinates for which you wish to obtain the 3 word
            address.
        :type query: :class:`geopy.point.Point`, list or tuple of ``(latitude,
            longitude)``, or string as ``"%(latitude)s, %(longitude)s"``.

        :param str lang: two character language code as supported by the
            API (https://developer.what3words.com/public-api/docs#available-languages).

        :param bool exactly_one: Return one result or a list of results, if
            available. Due to the address scheme there is always exactly one
            result for each `3 words` address, so this parameter is rather
            useless for this geocoder.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :rtype: :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.

        '''
