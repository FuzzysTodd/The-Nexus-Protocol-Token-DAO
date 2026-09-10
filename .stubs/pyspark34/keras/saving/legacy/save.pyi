from _typeshed import Incomplete
from keras import backend as backend
from keras.saving import object_registration as object_registration
from keras.saving.legacy import hdf5_format as hdf5_format, saving_utils as saving_utils, serialization as serialization
from keras.saving.legacy.saved_model import load_context as load_context
from keras.saving.legacy.saved_model.utils import keras_option_scope as keras_option_scope
from keras.utils import io_utils as io_utils, traceback_utils as traceback_utils

def save_model(model, filepath, overwrite: bool = True, include_optimizer: bool = True, save_format: Incomplete | None = None, signatures: Incomplete | None = None, options: Incomplete | None = None, save_traces: bool = True) -> None:
    '''Saves a model as a TensorFlow SavedModel or HDF5 file.

    See the [Serialization and Saving
    guide](https://keras.io/guides/serialization_and_saving/) for details.

    Usage:

    >>> model = tf.keras.Sequential([
    ...     tf.keras.layers.Dense(5, input_shape=(3,)),
    ...     tf.keras.layers.Softmax()])
    >>> model.save(\'/tmp/model\')
    >>> loaded_model = tf.keras.models.load_model(\'/tmp/model\')
    >>> x = tf.random.uniform((10, 3))
    >>> assert np.allclose(model.predict(x), loaded_model.predict(x))

    Note that `model.save()` is an alias for `tf.keras.models.save_model()`.

    The SavedModel and HDF5 file contains:

    - the model\'s configuration (topology)
    - the model\'s weights
    - the model\'s optimizer\'s state (if any)

    Thus models can be reinstantiated in the exact same state, without any of
    the code used for model definition or training.

    Note that the model weights may have different scoped names after being
    loaded. Scoped names include the model/layer names, such as
    `"dense_1/kernel:0"`. It is recommended that you use the layer properties to
    access specific variables, e.g. `model.get_layer("dense_1").kernel`.

    __SavedModel serialization format__

    Keras SavedModel uses `tf.saved_model.save` to save the model and all
    trackable objects attached to the model (e.g. layers and variables). The
    model config, weights, and optimizer are saved in the SavedModel.
    Additionally, for every Keras layer attached to the model, the SavedModel
    stores:

      * the config and metadata -- e.g. name, dtype, trainable status
      * traced call and loss functions, which are stored as TensorFlow
        subgraphs.

    The traced functions allow the SavedModel format to save and load custom
    layers without the original class definition.

    You can choose to not save the traced functions by disabling the
    `save_traces` option. This will decrease the time it takes to save the model
    and the amount of disk space occupied by the output SavedModel. If you
    enable this option, then you _must_ provide all custom class definitions
    when loading the model. See the `custom_objects` argument in
    `tf.keras.models.load_model`.

    Args:
        model: Keras model instance to be saved.
        filepath: One of the following:
          - String or `pathlib.Path` object, path where to save the model
          - `h5py.File` object where to save the model
        overwrite: Whether we should overwrite any existing model at the target
          location, or instead ask the user with a manual prompt.
        include_optimizer: If True, save optimizer\'s state together.
        save_format: Either \'tf\' or \'h5\', indicating whether to save the model
          to Tensorflow SavedModel or HDF5. Defaults to \'tf\' in TF 2.X, and \'h5\'
          in TF 1.X.
        signatures: Signatures to save with the SavedModel. Applicable to the
          \'tf\' format only. Please see the `signatures` argument in
          `tf.saved_model.save` for details.
        options: (only applies to SavedModel format)
          `tf.saved_model.SaveOptions` object that specifies options for saving
          to SavedModel.
        save_traces: (only applies to SavedModel format) When enabled, the
          SavedModel will store the function traces for each layer. This
          can be disabled, so that only the configs of each layer are stored.
          Defaults to `True`. Disabling this will decrease serialization time
          and reduce file size, but it requires that all custom layers/models
          implement a `get_config()` method.

    Raises:
        ImportError: If save format is hdf5, and h5py is not available.
    '''
def load_model(filepath, custom_objects: Incomplete | None = None, compile: bool = True, options: Incomplete | None = None):
    '''Loads a model saved via `model.save()`.

    Usage:

    >>> model = tf.keras.Sequential([
    ...     tf.keras.layers.Dense(5, input_shape=(3,)),
    ...     tf.keras.layers.Softmax()])
    >>> model.save(\'/tmp/model\')
    >>> loaded_model = tf.keras.models.load_model(\'/tmp/model\')
    >>> x = tf.random.uniform((10, 3))
    >>> assert np.allclose(model.predict(x), loaded_model.predict(x))

    Note that the model weights may have different scoped names after being
    loaded. Scoped names include the model/layer names, such as
    `"dense_1/kernel:0"`. It is recommended that you use the layer properties to
    access specific variables, e.g. `model.get_layer("dense_1").kernel`.

    Args:
        filepath: One of the following:
            - String or `pathlib.Path` object, path to the saved model
            - `h5py.File` object from which to load the model
        custom_objects: Optional dictionary mapping names
            (strings) to custom classes or functions to be
            considered during deserialization.
        compile: Boolean, whether to compile the model
            after loading.
        options: Optional `tf.saved_model.LoadOptions` object that specifies
          options for loading from SavedModel.

    Returns:
        A Keras model instance. If the original model was compiled, and saved
        with the optimizer, then the returned model will be compiled. Otherwise,
        the model will be left uncompiled. In the case that an uncompiled model
        is returned, a warning is displayed if the `compile` argument is set to
        `True`.

    Raises:
        ImportError: if loading from an hdf5 file and h5py is not available.
        IOError: In case of an invalid savefile.
    '''
def save_weights(model, filepath, overwrite: bool = True, save_format: Incomplete | None = None, options: Incomplete | None = None) -> None:
    """Saves all layer weights.

    Either saves in HDF5 or in TensorFlow format based on the `save_format`
    argument.

    When saving in HDF5 format, the weight file has:
        - `layer_names` (attribute), a list of strings
            (ordered names of model layers).
        - For every layer, a `group` named `layer.name`
            - For every such layer group, a group attribute `weight_names`,
                a list of strings
                (ordered names of weights tensor of the layer).
            - For every weight in the layer, a dataset
                storing the weight value, named after the weight tensor.

    When saving in TensorFlow format, all objects referenced by the network
    are saved in the same format as `tf.train.Checkpoint`, including any
    `Layer` instances or `Optimizer` instances assigned to object
    attributes. For networks constructed from inputs and outputs using
    `tf.keras.Model(inputs, outputs)`, `Layer` instances used by the network
    are tracked/saved automatically. For user-defined classes which inherit
    from `tf.keras.Model`, `Layer` instances must be assigned to object
    attributes, typically in the constructor. See the documentation of
    `tf.train.Checkpoint` and `tf.keras.Model` for details.

    While the formats are the same, do not mix `save_weights` and
    `tf.train.Checkpoint`. Checkpoints saved by `Model.save_weights` should
    be loaded using `Model.load_weights`. Checkpoints saved using
    `tf.train.Checkpoint.save` should be restored using the corresponding
    `tf.train.Checkpoint.restore`. Prefer `tf.train.Checkpoint` over
    `save_weights` for training checkpoints.

    The TensorFlow format matches objects and variables by starting at a
    root object, `self` for `save_weights`, and greedily matching attribute
    names. For `Model.save` this is the `Model`, and for `Checkpoint.save`
    this is the `Checkpoint` even if the `Checkpoint` has a model attached.
    This means saving a `tf.keras.Model` using `save_weights` and loading
    into a `tf.train.Checkpoint` with a `Model` attached (or vice versa)
    will not match the `Model`'s variables. See the
    [guide to training checkpoints](
    https://www.tensorflow.org/guide/checkpoint) for details on
    the TensorFlow format.

    Args:
        filepath: String or PathLike, path to the file to save the weights
            to. When saving in TensorFlow format, this is the prefix used
            for checkpoint files (multiple files are generated). Note that
            the '.h5' suffix causes weights to be saved in HDF5 format.
        overwrite: Whether to silently overwrite any existing file at the
            target location, or provide the user with a manual prompt.
        save_format: Either 'tf' or 'h5'. A `filepath` ending in '.h5' or
            '.keras' will default to HDF5 if `save_format` is `None`.
            Otherwise `None` defaults to 'tf'.
        options: Optional `tf.train.CheckpointOptions` object that specifies
            options for saving weights.

    Raises:
        ImportError: If `h5py` is not available when attempting to save in
            HDF5 format.
    """
def load_weights(model, filepath, by_name: bool = False, skip_mismatch: bool = False, options: Incomplete | None = None):
    """Loads all layer weights, either from a SavedModel or H5 weights file.

    If `by_name` is False weights are loaded based on the network's
    topology. This means the architecture should be the same as when the
    weights were saved.  Note that layers that don't have weights are not
    taken into account in the topological ordering, so adding or removing
    layers is fine as long as they don't have weights.

    If `by_name` is True, weights are loaded into layers only if they share
    the same name. This is useful for fine-tuning or transfer-learning
    models where some of the layers have changed.

    Only topological loading (`by_name=False`) is supported when loading
    weights from the TensorFlow format. Note that topological loading
    differs slightly between TensorFlow and HDF5 formats for user-defined
    classes inheriting from `tf.keras.Model`: HDF5 loads based on a
    flattened list of weights, while the TensorFlow format loads based on
    the object-local names of attributes to which layers are assigned in the
    `Model`'s constructor.

    Args:
        filepath: String, path to the weights file to load. For weight files
            in TensorFlow format, this is the file prefix (the same as was
            passed to `save_weights`). This can also be a path to a
            SavedModel saved from `model.save`.
        by_name: Boolean, whether to load weights by name or by topological
            order. Only topological loading is supported for weight files in
            TensorFlow format.
        skip_mismatch: Boolean, whether to skip loading of layers where
            there is a mismatch in the number of weights, or a mismatch in
            the shape of the weight (only valid when `by_name=True`).
        options: Optional `tf.train.CheckpointOptions` object that specifies
            options for loading weights.

    Returns:
        When loading a weight file in TensorFlow format, returns the same
        status object as `tf.train.Checkpoint.restore`. When graph building,
        restore ops are run automatically as soon as the network is built
        (on first call for user-defined classes inheriting from `Model`,
        immediately if it is already built).

        When loading weights in HDF5 format, returns `None`.

    Raises:
        ImportError: If `h5py` is not available and the weight file is in
            HDF5 format.
        ValueError: If `skip_mismatch` is set to `True` when `by_name` is
            `False`.
    """
