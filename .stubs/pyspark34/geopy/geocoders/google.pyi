from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['GoogleV3']

class GoogleV3(Geocoder):
    """Geocoder using the Google Maps v3 API.

    Documentation at:
        https://developers.google.com/maps/documentation/geocoding/

    Pricing details:
        https://developers.google.com/maps/documentation/geocoding/usage-and-billing
    """
    api_path: str
    timezone_path: str
    premier: Incomplete
    client_id: Incomplete
    secret_key: Incomplete
    api_key: Incomplete
    domain: Incomplete
    channel: Incomplete
    api: Incomplete
    tz_api: Incomplete
    def __init__(self, api_key: Incomplete | None = None, *, domain: str = 'maps.googleapis.com', scheme: Incomplete | None = None, client_id: Incomplete | None = None, secret_key: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None, channel: str = '') -> None:
        """

        :param str api_key: The API key required by Google to perform
            geocoding requests, mandatory (unless premier is used,
            then both ``client_id`` and ``secret_key`` must be specified
            instead).
            API keys are managed through
            the Google APIs console (https://code.google.com/apis/console).
            Make sure to have both ``Geocoding API`` and ``Time Zone API``
            services enabled for this API key.

            .. versionchanged:: 2.1
               Previously a warning has been emitted when neither ``api_key``
               nor premier were specified. Now a :class:`geopy.exc.ConfigurationError`
               is raised.

        :param str domain: Should be the localized Google Maps domain to
            connect to. The default is 'maps.googleapis.com', but if you're
            geocoding address in the UK (for example), you may want to set it
            to 'maps.google.co.uk' to properly bias results.

        :param str scheme:
            See :attr:`geopy.geocoders.options.default_scheme`.

        :param str client_id: If using premier, the account client id.

        :param str secret_key: If using premier, the account secret key.

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

        :param str channel: If using premier, the channel identifier.
        """
    def geocode(self, query: Incomplete | None = None, *, exactly_one: bool = True, timeout=..., bounds: Incomplete | None = None, region: Incomplete | None = None, components: Incomplete | None = None, place_id: Incomplete | None = None, language: Incomplete | None = None, sensor: bool = False):
        '''
        Return a location point by address.

        :param str query: The address or query you wish to geocode. Optional,
            if ``components`` param is set::

                >>> g.geocode(components={"city": "Paris", "country": "FR"})
                Location(France, (46.227638, 2.213749, 0.0))

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :type bounds: list or tuple of 2 items of :class:`geopy.point.Point` or
            ``(latitude, longitude)`` or ``"%(latitude)s, %(longitude)s"``.
        :param bounds: The bounding box of the viewport within which
            to bias geocode results more prominently.
            Example: ``[Point(22, 180), Point(-22, -180)]``.

        :param str region: The region code, specified as a ccTLD
            ("top-level domain") two-character value.

        :type components: dict or list
        :param components: Restricts to an area. Can use any combination of:
            `route`, `locality`, `administrative_area`, `postal_code`,
            `country`.

            Pass a list of tuples if you want to specify multiple components of
            the same type, e.g.:

                >>> [(\'administrative_area\', \'VA\'), (\'administrative_area\', \'Arlington\')]

        :param str place_id: Retrieve a Location using a Place ID.
            Cannot be not used with ``query`` or ``bounds`` parameters.

                >>> g.geocode(place_id=\'ChIJOcfP0Iq2j4ARDrXUa7ZWs34\')

        :param str language: The language in which to return results.

        :param bool sensor: Whether the geocoding request comes from a
            device with a location sensor.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
    def reverse(self, query, *, exactly_one: bool = True, timeout=..., language: Incomplete | None = None, sensor: bool = False):
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

        :param str language: The language in which to return results.

        :param bool sensor: Whether the geocoding request comes from a
            device with a location sensor.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
    def reverse_timezone(self, query, *, at_time: Incomplete | None = None, timeout=...):
        '''
        Find the timezone a point in `query` was in for a specified `at_time`.

        `None` will be returned for points without an assigned
        Olson timezone id (e.g. for Antarctica).

        :param query: The coordinates for which you want a timezone.
        :type query: :class:`geopy.point.Point`, list or tuple of (latitude,
            longitude), or string as "%(latitude)s, %(longitude)s"

        :param at_time: The time at which you want the timezone of this
            location. This is optional, and defaults to the time that the
            function is called in UTC. Timezone-aware datetimes are correctly
            handled and naive datetimes are silently treated as UTC.
        :type at_time: :class:`datetime.datetime` or None

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :rtype: ``None`` or :class:`geopy.timezone.Timezone`.
        '''
