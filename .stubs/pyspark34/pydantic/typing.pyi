from .fields import ModelField
from _typeshed import Incomplete
from os import PathLike
from typing import AbstractSet, Any, Callable as TypingCallable, Dict, ForwardRef, Generator, Iterable, List, Mapping, Sequence, Set, Tuple, Type, _Final as typing_base

__all__ = ['AnyCallable', 'NoArgAnyCallable', 'NoneType', 'is_none_type', 'display_as_type', 'resolve_annotations', 'is_callable_type', 'is_literal_type', 'all_literal_values', 'is_namedtuple', 'is_typeddict', 'is_typeddict_special', 'is_new_type', 'new_type_supertype', 'is_classvar', 'is_finalvar', 'update_field_forward_refs', 'update_model_forward_refs', 'TupleGenerator', 'DictStrAny', 'DictAny', 'SetStr', 'ListStr', 'IntStr', 'AbstractSetIntStr', 'DictIntStrAny', 'CallableGenerator', 'ReprArgs', 'AnyClassMethod', 'CallableGenerator', 'WithArgsTypes', 'get_args', 'get_origin', 'get_sub_types', 'typing_base', 'get_all_type_hints', 'is_union', 'StrPath', 'MappingIntStrAny']

def get_all_type_hints(obj: Any, globalns: Any = None, localns: Any = None) -> Any: ...
AnyCallable = TypingCallable[..., Any]
NoArgAnyCallable: Incomplete

def get_origin(tp: Type[Any]) -> Type[Any] | None:
    """
        We can't directly use `typing.get_origin` since we need a fallback to support
        custom generic classes like `ConstrainedList`
        It should be useless once https://github.com/cython/cython/issues/3537 is
        solved and https://github.com/pydantic/pydantic/pull/1753 is merged.
        """
def get_args(tp: Type[Any]) -> Tuple[Any, ...]:
    """Get type arguments with all substitutions performed.

        For unions, basic simplifications used by Union constructor are performed.
        Examples::
            get_args(Dict[str, int]) == (str, int)
            get_args(int) == ()
            get_args(Union[int, Union[T, int], str][int]) == (int, str)
            get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
            get_args(Callable[[], T][int]) == ([], int)
        """
def is_union(tp: Type[Any] | None) -> bool: ...

WithArgsTypes: Incomplete
StrPath = str | PathLike
TupleGenerator = Generator[Tuple[str, Any], None, None]
DictStrAny = Dict[str, Any]
DictAny = Dict[Any, Any]
SetStr = Set[str]
ListStr = List[str]
IntStr = int | str
AbstractSetIntStr = AbstractSet[IntStr]
DictIntStrAny = Dict[IntStr, Any]
MappingIntStrAny = Mapping[IntStr, Any]
CallableGenerator = Generator[AnyCallable, None, None]
ReprArgs = Sequence[Tuple[str | None, Any]]
AnyClassMethod = classmethod[Any]
NoneType: Incomplete

def is_none_type(type_: Any) -> bool: ...
def display_as_type(v: Type[Any]) -> str: ...
def resolve_annotations(raw_annotations: Dict[str, Type[Any]], module_name: str | None) -> Dict[str, Type[Any]]:
    """
    Partially taken from typing.get_type_hints.

    Resolve string or ForwardRef annotations into type objects if possible.
    """
def is_callable_type(type_: Type[Any]) -> bool: ...
def is_literal_type(type_: Type[Any]) -> bool: ...
def all_literal_values(type_: Type[Any]) -> Tuple[Any, ...]:
    '''
    This method is used to retrieve all Literal values as
    Literal can be used recursively (see https://www.python.org/dev/peps/pep-0586)
    e.g. `Literal[Literal[Literal[1, 2, 3], "foo"], 5, None]`
    '''
def is_namedtuple(type_: Type[Any]) -> bool:
    """
    Check if a given class is a named tuple.
    It can be either a `typing.NamedTuple` or `collections.namedtuple`
    """
def is_typeddict(type_: Type[Any]) -> bool:
    """
    Check if a given class is a typed dict (from `typing` or `typing_extensions`)
    In 3.10, there will be a public method (https://docs.python.org/3.10/library/typing.html#typing.is_typeddict)
    """
def is_typeddict_special(type_: Any) -> bool:
    """
    Check if type is a TypedDict special form (Required or NotRequired).
    """
def is_new_type(type_: Type[Any]) -> bool:
    """
    Check whether type_ was created using typing.NewType
    """
def new_type_supertype(type_: Type[Any]) -> Type[Any]: ...
def is_classvar(ann_type: Type[Any]) -> bool: ...
def is_finalvar(ann_type: Type[Any]) -> bool: ...
def update_field_forward_refs(field: ModelField, globalns: Any, localns: Any) -> None:
    """
    Try to update ForwardRefs on fields based on this ModelField, globalns and localns.
    """
def update_model_forward_refs(model: Type[Any], fields: Iterable['ModelField'], json_encoders: Dict[Type[Any] | str | ForwardRef, AnyCallable], localns: DictStrAny, exc_to_suppress: Tuple[Type[BaseException], ...] = ()) -> None:
    """
    Try to update model fields ForwardRefs based on model and localns.
    """
def get_sub_types(tp: Any) -> List[Any]:
    """
    Return all the types that are allowed by type `tp`
    `tp` can be a `Union` of allowed types or an `Annotated` type
    """
