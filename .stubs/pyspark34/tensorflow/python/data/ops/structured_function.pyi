from _typeshed import Incomplete
from tensorflow.python.data.ops import debug_mode as debug_mode
from tensorflow.python.data.util import nest as nest, structure as structure
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import function as function, ops as ops
from tensorflow.python.ops import script_ops as script_ops
from tensorflow.python.util import function_utils as function_utils, lazy_loader as lazy_loader, variable_utils as variable_utils

autograph: Incomplete
autograph_ctx: Incomplete

class StructuredFunctionWrapper:
    """A function wrapper that supports structured arguments and return values."""
    def __init__(self, func, transformation_name, dataset: Incomplete | None = None, input_classes: Incomplete | None = None, input_shapes: Incomplete | None = None, input_types: Incomplete | None = None, input_structure: Incomplete | None = None, add_to_graph: bool = True, use_legacy_function: bool = False, defun_kwargs: Incomplete | None = None) -> None:
        """Creates a new `StructuredFunctionWrapper` for the given function.

    Args:
      func: A function from a (nested) structure to another (nested) structure.
      transformation_name: Human-readable name of the transformation in which
        this function is being instantiated, for error messages.
      dataset: (Optional.) A `tf.data.Dataset`. If given, the structure of this
        dataset will be assumed as the structure for `func` arguments; otherwise
        `input_classes`, `input_shapes`, and `input_types` must be defined.
      input_classes: (Optional.) A (nested) structure of `type`. If given, this
        argument defines the Python types for `func` arguments.
      input_shapes: (Optional.) A (nested) structure of `tf.TensorShape`. If
        given, this argument defines the shapes and structure for `func`
        arguments.
      input_types: (Optional.) A (nested) structure of `tf.DType`. If given,
        this argument defines the element types and structure for `func`
        arguments.
      input_structure: (Optional.) A `Structure` object. If given, this argument
        defines the element types and structure for `func` arguments.
      add_to_graph: (Optional.) If `True`, the function will be added to the
        default graph, if it exists.
      use_legacy_function: (Optional.) A boolean that determines whether the
        function be created using `tensorflow.python.eager.function.defun`
        (default behavior) or `tensorflow.python.framework.function.Defun`
        (legacy behavior).
      defun_kwargs: (Optional.) A dictionary mapping string argument names to
        values. If supplied, will be passed to `function` as keyword arguments.

    Raises:
      ValueError: If an invalid combination of `dataset`, `input_classes`,
        `input_shapes`, and `input_types` is passed.
    """
    @property
    def output_structure(self): ...
    @property
    def output_classes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def output_types(self): ...
    @property
    def function(self): ...
