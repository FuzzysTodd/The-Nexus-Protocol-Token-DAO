from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['AlgoliaPlaces']

class AlgoliaPlaces(Geocoder):
    """Geocoder using the Algolia Places API.

    Documentation at:
        https://community.algolia.com/places/documentation.html
    """
    geocode_path: str
    reverse_path: str
    domain: Incomplete
    app_id: Incomplete
    api_key: Incomplete
    geocode_api: Incomplete
    reverse_api: Incomplete
    def __init__(self, *, app_id: Incomplete | None = None, api_key: Incomplete | None = None, domain: str = 'places-dsn.algolia.net', scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """
        :param str app_id: Unique application identifier. It's used to
            identify you when using Algolia's API.
            See https://www.algolia.com/dashboard.

        :param str api_key: Algolia's user API key.

        :param str domain: Currently it is ``'places-dsn.algolia.net'``,
            can be changed for testing purposes.

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
    def geocode(self, query, *, exactly_one: bool = True, timeout=..., type: Incomplete | None = None, restrict_searchable_attributes: Incomplete | None = None, limit: Incomplete | None = None, language: Incomplete | None = None, countries: Incomplete | None = None, around: Incomplete | None = None, around_via_ip: Incomplete | None = None, around_radius: Incomplete | None = None, x_forwarded_for: Incomplete | None = None):
        '''
        Return a location point by address.

        :param str query: The address or query you wish to geocode.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :param str type: Restrict the search results to a specific type.
            Available types are defined in documentation:
            https://community.algolia.com/places/api-clients.html#api-options-type

        :param str restrict_searchable_attributes: Restrict the fields in which
            the search is done.

        :param int limit: Limit the maximum number of items in the
            response. If not provided and there are multiple results
            Algolia API will return 20 results by default. This will be
            reset to one if ``exactly_one`` is True.

        :param str language: If specified, restrict the search results
            to a single language. You can pass two letters country
            codes (ISO 639-1).

        :param list countries: If specified, restrict the search results
            to a specific list of countries. You can pass two letters
            country codes (ISO 3166-1).

        :param around: Force to first search around a specific
            latitude longitude.
        :type around: :class:`geopy.point.Point`, list or tuple of
            ``(latitude, longitude)``, or string as ``"%(latitude)s,
            %(longitude)s"``.

        :param bool around_via_ip: Whether or not to first search
            around the geolocation of the user found via his IP address.
            This is true by default.

        :param int around_radius: Radius in meters to search around the
            latitude/longitude. Otherwise a default radius is
            automatically computed given the area density.

        :param str x_forwarded_for: Override the HTTP header X-Forwarded-For.
            With this you can control the source IP address used to resolve
            the geo-location of the user. This is particularly useful when
            you want to use the API from your backend as if it was from your
            end-users\' locations.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.

        '''
    def reverse(self, query, *, exactly_one: bool = True, timeout=..., limit: Incomplete | None = None, language: Incomplete | None = None):
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

        :param int limit: Limit the maximum number of items in the
            response. If not provided and there are multiple results
            Algolia API will return 20 results by default. This will be
            reset to one if ``exactly_one`` is True.

        :param str language: If specified, restrict the search results
            to a single language. You can pass two letters country
            codes (ISO 639-1).

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
