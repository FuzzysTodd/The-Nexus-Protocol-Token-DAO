from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['Yandex']

class Yandex(Geocoder):
    """Yandex geocoder.

    Documentation at:
        https://tech.yandex.com/maps/doc/geocoder/desc/concepts/input_params-docpage/
    """
    api_path: str
    api_key: Incomplete
    api: Incomplete
    def __init__(self, api_key, *, timeout=..., proxies=..., user_agent: Incomplete | None = None, scheme: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """

        :param str api_key: Yandex API key, mandatory.
            The key can be created at https://developer.tech.yandex.ru/

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
    def geocode(self, query, *, exactly_one: bool = True, timeout=..., lang: Incomplete | None = None):
        """
        Return a location point by address.

        :param str query: The address or query you wish to geocode.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder's initialization.

        :param str lang: Language of the response and regional settings
            of the map. List of supported values:

            - ``tr_TR`` -- Turkish (only for maps of Turkey);
            - ``en_RU`` -- response in English, Russian map features;
            - ``en_US`` -- response in English, American map features;
            - ``ru_RU`` -- Russian (default);
            - ``uk_UA`` -- Ukrainian;
            - ``be_BY`` -- Belarusian.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        """
    def reverse(self, query, *, exactly_one: bool = True, timeout=..., kind: Incomplete | None = None, lang: Incomplete | None = None):
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

        :param str kind: Type of toponym. Allowed values: `house`, `street`, `metro`,
            `district`, `locality`.

        :param str lang: Language of the response and regional settings
            of the map. List of supported values:

            - ``tr_TR`` -- Turkish (only for maps of Turkey);
            - ``en_RU`` -- response in English, Russian map features;
            - ``en_US`` -- response in English, American map features;
            - ``ru_RU`` -- Russian (default);
            - ``uk_UA`` -- Ukrainian;
            - ``be_BY`` -- Belarusian.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        '''
