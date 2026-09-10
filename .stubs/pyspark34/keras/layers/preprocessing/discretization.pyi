from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import base_preprocessing_layer as base_preprocessing_layer
from keras.utils import layer_utils as layer_utils, tf_utils as tf_utils

INT: Incomplete
MULTI_HOT: Incomplete
ONE_HOT: Incomplete
COUNT: Incomplete

def summarize(values, epsilon):
    """Reduce a 1D sequence of values to a summary.

    This algorithm is based on numpy.quantiles but modified to allow for
    intermediate steps between multiple data sets. It first finds the target
    number of bins as the reciprocal of epsilon and then takes the individual
    values spaced at appropriate intervals to arrive at that target.
    The final step is to return the corresponding counts between those values
    If the target num_bins is larger than the size of values, the whole array is
    returned (with weights of 1).

    Args:
        values: 1D `np.ndarray` to be summarized.
        epsilon: A `'float32'` that determines the approximate desired
          precision.

    Returns:
        A 2D `np.ndarray` that is a summary of the inputs. First column is the
        interpolated partition values, the second is the weights (counts).
    """
def compress(summary, epsilon):
    """Compress a summary to within `epsilon` accuracy.

    The compression step is needed to keep the summary sizes small after
    merging, and also used to return the final target boundaries. It finds the
    new bins based on interpolating cumulative weight percentages from the large
    summary.  Taking the difference of the cumulative weights from the previous
    bin's cumulative weight will give the new weight for that bin.

    Args:
        summary: 2D `np.ndarray` summary to be compressed.
        epsilon: A `'float32'` that determines the approxmiate desired
          precision.

    Returns:
        A 2D `np.ndarray` that is a compressed summary. First column is the
        interpolated partition values, the second is the weights (counts).
    """
def merge_summaries(prev_summary, next_summary, epsilon):
    """Weighted merge sort of summaries.

    Given two summaries of distinct data, this function merges (and compresses)
    them to stay within `epsilon` error tolerance.

    Args:
        prev_summary: 2D `np.ndarray` summary to be merged with `next_summary`.
        next_summary: 2D `np.ndarray` summary to be merged with `prev_summary`.
        epsilon: A float that determines the approxmiate desired precision.

    Returns:
        A 2-D `np.ndarray` that is a merged summary. First column is the
        interpolated partition values, the second is the weights (counts).
    """
def get_bin_boundaries(summary, num_bins): ...

class Discretization(base_preprocessing_layer.PreprocessingLayer):
    '''A preprocessing layer which buckets continuous features by ranges.

    This layer will place each element of its input data into one of several
    contiguous ranges and output an integer index indicating which range each
    element was placed in.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Input shape:
      Any `tf.Tensor` or `tf.RaggedTensor` of dimension 2 or higher.

    Output shape:
      Same as input shape.

    Arguments:
      bin_boundaries: A list of bin boundaries. The leftmost and rightmost bins
        will always extend to `-inf` and `inf`, so `bin_boundaries=[0., 1., 2.]`
        generates bins `(-inf, 0.)`, `[0., 1.)`, `[1., 2.)`, and `[2., +inf)`.
        If this option is set, `adapt()` should not be called.
      num_bins: The integer number of bins to compute. If this option is set,
        `adapt()` should be called to learn the bin boundaries.
      epsilon: Error tolerance, typically a small fraction close to zero (e.g.
        0.01). Higher values of epsilon increase the quantile approximation, and
        hence result in more unequal buckets, but could improve performance
        and resource consumption.
      output_mode: Specification for the output of the layer. Defaults to
        `"int"`.  Values can be `"int"`, `"one_hot"`, `"multi_hot"`, or
        `"count"` configuring the layer as follows:
          - `"int"`: Return the discretized bin indices directly.
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

    Examples:

    Bucketize float values based on provided buckets.
    >>> input = np.array([[-1.5, 1.0, 3.4, .5], [0.0, 3.0, 1.3, 0.0]])
    >>> layer = tf.keras.layers.Discretization(bin_boundaries=[0., 1., 2.])
    >>> layer(input)
    <tf.Tensor: shape=(2, 4), dtype=int64, numpy=
    array([[0, 2, 3, 1],
           [1, 3, 2, 1]])>

    Bucketize float values based on a number of buckets to compute.
    >>> input = np.array([[-1.5, 1.0, 3.4, .5], [0.0, 3.0, 1.3, 0.0]])
    >>> layer = tf.keras.layers.Discretization(num_bins=4, epsilon=0.01)
    >>> layer.adapt(input)
    >>> layer(input)
    <tf.Tensor: shape=(2, 4), dtype=int64, numpy=
    array([[0, 2, 3, 2],
           [1, 3, 3, 1]])>
    '''
    input_bin_boundaries: Incomplete
    bin_boundaries: Incomplete
    num_bins: Incomplete
    epsilon: Incomplete
    output_mode: Incomplete
    sparse: Incomplete
    def __init__(self, bin_boundaries: Incomplete | None = None, num_bins: Incomplete | None = None, epsilon: float = 0.01, output_mode: str = 'int', sparse: bool = False, **kwargs) -> None: ...
    summary: Incomplete
    def build(self, input_shape): ...
    def adapt(self, data, batch_size: Incomplete | None = None, steps: Incomplete | None = None) -> None:
        """Computes bin boundaries from quantiles in a input dataset.

        Calling `adapt()` on a `Discretization` layer is an alternative to
        passing in a `bin_boundaries` argument during construction. A
        `Discretization` layer should always be either adapted over a dataset or
        passed `bin_boundaries`.

        During `adapt()`, the layer will estimate the quantile boundaries of the
        input dataset. The number of quantiles can be controlled via the
        `num_bins` argument, and the error tolerance for quantile boundaries can
        be controlled via the `epsilon` argument.

        In order to make `Discretization` efficient in any distribution context,
        the computed boundaries are kept static with respect to any compiled
        `tf.Graph`s that call the layer. As a consequence, if the layer is
        adapted a second time, any models using the layer should be re-compiled.
        For more information see
        `tf.keras.layers.experimental.preprocessing.PreprocessingLayer.adapt`.

        `adapt()` is meant only as a single machine utility to compute layer
        state.  To analyze a dataset that cannot fit on a single machine, see
        [Tensorflow Transform](
        https://www.tensorflow.org/tfx/transform/get_started) for a
        multi-machine, map-reduce solution.

        Arguments:
          data: The data to train on. It can be passed either as a
              `tf.data.Dataset`, or as a numpy array.
          batch_size: Integer or `None`.
              Number of samples per state update.
              If unspecified, `batch_size` will default to 32.
              Do not specify the `batch_size` if your data is in the
              form of datasets, generators, or `keras.utils.Sequence` instances
              (since they generate batches).
          steps: Integer or `None`.
              Total number of steps (batches of samples)
              When training with input tensors such as
              TensorFlow data tensors, the default `None` is equal to
              the number of samples in your dataset divided by
              the batch size, or 1 if that cannot be determined. If x is a
              `tf.data` dataset, and 'steps' is None, the epoch will run until
              the input dataset is exhausted. When passing an infinitely
              repeating dataset, you must specify the `steps` argument. This
              argument is not supported with array inputs.
        """
    def update_state(self, data) -> None: ...
    def finalize_state(self) -> None: ...
    def reset_state(self) -> None: ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...
    def compute_output_signature(self, input_spec): ...
    def call(self, inputs): ...
