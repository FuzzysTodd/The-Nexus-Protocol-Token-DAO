from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['Photon']

class Photon(Geocoder):
    """Geocoder using Photon geocoding service (data based on OpenStreetMap
    and service provided by Komoot on https://photon.komoot.io).

    Documentation at:
        https://github.com/komoot/photon

    Photon/Komoot geocoder aims to let you `search as you type with
    OpenStreetMap`. No API Key is needed by this platform.

    .. versionchanged:: 2.2
        Changed default domain from ``photon.komoot.de``
        to ``photon.komoot.io``.
    """
    geocode_path: str
    reverse_path: str
    domain: Incomplete
    api: Incomplete
    reverse_api: Incomplete
    def __init__(self, *, scheme: Incomplete | None = None, timeout=..., proxies=..., domain: str = 'photon.komoot.io', user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """

        :param str scheme:
            See :attr:`geopy.geocoders.options.default_scheme`.

        :param int timeout:
            See :attr:`geopy.geocoders.options.default_timeout`.

        :param dict proxies:
            See :attr:`geopy.geocoders.options.default_proxies`.

        :param str domain: Should be the localized Photon domain to
            connect to. The default is ``'photon.komoot.io'``, but you
            can change it to a domain of your own.

        :param str user_agent:
            See :attr:`geopy.geocoders.options.default_user_agent`.

        :type ssl_context: :class:`ssl.SSLContext`
        :param ssl_context:
            See :attr:`geopy.geocoders.options.default_ssl_context`.

        :param callable adapter_factory:
            See :attr:`geopy.geocoders.options.default_adapter_factory`.

            .. versionadded:: 2.0
        """
    def geocode(self, query, *, exactly_one: bool = True, timeout=..., location_bias: Incomplete | None = None, language: bool = False, limit: Incomplete | None = None, osm_tag: Incomplete | None = None, bbox: Incomplete | None = None):
        '''
        Return a location point by address.

        :param str query: The address or query you wish to geocode.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :param location_bias: The coordinates to use as location bias.
        :type location_bias: :class:`geopy.point.Point`, list or tuple of
            ``(latitude, longitude)``, or string
            as ``"%(latitude)s, %(longitude)s"``.

        :param str language: Preferred language in which to return results.

        :param int limit: Limit the number of returned results, defaults to no
            limit.

        :param osm_tag: The expression to filter (include/exclude) by key and/
            or value, str as ``\'key:value\'`` or list/set of str if multiple
            filters are required as ``[\'key:!val\', \'!key\', \':!value\']``.
        :type osm_tag: str or list or set

        :param bbox: The bounding box of the viewport within which
            to bias geocode results more prominently.
            Example: ``[Point(22, 180), Point(-22, -180)]``.

            .. versionadded:: 2.2
        :type bbox: list or tuple of 2 items of :class:`geopy.point.Point` or
            ``(latitude, longitude)`` or ``"%(latitude)s, %(longitude)s"``.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.

        '''
    def reverse(self, query, *, exactly_one: bool = True, timeout=..., language: bool = False, limit: Incomplete | None = None):
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

        :param int limit: Limit the number of returned results, defaults to no
            limit.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
