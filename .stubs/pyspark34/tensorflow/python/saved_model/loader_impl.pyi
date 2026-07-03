from _typeshed import Incomplete
from tensorflow.core.protobuf import graph_debug_info_pb2 as graph_debug_info_pb2, meta_graph_pb2 as meta_graph_pb2, saved_model_pb2 as saved_model_pb2
from tensorflow.python.framework import ops as ops
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import variables as variables
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.saved_model import constants as constants, path_helpers as path_helpers, signature_def_utils as signature_def_utils
from tensorflow.python.saved_model.pywrap_saved_model import metrics as metrics
from tensorflow.python.util import compat as compat, deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

def parse_saved_model_with_debug_info(export_dir):
    """Reads the savedmodel as well as the graph debug info.

  Args:
    export_dir: Directory containing the SavedModel and GraphDebugInfo files.

  Returns:
    `SavedModel` and `GraphDebugInfo` protocol buffers.

  Raises:
    IOError: If the saved model file does not exist, or cannot be successfully
    parsed. Missing graph debug info file is fine.
  """
def parse_saved_model(export_dir):
    """Reads the savedmodel.pb or savedmodel.pbtxt file containing `SavedModel`.

  Args:
    export_dir: String or Pathlike, path to the directory containing the
    SavedModel file.

  Returns:
    A `SavedModel` protocol buffer.

  Raises:
    IOError: If the file does not exist, or cannot be successfully parsed.
  """
def get_asset_tensors(export_dir, meta_graph_def_to_load, import_scope: Incomplete | None = None):
    """Gets the asset tensors, if defined in the meta graph def to load.

  Args:
    export_dir: Directory where the SavedModel is located.
    meta_graph_def_to_load: The meta graph def from the SavedModel to be loaded.
    import_scope: Optional `string` -- if specified, prepend this followed by
        '/' to all returned asset tensor names.

  Returns:
    A dictionary of asset tensors, keyed by the name of the asset tensor. The
    value in the map corresponds to the absolute path of the asset file.
  """
def get_init_op(meta_graph_def, import_scope: Incomplete | None = None): ...
def get_train_op(meta_graph_def, import_scope: Incomplete | None = None): ...
def maybe_saved_model_directory(export_dir):
    """Checks whether the provided export directory could contain a SavedModel.

  Note that the method does not load any data by itself. If the method returns
  `false`, the export directory definitely does not contain a SavedModel. If the
  method returns `true`, the export directory may contain a SavedModel but
  provides no guarantee that it can be loaded.

  Args:
    export_dir: Absolute string path to possible export location. For example,
                '/my/foo/model'.

  Returns:
    True if the export directory contains SavedModel files, False otherwise.
  """
def contains_saved_model(export_dir):
    """Checks whether the provided export directory could contain a SavedModel.

  Note that the method does not load any data by itself. If the method returns
  `false`, the export directory definitely does not contain a SavedModel. If the
  method returns `true`, the export directory may contain a SavedModel but
  provides no guarantee that it can be loaded.

  Args:
    export_dir: Absolute path to possible export location. For example,
                '/my/foo/model'.

  Returns:
    True if the export directory contains SavedModel files, False otherwise.
  """
def load(sess, tags, export_dir, import_scope: Incomplete | None = None, **saver_kwargs):
    '''Loads the model from a SavedModel as specified by tags.

  Args:
    sess: The TensorFlow session to restore the variables.
    tags: Set of string tags to identify the required MetaGraphDef. These should
        correspond to the tags used when saving the variables using the
        SavedModel `save()` API.
    export_dir: Directory in which the SavedModel protocol buffer and variables
        to be loaded are located.
    import_scope: Optional `string` -- if specified, prepend this string
        followed by \'/\' to all loaded tensor names. This scope is applied to
        tensor instances loaded into the passed session, but it is *not* written
        through to the static `MetaGraphDef` protocol buffer that is returned.
    **saver_kwargs: Optional keyword arguments passed through to Saver.

  Returns:
    The `MetaGraphDef` protocol buffer loaded in the provided session. This
    can be used to further extract signature-defs, collection-defs, etc.

  Raises:
    RuntimeError: MetaGraphDef associated with the tags cannot be found.

  @compatibility(TF2)

  `tf.compat.v1.saved_model.load` or `tf.compat.v1.saved_model.loader.load` is
  not compatible with eager execution. Please use `tf.saved_model.load` instead
  to load your model. You can refer to the [SavedModel guide]
  (https://www.tensorflow.org/guide/saved_model) for more information as well as
  "Importing SavedModels from TensorFlow 1.x" in the [`tf.saved_model.load`]
  (https://www.tensorflow.org/api_docs/python/tf/saved_model/load) docstring.

  #### How to Map Arguments

  | TF1 Arg Name          | TF2 Arg Name    | Note                       |
  | :-------------------- | :-------------- | :------------------------- |
  | `sess`                | Not supported   | -                          |
  | `tags`                | `tags`          | -                          |
  | `export_dir`          | `export_dir`    | -                          |
  | `import_scope`        | Not supported   | Name scopes are not needed.
  :                       :                 : By default, variables are  :
  :                       :                 : associated with the loaded :
  :                       :                 : object and function names  :
  :                       :                 : are deduped.               :
  | `saver_kwargs`        | Not supported   | -                          |

  #### Before & After Usage Example

  Before:

  ```
  with tf.compat.v1.Session(graph=tf.Graph()) as sess:
    tf.compat.v1.saved_model.loader.load(sess, ["foo-tag"], export_dir)
  ```

  After:

  ```
  model = tf.saved_model.load(export_dir, tags=["foo-tag"])
  ```
  @end_compatibility
  '''

class SavedModelLoader:
    """Load graphs and restore variable values from a `SavedModel`."""
    def __init__(self, export_dir) -> None:
        """Creates a `SavedModelLoader`.

    Args:
      export_dir: Directory in which the SavedModel protocol buffer and
        variables to be loaded are located.
    """
    @property
    def export_dir(self):
        """Directory containing the SavedModel."""
    @property
    def variables_path(self):
        """Path to variable checkpoint files."""
    @property
    def saved_model(self):
        """SavedModel object parsed from the export directory."""
    def get_meta_graph_def_from_tags(self, tags):
        """Return MetaGraphDef with the exact specified tags.

    Args:
      tags: A list or set of string tags that identify the MetaGraphDef.

    Returns:
      MetaGraphDef with the same tags.

    Raises:
      RuntimeError: if no metagraphs were found with the associated tags.
    """
    def load_graph(self, graph, tags, import_scope: Incomplete | None = None, **saver_kwargs):
        """Load ops and nodes from SavedModel MetaGraph into graph.

    Args:
      graph: tf.Graph object.
      tags: a set of string tags identifying a MetaGraphDef.
      import_scope: Optional `string` -- if specified, prepend this string
        followed by '/' to all loaded tensor names. This scope is applied to
        tensor instances loaded into the passed session, but it is *not* written
        through to the static `MetaGraphDef` protocol buffer that is returned.
      **saver_kwargs: keyword arguments to pass to tf.train.import_meta_graph.

    Returns:
      A tuple of
        * Saver defined by the MetaGraph, which can be used to restore the
          variable values.
        * List of `Operation`/`Tensor` objects returned from
          `tf.import_graph_def` (may be `None`).
    """
    def restore_variables(self, sess, saver, import_scope: Incomplete | None = None) -> None:
        """Restore SavedModel variable values into the session.

    Args:
      sess: tf.compat.v1.Session to restore variable values.
      saver: a tf.compat.v1.train.Saver object. Can be None if there are no
        variables in graph. This may be the saver returned by the load_graph()
        function, or a default `tf.compat.v1.train.Saver()`.
      import_scope: Optional `string` -- if specified, prepend this string
        followed by '/' to all loaded tensor names. This scope is applied to
        tensor instances loaded into the passed session, but it is *not* written
        through to the static `MetaGraphDef` protocol buffer that is returned.

    Raises:
      ValueError: if no saver was passed to the saver argument, and there are
        variables in the graph.
    """
    def run_init_ops(self, sess, tags, import_scope: Incomplete | None = None) -> None:
        """Run initialization ops defined in the `MetaGraphDef`.

    Args:
      sess: tf.compat.v1.Session to restore variable values.
      tags: a set of string tags identifying a MetaGraphDef.
      import_scope: Optional `string` -- if specified, prepend this string
        followed by '/' to all loaded tensor names. This scope is applied to
        tensor instances loaded into the passed session, but it is *not* written
        through to the static `MetaGraphDef` protocol buffer that is returned.
    """
    def load(self, sess, tags, import_scope: Incomplete | None = None, **saver_kwargs):
        """Load the MetaGraphDef graph and restore variable values into the session.

    Args:
      sess: tf.compat.v1.Session to restore variable values.
      tags: a set of string tags identifying a MetaGraphDef.
      import_scope: Optional `string` -- if specified, prepend this string
        followed by '/' to all loaded tensor names. This scope is applied to
        tensor instances loaded into the passed session, but it is *not* written
        through to the static `MetaGraphDef` protocol buffer that is returned.
      **saver_kwargs: keyword arguments to pass to tf.train.import_meta_graph.

    Returns:
      `MetagraphDef` proto of the graph that was loaded.
    """
