from _typeshed import Incomplete
from jax.experimental import jax2tf as jax2tf

def jax_to_ir(fn, input_shapes, *, constants: Incomplete | None = None, format):
    """Converts a JAX function to a serialized ir and a debug txt dump.

  Args:
    fn: Function to convert.
    input_shapes: List of tuples (arg name, jax.core.ShapedArray),
      indicating the shapes of the arguments to fn.  The order of parameters in
      the resulting XLA program will match the order in this list.
    constants: Dict mapping function argument name to a Python value.  Specified
      arguments these values as compile-time constants.
    format: Which IR format to use. Supported values are 'HLO' and 'TF'.

  Returns:
    A tuple of (compiler_suitable_ir, human_readable_ir).
  """
def tf_wrap_with_input_names(f, input_shapes): ...

jax_to_hlo: Incomplete
jax_to_tf: Incomplete

def main(argv) -> None: ...
def parse_shape_str(s): ...
def set_up_flags() -> None: ...
