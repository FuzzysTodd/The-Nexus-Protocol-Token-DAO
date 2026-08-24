from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['TomTom']

class TomTom(Geocoder):
    """TomTom geocoder.

    Documentation at:
        https://developer.tomtom.com/search-api/search-api-documentation
    """
    geocode_path: str
    reverse_path: str
    api_key: Incomplete
    api: Incomplete
    api_reverse: Incomplete
    def __init__(self, api_key, *, scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None, domain: str = 'api.tomtom.com') -> None:
        """
        :param str api_key: TomTom API key.

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

        :param str domain: Domain where the target TomTom service
            is hosted.
        """
    def geocode(self, query, *, exactly_one: bool = True, timeout=..., limit: Incomplete | None = None, typeahead: bool = False, language: Incomplete | None = None):
        '''
        Return a location point by address.

        :param str query: The address or query you wish to geocode.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :param int limit: Maximum amount of results to return from the service.
            Unless exactly_one is set to False, limit will always be 1.

        :param bool typeahead: If the "typeahead" flag is set, the query
            will be interpreted as a partial input and the search will
            enter predictive mode.

        :param str language: Language in which search results should be
            returned. When data in specified language is not
            available for a specific field, default language is used.
            List of supported languages (case-insensitive):
            https://developer.tomtom.com/online-search/online-search-documentation/supported-languages

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
    def reverse(self, query, *, exactly_one: bool = True, timeout=..., language: Incomplete | None = None):
        '''
        Return an address by location point.

        :param query: The coordinates for which you wish to obtain the
            closest human-readable addresses.
        :type query: :class:`geopy.point.Point`, list or tuple of ``(latitude,
            longitude)``, or string as ``"%(latitude)s, %(longitude)s"``.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :param str language: Language in which search results should be
            returned. When data in specified language is not
            available for a specific field, default language is used.
            List of supported languages (case-insensitive):
            https://developer.tomtom.com/online-search/online-search-documentation/supported-languages

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
