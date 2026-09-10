from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.core.config import flags as flags
from tensorflow.core.framework import function_pb2 as function_pb2, versions_pb2 as versions_pb2
from tensorflow.core.protobuf import fingerprint_pb2 as fingerprint_pb2, meta_graph_pb2 as meta_graph_pb2, saved_model_pb2 as saved_model_pb2, saved_object_graph_pb2 as saved_object_graph_pb2
from tensorflow.python.checkpoint import checkpoint as checkpoint, checkpoint_options as checkpoint_options, functional_saver as functional_saver, graph_view as graph_view, save_util_v1 as save_util_v1
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.eager.polymorphic_function import saved_model_exported_concrete as saved_model_exported_concrete, saved_model_utils as saved_model_utils
from tensorflow.python.framework import dtypes as dtypes, error_interpolation as error_interpolation, errors as errors, meta_graph as meta_graph, ops as ops, tensor_util as tensor_util, versions as versions
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.saved_model import builder_impl as builder_impl, function_serialization as function_serialization, path_helpers as path_helpers, pywrap_saved_model as pywrap_saved_model, registration as registration, revived_types as revived_types, save_context as save_context, save_options as save_options, signature_constants as signature_constants, signature_def_utils as signature_def_utils, signature_serialization as signature_serialization, tag_constants as tag_constants, tracing_utils as tracing_utils, utils_impl as utils_impl
from tensorflow.python.saved_model.pywrap_saved_model import constants as constants, fingerprinting as fingerprinting, metrics as metrics
from tensorflow.python.trackable import asset as asset, base as base, resource as resource, trackable_utils as trackable_utils
from tensorflow.python.training.saving import saveable_object_util as saveable_object_util
from tensorflow.python.util import compat as compat, object_identity as object_identity
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class _CapturedTensor(NamedTuple):
    name: Incomplete
    concrete_function: Incomplete

class _AugmentedGraphView(graph_view.ObjectGraphView):
    """An extendable graph which also tracks functions attached to objects.

  Extensions through `add_object` appear in the object graph and any checkpoints
  generated from it, even if they are not dependencies of the node they were
  attached to in the saving program. For example a `.signatures` attribute is
  added to exported SavedModel root objects without modifying the root object
  itself.

  Also tracks functions attached to objects in the graph, through the caching
  `_list_functions` method. Enumerating functions only through this method
  ensures that we get a consistent view of functions, even if object attributes
  create new functions every time they are accessed.
  """
    untraced_functions: Incomplete
    def __init__(self, root) -> None: ...
    def set_signature(self, signature_map, wrapped_functions) -> None:
        """Attach signature to the root object.

    Args:
      signature_map: An object that contains signature functions.
      wrapped_functions: A dictionary mapping functions to functions that are
        guaranteed to not capture cached variables (functions that capture
        cached variables can't be saved).
    """
    def list_children(self, obj) -> Generator[Incomplete, None, None]:
        """Lists children of `obj` for SavedModel."""
    def get_child(self, obj, name): ...
    def list_dependencies(self, obj) -> Generator[Incomplete, None, None]:
        """Yields `Trackables` that must be loaded before `obj`.

    Dependencies and children are both dictionaries of `Trackables`. Children
    define the object graph structure (used in both checkpoints and SavedModel),
    while dependency defines the order used to load the SavedModel

    Args:
      obj: A `Trackable` object

    Yields:
      Tuple of dependency names and trackable objects.

    Raises:
      TypeError: if any of the returned dependencies are not instances of
        `Trackable`.
    """

class _SaveableView:
    """Provides a frozen view over a trackable root.

  This class helps to create a single stable view over an object to save. The
  saving code should access properties and functions via this class and not via
  the original object as there are cases where an object construct their
  trackable attributes and functions dynamically per call and will yield
  different objects if invoked more than once.

  Changes to the graph, for example adding objects, must happen in
  `augmented_graph_view` (an `_AugmentedGraphView`) before the `_SaveableView`
  is constructed. Changes after the `_SaveableView` has been constructed will be
  ignored.
  """
    augmented_graph_view: Incomplete
    captured_tensor_node_ids: Incomplete
    def __init__(self, augmented_graph_view, options) -> None:
        """Initializes a SaveableView.

    Args:
      augmented_graph_view: A GraphView object.
      options: A SaveOptions instance.
    """
    @property
    def concrete_and_gradient_functions(self): ...
    @property
    def root(self): ...
    def fill_object_graph_proto(self, proto) -> None:
        """Populate the nodes, children and slot_variables of a SavedObjectGraph."""
    def map_resources(self):
        """Makes new resource handle ops corresponding to existing resource tensors.

    Creates resource handle ops in the current default graph, whereas
    `accessible_objects` will be from an eager context. Resource mapping adds
    resource handle ops to the main GraphDef of a SavedModel, which allows the
    C++ loader API to interact with resources.

    Returns:
      A tuple of (object_map, tensor_map, asset_info):
        object_map: A dictionary mapping from object in `accessible_objects` to
          replacement objects created to hold the new resource tensors.
        tensor_map: A dictionary mapping from resource tensors extracted from
          `accessible_objects` to newly created resource tensors.
        asset_info: An _AssetInfo tuple describing external assets referenced
          from accessible_objects.
    """
    def add_capture_and_node(self, capture, node): ...
    def get_concrete_resource_initializers(self): ...

class _AssetInfo(NamedTuple):
    asset_defs: Incomplete
    asset_initializers_by_resource: Incomplete
    asset_filename_map: Incomplete
    asset_index: Incomplete

def save(obj, export_dir, signatures: Incomplete | None = None, options: Incomplete | None = None) -> None:
    '''Exports a [tf.Module](https://www.tensorflow.org/api_docs/python/tf/Module) (and subclasses) `obj` to [SavedModel format](https://www.tensorflow.org/guide/saved_model#the_savedmodel_format_on_disk).

  The `obj` must inherit from the [`Trackable`
  class](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/training/tracking/base.py#L591).

  Example usage:

  >>> class Adder(tf.Module):
  ...   @tf.function(input_signature=[tf.TensorSpec(shape=[], dtype=tf.float32)])
  ...   def add(self, x):
  ...     return x + x

  >>> model = Adder()
  >>> tf.saved_model.save(model, \'/tmp/adder\')

  The resulting SavedModel is then servable with an input named "x", a scalar
  with dtype float32.

  _Signatures_

  Signatures define the input and output types for a computation. The optional
  save `signatures` argument controls which methods in `obj` will be
  available to programs which consume `SavedModel`s, for example, serving
  APIs. Python functions may be decorated with
  `@tf.function(input_signature=...)` and passed as signatures directly, or
  lazily with a call to `get_concrete_function` on the method decorated with
  `@tf.function`.

  Example:

  >>> class Adder(tf.Module):
  ...   @tf.function
  ...   def add(self, x):
  ...     return x + x

  >>> model = Adder()
  >>> tf.saved_model.save(
  ...   model, \'/tmp/adder\',signatures=model.add.get_concrete_function(
  ...     tf.TensorSpec([], tf.float32)))

  If a `@tf.function` does not have an input signature and
  `get_concrete_function` is not called on that method, the function will not
  be directly callable in the restored SavedModel.

  Example:

  >>> class Adder(tf.Module):
  ...   @tf.function
  ...   def add(self, x):
  ...     return x + x

  >>> model = Adder()
  >>> tf.saved_model.save(model, \'/tmp/adder\')
  >>> restored = tf.saved_model.load(\'/tmp/adder\')
  >>> restored.add(1.)
  Traceback (most recent call last):
  ...
  ValueError: Found zero restored functions for caller function.

  If the `signatures` argument is omitted, `obj` will be searched for
  `@tf.function`-decorated methods. If exactly one traced `@tf.function` is
  found, that method will be used as the default signature for the SavedModel.
  Else, any `@tf.function` attached to `obj` or its dependencies will be
  exported for use with `tf.saved_model.load`.

  When invoking a signature in an exported SavedModel, `Tensor` arguments are
  identified by name. These names will come from the Python function\'s argument
  names by default. They may be overridden by specifying a `name=...` argument
  in the corresponding `tf.TensorSpec` object. Explicit naming is required if
  multiple `Tensor`s are passed through a single argument to the Python
  function.

  The outputs of functions used as `signatures` must either be flat lists, in
  which case outputs will be numbered, or a dictionary mapping string keys to
  `Tensor`, in which case the keys will be used to name outputs.

  Signatures are available in objects returned by `tf.saved_model.load` as a
  `.signatures` attribute. This is a reserved attribute: `tf.saved_model.save`
  on an object with a custom `.signatures` attribute will raise an exception.

  _Using `tf.saved_model.save` with Keras models_

  While Keras has its own [saving and loading
  API](https://www.tensorflow.org/guide/keras/save_and_serialize),
  this function can be used to export Keras models. For example, exporting with
  a signature specified:

  >>> class Adder(tf.keras.Model):
  ...   @tf.function(input_signature=[tf.TensorSpec(shape=[], dtype=tf.string)])
  ...   def concat(self, x):
  ...      return x + x

  >>> model = Adder()
  >>> tf.saved_model.save(model, \'/tmp/adder\')

  Exporting from a function without a fixed signature:

  >>> class Adder(tf.keras.Model):
  ...   @tf.function
  ...   def concat(self, x):
  ...      return x + x

  >>> model = Adder()
  >>> tf.saved_model.save(
  ...   model, \'/tmp/adder\',
  ...   signatures=model.concat.get_concrete_function(
  ...     tf.TensorSpec(shape=[], dtype=tf.string, name="string_input")))

  `tf.keras.Model` instances constructed from inputs and outputs already have a
  signature and so do not require a `@tf.function` decorator or a `signatures`
  argument. If neither are specified, the model\'s forward pass is exported.

  >>> x = tf.keras.layers.Input((4,), name="x")
  >>> y = tf.keras.layers.Dense(5, name="out")(x)
  >>> model = tf.keras.Model(x, y)
  >>> tf.saved_model.save(model, \'/tmp/saved_model/\')

  The exported SavedModel takes "x" with shape [None, 4] and returns "out"
  with shape [None, 5]

  _Variables and Checkpoints_

  Variables must be tracked by assigning them to an attribute of a tracked
  object or to an attribute of `obj` directly. TensorFlow objects (e.g. layers
  from `tf.keras.layers`, optimizers from `tf.train`) track their variables
  automatically. This is the same tracking scheme that `tf.train.Checkpoint`
  uses, and an exported `Checkpoint` object may be restored as a training
  checkpoint by pointing `tf.train.Checkpoint.restore` to the SavedModel\'s
  "variables/" subdirectory.

  `tf.function` does not hard-code device annotations from outside the function
  body, instead of using the calling context\'s device. This means for example
  that exporting a model that runs on a GPU and serving it on a CPU will
  generally work, with some exceptions:

    * `tf.device` annotations inside the body of the function will be hard-coded
      in the exported model; this type of annotation is discouraged.
    * Device-specific operations, e.g. with "cuDNN" in the name or with
      device-specific layouts, may cause issues.
    * For `ConcreteFunctions`, active distribution strategies will cause device
      placements to be hard-coded in the function.

  SavedModels exported with `tf.saved_model.save` [strip default-valued
  attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes)
  automatically, which removes one source of incompatibilities when the consumer
  of a SavedModel is running an older TensorFlow version than the
  producer. There are however other sources of incompatibilities which are not
  handled automatically, such as when the exported model contains operations
  which the consumer does not have definitions for.

  Args:
    obj: A trackable object (e.g. tf.Module or tf.train.Checkpoint) to export.
    export_dir: A directory in which to write the SavedModel.
    signatures: Optional, one of three types: * a `tf.function` with an input
      signature specified, which will use the default serving signature key, *
      the result of `f.get_concrete_function` on a `@tf.function`-decorated
      function `f`, in which case `f` will be used to generate a signature for
      the SavedModel under the default serving signature key, * a dictionary,
      which maps signature keys to either `tf.function` instances with input
      signatures or concrete functions. Keys of such a dictionary may be
      arbitrary strings, but will typically be from the
      `tf.saved_model.signature_constants` module.
    options: `tf.saved_model.SaveOptions` object for configuring save options.

  Raises:
    ValueError: If `obj` is not trackable.

  @compatibility(eager)
  Not well supported when graph building. From TensorFlow 1.x,
  `tf.compat.v1.enable_eager_execution()` should run first. Calling
  tf.saved_model.save in a loop when graph building from TensorFlow 1.x will
  add new save operations to the default graph each iteration.

  May not be called from within a function body.
  @end_compatibility
  '''
def save_and_return_nodes(obj, export_dir, signatures: Incomplete | None = None, options: Incomplete | None = None, experimental_skip_checkpoint: bool = False):
    """Saves a SavedModel while returning all saved nodes and their paths.

  Please see `tf.saved_model.save` for details.

  Args:
    obj: A trackable object to export.
    export_dir: A directory in which to write the SavedModel.
    signatures: A function or dictionary of functions to save in the SavedModel
      as signatures.
    options: `tf.saved_model.SaveOptions` object for configuring save options.
    experimental_skip_checkpoint: If set to `True`, the checkpoint will not be
      written.

  Returns:
    A tuple of (a list of saved nodes in the order they are serialized to the
      `SavedObjectGraph`, dictionary mapping nodes to one possible path from
      the root node to the key node)
  """
def export_meta_graph(obj, filename, signatures: Incomplete | None = None, options: Incomplete | None = None) -> None:
    """Exports the MetaGraph proto of the `obj` to a file.

  This function goes through the same procedures saved_model.save goes to
  produce the given object's MetaGraph, then saves it to the given file. It
  skips saving checkpoint information, and is useful when all one wants is the
  graph defining the model.

  Args:
    obj: A trackable object to build the MetaGraph from.
    filename: The file into which to write the MetaGraph.
    signatures: Optional, either a `tf.function` with an input signature
      specified or the result of `f.get_concrete_function` on a
      `@tf.function`-decorated function `f`, in which case `f` will be used to
      generate a signature for the SavedModel under the default serving
      signature key. `signatures` may also be a dictionary, in which case it
      maps from signature keys to either `tf.function` instances with input
      signatures or concrete functions. The keys of such a dictionary may be
      arbitrary strings, but will typically be from the
      `tf.saved_model.signature_constants` module.
    options: Optional, `tf.saved_model.SaveOptions` object that specifies
      options for saving.
  """
