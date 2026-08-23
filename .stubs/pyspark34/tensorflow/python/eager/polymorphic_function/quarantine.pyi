from _typeshed import Incomplete
from tensorflow.python.eager.polymorphic_function import monomorphic_function as monomorphic_function, polymorphic_function as polymorphic_function, tracing_compiler as tracing_compiler
from tensorflow.python.util import deprecation as deprecation, tf_decorator as tf_decorator
from tensorflow.python.util.tf_export import tf_export as tf_export

def defun_with_attributes(func: Incomplete | None = None, input_signature: Incomplete | None = None, attributes: Incomplete | None = None, autograph: bool = True, experimental_autograph_options: Incomplete | None = None, jit_compile: Incomplete | None = None, reduce_retracing: bool = False):
    """Compiles a Python function into a callable TensorFlow graph.

  This function supports adding extra function attributes. See detailed
  documentation in defun(). Currently this is not exposed in public API since we
  don't expect user to directly use attributes, and attribute won't work by
  itself. This assumption might change in future.

  Args:
    func: function to be compiled.
    input_signature: same as defun()'s input_signature.
    attributes: A dictionary of arguments which will be added to function def as
      attributes. Currently only support primitive types as value, and only
      allowlisted attribute name is allowed. Unallowlisted attribute name or
      unsupported value will result into ValueError. `func_name` is also one of
      the allowlisted argument which is a python string, and sets the name for
      this `ConcreteFunction` in the graph.
    autograph: same as defun()'s autograph.
    experimental_autograph_options: same as defun()'s
      experimental_autograph_options.
    jit_compile: same as defun()'s jit_compile.
    reduce_retracing: same as defun()'s reduce_retracing

  Returns:
    Same as the return value of defun, with attributes added to the function in
    graph.
  """
def add_function_callback(function_callback) -> None:
    """Add a callback function for Function creation.

  The callback function has the signature:

    `def function_callback(function, name, graph, inputs, outputs):`

  where:
  - `function`: _EagerDefinedFunction being created before finalizing the graph.
      Do not modify the function directly but instead modify the graph.
  - `name`: name of the function.
  - `graph`: Graph of the function.
  - `inputs`: `tuple` of tensors used as inputs to the function.
  - `outputs`: `tuple` of tensors used as outputs from the function.

  The callback is at the top of the `_EagerDefinedFunction` construction, giving
  callback an opportunity to make the last edits to the graph. Do not make
  changes to `graph, inputs`, and `outputs` manually, but, instead, set the
  `graph` as the default then define ops.

  Repeated registration of the same callback function is idempotent.
  After a callback is added, it can be removed with the
  `remove_function_callback()` method.

  Args:
    function_callback: The callback to add.
  """
def remove_function_callback(function_callback) -> None:
    """Remove an already-added function callback.

  See the doc string of `add_function_callback()` for more information.

  Args:
    function_callback: The callback to remove.
  """
def clear_function_callbacks() -> None:
    """Clear all function callbacks, if any have been regisered."""
def experimental_run_functions_eagerly(run_eagerly):
    """Enables / disables eager execution of `tf.function`s.

  Calling `tf.config.experimental_run_functions_eagerly(True)` will make all
  invocations of `tf.function` run eagerly instead of running as a traced graph
  function.

  See `tf.config.run_functions_eagerly` for an example.

  Note: This flag has no effect on functions passed into tf.data transformations
  as arguments. tf.data functions are never executed eagerly and are always
  executed as a compiled Tensorflow Graph.

  Args:
    run_eagerly: Boolean. Whether to run functions eagerly.

  Returns:
    None
  """
def experimental_functions_run_eagerly():
    """Returns the value of the `experimental_run_functions_eagerly` setting."""
