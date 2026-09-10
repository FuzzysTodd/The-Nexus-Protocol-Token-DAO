from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['Here', 'HereV7']

class Here(Geocoder):
    """Geocoder using the HERE Geocoder API.

    Documentation at:
        https://developer.here.com/documentation/geocoder/

    .. attention::
        This class uses a v6 API which is in maintenance mode.
        Consider using the newer :class:`.HereV7` class.
    """
    structured_query_params: Incomplete
    geocode_path: str
    reverse_path: str
    app_id: Incomplete
    app_code: Incomplete
    apikey: Incomplete
    api: Incomplete
    reverse_api: Incomplete
    def __init__(self, *, app_id: Incomplete | None = None, app_code: Incomplete | None = None, apikey: Incomplete | None = None, scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """

        :param str app_id: Should be a valid HERE Maps APP ID. Will eventually
            be replaced with APIKEY.
            See https://developer.here.com/authenticationpage.

            .. attention::
                App ID and App Code are being replaced by API Keys and OAuth 2.0
                by HERE. Consider getting an ``apikey`` instead of using
                ``app_id`` and ``app_code``.

        :param str app_code: Should be a valid HERE Maps APP CODE. Will
            eventually be replaced with APIKEY.
            See https://developer.here.com/authenticationpage.

            .. attention::
                App ID and App Code are being replaced by API Keys and OAuth 2.0
                by HERE. Consider getting an ``apikey`` instead of using
                ``app_id`` and ``app_code``.

        :param str apikey: Should be a valid HERE Maps APIKEY. These keys were
            introduced in December 2019 and will eventually replace the legacy
            APP CODE/APP ID pairs which are already no longer available for new
            accounts (but still work for old accounts).
            More authentication details are available at
            https://developer.here.com/blog/announcing-two-new-authentication-types.
            See https://developer.here.com/authenticationpage.

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
        """
    def geocode(self, query, *, bbox: Incomplete | None = None, mapview: Incomplete | None = None, exactly_one: bool = True, maxresults: Incomplete | None = None, pageinformation: Incomplete | None = None, language: Incomplete | None = None, additional_data: bool = False, timeout=...):
        '''
        Return a location point by address.

        This implementation supports only a subset of all available parameters.
        A list of all parameters of the pure REST API is available here:
        https://developer.here.com/documentation/geocoder/topics/resource-geocode.html

        :param query: The address or query you wish to geocode.

            For a structured query, provide a dictionary whose keys
            are one of: `city`, `county`, `district`, `country`, `state`,
            `street`, `housenumber`, or `postalcode`.
        :type query: str or dict

        :param bbox: A type of spatial filter, limits the search for any other attributes
            in the request. Specified by two coordinate (lat/lon)
            pairs -- corners of the box. `The bbox search is currently similar
            to mapview but it is not extended` (cited from the REST API docs).
            Relevant global results are also returned.
            Example: ``[Point(22, 180), Point(-22, -180)]``.
        :type bbox: list or tuple of 2 items of :class:`geopy.point.Point` or
            ``(latitude, longitude)`` or ``"%(latitude)s, %(longitude)s"``.

        :param mapview: The app\'s viewport, given as two coordinate pairs, specified
            by two lat/lon pairs -- corners of the bounding box,
            respectively. Matches from within the set map view plus an extended area
            are ranked highest. Relevant global results are also returned.
            Example: ``[Point(22, 180), Point(-22, -180)]``.
        :type mapview: list or tuple of 2 items of :class:`geopy.point.Point` or
            ``(latitude, longitude)`` or ``"%(latitude)s, %(longitude)s"``.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int maxresults: Defines the maximum number of items in the
            response structure. If not provided and there are multiple results
            the HERE API will return 10 results by default. This will be reset
            to one if ``exactly_one`` is True.

        :param int pageinformation: A key which identifies the page to be returned
            when the response is separated into multiple pages. Only useful when
            ``maxresults`` is also provided.

        :param str language: Affects the language of the response,
            must be a RFC 4647 language code, e.g. \'en-US\'.

        :param str additional_data: A string with key-value pairs as described on
            https://developer.here.com/documentation/geocoder/topics/resource-params-additional.html.
            These will be added as one query parameter to the URL.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
    def reverse(self, query, *, radius: Incomplete | None = None, exactly_one: bool = True, maxresults: Incomplete | None = None, pageinformation: Incomplete | None = None, language: Incomplete | None = None, mode: str = 'retrieveAddresses', timeout=...):
        '''
        Return an address by location point.

        This implementation supports only a subset of all available parameters.
        A list of all parameters of the pure REST API is available here:
        https://developer.here.com/documentation/geocoder/topics/resource-reverse-geocode.html

        :param query: The coordinates for which you wish to obtain the
            closest human-readable addresses.
        :type query: :class:`geopy.point.Point`, list or tuple of ``(latitude,
            longitude)``, or string as ``"%(latitude)s, %(longitude)s"``.

        :param float radius: Proximity radius in meters.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int maxresults: Defines the maximum number of items in the
            response structure. If not provided and there are multiple results
            the HERE API will return 10 results by default. This will be reset
            to one if ``exactly_one`` is True.

        :param int pageinformation: A key which identifies the page to be returned
            when the response is separated into multiple pages. Only useful when
            ``maxresults`` is also provided.

        :param str language: Affects the language of the response,
            must be a RFC 4647 language code, e.g. \'en-US\'.

        :param str mode: Affects the type of returned response items, must be
            one of: \'retrieveAddresses\' (default), \'retrieveAreas\', \'retrieveLandmarks\',
            \'retrieveAll\', or \'trackPosition\'. See online documentation for more
            information.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''

class HereV7(Geocoder):
    """Geocoder using the HERE Geocoding & Search v7 API.

    Documentation at:
        https://developer.here.com/documentation/geocoding-search-api/

    Terms of Service at:
        https://legal.here.com/en-gb/terms

    .. versionadded:: 2.2
    """
    structured_query_params: Incomplete
    geocode_path: str
    reverse_path: str
    apikey: Incomplete
    api: Incomplete
    reverse_api: Incomplete
    def __init__(self, apikey, *, scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """

        :param str apikey: Should be a valid HERE Maps apikey.
            A project can be created at
            https://developer.here.com/projects.

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
        """
    def geocode(self, query: Incomplete | None = None, *, components: Incomplete | None = None, at: Incomplete | None = None, countries: Incomplete | None = None, language: Incomplete | None = None, limit: Incomplete | None = None, exactly_one: bool = True, timeout=...):
        '''
        Return a location point by address.

        :param str query: The address or query you wish to geocode. Optional,
            if ``components`` param is set.

        :param dict components: A structured query. Can be used along with
            the free-text ``query``. Should be a dictionary whose keys
            are one of:
            `country`, `state`, `county`, `city`, `district`, `street`,
            `houseNumber`, `postalCode`.

        :param at: The center of the search context.
        :type at: :class:`geopy.point.Point`, list or tuple of ``(latitude,
            longitude)``, or string as ``"%(latitude)s, %(longitude)s"``.

        :param list countries: A list of country codes specified in
            `ISO 3166-1 alpha-3 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`_
            format, e.g. ``[\'USA\', \'CAN\']``.
            This is a hard filter.

        :param str language: Affects the language of the response,
            must be a BCP 47 compliant language code, e.g. ``en-US``.

        :param int limit: Defines the maximum number of items in the
            response structure. If not provided and there are multiple results
            the HERE API will return 20 results by default. This will be reset
            to one if ``exactly_one`` is True.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
    def reverse(self, query, *, language: Incomplete | None = None, limit: Incomplete | None = None, exactly_one: bool = True, timeout=...):
        '''
        Return an address by location point.

        :param query: The coordinates for which you wish to obtain the
            closest human-readable addresses.
        :type query: :class:`geopy.point.Point`, list or tuple of ``(latitude,
            longitude)``, or string as ``"%(latitude)s, %(longitude)s"``.

        :param str language: Affects the language of the response,
            must be a BCP 47 compliant language code, e.g. ``en-US``.

        :param int limit: Maximum number of results to be returned.
            This will be reset to one if ``exactly_one`` is True.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
