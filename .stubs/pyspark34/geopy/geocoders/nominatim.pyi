from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['Nominatim']

class Nominatim(Geocoder):
    '''Nominatim geocoder for OpenStreetMap data.

    Documentation at:
        https://nominatim.org/release-docs/develop/api/Overview/

    .. attention::
       Using Nominatim with the default `user_agent` is strongly discouraged,
       as it violates Nominatim\'s Usage Policy
       https://operations.osmfoundation.org/policies/nominatim/
       and may possibly cause 403 and 429 HTTP errors. Please make sure
       to specify a custom `user_agent` with
       ``Nominatim(user_agent="my-application")`` or by
       overriding the default `user_agent`:
       ``geopy.geocoders.options.default_user_agent = "my-application"``.
       An exception will be thrown if a custom `user_agent` is not specified.
    '''
    structured_query_params: Incomplete
    geocode_path: str
    reverse_path: str
    domain: Incomplete
    api: Incomplete
    reverse_api: Incomplete
    def __init__(self, *, timeout=..., proxies=..., domain=..., scheme: Incomplete | None = None, user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """

        :param int timeout:
            See :attr:`geopy.geocoders.options.default_timeout`.

        :param dict proxies:
            See :attr:`geopy.geocoders.options.default_proxies`.

        :param str domain: Domain where the target Nominatim service
            is hosted.

        :param str scheme:
            See :attr:`geopy.geocoders.options.default_scheme`.

        :param str user_agent:
            See :attr:`geopy.geocoders.options.default_user_agent`.

        :type ssl_context: :class:`ssl.SSLContext`
        :param ssl_context:
            See :attr:`geopy.geocoders.options.default_ssl_context`.

        :param callable adapter_factory:
            See :attr:`geopy.geocoders.options.default_adapter_factory`.

            .. versionadded:: 2.0
        """
    def geocode(self, query, *, exactly_one: bool = True, timeout=..., limit: Incomplete | None = None, addressdetails: bool = False, language: bool = False, geometry: Incomplete | None = None, extratags: bool = False, country_codes: Incomplete | None = None, viewbox: Incomplete | None = None, bounded: bool = False, featuretype: Incomplete | None = None, namedetails: bool = False):
        '''
        Return a location point by address.

        :param query: The address, query or a structured query
            you wish to geocode.

            For a structured query, provide a dictionary whose keys
            are one of: `street`, `city`, `county`, `state`, `country`, or
            `postalcode`. For more information, see Nominatim\'s
            documentation for `structured requests`:

                https://nominatim.org/release-docs/develop/api/Search

        :type query: dict or str

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :param int limit: Maximum amount of results to return from Nominatim.
            Unless exactly_one is set to False, limit will always be 1.

        :param bool addressdetails: If you want in *Location.raw* to include
            address details such as house_number, city_district, postcode, etc
            (in a structured form) set it to True

        :param str language: Preferred language in which to return results.
            Either uses standard
            `RFC2616 <http://www.ietf.org/rfc/rfc2616.txt>`_
            accept-language string or a simple comma-separated
            list of language codes.

        :param str geometry: If present, specifies whether the geocoding
            service should return the result\'s geometry in `wkt`, `svg`,
            `kml`, or `geojson` formats. This is available via the
            `raw` attribute on the returned :class:`geopy.location.Location`
            object.

        :param bool extratags: Include additional information in the result if available,
            e.g. wikipedia link, opening hours.

        :param country_codes: Limit search results
            to a specific country (or a list of countries).
            A country_code should be the ISO 3166-1alpha2 code,
            e.g. ``gb`` for the United Kingdom, ``de`` for Germany, etc.

        :type country_codes: str or list

        :type viewbox: list or tuple of 2 items of :class:`geopy.point.Point` or
            ``(latitude, longitude)`` or ``"%(latitude)s, %(longitude)s"``.

        :param viewbox: Prefer this area to find search results. By default this is
            treated as a hint, if you want to restrict results to this area,
            specify ``bounded=True`` as well.
            Example: ``[Point(22, 180), Point(-22, -180)]``.

        :param bool bounded: Restrict the results to only items contained
            within the bounding ``viewbox``.

        :param str featuretype: If present, restrict results to certain type of features.
            Allowed values: `country`, `state`, `city`, `settlement`.

        :param bool namedetails: If you want in *Location.raw* to include
            namedetails, set it to True. This will be a list of alternative names,
            including language variants, etc.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.

        '''
    def reverse(self, query, *, exactly_one: bool = True, timeout=..., language: bool = False, addressdetails: bool = True, zoom: Incomplete | None = None, namedetails: bool = False):
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

        :param bool addressdetails: Whether or not to include address details,
            such as city, county, state, etc. in *Location.raw*

        :param int zoom: Level of detail required for the address,
            an integer in range from 0 (country level) to 18 (building level),
            default is 18.

        :param bool namedetails: If you want in *Location.raw* to include
            namedetails, set it to True. This will be a list of alternative names,
            including language variants, etc.

            .. versionadded:: 2.3

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.

        '''
