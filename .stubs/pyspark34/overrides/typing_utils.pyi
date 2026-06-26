import typing

__all__ = ['issubtype', 'get_origin', 'get_args', 'get_type_hints']

get_type_hints = typing.get_type_hints

def get_origin(type_):
    """Get the unsubscripted version of a type.
    This supports generic types, Callable, Tuple, Union, Literal, Final and ClassVar.
    Return None for unsupported types.

    Examples:

    ```python
        from typing_utils import get_origin

        get_origin(Literal[42]) is Literal
        get_origin(int) is None
        get_origin(ClassVar[int]) is ClassVar
        get_origin(Generic) is Generic
        get_origin(Generic[T]) is Generic
        get_origin(Union[T, int]) is Union
        get_origin(List[Tuple[T, T]][int]) == list
    ```
    """
def get_args(type_) -> typing.Tuple:
    """Get type arguments with all substitutions performed.
    For unions, basic simplifications used by Union constructor are performed.

    Examples:

    ```python
        from typing_utils import get_args

        get_args(Dict[str, int]) == (str, int)
        get_args(int) == ()
        get_args(Union[int, Union[T, int], str][int]) == (int, str)
        get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
        get_args(Callable[[], T][int]) == ([], int)
    ```
    """

class NormalizedType(typing.NamedTuple):
    """
    Normalized type, made it possible to compare, hash between types.
    """
    origin: Type
    args: tuple | frozenset = ...
    def __eq__(self, other): ...
    def __hash__(self) -> int: ...

def issubtype(left: Type, right: Type, forward_refs: dict | None = None) -> bool | None:
    '''Check that the left argument is a subtype of the right.
    For unions, check if the type arguments of the left is a subset of the right.
    Also works for nested types including ForwardRefs.

    Examples:

    ```python
        from typing_utils import issubtype

        issubtype(typing.List, typing.Any) == True
        issubtype(list, list) == True
        issubtype(list, typing.List) == True
        issubtype(list, typing.Sequence) == True
        issubtype(typing.List[int], list) == True
        issubtype(typing.List[typing.List], list) == True
        issubtype(list, typing.List[int]) == False
        issubtype(list, typing.Union[typing.Tuple, typing.Set]) == False
        issubtype(typing.List[typing.List], typing.List[typing.Sequence]) == True
        JSON = typing.Union[
            int, float, bool, str, None, typing.Sequence["JSON"],
            typing.Mapping[str, "JSON"]
        ]
        issubtype(str, JSON, forward_refs={\'JSON\': JSON}) == True
        issubtype(typing.Dict[str, str], JSON, forward_refs={\'JSON\': JSON}) == True
        issubtype(typing.Dict[str, bytes], JSON, forward_refs={\'JSON\': JSON}) == False
    ```
    '''
