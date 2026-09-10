from _typeshed import Incomplete
from keras import losses as losses
from keras.engine import base_layer as base_layer
from keras.optimizers import optimizer as optimizer
from keras.saving.serialization_lib import ObjectSharingScope as ObjectSharingScope, deserialize_keras_object as deserialize_keras_object, serialize_keras_object as serialize_keras_object
from keras.utils import generic_utils as generic_utils, io_utils as io_utils

ATTR_SKIPLIST: Incomplete

def save_model(model, filepath, weights_format: str = 'h5') -> None:
    """Save a zip-archive representing a Keras model to the given filepath.

    The zip-based archive contains the following structure:

    - JSON-based configuration file (config.json): Records of model, layer, and
        other trackables' configuration.
    - NPZ-based trackable state files, found in respective directories, such as
        model/states.npz, model/dense_layer/states.npz, etc.
    - Metadata file.

    The states of Keras trackables (layers, optimizers, loss, and metrics) are
    automatically saved as long as they can be discovered through the attributes
    returned by `dir(Model)`. Typically, the state includes the variables
    associated with the trackable, but some specially purposed layers may
    contain more such as the vocabularies stored in the hashmaps. The trackables
    define how their states are saved by exposing `save_state()` and
    `load_state()` APIs.

    For the case of layer states, the variables will be visited as long as
    they are either 1) referenced via layer attributes, or 2) referenced via a
    container (list, tuple, or dict), and the container is referenced via a
    layer attribute.
    """
def load_model(filepath, custom_objects: Incomplete | None = None, compile: bool = True, safe_mode: bool = True):
    """Load a zip archive representing a Keras model."""
def save_weights_only(model, filepath) -> None:
    """Save only the weights of a model to a target filepath (.weights.h5).

    Note: only supports h5 for now.
    """
def load_weights_only(model, filepath, skip_mismatch: bool = False) -> None:
    """Load the weights of a model from a filepath (.keras or .weights.h5).

    Note: only supports h5 for now.
    """

class DiskIOStore:
    """Asset store backed by disk storage.

    If `archive` is specified, then `root_path` refers to the filename
    inside the archive.

    If `archive` is not specified, then `root_path` refers to the full path of
    the target directory.
    """
    mode: Incomplete
    root_path: Incomplete
    archive: Incomplete
    tmp_dir: Incomplete
    working_dir: Incomplete
    def __init__(self, root_path, archive: Incomplete | None = None, mode: Incomplete | None = None) -> None: ...
    def make(self, path): ...
    def get(self, path): ...
    def close(self) -> None: ...

class H5IOStore:
    root_path: Incomplete
    mode: Incomplete
    archive: Incomplete
    io_file: Incomplete
    h5_file: Incomplete
    def __init__(self, root_path, archive: Incomplete | None = None, mode: str = 'r') -> None:
        """Numerical variable store backed by HDF5.

        If `archive` is specified, then `root_path` refers to the filename
        inside the archive.

        If `archive` is not specified, then `root_path` refers to the path of
        the h5 file on disk.
        """
    def make(self, path): ...
    def get(self, path): ...
    def close(self) -> None: ...

class NpzIOStore:
    root_path: Incomplete
    mode: Incomplete
    archive: Incomplete
    contents: Incomplete
    f: Incomplete
    def __init__(self, root_path, archive: Incomplete | None = None, mode: str = 'r') -> None:
        """Numerical variable store backed by NumPy.savez/load.

         If `archive` is specified, then `root_path` refers to the filename
        inside the archive.

        If `archive` is not specified, then `root_path` refers to the path of
        the npz file on disk.
        """
    def make(self, path): ...
    def get(self, path): ...
    def close(self) -> None: ...

def saving_v3_enabled(): ...
