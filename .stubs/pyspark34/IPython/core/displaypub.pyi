from .display_functions import publish_display_data as publish_display_data
from _typeshed import Incomplete
from traitlets.config.configurable import Configurable

class DisplayPublisher(Configurable):
    """A traited class that publishes display data to frontends.

    Instances of this class are created by the main IPython object and should
    be accessed there.
    """
    shell: Incomplete
    def __init__(self, shell: Incomplete | None = None, *args, **kwargs) -> None: ...
    def publish(self, data, metadata: Incomplete | None = None, source: Incomplete | None = None, *, transient: Incomplete | None = None, update: bool = False, **kwargs) -> None:
        """Publish data and metadata to all frontends.

        See the ``display_data`` message in the messaging documentation for
        more details about this message type.

        The following MIME types are currently implemented:

        * text/plain
        * text/html
        * text/markdown
        * text/latex
        * application/json
        * application/javascript
        * image/png
        * image/jpeg
        * image/svg+xml

        Parameters
        ----------
        data : dict
            A dictionary having keys that are valid MIME types (like
            'text/plain' or 'image/svg+xml') and values that are the data for
            that MIME type. The data itself must be a JSON'able data
            structure. Minimally all data should have the 'text/plain' data,
            which can be displayed by all frontends. If more than the plain
            text is given, it is up to the frontend to decide which
            representation to use.
        metadata : dict
            A dictionary for metadata related to the data. This can contain
            arbitrary key, value pairs that frontends can use to interpret
            the data.  Metadata specific to each mime-type can be specified
            in the metadata dict with the same mime-type keys as
            the data itself.
        source : str, deprecated
            Unused.
        transient : dict, keyword-only
            A dictionary for transient data.
            Data in this dictionary should not be persisted as part of saving this output.
            Examples include 'display_id'.
        update : bool, keyword-only, default: False
            If True, only update existing outputs with the same display_id,
            rather than creating a new output.
        """
    def clear_output(self, wait: bool = False) -> None:
        """Clear the output of the cell receiving output."""

class CapturingDisplayPublisher(DisplayPublisher):
    """A DisplayPublisher that stores"""
    outputs: Incomplete
    def publish(self, data, metadata: Incomplete | None = None, source: Incomplete | None = None, *, transient: Incomplete | None = None, update: bool = False) -> None: ...
    def clear_output(self, wait: bool = False) -> None: ...
