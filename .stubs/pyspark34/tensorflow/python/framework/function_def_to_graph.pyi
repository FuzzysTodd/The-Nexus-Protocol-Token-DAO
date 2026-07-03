from _typeshed import Incomplete
from tensorflow.core.framework import function_pb2 as function_pb2, graph_pb2 as graph_pb2, tensor_shape_pb2 as tensor_shape_pb2, types_pb2 as types_pb2, versions_pb2 as versions_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import cpp_shape_inference_pb2 as cpp_shape_inference_pb2, importer as importer, ops as ops, versions as versions
from tensorflow.python.framework.func_graph import FuncGraph as FuncGraph
from tensorflow.python.ops import resource_variable_ops as resource_variable_ops

def function_def_to_graph(fdef, structured_input_signature: Incomplete | None = None, structured_outputs: Incomplete | None = None, input_shapes: Incomplete | None = None, propagate_device_spec: bool = False):
    '''Converts a FunctionDef to a FuncGraph (sub-class Graph).

  The returned FuncGraph\'s `name`, `inputs` and `outputs` fields will be set.
  The input tensors are represented as placeholders.

  Note: `FuncGraph.inputs` and `FuncGraph.captures` are not set and may be set
  by the caller.

  Args:
    fdef: FunctionDef.
    structured_input_signature: Optional. The structured input signature to
      use for initializing the FuncGraph. See the docstring for FuncGraph for
      more information.
    structured_outputs: Optional. The structured outputs to use for
      initializing the FuncGraph. See the docstring for FuncGraph for more
      information.
    input_shapes: Optional. A list of TensorShape objects of the shapes of
      function inputs. Defaults to the function\'s "_input_shapes" attribute. If
      specified, its length must match length of `fdef.signature.input_arg`. If
      a shape is None, the corresponding input placeholder will have unknown
      shape.
    propagate_device_spec: Optional. Whether to propagate assigned device
      information when constructing a new Graph from a FunctionDef.

  Returns:
    A FuncGraph.
  '''
def is_function(fname):
    """Checks for a function definition with `fname` in the current context."""
def function_def_to_graph_def(fdef, input_shapes: Incomplete | None = None):
    """Convert a FunctionDef to a GraphDef.

  Steps:
  1. Creates placeholder nodes corresponding to inputs in
     `FunctionDef.signature.input_arg`.
  2. Adds NodeDefs in `FunctionDef.node_def` to `GraphDef.node`.
  3. Renames inputs of all nodes to use the convention of GraphDef instead of
     FunctionDef. See comment on `FunctionDef.node_def` on how the tensor naming
     in FunctionDefs is different from GraphDefs.

  Args:
    fdef: FunctionDef.
    input_shapes: Optional. A list of TensorShape objects of the shapes of
      function inputs. If specified, its length must match length of
      `fdef.signature.input_arg`. If a shape is None, the corresponding input
      placeholder will have unknown shape.

  Returns:
    A tuple of (GraphDef, dict<string, string>). The dict contains a mapping
    from nested tensor names (in FunctionDef) to flattened names (in GraphDef).

  Raises:
    ValueError: If the length of input_shapes does not match the number of
      input_args or if the FunctionDef is invalid.
  """
