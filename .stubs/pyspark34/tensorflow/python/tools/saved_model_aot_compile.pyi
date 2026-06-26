from tensorflow.core.protobuf import config_pb2 as config_pb2, meta_graph_pb2 as meta_graph_pb2
from tensorflow.python.client import session as session
from tensorflow.python.framework import graph_util as graph_util, tensor_shape as tensor_shape, versions as versions
from tensorflow.python.grappler import tf_optimizer as tf_optimizer
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.platform import test as test
from typing import List, Tuple

def freeze_model(checkpoint_path: str, meta_graph_def: meta_graph_pb2.MetaGraphDef, output_prefix: str, signature_def_key: str, variables_to_feed: List[str]) -> Tuple[str, str]:
    """Freeze a `MetaGraphDef` in preparation for tfcompile`.

  The graph is always optimized with grappler, and optionally (by default)
  variables are frozen as constants, before compilation happens.

  Args:
    checkpoint_path: Python string.  Path to checkpoints/variables.
    meta_graph_def: Instance of `MetaGraphDef`.
    output_prefix: Python string.  Path prefix for outputs.
    signature_def_key: String, the signature_def to use in the SavedModel.
    variables_to_feed: A list of strings, the variables that will be fed by the
      user; these won't be frozen.  If `None`, then we will extract all the
      variables in the graph and mark them as to-feed.  The default behavior is
      an empty tuple: all variables must be frozen.
  Returns:
    a pair containing the path to the frozen model and the path to the config.
  Raises:
    RuntimeError: If tensorflow was not built with XLA.
    ImportError: If tensorflow was built with XLA but there was another
      issue importing the tfcompile python wrapper.
    ValueError: If `meta_graph_def.signature_def[signature_def_key]` is
      missing or has empty outputs.
  """
def aot_compile_cpu_meta_graph_def(checkpoint_path, meta_graph_def, output_prefix, signature_def_key, cpp_class, target_triple, target_cpu, variables_to_feed=(), multithreading: bool = False) -> None:
    """Compile a `MetaGraphDef` to header+object files in `output_prefix`.

  Use XLA AOT (`tfcompile`) to convert the given meta graph and
  signature into a header + object files.  Also create an include makefile
  that helps identify the appropriate necessary include and library paths
  to incorporate these files into your C++ program.

  Freezing a graph entails restoring the checkpoint and replacing any inputs and
  variables with constants. If values are feed, those are used, else inputs are
  replaced with default all-zero constants. Finally, the graph is pruned and
  then optimized with grappler.

  If the `freeze_graph` is `True`, all variables are embedded as constants
  into the graph and binary objects.  If it is `False`, then the variable
  values become inputs and outputs of the compiled class and the C++
  caller must set these values manually.

  Args:
    checkpoint_path: Python string.  Path to checkpoints/variables.
    meta_graph_def: Instance of `MetaGraphDef`.
    output_prefix: Python string.  Path prefix for outputs.
    signature_def_key: String, the signature_def to use in the SavedModel.
    cpp_class: String, Name of output C++ class.
    target_triple: String, LLVM target triple.
    target_cpu: String, LLVM target cpu name.
    variables_to_feed: A list of strings, the variables that will be fed by the
      user; these won't be frozen.  If `None`, then we will extract all the
      variables in the graph and mark them as to-feed.  The default behavior is
      an empty tuple: all variables must be frozen.
    multithreading: Whether to enable multithreading in the compiled
      computation.  Note that if using this option, the resulting object files
      may have external dependencies on multithreading libraries like nsync.

  Raises:
    RuntimeError: If tensorflow was not built with XLA.
    ImportError: If tensorflow was built with XLA but there was another
      issue importing the tfcompile python wrapper.
    ValueError: If `meta_graph_def.signature_def[signature_def_key]` is
      missing or has empty outputs.
  """
