from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['MapQuest']

class MapQuest(Geocoder):
    """Geocoder using the MapQuest API based on Licensed data.

    Documentation at:
        https://developer.mapquest.com/documentation/geocoding-api/

    MapQuest provides two Geocoding APIs:

    - :class:`geopy.geocoders.OpenMapQuest` Nominatim-alike API
      which is based on Open data from OpenStreetMap.
    - :class:`geopy.geocoders.MapQuest` (this class) MapQuest's own API
      which is based on Licensed data.
    """
    geocode_path: str
    reverse_path: str
    api_key: Incomplete
    domain: Incomplete
    geocode_api: Incomplete
    reverse_api: Incomplete
    def __init__(self, api_key, *, scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None, domain: str = 'www.mapquestapi.com') -> None:
        '''
        :param str api_key: The API key required by Mapquest to perform
            geocoding requests. API keys are managed through MapQuest\'s "Manage Keys"
            page (https://developer.mapquest.com/user/me/apps).

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

        :param str domain: base api domain for mapquest
        '''
    def geocode(self, query, *, exactly_one: bool = True, timeout=..., limit: Incomplete | None = None, bounds: Incomplete | None = None):
        '''
        Return a location point by address.

        :param str query: The address or query you wish to geocode.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :param int limit: Limit the maximum number of items in the
            response. This will be reset to one if ``exactly_one`` is True.

        :param bounds: The bounding box of the viewport within which
            to bias geocode results more prominently.
            Example: ``[Point(22, 180), Point(-22, -180)]``.
        :type bounds: list or tuple of 2 items of :class:`geopy.point.Point` or
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
