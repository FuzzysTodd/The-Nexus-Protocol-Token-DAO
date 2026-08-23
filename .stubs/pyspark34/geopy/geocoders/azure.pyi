from _typeshed import Incomplete
from geopy.geocoders.tomtom import TomTom

__all__ = ['AzureMaps']

class AzureMaps(TomTom):
    """AzureMaps geocoder based on TomTom.

    Documentation at:
        https://docs.microsoft.com/en-us/azure/azure-maps/index
    """
    geocode_path: str
    reverse_path: str
    def __init__(self, subscription_key, *, scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None, domain: str = 'atlas.microsoft.com') -> None:
        """
        :param str subscription_key: Azure Maps subscription key.

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

        :param str domain: Domain where the target Azure Maps service
            is hosted.
        """
