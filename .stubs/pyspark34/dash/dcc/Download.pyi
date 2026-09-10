from _typeshed import Incomplete
from dash.development.base_component import Component as Component

class Download(Component):
    """A Download component.
    The Download component opens a download dialog when the data property changes.

    Keyword arguments:

    - id (string; optional):
        The ID of this component, used to identify dash components in
        callbacks.

    - base64 (boolean; default False):
        Default value for base64, used when not set as part of the data
        property.

    - data (dict; optional):
        On change, a download is invoked.

        `data` is a dict with keys:

        - base64 (boolean; optional):
            Set to True, when data is base64 encoded.

        - content (string; required):
            File content.

        - filename (string; required):
            Suggested filename in the download dialogue.

        - type (string; optional):
            Blob type, usually a MIME-type.

    - type (string; default 'text/plain'):
        Default value for type, used when not set as part of the data
        property."""
    available_properties: Incomplete
    available_wildcard_properties: Incomplete
    def __init__(self, id=..., data=..., base64=..., type=..., **kwargs) -> None: ...
