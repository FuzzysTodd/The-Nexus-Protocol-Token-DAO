import abc
from typing import Any, Dict, List, Type, TypeVar

__all__ = ['trace', 'dump', 'load', 'PayloadTooLarge', 'Translatable', 'Traceable', 'is_traceable', 'is_wrapped_with_trace']

T = TypeVar('T')

class PayloadTooLarge(Exception): ...

class Traceable:
    """
    A traceable object have copy and dict. Copy and mutate are used to copy the object for further mutations.
    Dict returns a TraceDictType to enable serialization.
    """
    def trace_copy(self) -> Traceable:
        '''
        Perform a shallow copy.
        NOTE: NONE of the attributes will be preserved.
        This is the one that should be used when you want to "mutate" a serializable object.
        '''
    @property
    def trace_symbol(self) -> Any:
        """
        Symbol object. Could be a class or a function.
        ``get_hybrid_cls_or_func_name`` and ``import_cls_or_func_from_hybrid_name`` is a pair to
        convert the symbol into a string and convert the string back to symbol.
        """
    @property
    def trace_args(self) -> List[Any]:
        """
        List of positional arguments passed to symbol. Usually empty if ``kw_only`` is true,
        in which case all the positional arguments are converted into keyword arguments.
        """
    @property
    def trace_kwargs(self) -> Dict[str, Any]:
        """
        Dict of keyword arguments.
        """
    def get(self) -> Any:
        """
        Get the original object. Usually used together with ``trace_copy``.
        """

class Translatable(abc.ABC, metaclass=abc.ABCMeta):
    """
    Inherit this class and implement ``translate`` when the wrapped class needs a different
    parameter from the wrapper class in its init function.
    """

def is_traceable(obj: Any) -> bool:
    '''
    Check whether an object is a traceable instance or type.

    Note that an object is traceable only means that it implements the "Traceable" interface,
    and the properties have been implemented. It doesn\'t necessary mean that its type is wrapped with trace,
    because the properties could be added **after** the instance has been created.
    '''
def is_wrapped_with_trace(cls_or_func: Any) -> bool:
    '''
    Check whether a function or class is already wrapped with ``@nni.trace``.
    If a class or function is already wrapped with trace, then the created object must be "traceable".
    '''

class SerializableObject(Traceable):
    """
    Serializable object is a wrapper of existing python objects, that supports dump and load easily.
    Stores a symbol ``s`` and a dict of arguments ``args``, and the object can be restored with ``s(**args)``.
    """
    def __init__(self, symbol: Type, args: List[Any], kwargs: Dict[str, Any], call_super: bool = False) -> None: ...
    def trace_copy(self) -> SerializableObject: ...
    def get(self) -> Any: ...
    @property
    def trace_symbol(self) -> Any: ...
    @trace_symbol.setter
    def trace_symbol(self, symbol: Any) -> None: ...
    @property
    def trace_args(self) -> List[Any]: ...
    @trace_args.setter
    def trace_args(self, args: List[Any]): ...
    @property
    def trace_kwargs(self) -> Dict[str, Any]: ...
    @trace_kwargs.setter
    def trace_kwargs(self, kwargs: Dict[str, Any]): ...

def trace(cls_or_func: T = ..., *, kw_only: bool = True, inheritable: bool = False) -> T:
    '''
    Annotate a function or a class if you want to preserve where it comes from.
    This is usually used in the following scenarios:

    1) Care more about execution configuration rather than results, which is usually the case in AutoML. For example,
       you want to mutate the parameters of a function.
    2) Repeat execution is not an issue (e.g., reproducible, execution is fast without side effects).

    When a class/function is annotated, all the instances/calls will return a object as it normally will.
    Although the object might act like a normal object, it\'s actually a different object with NNI-specific properties.
    One exception is that if your function returns None, it will return an empty traceable object instead,
    which should raise your attention when you want to check whether the None ``is None``.

    When parameters of functions are received, it is first stored, and then a shallow copy will be passed to wrapped function/class.
    This is to prevent mutable objects gets modified in the wrapped function/class.
    When the function finished execution, we also record extra information about where this object comes from.
    That\'s why it\'s called "trace".
    When call ``nni.dump``, that information will be used, by default.

    If ``kw_only`` is true, try to convert all parameters into kwargs type. This is done by inspecting the argument
    list and types. This can be useful to extract semantics, but can be tricky in some corner cases.
    Therefore, in some cases, some positional arguments will still be kept.

    If ``inheritable`` is true, the trace information from superclass will also be available in subclass.
    This however, will make the subclass un-trace-able. Note that this argument has no effect when tracing functions.

    .. warning::

        Generators will be first expanded into a list, and the resulting list will be further passed into the wrapped function/class.
        This might hang when generators produce an infinite sequence. We might introduce an API to control this behavior in future.

    Example:

    .. code-block:: python

        @nni.trace
        def foo(bar):
            pass
    '''
def dump(obj: Any, fp: Any | None = None, *, use_trace: bool = True, pickle_size_limit: int = 4096, allow_nan: bool = True, **json_tricks_kwargs) -> str:
    """
    Convert a nested data structure to a json string. Save to file if fp is specified.
    Use json-tricks as main backend. For unhandled cases in json-tricks, use cloudpickle.
    The serializer is not designed for long-term storage use, but rather to copy data between processes.
    The format is also subject to change between NNI releases.

    To compress the payload, please use :func:`dump_bytes`.

    Parameters
    ----------
    obj : any
        The object to dump.
    fp : file handler or path
        File to write to. Keep it none if you want to dump a string.
    pickle_size_limit : int
        This is set to avoid too long serialization result. Set to -1 to disable size check.
    allow_nan : bool
        Whether to allow nan to be serialized. Different from default value in json-tricks, our default value is true.
    json_tricks_kwargs : dict
        Other keyword arguments passed to json tricks (backend), e.g., indent=2.

    Returns
    -------
    str or bytes
        Normally str. Sometimes bytes (if compressed).
    """
def load(string: str | None = None, *, fp: Any | None = None, preserve_order: bool = False, ignore_comments: bool = True, **json_tricks_kwargs) -> Any:
    """
    Load the string or from file, and convert it to a complex data structure.
    At least one of string or fp has to be not none.

    Parameters
    ----------
    string : str
        JSON string to parse. Can be set to none if fp is used.
    fp : str
        File path to load JSON from. Can be set to none if string is used.
    preserve_order : bool
        `json_tricks parameter <https://json-tricks.readthedocs.io/en/latest/#order>`_
        to use ``OrderedDict`` instead of ``dict``.
        The order is in fact always preserved even when this is False.
    ignore_comments : bool
        Remove comments (starting with ``#`` or ``//``). Default is true.

    Returns
    -------
    any
        The loaded object.
    """

class _unwrap_metaclass(type):
    def __new__(cls, name, bases, dct): ...
    def __subclasscheck__(cls, subclass): ...
    def __instancecheck__(cls, instance): ...

class _pickling_object:
    def __new__(cls, type_, kw_only, data): ...
