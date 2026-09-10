from _typeshed import Incomplete
from dash.development.base_component import Component as Component

class Location(Component):
    '''A Location component.
    Update and track the current window.location object through the window.history state.
    Use in conjunction with the `dash_core_components.Link` component to make apps with multiple pages.

    Keyword arguments:

    - id (string; required):
        The ID of this component, used to identify dash components in
        callbacks. The ID needs to be unique across all of the components
        in an app.

    - hash (string; optional):
        hash in window.location - e.g., "#myhash".

    - href (string; optional):
        href in window.location - e.g.,
        "/my/full/pathname?myargument=1#myhash".

    - pathname (string; optional):
        pathname in window.location - e.g., "/my/full/pathname".

    - refresh (a value equal to: \'callback-nav\' | boolean; default True):
        Use `True` to navigate outside the Dash app or to manually refresh
        a page. Use `False` if the same callback that updates the Location
        component is also updating the page content - typically used in
        multi-page apps that do not use Pages. Use \'callback-nav\' if you
        are updating the URL in a callback, or a different callback will
        respond to the new Location with updated content. This is typical
        with multi-page apps that use Pages. This will allow for
        navigating to a new page without refreshing the page.

    - search (string; optional):
        search in window.location - e.g., "?myargument=1".'''
    available_properties: Incomplete
    available_wildcard_properties: Incomplete
    def __init__(self, id=..., pathname=..., search=..., hash=..., href=..., refresh=..., **kwargs) -> None: ...
