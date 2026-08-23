from _typeshed import Incomplete
from geopy.geocoders.base import Geocoder

__all__ = ['DataBC']

class DataBC(Geocoder):
    """Geocoder using the Physical Address Geocoder from DataBC.

    Documentation at:
        http://www.data.gov.bc.ca/dbc/geographic/locate/geocoding.page
    """
    geocode_path: str
    api: Incomplete
    def __init__(self, *, scheme: Incomplete | None = None, timeout=..., proxies=..., user_agent: Incomplete | None = None, ssl_context=..., adapter_factory: Incomplete | None = None) -> None:
        """

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
    def geocode(self, query, *, max_results: int = 25, set_back: int = 0, location_descriptor: str = 'any', exactly_one: bool = True, timeout=...):
        """
        Return a location point by address.

        :param str query: The address or query you wish to geocode.

        :param int max_results: The maximum number of resutls to request.

        :param float set_back: The distance to move the accessPoint away
            from the curb (in meters) and towards the interior of the parcel.
            location_descriptor must be set to accessPoint for set_back to
            take effect.

        :param str location_descriptor: The type of point requested. It
            can be any, accessPoint, frontDoorPoint, parcelPoint,
            rooftopPoint and routingPoint.

        :param bool exactly_one: Return one result or a list of results, if
            available.

        :param int timeout: Time, in seconds, to wait for the geocoding service
            to respond before raising a :class:`geopy.exc.GeocoderTimedOut`
            exception. Set this only if you wish to override, on this call
            only, the value set during the geocoder's initialization.

        :rtype: ``None``, :class:`geopy.location.Location` or a list of them, if
            ``exactly_one=False``.
        """
