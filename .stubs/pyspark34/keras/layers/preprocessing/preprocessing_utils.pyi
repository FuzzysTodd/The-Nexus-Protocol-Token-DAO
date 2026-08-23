from _typeshed import Incomplete
from keras.utils import tf_utils as tf_utils

INT: str
ONE_HOT: str
MULTI_HOT: str
COUNT: str
TF_IDF: str

def ensure_tensor(inputs, dtype: Incomplete | None = None):
    """Ensures the input is a Tensor, SparseTensor or RaggedTensor."""
def listify_tensors(x):
    """Convert any tensors or numpy arrays to lists for config serialization."""
def sparse_bincount(inputs, depth, binary_output, dtype, count_weights: Incomplete | None = None):
    """Apply binary or count encoding to an input and return a sparse tensor."""
def dense_bincount(inputs, depth, binary_output, dtype, count_weights: Incomplete | None = None):
    """Apply binary or count encoding to an input."""
def expand_dims(inputs, axis):
    """Expand dims on sparse, ragged, or dense tensors."""
def encode_categorical_inputs(inputs, output_mode, depth, dtype: str = 'float32', sparse: bool = False, count_weights: Incomplete | None = None, idf_weights: Incomplete | None = None):
    """Encodes categoical inputs according to output_mode."""
def compute_shape_for_encode_categorical(shape, output_mode, depth):
    """Computes the output shape of `encode_categorical_inputs`."""
