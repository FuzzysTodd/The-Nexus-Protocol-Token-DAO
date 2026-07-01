from ._grouping import flatten_grouping as flatten_grouping, make_grouping_by_index as make_grouping_by_index
from ._validate import validate_callback as validate_callback
from _typeshed import Incomplete
from dash.development.base_component import Component as Component

class _Wildcard:
    def __init__(self, name) -> None: ...
    def to_json(self): ...

MATCH: Incomplete
ALL: Incomplete
ALLSMALLER: Incomplete

class DashDependency:
    component_id: Incomplete
    component_property: Incomplete
    allow_duplicate: bool
    def __init__(self, component_id, component_property) -> None: ...
    def component_id_str(self): ...
    def to_dict(self): ...
    def __eq__(self, other):
        '''
        We use "==" to denote two deps that refer to the same prop on
        the same component. In the case of wildcard deps, this means
        the same prop on *at least one* of the same components.
        '''
    def __hash__(self): ...
    def has_wildcard(self):
        """
        Return true if id contains a wildcard (MATCH, ALL, or ALLSMALLER)
        """

class Output(DashDependency):
    """Output of a callback."""
    allowed_wildcards: Incomplete
    allow_duplicate: Incomplete
    def __init__(self, component_id, component_property, allow_duplicate: bool = False) -> None: ...

class Input(DashDependency):
    """Input of callback: trigger an update when it is updated."""
    allowed_wildcards: Incomplete

class State(DashDependency):
    """Use the value of a State in a callback but don't trigger updates."""
    allowed_wildcards: Incomplete

class ClientsideFunction:
    namespace: Incomplete
    function_name: Incomplete
    def __init__(self, namespace: Incomplete | None = None, function_name: Incomplete | None = None) -> None: ...

def extract_grouped_output_callback_args(args, kwargs): ...
def extract_grouped_input_state_callback_args_from_kwargs(kwargs): ...
def extract_grouped_input_state_callback_args_from_args(args): ...
def extract_grouped_input_state_callback_args(args, kwargs): ...
def compute_input_state_grouping_indices(input_state_grouping): ...
def handle_grouped_callback_args(args, kwargs):
    """Split args into outputs, inputs and states"""
def extract_callback_args(args, kwargs, name, type_):
    """Extract arguments for callback from a name and type"""
def handle_callback_args(args, kwargs):
    """Split args into outputs, inputs and states"""
