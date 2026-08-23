__all__ = ['Timezone']

class Timezone:
    """
    Contains a parsed response for a timezone request, which is
    implemented in few geocoders which provide such lookups.
    """
    def __init__(self, pytz_timezone, raw) -> None: ...
    @property
    def pytz_timezone(self):
        """
        pytz timezone instance.

        :rtype: :class:`pytz.tzinfo.BaseTzInfo`
        """
    @property
    def raw(self):
        """
        Timezone's raw, unparsed geocoder response. For details on this,
        consult the service's documentation.

        :rtype: dict
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...
