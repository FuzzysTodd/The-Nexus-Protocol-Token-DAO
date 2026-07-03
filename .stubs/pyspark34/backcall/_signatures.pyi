from _typeshed import Incomplete

__all__ = ['BoundArguments', 'Parameter', 'Signature', 'signature']

def signature(obj):
    """Get a signature object for the passed callable."""

class _void:
    """A private marker - used in Parameter & Signature"""
class _empty: ...

class _ParameterKind(int):
    def __new__(self, *args, **kwargs): ...

class Parameter:
    """Represents a parameter in a function signature.

    Has the following public attributes:

    * name : str
        The name of the parameter as a string.
    * default : object
        The default value for the parameter if specified.  If the
        parameter has no default value, this attribute is not set.
    * annotation
        The annotation for the parameter if specified.  If the
        parameter has no annotation, this attribute is not set.
    * kind : str
        Describes how argument values are bound to the parameter.
        Possible values: `Parameter.POSITIONAL_ONLY`,
        `Parameter.POSITIONAL_OR_KEYWORD`, `Parameter.VAR_POSITIONAL`,
        `Parameter.KEYWORD_ONLY`, `Parameter.VAR_KEYWORD`.
    """
    POSITIONAL_ONLY: Incomplete
    POSITIONAL_OR_KEYWORD: Incomplete
    VAR_POSITIONAL: Incomplete
    KEYWORD_ONLY: Incomplete
    VAR_KEYWORD: Incomplete
    empty: Incomplete
    def __init__(self, name, kind, default=..., annotation=..., _partial_kwarg: bool = False) -> None: ...
    @property
    def name(self): ...
    @property
    def default(self): ...
    @property
    def annotation(self): ...
    @property
    def kind(self): ...
    def replace(self, name=..., kind=..., annotation=..., default=..., _partial_kwarg=...):
        """Creates a customized copy of the Parameter."""
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class BoundArguments:
    """Result of `Signature.bind` call.  Holds the mapping of arguments
    to the function's parameters.

    Has the following public attributes:

    * arguments : OrderedDict
        An ordered mutable mapping of parameters' names to arguments' values.
        Does not contain arguments' default values.
    * signature : Signature
        The Signature object that created this instance.
    * args : tuple
        Tuple of positional arguments values.
    * kwargs : dict
        Dict of keyword arguments values.
    """
    arguments: Incomplete
    def __init__(self, signature, arguments) -> None: ...
    @property
    def signature(self): ...
    @property
    def args(self): ...
    @property
    def kwargs(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class Signature:
    """A Signature object represents the overall signature of a function.
    It stores a Parameter object for each parameter accepted by the
    function, as well as information specific to the function itself.

    A Signature object has the following public attributes and methods:

    * parameters : OrderedDict
        An ordered mapping of parameters' names to the corresponding
        Parameter objects (keyword-only arguments are in the same order
        as listed in `code.co_varnames`).
    * return_annotation : object
        The annotation for the return type of the function if specified.
        If the function has no annotation for its return type, this
        attribute is not set.
    * bind(*args, **kwargs) -> BoundArguments
        Creates a mapping from positional and keyword arguments to
        parameters.
    * bind_partial(*args, **kwargs) -> BoundArguments
        Creates a partial mapping from positional and keyword arguments
        to parameters (simulating 'functools.partial' behavior.)
    """
    empty: Incomplete
    def __init__(self, parameters: Incomplete | None = None, return_annotation=..., __validate_parameters__: bool = True) -> None:
        """Constructs Signature from the given list of Parameter
        objects and 'return_annotation'.  All arguments are optional.
        """
    @classmethod
    def from_function(cls, func):
        """Constructs Signature for the given python function"""
    @property
    def parameters(self): ...
    @property
    def return_annotation(self): ...
    def replace(self, parameters=..., return_annotation=...):
        """Creates a customized copy of the Signature.
        Pass 'parameters' and/or 'return_annotation' arguments
        to override them in the new copy.
        """
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def bind(self, *args, **kwargs):
        """Get a BoundArguments object, that maps the passed `args`
        and `kwargs` to the function's signature.  Raises `TypeError`
        if the passed arguments can not be bound.
        """
    def bind_partial(self, *args, **kwargs):
        """Get a BoundArguments object, that partially maps the
        passed `args` and `kwargs` to the function's signature.
        Raises `TypeError` if the passed arguments can not be bound.
        """
