from _typeshed import Incomplete
from dash.development.base_component import Component as Component

class Link(Component):
    """A Link component.
    Link allows you to create a clickable link within a multi-page app.

    For links with destinations outside the current app, `html.A` is a better
    component to use.

    Keyword arguments:

    - children (a list of or a singular dash component, string or number; optional):
        The children of this component.

    - href (string; required):
        The URL of a linked resource.

    - target (string; optional):
        Specifies where to open the link reference.

    - refresh (boolean; default False):
        Controls whether or not the page will refresh when the link is
        clicked.

    - title (string; optional):
        Adds the title attribute to your link, which can contain
        supplementary information.

    - className (string; optional):
        Often used with CSS to style elements with common properties.

    - style (dict; optional):
        Defines CSS styles which will override styles previously set.

    - id (string; optional):
        The ID of this component, used to identify dash components in
        callbacks. The ID needs to be unique across all of the components
        in an app.

    - loading_state (dict; optional):
        Object that holds the loading state object coming from
        dash-renderer.

        `loading_state` is a dict with keys:

        - component_name (string; optional):
            Holds the name of the component that is loading.

        - is_loading (boolean; optional):
            Determines if the component is loading or not.

        - prop_name (string; optional):
            Holds which property is loading."""
    available_properties: Incomplete
    available_wildcard_properties: Incomplete
    def __init__(self, children: Incomplete | None = None, href=..., target=..., refresh=..., title=..., className=..., style=..., id=..., loading_state=..., **kwargs) -> None: ...
