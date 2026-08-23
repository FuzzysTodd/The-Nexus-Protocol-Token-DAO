from . import exceptions as exceptions
from ._utils import AttributeDict as AttributeDict
from _typeshed import Incomplete

context_value: Incomplete

def has_context(func): ...

class FalsyList(list):
    def __bool__(self) -> bool: ...
    def __nonzero__(self): ...

falsy_triggered: Incomplete

class CallbackContext:
    @property
    def inputs(self): ...
    @property
    def states(self): ...
    @property
    def triggered(self):
        """
        Returns a list of all the Input props that changed and caused the callback to execute. It is empty when the
        callback is called on initial load, unless an Input prop got its value from another initial callback.
        Callbacks triggered by user actions typically have one item in triggered, unless the same action changes
        two props at once or the callback has several Input props that are all modified by another callback based on
        a single user action.

        Example:  To get the id of the component that triggered the callback:
        `component_id = ctx.triggered[0]['prop_id'].split('.')[0]`

        Example:  To detect initial call, empty triggered is not really empty, it's falsy so that you can use:
        `if ctx.triggered:`
        """
    @property
    def triggered_prop_ids(self):
        '''
        Returns a dictionary of all the Input props that changed and caused the callback to execute. It is empty when
        the callback is called on initial load, unless an Input prop got its value from another initial callback.
        Callbacks triggered by user actions typically have one item in triggered, unless the same action changes
        two props at once or the callback has several Input props that are all modified by another callback based
        on a single user action.

        triggered_prop_ids (dict):
        - keys (str) : the triggered "prop_id" composed of "component_id.component_property"
        - values (str or dict): the id of the component that triggered the callback. Will be the dict id for pattern matching callbacks

        Example - regular callback
        {"btn-1.n_clicks": "btn-1"}

        Example - pattern matching callbacks:
        {\'{"index":0,"type":"filter-dropdown"}.value\': {"index":0,"type":"filter-dropdown"}}

        Example usage:
        `if "btn-1.n_clicks" in ctx.triggered_prop_ids:
            do_something()`
        '''
    @property
    def triggered_id(self):
        '''
        Returns the component id (str or dict) of the Input component that triggered the callback.

        Note - use `triggered_prop_ids` if you need both the component id and the prop that triggered the callback or if
        multiple Inputs triggered the callback.

        Example usage:
        `if "btn-1" == ctx.triggered_id:
            do_something()`

        '''
    @property
    def args_grouping(self):
        '''
        args_grouping is a dict of the inputs used with flexible callback signatures. The keys are the variable names
        and the values are dictionaries containing:
        - “id”: (string or dict) the component id. If it’s a pattern matching id, it will be a dict.
        - “id_str”: (str) for pattern matching ids, it’s the stringified dict id with no white spaces.
        - “property”: (str) The component property used in the callback.
        - “value”: the value of the component property at the time the callback was fired.
        - “triggered”: (bool)Whether this input triggered the callback.

        Example usage:
        @app.callback(
            Output("container", "children"),
            inputs=dict(btn1=Input("btn-1", "n_clicks"), btn2=Input("btn-2", "n_clicks")),
        )
        def display(btn1, btn2):
            c = ctx.args_grouping
            if c.btn1.triggered:
                return f"Button 1 clicked {btn1} times"
            elif c.btn2.triggered:
                return f"Button 2 clicked {btn2} times"
            else:
               return "No clicks yet"

        '''
    @property
    def outputs_grouping(self): ...
    @property
    def outputs_list(self): ...
    @property
    def inputs_list(self): ...
    @property
    def states_list(self): ...
    @property
    def response(self): ...
    @staticmethod
    def record_timing(name, duration: Incomplete | None = None, description: Incomplete | None = None) -> None:
        """Records timing information for a server resource.

        :param name: The name of the resource.
        :type name: string

        :param duration: The time in seconds to report. Internally, this
            is rounded to the nearest millisecond.
        :type duration: float or None

        :param description: A description of the resource.
        :type description: string or None
        """
    @property
    def using_args_grouping(self):
        """
        Return True if this callback is using dictionary or nested groupings for
        Input/State dependencies, or if Input and State dependencies are interleaved
        """
    @property
    def using_outputs_grouping(self):
        """
        Return True if this callback is using dictionary or nested groupings for
        Output dependencies.
        """
    @property
    def timing_information(self): ...

callback_context: Incomplete
