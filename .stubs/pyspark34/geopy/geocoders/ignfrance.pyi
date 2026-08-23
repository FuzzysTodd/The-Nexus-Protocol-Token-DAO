from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['IGNFrance']

class IGNFrance(Geocoder):
    """Geocoder using the IGN France GeoCoder OpenLS API.

    Documentation at:
        https://geoservices.ign.fr/services-web-essentiels
    """
    xml_request: str
    api_path: str
    domain: Incomplete
    api: Incomplete
    def __init__(self, api_key: Incomplete | None = None, *, username: Incomplete | None = None, password: Incomplete | None = None, referer: Incomplete | None = None, domain: str = 'wxs.ign.fr', scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """

        :param str api_key: Not used.

            .. deprecated:: 2.3
                IGNFrance geocoding methods no longer accept or require
                authentication, see `<https://geoservices.ign.fr/actualites/2021-10-04-evolution-des-modalites-dacces-aux-services-web>`_.
                This parameter is scheduled for removal in geopy 3.0.

        :param str username: Not used.

            .. deprecated:: 2.3
                See the `api_key` deprecation note.

        :param str password: Not used.

            .. deprecated:: 2.3
                See the `api_key` deprecation note.

        :param str referer: Not used.

            .. deprecated:: 2.3
                See the `api_key` deprecation note.

        :param str domain: Currently it is ``'wxs.ign.fr'``, can
            be changed for testing purposes for developer API
            e.g ``'gpp3-wxs.ign.fr'`` at the moment.

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
    def geocode(self, query, *, query_type: str = 'StreetAddress', maximum_responses: int = 25, is_freeform: bool = False, filtering: Incomplete | None = None, exactly_one: bool = True, timeout=...):
        """
        Return a location point by address.

        :param str query: The query string to be geocoded.

        :param str query_type: The type to provide for geocoding. It can be
            `PositionOfInterest`, `StreetAddress` or `CadastralParcel`.
            `StreetAddress` is the default choice if none provided.

        :param int maximum_responses: The maximum number of responses
            to ask to the API in the query body.

        :param str is_freeform: Set if return is structured with
            freeform structure or a more structured returned.
            By default, value is False.

        :param str filtering: Provide string that help setting geocoder
            filter. It contains an XML string. See examples in documentation
            and ignfrance.py file in directory tests.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder's initialization.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.

        """
    def reverse(self, query, *, reverse_geocode_preference=('StreetAddress',), maximum_responses: int = 25, filtering: str = '', exactly_one: bool = True, timeout=...):
        '''
        Return an address by location point.

        :param query: The coordinates for which you wish to obtain the
            closest human-readable addresses.
        :type query: :class:`geopy.point.Point`, list or tuple of ``(latitude,
            longitude)``, or string as ``"%(latitude)s, %(longitude)s"``.

        :param list reverse_geocode_preference: Enable to set expected results
            type. It can be `StreetAddress` or `PositionOfInterest`.
            Default is set to `StreetAddress`.

        :param int maximum_responses: The maximum number of responses
            to ask to the API in the query body.

        :param str filtering: Provide string that help setting geocoder
            filter. It contains an XML string. See examples in documentation
            and ignfrance.py file in directory tests.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.

        '''
