from _typeshed import Incomplete
from collections.abc import Generator
from jedi import debug as debug, settings as settings
from jedi.inference import recursion as recursion
from jedi.inference.base_value import HelperValueMixin as HelperValueMixin, NO_VALUES as NO_VALUES, ValueSet as ValueSet, ValueWrapper as ValueWrapper
from jedi.inference.cache import inference_state_method_cache as inference_state_method_cache
from jedi.inference.helpers import infer_call_of_leaf as infer_call_of_leaf
from jedi.inference.lazy_value import LazyKnownValues as LazyKnownValues

def check_array_additions(context, sequence):
    """ Just a mapper function for the internal _internal_check_array_additions """
def get_dynamic_array_instance(instance, arguments):
    """Used for set() and list() instances."""

class _DynamicArrayAdditions(HelperValueMixin):
    """
    Used for the usage of set() and list().
    This is definitely a hack, but a good one :-)
    It makes it possible to use set/list conversions.

    This is not a proper context, because it doesn't have to be. It's not used
    in the wild, it's just used within typeshed as an argument to `__init__`
    for set/list and never used in any other place.
    """
    def __init__(self, instance, arguments) -> None: ...
    def py__class__(self): ...
    def py__iter__(self, contextualized_node: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]: ...
    def iterate(self, contextualized_node: Incomplete | None = None, is_async: bool = False): ...

class _Modification(ValueWrapper):
    def __init__(self, wrapped_value, assigned_values, contextualized_key) -> None: ...
    def py__getitem__(self, *args, **kwargs): ...
    def py__simple_getitem__(self, index): ...

class DictModification(_Modification):
    def py__iter__(self, contextualized_node: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]: ...
    def get_key_values(self): ...

class ListModification(_Modification):
    def py__iter__(self, contextualized_node: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]: ...
