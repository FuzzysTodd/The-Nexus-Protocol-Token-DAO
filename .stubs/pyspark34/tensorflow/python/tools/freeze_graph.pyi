from _typeshed import Incomplete
from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.core.protobuf import saver_pb2 as saver_pb2
from tensorflow.core.protobuf.meta_graph_pb2 import MetaGraphDef as MetaGraphDef
from tensorflow.python.checkpoint import checkpoint_management as checkpoint_management
from tensorflow.python.client import session as session
from tensorflow.python.framework import convert_to_constants as convert_to_constants, importer as importer
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.saved_model import loader as loader, tag_constants as tag_constants
from tensorflow.python.tools import saved_model_utils as saved_model_utils
from tensorflow.python.training import py_checkpoint_reader as py_checkpoint_reader

def freeze_graph_with_def_protos(input_graph_def, input_saver_def, input_checkpoint, output_node_names, restore_op_name, filename_tensor_name, output_graph, clear_devices, initializer_nodes, variable_names_whitelist: str = '', variable_names_denylist: str = '', input_meta_graph_def: Incomplete | None = None, input_saved_model_dir: Incomplete | None = None, saved_model_tags: Incomplete | None = None, checkpoint_version=...):
    """Converts all variables in a graph and checkpoint into constants.

  Args:
    input_graph_def: A `GraphDef`.
    input_saver_def: A `SaverDef` (optional).
    input_checkpoint: The prefix of a V1 or V2 checkpoint, with V2 taking
      priority.  Typically the result of `Saver.save()` or that of
      `tf.train.latest_checkpoint()`, regardless of sharded/non-sharded or
      V1/V2.
    output_node_names: The name(s) of the output nodes, comma separated.
    restore_op_name: Unused.
    filename_tensor_name: Unused.
    output_graph: String where to write the frozen `GraphDef`.
    clear_devices: A Bool whether to remove device specifications.
    initializer_nodes: Comma separated string of initializer nodes to run before
                       freezing.
    variable_names_whitelist: The set of variable names to convert (optional, by
                              default, all variables are converted).
    variable_names_denylist: The set of variable names to omit converting
                              to constants (optional).
    input_meta_graph_def: A `MetaGraphDef` (optional),
    input_saved_model_dir: Path to the dir with TensorFlow 'SavedModel' file
                           and variables (optional).
    saved_model_tags: Group of comma separated tag(s) of the MetaGraphDef to
                      load, in string format (optional).
    checkpoint_version: Tensorflow variable file format (saver_pb2.SaverDef.V1
                        or saver_pb2.SaverDef.V2)

  Returns:
    Location of the output_graph_def.
  """
def freeze_graph(input_graph, input_saver, input_binary, input_checkpoint, output_node_names, restore_op_name, filename_tensor_name, output_graph, clear_devices, initializer_nodes, variable_names_whitelist: str = '', variable_names_denylist: str = '', input_meta_graph: Incomplete | None = None, input_saved_model_dir: Incomplete | None = None, saved_model_tags=..., checkpoint_version=...):
    """Converts all variables in a graph and checkpoint into constants.

  Args:
    input_graph: A `GraphDef` file to load.
    input_saver: A TensorFlow Saver file.
    input_binary: A Bool. True means input_graph is .pb, False indicates .pbtxt.
    input_checkpoint: The prefix of a V1 or V2 checkpoint, with V2 taking
      priority.  Typically the result of `Saver.save()` or that of
      `tf.train.latest_checkpoint()`, regardless of sharded/non-sharded or
      V1/V2.
    output_node_names: The name(s) of the output nodes, comma separated.
    restore_op_name: Unused.
    filename_tensor_name: Unused.
    output_graph: String where to write the frozen `GraphDef`.
    clear_devices: A Bool whether to remove device specifications.
    initializer_nodes: Comma separated list of initializer nodes to run before
                       freezing.
    variable_names_whitelist: The set of variable names to convert (optional, by
                              default, all variables are converted),
    variable_names_denylist: The set of variable names to omit converting
                              to constants (optional).
    input_meta_graph: A `MetaGraphDef` file to load (optional).
    input_saved_model_dir: Path to the dir with TensorFlow 'SavedModel' file and
                           variables (optional).
    saved_model_tags: Group of comma separated tag(s) of the MetaGraphDef to
                      load, in string format.
    checkpoint_version: Tensorflow variable file format (saver_pb2.SaverDef.V1
                        or saver_pb2.SaverDef.V2).
  Returns:
    String that is the location of frozen GraphDef.
  """
def main(unused_args, flags) -> None: ...
def run_main():
    """Main function of freeze_graph."""
