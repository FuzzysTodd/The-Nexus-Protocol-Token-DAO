from _typeshed import Incomplete
from jedi.inference.base_value import LazyValueWrapper as LazyValueWrapper
from jedi.inference.compiled.value import CompiledName as CompiledName, CompiledValue as CompiledValue, CompiledValueFilter as CompiledValueFilter, CompiledValueName as CompiledValueName, create_from_access_path as create_from_access_path

def builtin_from_name(inference_state, string): ...

class ExactValue(LazyValueWrapper):
    '''
    This class represents exact values, that makes operations like additions
    and exact boolean values possible, while still being a "normal" stub.
    '''
    inference_state: Incomplete
    def __init__(self, compiled_value) -> None: ...
    def __getattribute__(self, name): ...

def create_simple_object(inference_state, obj):
    """
    Only allows creations of objects that are easily picklable across Python
    versions.
    """
def get_string_value_set(inference_state): ...
def load_module(inference_state, dotted_name, **kwargs): ...
