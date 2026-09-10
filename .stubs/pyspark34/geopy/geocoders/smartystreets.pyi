from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['LiveAddress']

class LiveAddress(Geocoder):
    """Geocoder using the LiveAddress API provided by SmartyStreets.

    Documentation at:
        https://smartystreets.com/docs/cloud/us-street-api
    """
    geocode_path: str
    auth_id: Incomplete
    auth_token: Incomplete
    api: Incomplete
    def __init__(self, auth_id, auth_token, *, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """

        :param str auth_id: Valid `Auth ID` from SmartyStreets.

        :param str auth_token: Valid `Auth Token` from SmartyStreets.

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
    def geocode(self, query, *, exactly_one: bool = True, timeout=..., candidates: int = 1):
        """
        Return a location point by address.

        :param str query: The address or query you wish to geocode.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder's initialization.

        :param int candidates: An integer between 1 and 10 indicating the max
            number of candidate addresses to return if a valid address
            could be found.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        """
