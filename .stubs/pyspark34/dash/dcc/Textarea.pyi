from _typeshed import Incomplete
from dash.development.base_component import Component as Component

class Textarea(Component):
    """A Textarea component.
    A basic HTML textarea for entering multiline text.

    Keyword arguments:

    - id (string; optional):
        The ID of this component, used to identify dash components in
        callbacks. The ID needs to be unique across all of the components
        in an app.

    - accessKey (string; optional):
        Defines a keyboard shortcut to activate or add focus to the
        element.

    - autoFocus (string; optional):
        The element should be automatically focused after the page loaded.

    - className (string; optional):
        Often used with CSS to style elements with common properties.

    - cols (string | number; optional):
        Defines the number of columns in a textarea.

    - contentEditable (string | boolean; optional):
        Indicates whether the element's content is editable.

    - contextMenu (string; optional):
        Defines the ID of a <menu> element which will serve as the
        element's context menu.

    - dir (string; optional):
        Defines the text direction. Allowed values are ltr (Left-To-Right)
        or rtl (Right-To-Left).

    - disabled (string | boolean; optional):
        Indicates whether the user can interact with the element.

    - draggable (a value equal to: 'true', 'false' | boolean; optional):
        Defines whether the element can be dragged.

    - form (string; optional):
        Indicates the form that is the owner of the element.

    - hidden (string; optional):
        Prevents rendering of given element, while keeping child elements,
        e.g. script elements, active.

    - lang (string; optional):
        Defines the language used in the element.

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

    - maxLength (string | number; optional):
        Defines the maximum number of characters allowed in the element.

    - minLength (string | number; optional):
        Defines the minimum number of characters allowed in the element.

    - n_blur (number; default 0):
        Number of times the textarea lost focus.

    - n_blur_timestamp (number; default -1):
        Last time the textarea lost focus.

    - n_clicks (number; default 0):
        Number of times the textarea has been clicked.

    - n_clicks_timestamp (number; default -1):
        Last time the textarea was clicked.

    - name (string; optional):
        Name of the element. For example used by the server to identify
        the fields in form submits.

    - persisted_props (list of a value equal to: 'value's; default ['value']):
        Properties whose user interactions will persist after refreshing
        the component or the page. Since only `value` is allowed this prop
        can normally be ignored.

    - persistence (boolean | string | number; optional):
        Used to allow user interactions in this component to be persisted
        when the component - or the page - is refreshed. If `persisted` is
        truthy and hasn't changed from its previous value, a `value` that
        the user has changed while using the app will keep that change, as
        long as the new `value` also matches what was given originally.
        Used in conjunction with `persistence_type`.

    - persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
        Where persisted user changes will be stored: memory: only kept in
        memory, reset on page refresh. local: window.localStorage, data is
        kept after the browser quit. session: window.sessionStorage, data
        is cleared once the browser quit.

    - placeholder (string; optional):
        Provides a hint to the user of what can be entered in the field.

    - readOnly (boolean | a value equal to: 'readOnly', 'readonly', 'READONLY'; optional):
        Indicates whether the element can be edited. readOnly is an HTML
        boolean attribute - it is enabled by a boolean or 'readOnly'.
        Alternative capitalizations `readonly` & `READONLY` are also
        acccepted.

    - required (a value equal to: 'required', 'REQUIRED' | boolean; optional):
        Indicates whether this element is required to fill out or not.
        required is an HTML boolean attribute - it is enabled by a boolean
        or 'required'. Alternative capitalizations `REQUIRED` are also
        acccepted.

    - rows (string | number; optional):
        Defines the number of rows in a text area.

    - spellCheck (a value equal to: 'true', 'false' | boolean; optional):
        Indicates whether spell checking is allowed for the element.

    - style (dict; optional):
        Defines CSS styles which will override styles previously set.

    - tabIndex (string | number; optional):
        Overrides the browser's default tab order and follows the one
        specified instead.

    - title (string; optional):
        Text to be displayed in a tooltip when hovering over the element.

    - value (string; optional):
        The value of the textarea.

    - wrap (string; optional):
        Indicates whether the text should be wrapped."""
    available_properties: Incomplete
    available_wildcard_properties: Incomplete
    def __init__(self, id=..., value=..., autoFocus=..., cols=..., disabled=..., form=..., maxLength=..., minLength=..., name=..., placeholder=..., readOnly=..., required=..., rows=..., wrap=..., accessKey=..., className=..., contentEditable=..., contextMenu=..., dir=..., draggable=..., hidden=..., lang=..., spellCheck=..., style=..., tabIndex=..., title=..., n_blur=..., n_blur_timestamp=..., n_clicks=..., n_clicks_timestamp=..., loading_state=..., persistence=..., persisted_props=..., persistence_type=..., **kwargs) -> None: ...
