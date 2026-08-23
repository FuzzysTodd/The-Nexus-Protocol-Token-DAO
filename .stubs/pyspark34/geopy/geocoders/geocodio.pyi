from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['Geocodio']

class Geocodio(Geocoder):
    """Geocoder using the Geocod.io API.

    Documentation at:
        https://www.geocod.io/docs/

    Pricing details:
        https://www.geocod.io/pricing/

    .. versionadded:: 2.2
    """
    structured_query_params: Incomplete
    domain: str
    geocode_path: str
    reverse_path: str
    api_key: Incomplete
    def __init__(self, api_key, *, scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """
        :param str api_key:
            A valid Geocod.io API key. (https://dash.geocod.io/apikey/create)

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
        """
    def geocode(self, query, *, limit: Incomplete | None = None, exactly_one: bool = True, timeout=...):
        """
        Return a location point by address.

        :param query: The address, query or a structured query
            you wish to geocode.

            For a structured query, provide a dictionary whose keys
            are one of: `street`, `city`, `state`, `postal_code` or `country`.
        :type query: dict or str

        :param int limit: The maximum number of matches to return. This will be reset
            to 1 if ``exactly_one`` is ``True``.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder's initialization.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        """
    def reverse(self, query, *, exactly_one: bool = True, timeout=..., limit: Incomplete | None = None):
        """Return an address by location point.

        :param str query: The coordinates for which you wish to obtain the
            closest human-readable addresses

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder's initialization.

        :param int limit: The maximum number of matches to return. This will be reset
            to 1 if ``exactly_one`` is ``True``.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        """
