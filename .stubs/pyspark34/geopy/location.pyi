from geopy.point import Point as Point

class Location:
    """
    Contains a parsed geocoder response. Can be iterated over as
    ``(location<String>, (latitude<float>, longitude<Float))``.
    Or one can access the properties ``address``, ``latitude``,
    ``longitude``, or ``raw``. The last
    is a dictionary of the geocoder's response for this item.
    """
    def __init__(self, address, point, raw) -> None: ...
    @property
    def address(self):
        """
        Location as a formatted string returned by the geocoder or constructed
        by geopy, depending on the service.

        :rtype: str
        """
    @property
    def latitude(self):
        """
        Location's latitude.

        :rtype: float
        """
    @property
    def longitude(self):
        """
        Location's longitude.

        :rtype: float
        """
    @property
    def altitude(self):
        """
        Location's altitude.

        .. note::
            Geocoding services usually don't consider altitude neither in
            requests nor in responses, so almost always the value of this
            property would be zero.

        :rtype: float
        """
    @property
    def point(self):
        """
        :class:`geopy.point.Point` instance representing the location's
        latitude, longitude, and altitude.

        :rtype: :class:`geopy.point.Point`
        """
    @property
    def raw(self):
        """
        Location's raw, unparsed geocoder response. For details on this,
        consult the service's documentation.

        :rtype: dict
        """
    def __getitem__(self, index):
        """
        Backwards compatibility with geopy<0.98 tuples.
        """
    def __iter__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __len__(self) -> int: ...
