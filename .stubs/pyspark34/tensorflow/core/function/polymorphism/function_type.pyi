import collections
import inspect
from _typeshed import Incomplete
from tensorflow.core.function import trace_type as trace_type
from tensorflow.core.function.polymorphism import function_type_pb2 as function_type_pb2
from tensorflow.core.function.trace_type import serialization as serialization
from tensorflow.python.types import trace as trace
from typing import Any, Callable, Dict, Mapping, Optional, Sequence, Tuple

CAPTURED_DEFAULT_VALUE: Incomplete
PROTO_TO_PY_ENUM: Incomplete
PY_TO_PROTO_ENUM: Incomplete

class Parameter(inspect.Parameter):
    """Represents a parameter to a function."""
    def __init__(self, name: str, kind: Any, optional: bool, type_constraint: Optional[trace.TraceType]) -> None: ...
    @classmethod
    def from_proto(cls, proto: Any) -> Parameter: ...
    def to_proto(self) -> function_type_pb2.Parameter: ...
    @property
    def optional(self) -> bool:
        """If this parameter might not be supplied for a call."""
    @property
    def type_constraint(self) -> Optional[trace.TraceType]:
        """A supertype that the parameter's type must subtype for validity."""
    def is_subtype_of(self, other: Parameter) -> bool:
        """Returns True if self is a supertype of other Parameter."""
    def most_specific_common_supertype(self, others: Sequence['Parameter']) -> Optional['Parameter']:
        """Returns a common supertype (if exists)."""
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self): ...
    def __reduce__(self): ...

class FunctionType(inspect.Signature):
    """Represents the signature of a polymorphic/monomorphic function."""
    def __init__(self, parameters: Sequence[inspect.Parameter], captures: Optional[collections.OrderedDict] = None, **kwargs) -> None: ...
    @property
    def parameters(self) -> Mapping[str, Any]: ...
    @property
    def captures(self) -> collections.OrderedDict: ...
    @classmethod
    def from_callable(cls, obj: Callable[..., Any], *, follow_wrapped: bool = True) -> FunctionType:
        """Generate FunctionType from a python Callable."""
    @classmethod
    def get_default_values(cls, obj: Callable[..., Any], *, follow_wrapped: bool = True) -> Dict[str, Any]:
        """Inspects and returns a dictionary of default values."""
    @classmethod
    def from_proto(cls, proto: Any) -> FunctionType: ...
    def to_proto(self) -> Any: ...
    def bind_with_defaults(self, args, kwargs, default_values):
        """Returns BoundArguments with default values filled in."""
    def is_supertype_of(self, other: FunctionType) -> bool:
        """Returns True if self is a supertype of other FunctionType."""
    def most_specific_common_subtype(self, others: Sequence['FunctionType']) -> Optional['FunctionType']:
        """Returns a common subtype (if exists)."""
    def placeholder_arguments(self, placeholder_context: trace.PlaceholderContext) -> inspect.BoundArguments:
        """Returns BoundArguments of values that can be used for tracing."""
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

MAX_SANITIZATION_WARNINGS: int
sanitization_warnings_given: int

def sanitize_arg_name(name: str) -> str:
    """Sanitizes function argument names.

  Matches Python symbol naming rules.

  Without sanitization, names that are not legal Python parameter names can be
  set which makes it challenging to represent callables supporting the named
  calling capability.

  Args:
    name: The name to sanitize.

  Returns:
    A string that meets Python parameter conventions.
  """
def canonicalize_to_monomorphic(args: Tuple[Any, ...], kwargs: Dict[Any, Any], default_values: Dict[Any, Any], captures: Dict[Any, Any], polymorphic_type: FunctionType) -> Tuple[inspect.BoundArguments, FunctionType, trace_type.InternalTracingContext]:
    """Converts polymorphic parameters to monomorphic and associated type."""
def add_type_constraints(function_type: FunctionType, input_signature: Any, default_values: Dict[str, Any]):
    """Adds type constraints to a FunctionType based on the input_signature."""
