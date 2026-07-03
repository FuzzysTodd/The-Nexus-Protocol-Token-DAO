from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['Pelias']

class Pelias(Geocoder):
    """Pelias geocoder.

    Documentation at:
        https://github.com/pelias/documentation

    See also :class:`geopy.geocoders.GeocodeEarth` which is a Pelias-based
    service provided by the developers of Pelias itself.
    """
    geocode_path: str
    reverse_path: str
    api_key: Incomplete
    domain: Incomplete
    geocode_api: Incomplete
    reverse_api: Incomplete
    def __init__(self, domain, api_key: Incomplete | None = None, *, timeout=..., proxies=..., user_agent: Incomplete | None = None, scheme: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """
        :param str domain: Specify a domain for Pelias API.

        :param str api_key: Pelias API key, optional.

        :param int timeout:
            See :attr:`geopy.geocoders.options.default_timeout`.

        :param dict proxies:
            See :attr:`geopy.geocoders.options.default_proxies`.

        :param str user_agent:
            See :attr:`geopy.geocoders.options.default_user_agent`.

        :param str scheme:
            See :attr:`geopy.geocoders.options.default_scheme`.

        :type ssl_context: :class:`ssl.SSLContext`
        :param ssl_context:
            See :attr:`geopy.geocoders.options.default_ssl_context`.

        :param callable adapter_factory:
            See :attr:`geopy.geocoders.options.default_adapter_factory`.

            .. versionadded:: 2.0

        """
    def geocode(self, query, *, exactly_one: bool = True, timeout=..., boundary_rect: Incomplete | None = None, countries: Incomplete | None = None, country_bias: Incomplete | None = None, language: Incomplete | None = None):
        '''
        Return a location point by address.

        :param str query: The address or query you wish to geocode.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :type boundary_rect: list or tuple of 2 items of :class:`geopy.point.Point`
            or ``(latitude, longitude)`` or ``"%(latitude)s, %(longitude)s"``.
        :param boundary_rect: Coordinates to restrict search within.
            Example: ``[Point(22, 180), Point(-22, -180)]``.

        :param list countries: A list of country codes specified in
            `ISO 3166-1 alpha-2 or alpha-3
            <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`_
            format, e.g. ``[\'USA\', \'CAN\']``.
            This is a hard filter.

            .. versionadded:: 2.3

        :param str country_bias: Bias results to this country (ISO alpha-3).

            .. deprecated:: 2.3
                Use ``countries`` instead. This option behaves the same way,
                i.e. it\'s not a soft filter as the name suggests.
                This parameter is scheduled for removal in geopy 3.0.

        :param str language: Preferred language in which to return results.
            Either uses standard
            `RFC2616 <http://www.ietf.org/rfc/rfc2616.txt>`_
            accept-language string or a simple comma-separated
            list of language codes.

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

        :param str language: Preferred language in which to return results.
            Either uses standard
            `RFC2616 <http://www.ietf.org/rfc/rfc2616.txt>`_
            accept-language string or a simple comma-separated
            list of language codes.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
