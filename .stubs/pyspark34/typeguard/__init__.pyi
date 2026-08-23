from _typeshed import Incomplete
from enum import Enum
from typing import Any, AsyncGenerator, Callable, Dict, Generator, Sequence, TextIO, TypeVar, overload

__all__ = ['ForwardRefPolicy', 'TypeHintWarning', 'typechecked', 'check_return_type', 'check_argument_types', 'check_type', 'TypeWarning', 'TypeChecker', 'typeguard_ignore']

def typeguard_ignore(f: _F) -> _F:
    """This decorator is a noop during static type-checking."""
T_CallableOrType = TypeVar('T_CallableOrType', bound=Callable[..., Any])

class ForwardRefPolicy(Enum):
    """Defines how unresolved forward references are handled."""
    ERROR: int
    WARN: int
    GUESS: int

class TypeHintWarning(UserWarning):
    """
    A warning that is emitted when a type hint in string form could not be resolved to an actual
    type.
    """

class _TypeCheckMemo:
    globals: Incomplete
    locals: Incomplete
    def __init__(self, globals: Dict[str, Any], locals: Dict[str, Any]) -> None: ...

class _CallMemo(_TypeCheckMemo):
    func: Incomplete
    func_name: Incomplete
    is_generator: Incomplete
    arguments: Incomplete
    type_hints: Incomplete
    def __init__(self, func: Callable, frame_locals: Dict[str, Any] | None = None, args: tuple = None, kwargs: Dict[str, Any] = None, forward_refs_policy=...) -> None: ...

def check_type(argname: str, value, expected_type, memo: _TypeCheckMemo | None = None, *, globals: Dict[str, Any] | None = None, locals: Dict[str, Any] | None = None) -> None:
    """
    Ensure that ``value`` matches ``expected_type``.

    The types from the :mod:`typing` module do not support :func:`isinstance` or :func:`issubclass`
    so a number of type specific checks are required. This function knows which checker to call
    for which type.

    :param argname: name of the argument to check; used for error messages
    :param value: value to be checked against ``expected_type``
    :param expected_type: a class or generic type instance
    :param globals: dictionary of global variables to use for resolving forward references
        (defaults to the calling frame's globals)
    :param locals: dictionary of local variables to use for resolving forward references
        (defaults to the calling frame's locals)
    :raises TypeError: if there is a type mismatch

    """
def check_return_type(retval, memo: _CallMemo | None = None) -> bool:
    """
    Check that the return value is compatible with the return value annotation in the function.

    :param retval: the value about to be returned from the call
    :return: ``True``
    :raises TypeError: if there is a type mismatch

    """
def check_argument_types(memo: _CallMemo | None = None) -> bool:
    """
    Check that the argument values match the annotated types.

    Unless both ``args`` and ``kwargs`` are provided, the information will be retrieved from
    the previous stack frame (ie. from the function that called this).

    :return: ``True``
    :raises TypeError: if there is an argument type mismatch

    """

class TypeCheckedGenerator:
    def __init__(self, wrapped: Generator, memo: _CallMemo) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    def __getattr__(self, name: str) -> Any: ...
    def throw(self, *args): ...
    def close(self) -> None: ...
    def send(self, obj): ...

class TypeCheckedAsyncGenerator:
    def __init__(self, wrapped: AsyncGenerator, memo: _CallMemo) -> None: ...
    def __aiter__(self): ...
    def __anext__(self): ...
    def __getattr__(self, name: str) -> Any: ...
    def athrow(self, *args): ...
    def aclose(self): ...
    async def asend(self, obj): ...

@overload
def typechecked(*, always: bool = False) -> Callable[[T_CallableOrType], T_CallableOrType]: ...
@overload
def typechecked(func: T_CallableOrType, *, always: bool = False) -> T_CallableOrType: ...

class TypeWarning(UserWarning):
    """
    A warning that is emitted when a type check fails.

    :ivar str event: ``call`` or ``return``
    :ivar Callable func: the function in which the violation occurred (the called function if event
        is ``call``, or the function where a value of the wrong type was returned from if event is
        ``return``)
    :ivar str error: the error message contained by the caught :class:`TypeError`
    :ivar frame: the frame in which the violation occurred
    """
    func: Incomplete
    event: Incomplete
    error: Incomplete
    frame: Incomplete
    def __init__(self, memo: _CallMemo | None, event: str, frame, exception: str | TypeError) -> None: ...
    @property
    def stack(self):
        """Return the stack where the last frame is from the target function."""
    def print_stack(self, file: TextIO = None, limit: int = None) -> None:
        """
        Print the traceback from the stack frame where the target function was run.

        :param file: an open file to print to (prints to stdout if omitted)
        :param limit: the maximum number of stack frames to print

        """

class TypeChecker:
    """
    A type checker that collects type violations by hooking into :func:`sys.setprofile`.

    :param packages: list of top level modules and packages or modules to include for type checking
    :param all_threads: ``True`` to check types in all threads created while the checker is
        running, ``False`` to only check in the current one
    :param forward_refs_policy: how to handle unresolvable forward references in annotations

    .. deprecated:: 2.6
       Use :func:`~.importhook.install_import_hook` instead. This class will be removed in v3.0.
    """
    all_threads: Incomplete
    annotation_policy: Incomplete
    def __init__(self, packages: str | Sequence[str], *, all_threads: bool = True, forward_refs_policy: ForwardRefPolicy = ...) -> None: ...
    @property
    def active(self) -> bool:
        """Return ``True`` if currently collecting type violations."""
    def should_check_type(self, func: Callable) -> bool: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def __call__(self, frame, event: str, arg) -> None: ...
