from tensorflow.core.protobuf import saved_model_pb2 as saved_model_pb2
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.saved_model import constants as constants
from tensorflow.python.util import compat as compat

def read_saved_model(saved_model_dir):
    """Reads the saved_model.pb or saved_model.pbtxt file containing `SavedModel`.

  Args:
    saved_model_dir: Directory containing the SavedModel file.

  Returns:
    A `SavedModel` protocol buffer.

  Raises:
    IOError: If the file does not exist, or cannot be successfully parsed.
  """
def get_saved_model_tag_sets(saved_model_dir):
    """Retrieves all the tag-sets available in the SavedModel.

  Args:
    saved_model_dir: Directory containing the SavedModel.

  Returns:
    List of all tag-sets in the SavedModel, where a tag-set is represented as a
    list of strings.
  """
def get_meta_graph_def(saved_model_dir, tag_set):
    """Gets MetaGraphDef from SavedModel.

  Returns the MetaGraphDef for the given tag-set and SavedModel directory.

  Args:
    saved_model_dir: Directory containing the SavedModel to inspect.
    tag_set: Group of tag(s) of the MetaGraphDef to load, in string format,
        separated by ','. The empty string tag is ignored so that passing ''
        means the empty tag set. For tag-set contains multiple tags, all tags
        must be passed in.

  Raises:
    RuntimeError: An error when the given tag-set does not exist in the
        SavedModel.

  Returns:
    A MetaGraphDef corresponding to the tag-set.
  """
