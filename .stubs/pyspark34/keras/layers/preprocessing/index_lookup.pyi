import tensorflow.compat.v2 as tf
from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import base_layer_utils as base_layer_utils, base_preprocessing_layer as base_preprocessing_layer
from keras.saving.legacy.saved_model import layer_serialization as layer_serialization
from keras.utils import layer_utils as layer_utils, tf_utils as tf_utils

INT: Incomplete
MULTI_HOT: Incomplete
ONE_HOT: Incomplete
COUNT: Incomplete
TF_IDF: Incomplete

class NullInitializer(tf.lookup.KeyValueTensorInitializer):
    """A placeholder initializer for restoring this layer from a SavedModel."""
    def __init__(self, key_dtype, value_dtype) -> None:
        """Construct a table initializer object.

        Args:
          key_dtype: Type of the table keys.
          value_dtype: Type of the table values.
        """
    @property
    def key_dtype(self):
        """The expected table key dtype."""
    @property
    def value_dtype(self):
        """The expected table value dtype."""
    def initialize(self, table) -> None:
        """Returns the table initialization op."""

class VocabWeightHandler(base_layer_utils.TrackableWeightHandler):
    """Adds the vocabulary as a layer weight during serialization."""
    def __init__(self, lookup_layer) -> None: ...
    @property
    def num_tensors(self): ...
    def set_weights(self, weights) -> None: ...
    def get_tensors(self): ...

class IndexLookup(base_preprocessing_layer.PreprocessingLayer):
    '''Maps values from a vocabulary to integer indices.

    This layer translates a set of arbitrary hashables into an integer output
    via a table-based lookup, with optional out-of-vocabulary handling. This is
    the basis layer for both IntegerLookup and StringLookup; it holds the common
    logic but is not intended to be exported as part of the Keras API.

    Args:
      max_tokens: The maximum size of the vocabulary for this layer. If None,
        there is no cap on the size of the vocabulary. Note that this size
        includes the OOV and mask tokens.
      num_oov_indices: The number of out-of-vocabulary tokens to use. If this
        value is more than 1, OOV inputs are hashed to determine their OOV
        value. If this value is 0, OOV inputs will cause an error when calling
        the layer.
      mask_token: A token that represents masked inputs. When `output_mode` is
        `"int"`, the token is included in vocabulary and mapped to index 0. In
        other output modes, the token will not appear in the vocabulary and
        instances of the mask token in the input will be dropped. If set to
        None, no mask term will be added.
      oov_token: Only used when `invert` is True. The token to return for OOV
        indices.
      vocabulary: Optional. Either an array or a string path to a text file. If
        passing an array, can pass a tuple, list, 1D numpy array, or 1D tensor
        containing the vocbulary terms. If passing a file path, the file should
        contain one line per term in the vocabulary. If this argument is set,
        there is no need to `adapt` the layer.
      vocabulary_dtype: The dtype of the vocabulary terms. For example,
        `"int64"` or `"string"`.
      idf_weights: Only valid when `output_mode` is `"tf_idf"`. A tuple, list,
        1D numpy array, or 1D tensor or the same length as the vocabulary,
        containing the floating point inverse document frequency weights, which
        will be multiplied by per sample term counts for the final `tf_idf`
        weight. If the `vocabulary` argument is set, and `output_mode` is
        `"tf_idf"`, this argument must be supplied.
      invert: Only valid when `output_mode` is `"int"`. If True, this layer will
        map indices to vocabulary items instead of mapping vocabulary items to
        indices. Default to False.
      output_mode: Specification for the output of the layer. Defaults to
        `"int"`.  Values can be `"int"`, `"one_hot"`, `"multi_hot"`, `"count"`,
        or `"tf_idf"` configuring the layer as follows:
          - `"int"`: Return the raw integer indices of the input tokens.
          - `"one_hot"`: Encodes each individual element in the input into an
            array the same size as the vocabulary, containing a 1 at the element
            index. If the last dimension is size 1, will encode on that
            dimension.  If the last dimension is not size 1, will append a new
            dimension for the encoded output.
          - `"multi_hot"`: Encodes each sample in the input into a single array
            the same size as the vocabulary, containing a 1 for each vocabulary
            term present in the sample. Treats the last dimension as the sample
            dimension, if input shape is (..., sample_length), output shape will
            be (..., num_tokens).
          - `"count"`: As `"multi_hot"`, but the int array contains a count of
            the number of times the token at that index appeared in the sample.
          - `"tf_idf"`: As `"multi_hot"`, but the TF-IDF algorithm is applied to
            find the value in each token slot.
      pad_to_max_tokens: Only valid when `output_mode` is `"multi_hot"`,
        `"count"`, or `"tf_idf"`. If True, the output will have its feature axis
        padded to `max_tokens` even if the number of unique tokens in the
        vocabulary is less than max_tokens, resulting in a tensor of shape
        [batch_size, max_tokens] regardless of vocabulary size. Defaults to
        False.
      sparse: Boolean. Only applicable to `"one_hot"`, `"multi_hot"`, `"count"`
        and `"tf-idf"` output modes. If True, returns a `SparseTensor` instead
        of a dense `Tensor`. Defaults to False.
    '''
    invert: Incomplete
    max_tokens: Incomplete
    num_oov_indices: Incomplete
    mask_token: Incomplete
    oov_token: Incomplete
    output_mode: Incomplete
    sparse: Incomplete
    pad_to_max_tokens: Incomplete
    vocabulary_dtype: Incomplete
    input_vocabulary: Incomplete
    input_idf_weights: Incomplete
    idf_weights: Incomplete
    idf_weights_const: Incomplete
    lookup_table: Incomplete
    token_counts: Incomplete
    token_document_counts: Incomplete
    num_documents: Incomplete
    def __init__(self, max_tokens, num_oov_indices, mask_token, oov_token, vocabulary_dtype, vocabulary: Incomplete | None = None, idf_weights: Incomplete | None = None, invert: bool = False, output_mode: str = 'int', sparse: bool = False, pad_to_max_tokens: bool = False, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def compute_output_signature(self, input_spec): ...
    def get_vocabulary(self, include_special_tokens: bool = True):
        """Returns the current vocabulary of the layer.

        Args:
          include_special_tokens: If True, the returned vocabulary will include
            mask and OOV tokens, and a term's index in the vocabulary will equal
            the term's index when calling the layer. If False, the returned
            vocabulary will not include any mask or OOV tokens.
        """
    def vocabulary_size(self):
        """Gets the current size of the layer's vocabulary.

        Returns:
          The integer size of the vocabulary, including optional mask and oov
          indices.
        """
    def vocab_size(self): ...
    def get_config(self): ...
    def set_vocabulary(self, vocabulary, idf_weights: Incomplete | None = None) -> None:
        '''Sets vocabulary (and optionally document frequency) for this layer.

        This method sets the vocabulary and idf weights for this layer directly,
        instead of analyzing a dataset through `adapt`. It should be used
        whenever the vocab (and optionally document frequency) information is
        already known.  If vocabulary data is already present in the layer, this
        method will replace it.

        Args:
          vocabulary: Either an array or a string path to a text file. If
            passing an array, can pass a tuple, list, 1D numpy array, or 1D
            tensor containing the vocbulary terms. If passing a file path, the
            file should contain one line per term in the vocabulary.
          idf_weights: A tuple, list, 1D numpy array, or 1D tensor of inverse
            document frequency weights with equal length to vocabulary. Must be
            set if `output_mode` is `"tf_idf"`. Should not be set otherwise.

        Raises:
          ValueError: If there are too many inputs, the inputs do not match, or
            input data is missing.
          RuntimeError: If the vocabulary cannot be set when this function is
            called. This happens when `"multi_hot"`, `"count"`, and `"tf_idf"`
            modes, if `pad_to_max_tokens` is False and the layer itself has
            already been called.
          RuntimeError: If a tensor vocabulary is passed outside of eager
            execution.
        '''
    def update_state(self, data): ...
    def finalize_state(self) -> None: ...
    def reset_state(self) -> None: ...
    def call(self, inputs): ...
