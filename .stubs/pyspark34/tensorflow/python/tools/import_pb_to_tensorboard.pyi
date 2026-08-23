from tensorflow.contrib.tensorrt.ops.gen_trt_engine_op import *
from tensorflow.python.client import session as session
from tensorflow.python.framework import importer as importer, ops as ops
from tensorflow.python.summary import summary as summary
from tensorflow.python.tools import saved_model_utils as saved_model_utils

def import_to_tensorboard(model_dir, log_dir, tag_set) -> None:
    """View an SavedModel as a graph in Tensorboard.

  Args:
    model_dir: The directory containing the SavedModel to import.
    log_dir: The location for the Tensorboard log to begin visualization from.
    tag_set: Group of tag(s) of the MetaGraphDef to load, in string format,
      separated by ','. For tag-set contains multiple tags, all tags must be
      passed in.
  Usage: Call this function with your SavedModel location and desired log
    directory. Launch Tensorboard by pointing it to the log directory. View your
    imported SavedModel as a graph.
  """
def main(_) -> None: ...
