from _typeshed import Incomplete
from dash.development.base_component import Component as Component

class ConfirmDialogProvider(Component):
    """A ConfirmDialogProvider component.
    A wrapper component that will display a confirmation dialog
    when its child component has been clicked on.

    For example:
    ```
    dcc.ConfirmDialogProvider(
        html.Button('click me', id='btn'),
        message='Danger - Are you sure you want to continue.'
        id='confirm')
    ```

    Keyword arguments:

    - children (boolean | number | string | dict | list; optional):
        The children to hijack clicks from and display the popup.

    - id (string; optional):
        The ID of this component, used to identify dash components in
        callbacks. The ID needs to be unique across all of the components
        in an app.

    - cancel_n_clicks (number; default 0):
        Number of times the popup was canceled.

    - cancel_n_clicks_timestamp (number; default -1):
        Last time the cancel button was clicked.

    - displayed (boolean; optional):
        Is the modal currently displayed.

    - loading_state (dict; optional):
        Object that holds the loading state object coming from
        dash-renderer.

        `loading_state` is a dict with keys:

        - component_name (string; optional):
            Holds the name of the component that is loading.

        - is_loading (boolean; optional):
            Determines if the component is loading or not.

        - prop_name (string; optional):
            Holds which property is loading.

    - message (string; optional):
        Message to show in the popup.

    - submit_n_clicks (number; default 0):
        Number of times the submit was clicked.

    - submit_n_clicks_timestamp (number; default -1):
        Last time the submit button was clicked."""
    available_properties: Incomplete
    available_wildcard_properties: Incomplete
    def __init__(self, children: Incomplete | None = None, id=..., message=..., submit_n_clicks=..., submit_n_clicks_timestamp=..., cancel_n_clicks=..., cancel_n_clicks_timestamp=..., displayed=..., loading_state=..., **kwargs) -> None: ...
