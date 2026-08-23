from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['MapBox']

class MapBox(Geocoder):
    """Geocoder using the Mapbox API.

    Documentation at:
        https://www.mapbox.com/api-documentation/
    """
    api_path: str
    api_key: Incomplete
    domain: Incomplete
    api: Incomplete
    def __init__(self, api_key, *, scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None, domain: str = 'api.mapbox.com', referer: Incomplete | None = None) -> None:
        """
        :param str api_key: The API key required by Mapbox to perform
            geocoding requests. API keys are managed through Mapox's account
            page (https://www.mapbox.com/account/access-tokens).

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

        :param str domain: base api domain for mapbox

        :param str referer: The URL used to satisfy the URL restriction of
            mapbox tokens.

            .. versionadded:: 2.3
        """
    def geocode(self, query, *, exactly_one: bool = True, timeout=..., proximity: Incomplete | None = None, country: Incomplete | None = None, language: Incomplete | None = None, bbox: Incomplete | None = None):
        '''
        Return a location point by address.

        :param str query: The address or query you wish to geocode.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :param proximity: A coordinate to bias local results based on a provided
            location.
        :type proximity: :class:`geopy.point.Point`, list or tuple of ``(latitude,
            longitude)``, or string as ``"%(latitude)s, %(longitude)s"``.

        :param country: Country to filter result in form of
            ISO 3166-1 alpha-2 country code (e.g. ``FR``).
            Might be a Python list of strings.

        :type country: str or list

        :param str language: This parameter controls the language of the text supplied in
            responses, and also affects result scoring, with results matching the user’s
            query in the requested language being preferred over results that match in
            another language. You can pass two letters country codes (ISO 639-1).

            .. versionadded:: 2.3

        :param bbox: The bounding box of the viewport within which
            to bias geocode results more prominently.
            Example: ``[Point(22, 180), Point(-22, -180)]``.
        :type bbox: list or tuple of 2 items of :class:`geopy.point.Point` or
            ``(latitude, longitude)`` or ``"%(latitude)s, %(longitude)s"``.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
    def reverse(self, query, *, exactly_one: bool = True, timeout=...):
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

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
