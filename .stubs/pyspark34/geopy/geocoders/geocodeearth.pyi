from _typeshed import Incomplete
from geopy.geocoders.pelias import Pelias

__all__ = ['GeocodeEarth']

class GeocodeEarth(Pelias):
    """Geocode Earth, a Pelias-based service provided by the developers
    of Pelias itself.

    Documentation at:
        https://geocode.earth/docs

    Pricing details:
        https://geocode.earth/#pricing
    """
    def __init__(self, api_key, *, domain: str = 'api.geocode.earth', timeout=..., proxies=..., user_agent: Incomplete | None = None, scheme: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """
        :param str api_key: Geocode.earth API key, required.

        :param str domain: Specify a custom domain for Pelias API.

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
