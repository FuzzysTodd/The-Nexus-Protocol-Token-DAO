from tensorflow.lite.python import util as util
from tensorflow.lite.python.convert_phase import Component as Component, SubComponent as SubComponent, convert_phase as convert_phase
from tensorflow.python.client import session as session
from tensorflow.python.framework import ops as ops
from tensorflow.python.saved_model import constants as constants, loader as loader

def get_meta_graph_def(saved_model_dir, tag_set):
    """Validate saved_model and extract MetaGraphDef.

  Args:
    saved_model_dir: saved_model path to convert.
    tag_set: Set of tag(s) of the MetaGraphDef to load.

  Returns:
    The meta_graph_def used for tflite conversion.

  Raises:
    ValueError: No valid MetaGraphDef for given tag_set.
  """
def get_signature_def(meta_graph, signature_key):
    """Get the signature def from meta_graph with given signature_key.

  Args:
    meta_graph: meta_graph_def.
    signature_key: signature_def in the meta_graph_def.

  Returns:
    The signature_def used for tflite conversion.

  Raises:
    ValueError: Given signature_key is not valid for this meta_graph.
  """
def get_inputs_outputs(signature_def):
    """Get inputs and outputs from SignatureDef.

  Args:
    signature_def: SignatureDef in the meta_graph_def for conversion.

  Returns:
    The inputs and outputs in the graph for conversion.
  """
def freeze_saved_model(saved_model_dir, input_arrays, input_shapes, output_arrays, tag_set, signature_key):
    '''Converts a SavedModel to a frozen graph.

  Args:
    saved_model_dir: SavedModel directory to convert.
    input_arrays: List of input tensors to freeze graph with. Uses input arrays
      from SignatureDef when none are provided.
    input_shapes: Dict of strings representing input tensor names to list of
      integers representing input shapes (e.g., {"foo": : [1, 16, 16, 3]}).
      Automatically determined when input shapes is None (e.g., {"foo" : None}).
    output_arrays: List of output tensors to freeze graph with. Uses output
      arrays from SignatureDef when none are provided.
    tag_set: Set of tags identifying the MetaGraphDef within the SavedModel to
      analyze. All tags in the tag set must be present.
    signature_key: Key identifying SignatureDef containing inputs and outputs.

  Returns:
    frozen_graph_def: Frozen GraphDef.
    in_tensors: List of input tensors for the graph.
    out_tensors: List of output tensors for the graph.
    graph: `Graph` object.

  Raises:
    ValueError:
      SavedModel doesn\'t contain a MetaGraphDef identified by tag_set.
      signature_key is not in the MetaGraphDef.
      assets/ directory is in the MetaGraphDef.
      input_shapes does not match the length of input_arrays.
      input_arrays or output_arrays are not valid.
  '''
