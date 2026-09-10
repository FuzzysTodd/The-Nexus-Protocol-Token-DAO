from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['ArcGIS']

class ArcGIS(Geocoder):
    """Geocoder using the ERSI ArcGIS API.

    Documentation at:
        https://developers.arcgis.com/rest/geocode/api-reference/overview-world-geocoding-service.htm
    """
    auth_path: str
    geocode_path: str
    reverse_path: str
    username: Incomplete
    password: Incomplete
    referer: Incomplete
    auth_domain: Incomplete
    auth_api: Incomplete
    token_lifetime: Incomplete
    domain: Incomplete
    api: Incomplete
    reverse_api: Incomplete
    token: Incomplete
    token_expiry: Incomplete
    def __init__(self, username: Incomplete | None = None, password: Incomplete | None = None, *, referer: Incomplete | None = None, token_lifetime: int = 60, scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None, auth_domain: str = 'www.arcgis.com', domain: str = 'geocode.arcgis.com') -> None:
        """

        :param str username: ArcGIS username. Required if authenticated
            mode is desired.

        :param str password: ArcGIS password. Required if authenticated
            mode is desired.

        :param str referer: Required if authenticated mode is desired.
            `Referer` HTTP header to send with each request,
            e.g., ``'http://www.example.com'``. This is tied to an issued token,
            so fielding queries for multiple referrers should be handled by
            having multiple ArcGIS geocoder instances.

        :param int token_lifetime: Desired lifetime, in minutes, of an
            ArcGIS-issued token.

        :param str scheme:
            See :attr:`geopy.geocoders.options.default_scheme`.
            If authenticated mode is in use, it must be ``'https'``.

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

        :param str auth_domain: Domain where the target ArcGIS auth service
            is hosted. Used only in authenticated mode (i.e. username,
            password and referer are set).

        :param str domain: Domain where the target ArcGIS service
            is hosted.
        """
    def geocode(self, query, *, exactly_one: bool = True, timeout=..., out_fields: Incomplete | None = None):
        '''
        Return a location point by address.

        :param str query: The address or query you wish to geocode.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :param out_fields: A list of output fields to be returned in the
            attributes field of the raw data. This can be either a python
            list/tuple of fields or a comma-separated string. See
            https://developers.arcgis.com/rest/geocode/api-reference/geocoding-service-output.htm
            for a list of supported output fields. If you want to return all
            supported output fields, set ``out_fields="*"``.
        :type out_fields: str or iterable

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
    def reverse(self, query, *, exactly_one: bool = True, timeout=..., distance: Incomplete | None = None):
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

        :param int distance: Distance from the query location, in meters,
            within which to search. ArcGIS has a default of 100 meters, if not
            specified.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
