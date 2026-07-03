from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['GeoNames']

class GeoNames(Geocoder):
    """GeoNames geocoder.

    Documentation at:
        http://www.geonames.org/export/geonames-search.html

    Reverse geocoding documentation at:
        http://www.geonames.org/export/web-services.html#findNearbyPlaceName
    """
    geocode_path: str
    reverse_path: str
    reverse_nearby_path: str
    timezone_path: str
    username: Incomplete
    api: Incomplete
    api_reverse: Incomplete
    api_reverse_nearby: Incomplete
    api_timezone: Incomplete
    def __init__(self, username, *, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None, scheme: str = 'http') -> None:
        """

        :param str username: GeoNames username, required. Sign up here:
            http://www.geonames.org/login

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

        :param str scheme:
            See :attr:`geopy.geocoders.options.default_scheme`. Note that
            at the time of writing GeoNames doesn't support `https`, so
            the default scheme is `http`. The value of
            :attr:`geopy.geocoders.options.default_scheme` is not respected.
            This parameter is present to make it possible to switch to
            `https` once GeoNames adds support for it.
        """
    def geocode(self, query, *, exactly_one: bool = True, timeout=..., country: Incomplete | None = None, country_bias: Incomplete | None = None):
        """
        Return a location point by address.

        :param str query: The address or query you wish to geocode.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder's initialization.

        :param country: Limit records to the specified countries.
            Two letter country code ISO-3166 (e.g. ``FR``). Might be
            a single string or a list of strings.
        :type country: str or list

        :param str country_bias: Records from the country_bias are listed first.
            Two letter country code ISO-3166.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        """
    def reverse(self, query, *, exactly_one: bool = True, timeout=..., feature_code: Incomplete | None = None, lang: Incomplete | None = None, find_nearby_type: str = 'findNearbyPlaceName'):
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

        :param str feature_code: A GeoNames feature code

        :param str lang: language of the returned ``name`` element (the pseudo
            language code \'local\' will return it in local language)
            Full list of supported languages can be found here:
            https://www.geonames.org/countries/

        :param str find_nearby_type: A flag to switch between different
            GeoNames API endpoints. The default value is ``findNearbyPlaceName``
            which returns the closest populated place. Another currently
            implemented option is ``findNearby`` which returns
            the closest toponym for the lat/lng query.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.

        '''
    def reverse_timezone(self, query, *, timeout=...):
        '''
        Find the timezone for a point in `query`.

        GeoNames always returns a timezone: if the point being queried
        doesn\'t have an assigned Olson timezone id, a ``pytz.FixedOffset``
        timezone is used to produce the :class:`geopy.timezone.Timezone`.

        :param query: The coordinates for which you want a timezone.
        :type query: :class:`geopy.point.Point`, list or tuple of (latitude,
            longitude), or string as "%(latitude)s, %(longitude)s"

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :rtype: :class:`geopy.timezone.Timezone`.
        '''
