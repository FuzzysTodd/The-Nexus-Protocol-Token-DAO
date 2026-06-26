from _typeshed import Incomplete
from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.python import tf2 as tf2
from tensorflow.python.framework import c_api_util as c_api_util, errors as errors, function as function, op_def_registry as op_def_registry, ops as ops
from tensorflow.python.ops import control_flow_util as control_flow_util
from tensorflow.python.util import compat as compat
from tensorflow.python.util.deprecation import deprecated_args as deprecated_args
from tensorflow.python.util.tf_export import tf_export as tf_export

def import_graph_def(graph_def, input_map: Incomplete | None = None, return_elements: Incomplete | None = None, name: Incomplete | None = None, op_dict: Incomplete | None = None, producer_op_list: Incomplete | None = None):
    '''Imports the graph from `graph_def` into the current default `Graph`.

  This function provides a way to import a serialized TensorFlow
  [`GraphDef`](https://www.tensorflow.org/code/tensorflow/core/framework/graph.proto)
  protocol buffer, and extract individual objects in the `GraphDef` as
  `tf.Tensor` and `tf.Operation` objects. Once extracted,
  these objects are placed into the current default `Graph`. See
  `tf.Graph.as_graph_def` for a way to create a `GraphDef`
  proto.

  Args:
    graph_def: A `GraphDef` proto containing operations to be imported into
      the default graph.
    input_map: A dictionary mapping input names (as strings) in `graph_def`
      to `Tensor` objects. The values of the named input tensors in the
      imported graph will be re-mapped to the respective `Tensor` values.
    return_elements: A list of strings containing operation names in
      `graph_def` that will be returned as `Operation` objects; and/or
      tensor names in `graph_def` that will be returned as `Tensor` objects.
    name: (Optional.) A prefix that will be prepended to the names in
      `graph_def`. Note that this does not apply to imported function names.
      Defaults to `"import"`.
    op_dict: (Optional.) Deprecated, do not use.
    producer_op_list: (Optional.) An `OpList` proto with the (possibly stripped)
      list of `OpDef`s used by the producer of the graph. If provided,
      unrecognized attrs for ops in `graph_def` that have their default value
      according to `producer_op_list` will be removed. This will allow some more
      `GraphDef`s produced by later binaries to be accepted by earlier binaries.

  Returns:
    A list of `Operation` and/or `Tensor` objects from the imported graph,
    corresponding to the names in `return_elements`,
    and None if `returns_elements` is None.

  Raises:
    TypeError: If `graph_def` is not a `GraphDef` proto,
      `input_map` is not a dictionary mapping strings to `Tensor` objects,
      or `return_elements` is not a list of strings.
    ValueError: If `input_map`, or `return_elements` contains names that
      do not appear in `graph_def`, or `graph_def` is not well-formed (e.g.
      it refers to an unknown tensor).
  '''
def import_graph_def_for_function(graph_def, name: Incomplete | None = None, propagate_device_spec: bool = False):
    """Like import_graph_def but does not validate colocation constraints."""
