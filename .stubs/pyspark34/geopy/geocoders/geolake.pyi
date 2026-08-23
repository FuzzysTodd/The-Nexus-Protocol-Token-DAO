from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['Geolake']

class Geolake(Geocoder):
    """Geocoder using the Geolake API.

    Documentation at:
        https://geolake.com/docs/api

    Terms of Service at:
        https://geolake.com/terms-of-use
    """
    structured_query_params: Incomplete
    api_path: str
    api_key: Incomplete
    domain: Incomplete
    api: Incomplete
    def __init__(self, api_key, *, domain: str = 'api.geolake.com', scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """

        :param str api_key: The API key required by Geolake
            to perform geocoding requests. You can get your key here:
            https://geolake.com/

        :param str domain: Currently it is ``'api.geolake.com'``, can
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
    def geocode(self, query, *, country_codes: Incomplete | None = None, exactly_one: bool = True, timeout=...):
        """
        Return a location point by address.

        :param query: The address or query you wish to geocode.

            For a structured query, provide a dictionary whose keys
            are one of: `country`, `state`, `city`, `zipcode`, `street`, `address`,
            `houseNumber` or `subNumber`.
        :type query: str or dict

        :param country_codes: Provides the geocoder with a list
            of country codes that the query may reside in. This value will
            limit the geocoder to the supplied countries. The country code
            is a 2 character code as defined by the ISO-3166-1 alpha-2
            standard (e.g. ``FR``). Multiple countries can be specified with
            a Python list.

        :type country_codes: str or list

        :param bool exactly_one: Return one result or a list of one result.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder's initialization.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.

        """
