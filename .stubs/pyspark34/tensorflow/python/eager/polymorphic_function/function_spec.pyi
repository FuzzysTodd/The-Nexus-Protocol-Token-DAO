import inspect
from _typeshed import Incomplete
from tensorflow.core.function import trace_type as trace_type
from tensorflow.core.function.polymorphism import function_type as function_type_lib
from tensorflow.python.eager.polymorphic_function import composite_tensor_utils as composite_tensor_utils
from tensorflow.python.framework import composite_tensor as composite_tensor, constant_op as constant_op, ops as ops, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import resource_variable_ops as resource_variable_ops
from tensorflow.python.util import nest as nest
from typing import Any, Dict, Tuple

BOUND_VALUE: Incomplete

def to_fullargspec(function_type: function_type_lib.FunctionType, default_values: Dict[str, Any], is_bound_method: bool) -> inspect.FullArgSpec:
    """Generates backwards compatible FullArgSpec from FunctionType."""
def to_function_type(fullargspec):
    """Generates FunctionType and default values from fullargspec."""
def to_input_signature(function_type):
    """Extracts an input_signature from function_type instance."""

class FunctionSpec:
    """Specification of how to bind arguments to a function."""
    @classmethod
    def from_function_and_signature(cls, python_function, input_signature, is_pure: bool = False, jit_compile: Incomplete | None = None):
        """Creates a FunctionSpec instance given a python function and signature.

    Args:
      python_function: a function to inspect
      input_signature: a signature of the function (None, if variable)
      is_pure: if True all input arguments (including variables and constants)
        will be converted to tensors and no variable changes allowed.
      jit_compile: see `tf.function`

    Returns:
      instance of FunctionSpec
    """
    @classmethod
    def from_fullargspec_and_signature(cls, fullargspec, is_bound_method, input_signature, is_pure: bool = False, name: Incomplete | None = None, jit_compile: Incomplete | None = None):
        """Construct FunctionSpec from legacy FullArgSpec format."""
    def __init__(self, function_type, default_values, is_bound_method, is_pure: bool = False, name: Incomplete | None = None, jit_compile: Incomplete | None = None) -> None:
        """Constructs a FunctionSpec describing a python function.

    Args:
      function_type: A FunctionType describing the python function signature.
      default_values: Dictionary mapping parameter names to default values.
      is_bound_method: True if the underlying function is a bound method.
      is_pure: if True all input arguments (including variables and constants)
        will be converted to tensors and no variable changes allowed.
      name: Name of the function
      jit_compile: see `tf.function`.
    """
    @property
    def default_values(self):
        """Returns dict mapping parameter names to default values."""
    @property
    def function_type(self):
        """Returns a FunctionType representing the Python function signature."""
    @property
    def fullargspec(self): ...
    @property
    def is_method(self):
        """Returns True if the function is a method with a class instance bound."""
    @property
    def input_signature(self): ...
    @property
    def flat_input_signature(self): ...
    @property
    def is_pure(self): ...
    @property
    def jit_compile(self): ...
    @property
    def arg_names(self): ...
    def make_canonicalized_monomorphic_type(self, args: Any, kwargs: Any, captures: Any = None) -> Tuple[function_type_lib.FunctionType, trace_type.WeakrefDeletionObserver]:
        """Generates function type given the function arguments."""
    def signature_summary(self, default_values: bool = False):
        """Returns a string summarizing this function's signature.

    Args:
      default_values: If true, then include default values in the signature.

    Returns:
      A `string`.
    """
    def canonicalize_function_inputs(self, args, kwargs):
        """Canonicalizes `args` and `kwargs`.

    Canonicalize the inputs to the Python function using a `FunctionSpec`
    instance. In particular, we parse the varargs and kwargs that the
    original function was called with into a tuple corresponding to the
    Python function's positional (named) arguments and a dictionary
    corresponding to its kwargs.  Missing default arguments are added.

    If this `FunctionSpec` has an input signature, then it is used to convert
    arguments to tensors; otherwise, any inputs containing numpy arrays are
    converted to tensors.

    Additionally, any inputs containing numpy arrays are converted to Tensors.

    Args:
      args: The varargs this object was called with.
      kwargs: The keyword args this function was called with.

    Returns:
      A canonicalized ordering of the inputs, as well as full and filtered
      (Tensors and Variables only) versions of their concatenated flattened
      representations, represented by a tuple in the form (args, kwargs,
      flat_args, filtered_flat_args). Here: `args` is a full list of bound
      arguments, and `kwargs` contains only true keyword arguments, as opposed
      to named arguments called in a keyword-like fashion.

    Raises:
      ValueError: If a keyword in `kwargs` cannot be matched with a positional
        argument when an input signature is specified, or when the inputs
        do not conform to the input signature.
    """
    def bind_function_inputs(self, args, kwargs):
        """Bind `args` and `kwargs` into a canonicalized signature args, kwargs."""

def cast_inputs(args, kwargs, input_signature):
    """Casts args, kwargs to TF values based on an optional input_signature."""
def cast_numpy_inputs(inputs):
    """Converts numpy array inputs to tensors."""
def cast_inputs_to_signature(inputs, input_signature):
    """Converts inputs to pass into a function with an explicit signature."""
def filter_function_inputs(args, kwargs):
    """Filters and flattens args and kwargs."""
def is_same_structure(structure1, structure2, check_values: bool = False):
    """Check two structures for equality, optionally of types and of values."""
