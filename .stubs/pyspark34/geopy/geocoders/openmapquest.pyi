from _typeshed import Incomplete
from geopy.geocoders.nominatim import Nominatim

__all__ = ['OpenMapQuest']

class OpenMapQuest(Nominatim):
    """Geocoder using MapQuest Open Platform Web Services.

    Documentation at:
        https://developer.mapquest.com/documentation/open/

    MapQuest provides two Geocoding APIs:

    - :class:`geopy.geocoders.OpenMapQuest` (this class) Nominatim-alike API
      which is based on Open data from OpenStreetMap.
    - :class:`geopy.geocoders.MapQuest` MapQuest's own API which is based on
      Licensed data.
    """
    geocode_path: str
    reverse_path: str
    api_key: Incomplete
    def __init__(self, api_key, *, timeout=..., proxies=..., domain: str = 'open.mapquestapi.com', scheme: Incomplete | None = None, user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """

        :param str api_key: API key provided by MapQuest, required.

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
