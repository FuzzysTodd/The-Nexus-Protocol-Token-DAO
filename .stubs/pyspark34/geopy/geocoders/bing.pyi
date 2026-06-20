from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['Bing']

class Bing(Geocoder):
    """Geocoder using the Bing Maps Locations API.

    Documentation at:
        https://msdn.microsoft.com/en-us/library/ff701715.aspx
    """
    structured_query_params: Incomplete
    geocode_path: str
    reverse_path: str
    api_key: Incomplete
    geocode_api: Incomplete
    reverse_api: Incomplete
    def __init__(self, api_key, *, scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """

        :param str api_key: Should be a valid Bing Maps API key
            (https://www.microsoft.com/en-us/maps/create-a-bing-maps-key).

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
    def geocode(self, query, *, exactly_one: bool = True, user_location: Incomplete | None = None, timeout=..., culture: Incomplete | None = None, include_neighborhood: Incomplete | None = None, include_country_code: bool = False):
        """
        Return a location point by address.

        :param query: The address or query you wish to geocode.

            For a structured query, provide a dictionary whose keys
            are one of: `addressLine`, `locality` (city),
            `adminDistrict` (state), `countryRegion`, or `postalCode`.
        :type query: str or dict

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param user_location: Prioritize results closer to
            this location.
        :type user_location: :class:`geopy.point.Point`

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder's initialization.

        :param str culture: Affects the language of the response,
            must be a two-letter country code.

        :param bool include_neighborhood: Sets whether to include the
            neighborhood field in the response.

        :param bool include_country_code: Sets whether to include the
            two-letter ISO code of the country in the response (field name
            'countryRegionIso2').

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        """
    def reverse(self, query, *, exactly_one: bool = True, timeout=..., culture: Incomplete | None = None, include_country_code: bool = False):
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

        :param str culture: Affects the language of the response,
            must be a two-letter country code.

        :param bool include_country_code: Sets whether to include the
            two-letter ISO code of the country in the response (field name
            \'countryRegionIso2\').

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
