from tensorflow.python.eager import context as context, lift_to_graph as lift_to_graph, wrap_function as wrap_function
from tensorflow.python.framework import composite_tensor as composite_tensor, constant_op as constant_op, func_graph as func_graph, ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.saved_model import function_deserialization as function_deserialization, loader_impl as loader_impl, signature_serialization as signature_serialization
from tensorflow.python.saved_model.pywrap_saved_model import metrics as metrics
from tensorflow.python.trackable import asset as asset, autotrackable as autotrackable, resource as resource
from tensorflow.python.training import monitored_session as monitored_session
from tensorflow.python.util import nest as nest

class _Initializer(resource.CapturableResource):
    """Represents an initialization operation restored from a SavedModel.

  Without this object re-export of imported 1.x SavedModels would omit the
  original SavedModel's initialization procedure.

  Created when `tf.saved_model.load` loads a TF 1.x-style SavedModel with an
  initialization op. This object holds a function that runs the
  initialization. It does not require any manual user intervention;
  `tf.saved_model.save` will see this object and automatically add it to the
  exported SavedModel, and `tf.saved_model.load` runs the initialization
  function automatically.
  """
    def __init__(self, init_fn, asset_paths) -> None: ...

class _EagerSavedModelLoader(loader_impl.SavedModelLoader):
    """Loads a SavedModel without using Sessions."""
    def get_meta_graph_def_from_tags(self, tags):
        """Override to support implicit one-MetaGraph loading with tags=None."""
    def load_graph(self, returns, meta_graph_def) -> None:
        """Called from wrap_function to import `meta_graph_def`."""
    def restore_variables(self, wrapped, restore_from_saver) -> None:
        """Restores variables from the checkpoint."""
    def load(self, tags):
        """Creates an object from the MetaGraph identified by `tags`."""

def load(export_dir, tags):
    """Load a v1-style SavedModel as an object."""
