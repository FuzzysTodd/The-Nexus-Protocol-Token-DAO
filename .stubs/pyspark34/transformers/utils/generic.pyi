from .import_utils import is_flax_available as is_flax_available, is_tf_available as is_tf_available, is_torch_available as is_torch_available, is_torch_fx_proxy as is_torch_fx_proxy
from _typeshed import Incomplete
from collections import OrderedDict
from collections.abc import MutableMapping
from enum import Enum
from typing import Any, ContextManager, List, Tuple

class cached_property(property):
    """
    Descriptor that mimics @property but caches output in member variable.

    From tensorflow_datasets

    Built-in in functools from Python 3.8.
    """
    def __get__(self, obj, objtype: Incomplete | None = None): ...

def is_tensor(x):
    """
    Tests if `x` is a `torch.Tensor`, `tf.Tensor`, `jaxlib.xla_extension.DeviceArray` or `np.ndarray`.
    """
def is_numpy_array(x):
    """
    Tests if `x` is a numpy array or not.
    """
def is_torch_tensor(x):
    """
    Tests if `x` is a torch tensor or not. Safe to call even if torch is not installed.
    """
def is_torch_device(x):
    """
    Tests if `x` is a torch device or not. Safe to call even if torch is not installed.
    """
def is_torch_dtype(x):
    """
    Tests if `x` is a torch dtype or not. Safe to call even if torch is not installed.
    """
def is_tf_tensor(x):
    """
    Tests if `x` is a tensorflow tensor or not. Safe to call even if tensorflow is not installed.
    """
def is_jax_tensor(x):
    """
    Tests if `x` is a Jax tensor or not. Safe to call even if jax is not installed.
    """
def to_py_obj(obj):
    """
    Convert a TensorFlow tensor, PyTorch tensor, Numpy array or python list to a python list.
    """
def to_numpy(obj):
    """
    Convert a TensorFlow tensor, PyTorch tensor, Numpy array or python list to a Numpy array.
    """

class ModelOutput(OrderedDict):
    """
    Base class for all model outputs as dataclass. Has a `__getitem__` that allows indexing by integer or slice (like a
    tuple) or strings (like a dictionary) that will ignore the `None` attributes. Otherwise behaves like a regular
    python dictionary.

    <Tip warning={true}>

    You can't unpack a `ModelOutput` directly. Use the [`~utils.ModelOutput.to_tuple`] method to convert it to a tuple
    before.

    </Tip>
    """
    def __post_init__(self) -> None: ...
    def __delitem__(self, *args, **kwargs) -> None: ...
    def setdefault(self, *args, **kwargs) -> None: ...
    def pop(self, *args, **kwargs) -> None: ...
    def update(self, *args, **kwargs) -> None: ...
    def __getitem__(self, k): ...
    def __setattr__(self, name, value) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def to_tuple(self) -> Tuple[Any]:
        """
        Convert self to a tuple containing all the attributes/keys that are not `None`.
        """

class ExplicitEnum(str, Enum):
    """
    Enum with more explicit error message for missing values.
    """

class PaddingStrategy(ExplicitEnum):
    """
    Possible values for the `padding` argument in [`PreTrainedTokenizerBase.__call__`]. Useful for tab-completion in an
    IDE.
    """
    LONGEST: str
    MAX_LENGTH: str
    DO_NOT_PAD: str

class TensorType(ExplicitEnum):
    """
    Possible values for the `return_tensors` argument in [`PreTrainedTokenizerBase.__call__`]. Useful for
    tab-completion in an IDE.
    """
    PYTORCH: str
    TENSORFLOW: str
    NUMPY: str
    JAX: str

class ContextManagers:
    """
    Wrapper for `contextlib.ExitStack` which enters a collection of context managers. Adaptation of `ContextManagers`
    in the `fastcore` library.
    """
    context_managers: Incomplete
    stack: Incomplete
    def __init__(self, context_managers: List[ContextManager]) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args, **kwargs) -> None: ...

def can_return_loss(model_class):
    """
    Check if a given model can return loss.

    Args:
        model_class (`type`): The class of the model.
    """
def find_labels(model_class):
    """
    Find the labels used by a given model.

    Args:
        model_class (`type`): The class of the model.
    """
def flatten_dict(d: MutableMapping, parent_key: str = '', delimiter: str = '.'):
    """Flatten a nested dict into a single level dict."""
def working_or_temp_dir(working_dir, use_temp_dir: bool = False): ...
def transpose(array, axes: Incomplete | None = None):
    """
    Framework-agnostic version of `numpy.transpose` that will work on torch/TensorFlow/Jax tensors as well as NumPy
    arrays.
    """
def reshape(array, newshape):
    """
    Framework-agnostic version of `numpy.reshape` that will work on torch/TensorFlow/Jax tensors as well as NumPy
    arrays.
    """
def squeeze(array, axis: Incomplete | None = None):
    """
    Framework-agnostic version of `numpy.squeeze` that will work on torch/TensorFlow/Jax tensors as well as NumPy
    arrays.
    """
def expand_dims(array, axis):
    """
    Framework-agnostic version of `numpy.expand_dims` that will work on torch/TensorFlow/Jax tensors as well as NumPy
    arrays.
    """
def tensor_size(array):
    """
    Framework-agnostic version of `numpy.size` that will work on torch/TensorFlow/Jax tensors as well as NumPy arrays.
    """
