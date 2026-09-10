from _typeshed import Incomplete
from dash.development.base_component import Component as Component

class Interval(Component):
    '''An Interval component.
    A component that repeatedly increments a counter `n_intervals`
    with a fixed time delay between each increment.
    Interval is good for triggering a component on a recurring basis.
    The time delay is set with the property "interval" in milliseconds.

    Keyword arguments:

    - id (string; optional):
        The ID of this component, used to identify dash components in
        callbacks. The ID needs to be unique across all of the components
        in an app.

    - disabled (boolean; optional):
        If True, the counter will no longer update.

    - interval (number; default 1000):
        This component will increment the counter `n_intervals` every
        `interval` milliseconds.

    - max_intervals (number; default -1):
        Number of times the interval will be fired. If -1, then the
        interval has no limit (the default) and if 0 then the interval
        stops running.

    - n_intervals (number; default 0):
        Number of times the interval has passed.'''
    available_properties: Incomplete
    available_wildcard_properties: Incomplete
    def __init__(self, id=..., interval=..., disabled=..., n_intervals=..., max_intervals=..., **kwargs) -> None: ...
