from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['OpenCage']

class OpenCage(Geocoder):
    """Geocoder using the OpenCageData API.

    Documentation at:
        https://opencagedata.com/api

    .. versionchanged:: 2.2
        Improved error handling by using the default errors map
        (e.g. to raise :class:`.exc.GeocoderQuotaExceeded` instead of
        :class:`.exc.GeocoderQueryError` for HTTP 402 error)
    """
    api_path: str
    api_key: Incomplete
    domain: Incomplete
    api: Incomplete
    def __init__(self, api_key, *, domain: str = 'api.opencagedata.com', scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """

        :param str api_key: The API key required by OpenCageData
            to perform geocoding requests. You can get your key here:
            https://opencagedata.com/

        :param str domain: Currently it is ``'api.opencagedata.com'``, can
            be changed for testing purposes.

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
    def geocode(self, query, *, bounds: Incomplete | None = None, country: Incomplete | None = None, language: Incomplete | None = None, annotations: bool = True, exactly_one: bool = True, timeout=...):
        '''
        Return a location point by address.

        :param str query: The address or query you wish to geocode.

        :type bounds: list or tuple of 2 items of :class:`geopy.point.Point` or
            ``(latitude, longitude)`` or ``"%(latitude)s, %(longitude)s"``.
        :param bounds: Provides the geocoder with a hint to the region
            that the query resides in. This value will help the geocoder
            but will not restrict the possible results to the supplied
            region. The bounds parameter should be specified as 2
            coordinate points -- corners of a bounding box.
            Example: ``[Point(22, 180), Point(-22, -180)]``.

        :param country: Restricts the results to the specified
            country or countries. The country code is a 2 character code as
            defined by the ISO 3166-1 Alpha 2 standard (e.g. ``fr``).
            Might be a Python list of strings.
        :type country: str or list

        :param str language: an IETF format language code (such as `es`
            for Spanish or pt-BR for Brazilian Portuguese); if this is
            omitted a code of `en` (English) will be assumed by the remote
            service.

        :param bool annotations: Enable
            `annotations <https://opencagedata.com/api#annotations>`_
            data, which can be accessed via :attr:`.Location.raw`.
            Set to False if you don\'t need it to gain a little performance
            win.

            .. versionadded:: 2.2

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.

        '''
    def reverse(self, query, *, language: Incomplete | None = None, exactly_one: bool = True, timeout=...):
        '''
        Return an address by location point.

        :param query: The coordinates for which you wish to obtain the
            closest human-readable addresses.
        :type query: :class:`geopy.point.Point`, list or tuple of ``(latitude,
            longitude)``, or string as ``"%(latitude)s, %(longitude)s"``.

        :param str language: The language in which to return results.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder\'s initialization.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.

        '''
