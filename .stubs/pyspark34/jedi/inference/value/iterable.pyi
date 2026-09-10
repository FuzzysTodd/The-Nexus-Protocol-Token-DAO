from _typeshed import Incomplete
from collections.abc import Generator as _Generator
from jedi.inference import analysis as analysis, compiled as compiled
from jedi.inference.base_value import ContextualizedNode as ContextualizedNode, LazyValueWrapper as LazyValueWrapper, NO_VALUES as NO_VALUES, Value as Value, ValueSet as ValueSet, iterate_values as iterate_values, sentinel as sentinel
from jedi.inference.cache import inference_state_method_cache as inference_state_method_cache
from jedi.inference.context import CompForContext as CompForContext
from jedi.inference.filters import LazyAttributeOverwrite as LazyAttributeOverwrite, publish_method as publish_method
from jedi.inference.helpers import SimpleGetItemNotFound as SimpleGetItemNotFound, get_int_or_none as get_int_or_none, is_string as is_string, reraise_getitem_errors as reraise_getitem_errors
from jedi.inference.lazy_value import LazyKnownValue as LazyKnownValue, LazyKnownValues as LazyKnownValues, LazyTreeValue as LazyTreeValue
from jedi.inference.utils import safe_property as safe_property, to_list as to_list
from jedi.inference.value.dynamic_arrays import check_array_additions as check_array_additions
from jedi.parser_utils import get_sync_comp_fors as get_sync_comp_fors

class IterableMixin:
    def py__next__(self, contextualized_node: Incomplete | None = None): ...
    def py__stop_iteration_returns(self): ...
    get_safe_value: Incomplete

class GeneratorBase(LazyAttributeOverwrite, IterableMixin):
    array_type: Incomplete
    def py__bool__(self): ...
    def py__stop_iteration_returns(self): ...
    @property
    def name(self): ...
    def get_annotated_class_object(self): ...

class Generator(GeneratorBase):
    """Handling of `yield` functions."""
    def __init__(self, inference_state, func_execution_context) -> None: ...
    def py__iter__(self, contextualized_node: Incomplete | None = None): ...
    def py__stop_iteration_returns(self): ...

def comprehension_from_atom(inference_state, value, atom): ...

class ComprehensionMixin:
    def py__iter__(self, contextualized_node: Incomplete | None = None) -> _Generator[Incomplete, None, None]: ...

class _DictMixin: ...

class Sequence(LazyAttributeOverwrite, IterableMixin):
    api_type: str
    @property
    def name(self): ...
    def py__bool__(self) -> None: ...
    def parent(self): ...
    def py__getitem__(self, index_value_set, contextualized_node): ...

class _BaseComprehension(ComprehensionMixin):
    def __init__(self, inference_state, defining_context, sync_comp_for_node, entry_node) -> None: ...

class ListComprehension(_BaseComprehension, Sequence):
    array_type: str
    def py__simple_getitem__(self, index): ...

class SetComprehension(_BaseComprehension, Sequence):
    array_type: str

class GeneratorComprehension(_BaseComprehension, GeneratorBase): ...

class _DictKeyMixin:
    def get_mapping_item_values(self): ...
    def get_key_values(self): ...

class DictComprehension(ComprehensionMixin, Sequence, _DictKeyMixin):
    array_type: str
    def __init__(self, inference_state, defining_context, sync_comp_for_node, key_node, value_node) -> None: ...
    def py__iter__(self, contextualized_node: Incomplete | None = None) -> _Generator[Incomplete, None, None]: ...
    def py__simple_getitem__(self, index): ...
    def exact_key_items(self): ...

class SequenceLiteralValue(Sequence):
    mapping: Incomplete
    atom: Incomplete
    array_type: str
    def __init__(self, inference_state, defining_context, atom) -> None: ...
    def py__simple_getitem__(self, index):
        """Here the index is an int/str. Raises IndexError/KeyError."""
    def py__iter__(self, contextualized_node: Incomplete | None = None) -> _Generator[Incomplete, Incomplete, None]:
        """
        While values returns the possible values for any array field, this
        function returns the value for a certain index.
        """
    def py__len__(self): ...
    def get_tree_entries(self): ...

class DictLiteralValue(_DictMixin, SequenceLiteralValue, _DictKeyMixin):
    array_type: str
    atom: Incomplete
    def __init__(self, inference_state, defining_context, atom) -> None: ...
    def py__simple_getitem__(self, index):
        """Here the index is an int/str. Raises IndexError/KeyError."""
    def py__iter__(self, contextualized_node: Incomplete | None = None) -> _Generator[Incomplete, None, None]:
        """
        While values returns the possible values for any array field, this
        function returns the value for a certain index.
        """
    def exact_key_items(self) -> _Generator[Incomplete, None, None]:
        """
        Returns a generator of tuples like dict.items(), where the key is
        resolved (as a string) and the values are still lazy values.
        """

class _FakeSequence(Sequence):
    def __init__(self, inference_state, lazy_value_list) -> None:
        '''
        type should be one of "tuple", "list"
        '''
    def py__simple_getitem__(self, index): ...
    def py__iter__(self, contextualized_node: Incomplete | None = None): ...
    def py__bool__(self): ...

class FakeTuple(_FakeSequence):
    array_type: str

class FakeList(_FakeSequence):
    array_type: str

class FakeDict(_DictMixin, Sequence, _DictKeyMixin):
    array_type: str
    def __init__(self, inference_state, dct) -> None: ...
    def py__iter__(self, contextualized_node: Incomplete | None = None) -> _Generator[Incomplete, None, None]: ...
    def py__simple_getitem__(self, index): ...
    def exact_key_items(self): ...

class MergedArray(Sequence):
    array_type: Incomplete
    def __init__(self, inference_state, arrays) -> None: ...
    def py__iter__(self, contextualized_node: Incomplete | None = None) -> _Generator[Incomplete, Incomplete, None]: ...
    def py__simple_getitem__(self, index): ...

def unpack_tuple_to_dict(context, types, exprlist):
    """
    Unpacking tuple assignments in for statements and expr_stmts.
    """

class Slice(LazyValueWrapper):
    inference_state: Incomplete
    def __init__(self, python_context, start, stop, step) -> None: ...
    def get_safe_value(self, default=...):
        """
        Imitate CompiledValue.obj behavior and return a ``builtin.slice()``
        object.
        """
