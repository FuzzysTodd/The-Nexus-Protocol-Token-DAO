from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import base_layer as base_layer, base_preprocessing_layer as base_preprocessing_layer
from keras.utils import layer_utils as layer_utils

INT: Incomplete
ONE_HOT: Incomplete

class HashedCrossing(base_layer.Layer):
    '''A preprocessing layer which crosses features using the "hashing trick".

    This layer performs crosses of categorical features using the "hasing
    trick".  Conceptually, the transformation can be thought of as:
    hash(concatenation of features) % `num_bins`.

    This layer currently only performs crosses of scalar inputs and batches of
    scalar inputs. Valid input shapes are `(batch_size, 1)`, `(batch_size,)` and
    `()`.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Args:
      num_bins: Number of hash bins.
      output_mode: Specification for the output of the layer. Defaults to
        `"int"`.  Values can be `"int"`, or `"one_hot"` configuring the layer as
        follows:
          - `"int"`: Return the integer bin indices directly.
          - `"one_hot"`: Encodes each individual element in the input into an
            array the same size as `num_bins`, containing a 1 at the input\'s bin
            index.
      sparse: Boolean. Only applicable to `"one_hot"` mode. If True, returns a
        `SparseTensor` instead of a dense `Tensor`. Defaults to False.
      **kwargs: Keyword arguments to construct a layer.

    Examples:

    **Crossing two scalar features.**

    >>> layer = tf.keras.layers.HashedCrossing(
    ...     num_bins=5)
    >>> feat1 = tf.constant([\'A\', \'B\', \'A\', \'B\', \'A\'])
    >>> feat2 = tf.constant([101, 101, 101, 102, 102])
    >>> layer((feat1, feat2))
    <tf.Tensor: shape=(5,), dtype=int64, numpy=array([1, 4, 1, 1, 3])>

    **Crossing and one-hotting two scalar features.**

    >>> layer = tf.keras.layers.HashedCrossing(
    ...     num_bins=5, output_mode=\'one_hot\')
    >>> feat1 = tf.constant([\'A\', \'B\', \'A\', \'B\', \'A\'])
    >>> feat2 = tf.constant([101, 101, 101, 102, 102])
    >>> layer((feat1, feat2))
    <tf.Tensor: shape=(5, 5), dtype=float32, numpy=
      array([[0., 1., 0., 0., 0.],
             [0., 0., 0., 0., 1.],
             [0., 1., 0., 0., 0.],
             [0., 1., 0., 0., 0.],
             [0., 0., 0., 1., 0.]], dtype=float32)>
    '''
    num_bins: Incomplete
    output_mode: Incomplete
    sparse: Incomplete
    def __init__(self, num_bins, output_mode: str = 'int', sparse: bool = False, **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shapes): ...
    def compute_output_signature(self, input_specs): ...
    def get_config(self): ...
