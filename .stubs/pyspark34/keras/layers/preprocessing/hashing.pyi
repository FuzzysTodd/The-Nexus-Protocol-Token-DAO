from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import base_layer as base_layer, base_preprocessing_layer as base_preprocessing_layer
from keras.utils import layer_utils as layer_utils

INT: Incomplete
MULTI_HOT: Incomplete
ONE_HOT: Incomplete
COUNT: Incomplete

class Hashing(base_layer.Layer):
    '''A preprocessing layer which hashes and bins categorical features.

    This layer transforms categorical inputs to hashed output. It element-wise
    converts a ints or strings to ints in a fixed range. The stable hash
    function uses `tensorflow::ops::Fingerprint` to produce the same output
    consistently across all platforms.

    This layer uses [FarmHash64](https://github.com/google/farmhash) by default,
    which provides a consistent hashed output across different platforms and is
    stable across invocations, regardless of device and context, by mixing the
    input bits thoroughly.

    If you want to obfuscate the hashed output, you can also pass a random
    `salt` argument in the constructor. In that case, the layer will use the
    [SipHash64](https://github.com/google/highwayhash) hash function, with
    the `salt` value serving as additional input to the hash function.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    **Example (FarmHash64)**

    >>> layer = tf.keras.layers.Hashing(num_bins=3)
    >>> inp = [[\'A\'], [\'B\'], [\'C\'], [\'D\'], [\'E\']]
    >>> layer(inp)
    <tf.Tensor: shape=(5, 1), dtype=int64, numpy=
      array([[1],
             [0],
             [1],
             [1],
             [2]])>

    **Example (FarmHash64) with a mask value**

    >>> layer = tf.keras.layers.Hashing(num_bins=3, mask_value=\'\')
    >>> inp = [[\'A\'], [\'B\'], [\'\'], [\'C\'], [\'D\']]
    >>> layer(inp)
    <tf.Tensor: shape=(5, 1), dtype=int64, numpy=
      array([[1],
             [1],
             [0],
             [2],
             [2]])>

    **Example (SipHash64)**

    >>> layer = tf.keras.layers.Hashing(num_bins=3, salt=[133, 137])
    >>> inp = [[\'A\'], [\'B\'], [\'C\'], [\'D\'], [\'E\']]
    >>> layer(inp)
    <tf.Tensor: shape=(5, 1), dtype=int64, numpy=
      array([[1],
             [2],
             [1],
             [0],
             [2]])>

    **Example (Siphash64 with a single integer, same as `salt=[133, 133]`)**

    >>> layer = tf.keras.layers.Hashing(num_bins=3, salt=133)
    >>> inp = [[\'A\'], [\'B\'], [\'C\'], [\'D\'], [\'E\']]
    >>> layer(inp)
    <tf.Tensor: shape=(5, 1), dtype=int64, numpy=
      array([[0],
             [0],
             [2],
             [1],
             [0]])>

    Args:
      num_bins: Number of hash bins. Note that this includes the `mask_value`
        bin, so the effective number of bins is `(num_bins - 1)` if `mask_value`
        is set.
      mask_value: A value that represents masked inputs, which are mapped to
        index 0. Defaults to None, meaning no mask term will be added and the
        hashing will start at index 0.
      salt: A single unsigned integer or None.
        If passed, the hash function used will be SipHash64, with these values
        used as an additional input (known as a "salt" in cryptography).
        These should be non-zero. Defaults to `None` (in that
        case, the FarmHash64 hash function is used). It also supports
        tuple/list of 2 unsigned integer numbers, see reference paper for
        details.
      output_mode: Specification for the output of the layer. Defaults to
        `"int"`.  Values can be `"int"`, `"one_hot"`, `"multi_hot"`, or
        `"count"` configuring the layer as follows:
          - `"int"`: Return the integer bin indices directly.
          - `"one_hot"`: Encodes each individual element in the input into an
            array the same size as `num_bins`, containing a 1 at the input\'s bin
            index. If the last dimension is size 1, will encode on that
            dimension.  If the last dimension is not size 1, will append a new
            dimension for the encoded output.
          - `"multi_hot"`: Encodes each sample in the input into a single array
            the same size as `num_bins`, containing a 1 for each bin index
            index present in the sample. Treats the last dimension as the sample
            dimension, if input shape is `(..., sample_length)`, output shape
            will be `(..., num_tokens)`.
          - `"count"`: As `"multi_hot"`, but the int array contains a count of
            the number of times the bin index appeared in the sample.
      sparse: Boolean. Only applicable to `"one_hot"`, `"multi_hot"`,
        and `"count"` output modes. If True, returns a `SparseTensor` instead of
        a dense `Tensor`. Defaults to False.
      **kwargs: Keyword arguments to construct a layer.

    Input shape:
      A single or list of string, int32 or int64 `Tensor`,
      `SparseTensor` or `RaggedTensor` of shape `(batch_size, ...,)`

    Output shape:
      An int64 `Tensor`, `SparseTensor` or `RaggedTensor` of shape
      `(batch_size, ...)`. If any input is `RaggedTensor` then output is
      `RaggedTensor`, otherwise if any input is `SparseTensor` then output is
      `SparseTensor`, otherwise the output is `Tensor`.

    Reference:
      - [SipHash with salt](https://www.131002.net/siphash/siphash.pdf)

    '''
    num_bins: Incomplete
    mask_value: Incomplete
    strong_hash: Incomplete
    output_mode: Incomplete
    sparse: Incomplete
    salt: Incomplete
    def __init__(self, num_bins, mask_value: Incomplete | None = None, salt: Incomplete | None = None, output_mode: str = 'int', sparse: bool = False, **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def compute_output_signature(self, input_spec): ...
    def get_config(self): ...
