import abc
from _typeshed import Incomplete
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.layers import base as base
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, embedding_ops as embedding_ops, init_ops as init_ops, lookup_ops as lookup_ops, math_ops as math_ops, nn_ops as nn_ops, parsing_ops as parsing_ops, resource_variable_ops as resource_variable_ops, sparse_ops as sparse_ops, string_ops as string_ops, template as template, variable_scope as variable_scope, variables as variables
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.training import checkpoint_utils as checkpoint_utils
from tensorflow.python.util import deprecation as deprecation, nest as nest
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import NamedTuple

def input_layer(features, feature_columns, weight_collections: Incomplete | None = None, trainable: bool = True, cols_to_vars: Incomplete | None = None, cols_to_output_tensors: Incomplete | None = None):
    '''Returns a dense `Tensor` as input layer based on given `feature_columns`.

  Generally a single example in training data is described with FeatureColumns.
  At the first layer of the model, this column oriented data should be converted
  to a single `Tensor`.

  Example:

  ```python
  price = numeric_column(\'price\')
  keywords_embedded = embedding_column(
      categorical_column_with_hash_bucket("keywords", 10K), dimensions=16)
  columns = [price, keywords_embedded, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  dense_tensor = input_layer(features, columns)
  for units in [128, 64, 32]:
    dense_tensor = tf.compat.v1.layers.dense(dense_tensor, units, tf.nn.relu)
  prediction = tf.compat.v1.layers.dense(dense_tensor, 1)
  ```

  Args:
    features: A mapping from key to tensors. `_FeatureColumn`s look up via these
      keys. For example `numeric_column(\'price\')` will look at \'price\' key in
      this dict. Values can be a `SparseTensor` or a `Tensor` depends on
      corresponding `_FeatureColumn`.
    feature_columns: An iterable containing the FeatureColumns to use as inputs
      to your model. All items should be instances of classes derived from
      `_DenseColumn` such as `numeric_column`, `embedding_column`,
      `bucketized_column`, `indicator_column`. If you have categorical features,
      you can wrap them with an `embedding_column` or `indicator_column`.
    weight_collections: A list of collection names to which the Variable will be
      added. Note that variables will also be added to collections
      `tf.GraphKeys.GLOBAL_VARIABLES` and `ops.GraphKeys.MODEL_VARIABLES`.
    trainable: If `True` also add the variable to the graph collection
      `GraphKeys.TRAINABLE_VARIABLES` (see `tf.Variable`).
    cols_to_vars: If not `None`, must be a dictionary that will be filled with a
      mapping from `_FeatureColumn` to list of `Variable`s.  For example, after
      the call, we might have cols_to_vars = {_EmbeddingColumn(
      categorical_column=_HashedCategoricalColumn( key=\'sparse_feature\',
      hash_bucket_size=5, dtype=tf.string), dimension=10): [<tf.Variable
      \'some_variable:0\' shape=(5, 10), <tf.Variable \'some_variable:1\' shape=(5,
      10)]} If a column creates no variables, its value will be an empty list.
    cols_to_output_tensors: If not `None`, must be a dictionary that will be
      filled with a mapping from \'_FeatureColumn\' to the associated output
      `Tensor`s.

  Returns:
    A `Tensor` which represents input layer of a model. Its shape
    is (batch_size, first_layer_dimension) and its dtype is `float32`.
    first_layer_dimension is determined based on given `feature_columns`.

  Raises:
    ValueError: if an item in `feature_columns` is not a `_DenseColumn`.
  '''

class InputLayer:
    """An object-oriented version of `input_layer` that reuses variables."""
    def __init__(self, feature_columns, weight_collections: Incomplete | None = None, trainable: bool = True, cols_to_vars: Incomplete | None = None, name: str = 'feature_column_input_layer', create_scope_now: bool = True) -> None:
        """See `input_layer`."""
    def __call__(self, features): ...
    @property
    def name(self): ...
    @property
    def non_trainable_variables(self): ...
    @property
    def non_trainable_weights(self): ...
    @property
    def trainable_variables(self): ...
    @property
    def trainable_weights(self): ...
    @property
    def variables(self): ...
    @property
    def weights(self): ...

def linear_model(features, feature_columns, units: int = 1, sparse_combiner: str = 'sum', weight_collections: Incomplete | None = None, trainable: bool = True, cols_to_vars: Incomplete | None = None):
    '''Returns a linear prediction `Tensor` based on given `feature_columns`.

  This function generates a weighted sum based on output dimension `units`.
  Weighted sum refers to logits in classification problems. It refers to the
  prediction itself for linear regression problems.

  Note on supported columns: `linear_model` treats categorical columns as
  `indicator_column`s. To be specific, assume the input as `SparseTensor` looks
  like:

  ```python
    shape = [2, 2]
    {
        [0, 0]: "a"
        [1, 0]: "b"
        [1, 1]: "c"
    }
  ```
  `linear_model` assigns weights for the presence of "a", "b", "c\' implicitly,
  just like `indicator_column`, while `input_layer` explicitly requires wrapping
  each of categorical columns with an `embedding_column` or an
  `indicator_column`.

  Example of usage:

  ```python
  price = numeric_column(\'price\')
  price_buckets = bucketized_column(price, boundaries=[0., 10., 100., 1000.])
  keywords = categorical_column_with_hash_bucket("keywords", 10K)
  keywords_price = crossed_column(\'keywords\', price_buckets, ...)
  columns = [price_buckets, keywords, keywords_price ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  prediction = linear_model(features, columns)
  ```

  The `sparse_combiner` argument works as follows
  For example, for two features represented as the categorical columns:

  ```python
    # Feature 1

    shape = [2, 2]
    {
        [0, 0]: "a"
        [0, 1]: "b"
        [1, 0]: "c"
    }

    # Feature 2

    shape = [2, 3]
    {
        [0, 0]: "d"
        [1, 0]: "e"
        [1, 1]: "f"
        [1, 2]: "f"
    }
  ```

  with `sparse_combiner` as "mean", the linear model outputs consequently
  are:

  ```
    y_0 = 1.0 / 2.0 * ( w_a + w_b ) + w_d + b
    y_1 = w_c + 1.0 / 3.0 * ( w_e + 2.0 * w_f ) + b
  ```

  where `y_i` is the output, `b` is the bias, and `w_x` is the weight
  assigned to the presence of `x` in the input features.

  Args:
    features: A mapping from key to tensors. `_FeatureColumn`s look up via these
      keys. For example `numeric_column(\'price\')` will look at \'price\' key in
      this dict. Values are `Tensor` or `SparseTensor` depending on
      corresponding `_FeatureColumn`.
    feature_columns: An iterable containing the FeatureColumns to use as inputs
      to your model. All items should be instances of classes derived from
      `_FeatureColumn`s.
    units: An integer, dimensionality of the output space. Default value is 1.
    sparse_combiner: A string specifying how to reduce if a categorical column
      is multivalent. Except `numeric_column`, almost all columns passed to
      `linear_model` are considered as categorical columns.  It combines each
      categorical column independently. Currently "mean", "sqrtn" and "sum" are
      supported, with "sum" the default for linear model. "sqrtn" often achieves
      good accuracy, in particular with bag-of-words columns.
        * "sum": do not
        normalize features in the column
        * "mean": do l1 normalization on features
        in the column
        * "sqrtn": do l2 normalization on features in the column
    weight_collections: A list of collection names to which the Variable will be
      added. Note that, variables will also be added to collections
      `tf.GraphKeys.GLOBAL_VARIABLES` and `ops.GraphKeys.MODEL_VARIABLES`.
    trainable: If `True` also add the variable to the graph collection
      `GraphKeys.TRAINABLE_VARIABLES` (see `tf.Variable`).
    cols_to_vars: If not `None`, must be a dictionary that will be filled with a
      mapping from `_FeatureColumn` to associated list of `Variable`s.  For
      example, after the call, we might have cols_to_vars = { _NumericColumn(
      key=\'numeric_feature1\', shape=(1,): [<tf.Variable
      \'linear_model/price2/weights:0\' shape=(1, 1)>], \'bias\': [<tf.Variable
      \'linear_model/bias_weights:0\' shape=(1,)>], _NumericColumn(
      key=\'numeric_feature2\', shape=(2,)): [<tf.Variable
      \'linear_model/price1/weights:0\' shape=(2, 1)>]} If a column creates no
      variables, its value will be an empty list. Note that cols_to_vars will
      also contain a string key \'bias\' that maps to a list of Variables.

  Returns:
    A `Tensor` which represents predictions/logits of a linear model. Its shape
    is (batch_size, units) and its dtype is `float32`.

  Raises:
    ValueError: if an item in `feature_columns` is neither a `_DenseColumn`
      nor `_CategoricalColumn`.
  '''

class _FCLinearWrapper(base.Layer):
    """Wraps a _FeatureColumn in a layer for use in a linear model.

  See `linear_model` above.
  """
    def __init__(self, feature_column, units: int = 1, sparse_combiner: str = 'sum', weight_collections: Incomplete | None = None, trainable: bool = True, name: Incomplete | None = None, **kwargs) -> None: ...
    built: bool
    def build(self, _) -> None: ...
    def call(self, builder): ...

class _BiasLayer(base.Layer):
    """A layer for the bias term."""
    def __init__(self, units: int = 1, trainable: bool = True, weight_collections: Incomplete | None = None, name: Incomplete | None = None, **kwargs) -> None: ...
    built: bool
    def build(self, _) -> None: ...
    def call(self, _): ...

class _LinearModel(base.Layer):
    """Creates a linear model using feature columns.

  See `linear_model` for details.
  """
    def __init__(self, feature_columns, units: int = 1, sparse_combiner: str = 'sum', weight_collections: Incomplete | None = None, trainable: bool = True, name: Incomplete | None = None, **kwargs) -> None: ...
    def cols_to_vars(self):
        """Returns a dict mapping _FeatureColumns to variables.

    See `linear_model` for more information.
    This is not populated till `call` is called i.e. layer is built.
    """
    def call(self, features): ...

def make_parse_example_spec(feature_columns):
    '''Creates parsing spec dictionary from input feature_columns.

  The returned dictionary can be used as arg \'features\' in
  `tf.io.parse_example`.

  Typical usage example:

  ```python
  # Define features and transformations
  feature_a = categorical_column_with_vocabulary_file(...)
  feature_b = numeric_column(...)
  feature_c_bucketized = bucketized_column(numeric_column("feature_c"), ...)
  feature_a_x_feature_c = crossed_column(
      columns=["feature_a", feature_c_bucketized], ...)

  feature_columns = set(
      [feature_b, feature_c_bucketized, feature_a_x_feature_c])
  features = tf.io.parse_example(
      serialized=serialized_examples,
      features=make_parse_example_spec(feature_columns))
  ```

  For the above example, make_parse_example_spec would return the dict:

  ```python
  {
      "feature_a": parsing_ops.VarLenFeature(tf.string),
      "feature_b": parsing_ops.FixedLenFeature([1], dtype=tf.float32),
      "feature_c": parsing_ops.FixedLenFeature([1], dtype=tf.float32)
  }
  ```

  Args:
    feature_columns: An iterable containing all feature columns. All items
      should be instances of classes derived from `_FeatureColumn`.

  Returns:
    A dict mapping each feature key to a `FixedLenFeature` or `VarLenFeature`
    value.

  Raises:
    ValueError: If any of the given `feature_columns` is not a `_FeatureColumn`
      instance.
  '''

class _EmbeddingColumnLayer(base.Layer):
    """A layer that stores all the state required for a embedding column."""
    def __init__(self, embedding_shape, initializer, weight_collections: Incomplete | None = None, trainable: bool = True, name: Incomplete | None = None, **kwargs) -> None:
        """Constructor.

    Args:
      embedding_shape: Shape of the embedding variable used for lookup.
      initializer: A variable initializer function to be used in embedding
        variable initialization.
      weight_collections: A list of collection names to which the Variable will
        be added. Note that, variables will also be added to collections
        `tf.GraphKeys.GLOBAL_VARIABLES` and `ops.GraphKeys.MODEL_VARIABLES`.
      trainable: If `True` also add the variable to the graph collection
        `GraphKeys.TRAINABLE_VARIABLES` (see `tf.Variable`).
      name: Name of the layer
      **kwargs: keyword named properties.
    """
    def set_weight_collections(self, weight_collections) -> None:
        """Sets the weight collections for the layer.

    Args:
      weight_collections: A list of collection names to which the Variable will
        be added.
    """
    built: bool
    def build(self, _) -> None: ...
    def call(self, _): ...

class _FeatureColumn(metaclass=abc.ABCMeta):
    '''Represents a feature column abstraction.

  WARNING: Do not subclass this layer unless you know what you are doing:
  the API is subject to future changes.

  To distinguish the concept of a feature family and a specific binary feature
  within a family, we refer to a feature family like "country" as a feature
  column. Following is an example feature in a `tf.Example` format:
    {key: "country",  value: [ "US" ]}
  In this example the value of feature is "US" and "country" refers to the
  column of the feature.

  This class is an abstract class. User should not create instances of this.
  '''
    @property
    @abc.abstractmethod
    def name(self):
        """Returns string. Used for naming and for name_scope."""
    def __lt__(self, other):
        '''Allows feature columns to be sorted in Python 3 as they are in Python 2.

    Feature columns need to occasionally be sortable, for example when used as
    keys in a features dictionary passed to a layer.

    In CPython, `__lt__` must be defined for all objects in the
    sequence being sorted. If any objects do not have an `__lt__` compatible
    with feature column objects (such as strings), then CPython will fall back
    to using the `__gt__` method below.
    https://docs.python.org/3/library/stdtypes.html#list.sort

    Args:
      other: The other object to compare to.

    Returns:
      True if the string representation of this object is lexicographically less
      than the string representation of `other`. For FeatureColumn objects,
      this looks like "<__main__.FeatureColumn object at 0xa>".
    '''
    def __gt__(self, other):
        '''Allows feature columns to be sorted in Python 3 as they are in Python 2.

    Feature columns need to occasionally be sortable, for example when used as
    keys in a features dictionary passed to a layer.

    `__gt__` is called when the "other" object being compared during the sort
    does not have `__lt__` defined.
    Example:
    ```
    # __lt__ only class
    class A():
      def __lt__(self, other): return str(self) < str(other)

    a = A()
    a < "b" # True
    "0" < a # Error

    # __lt__ and __gt__ class
    class B():
      def __lt__(self, other): return str(self) < str(other)
      def __gt__(self, other): return str(self) > str(other)

    b = B()
    b < "c" # True
    "0" < b # True
    ```


    Args:
      other: The other object to compare to.

    Returns:
      True if the string representation of this object is lexicographically
      greater than the string representation of `other`. For FeatureColumn
      objects, this looks like "<__main__.FeatureColumn object at 0xa>".
    '''

class _DenseColumn(_FeatureColumn, metaclass=abc.ABCMeta):
    """Represents a column which can be represented as `Tensor`.

  WARNING: Do not subclass this layer unless you know what you are doing:
  the API is subject to future changes.

  Some examples of this type are: numeric_column, embedding_column,
  indicator_column.
  """

class _CategoricalColumn(_FeatureColumn, metaclass=abc.ABCMeta):
    """Represents a categorical feature.

  WARNING: Do not subclass this layer unless you know what you are doing:
  the API is subject to future changes.

  A categorical feature typically handled with a `tf.sparse.SparseTensor` of
  IDs.
  """

    class IdWeightPair(NamedTuple):
        id_tensor: Incomplete
        weight_tensor: Incomplete

class _SequenceDenseColumn(_FeatureColumn, metaclass=abc.ABCMeta):
    """Represents dense sequence data."""

    class TensorSequenceLengthPair(NamedTuple):
        dense_tensor: Incomplete
        sequence_length: Incomplete

class _LazyBuilder:
    '''Handles caching of transformations while building the model.

  `_FeatureColumn` specifies how to digest an input column to the network. Some
  feature columns require data transformations. This class caches those
  transformations.

  Some features may be used in more than one place. For example, one can use a
  bucketized feature by itself and a cross with it. In that case we
  should create only one bucketization op instead of creating ops for each
  feature column separately. To handle re-use of transformed columns,
  `_LazyBuilder` caches all previously transformed columns.

  Example:
  We\'re trying to use the following `_FeatureColumn`s:

  ```python
  bucketized_age = fc.bucketized_column(fc.numeric_column("age"), ...)
  keywords = fc.categorical_column_with_hash_buckets("keywords", ...)
  age_X_keywords = fc.crossed_column([bucketized_age, "keywords"])
  ... = linear_model(features,
                          [bucketized_age, keywords, age_X_keywords]
  ```

  If we transform each column independently, then we\'ll get duplication of
  bucketization (one for cross, one for bucketization itself).
  The `_LazyBuilder` eliminates this duplication.
  '''
    def __init__(self, features) -> None:
        """Creates a `_LazyBuilder`.

    Args:
      features: A mapping from feature column to objects that are `Tensor` or
        `SparseTensor`, or can be converted to same via
        `sparse_tensor.convert_to_tensor_or_sparse_tensor`. A `string` key
        signifies a base feature (not-transformed). A `_FeatureColumn` key means
        that this `Tensor` is the output of an existing `_FeatureColumn` which
        can be reused.
    """
    def get(self, key):
        """Returns a `Tensor` for the given key.

    A `str` key is used to access a base feature (not-transformed). When a
    `_FeatureColumn` is passed, the transformed feature is returned if it
    already exists, otherwise the given `_FeatureColumn` is asked to provide its
    transformed output, which is then cached.

    Args:
      key: a `str` or a `_FeatureColumn`.

    Returns:
      The transformed `Tensor` corresponding to the `key`.

    Raises:
      ValueError: if key is not found or a transformed `Tensor` cannot be
        computed.
    """

class _NumericColumn(_DenseColumn, NamedTuple('_NumericColumn', [('key', Incomplete), ('shape', Incomplete), ('default_value', Incomplete), ('dtype', Incomplete), ('normalizer_fn', Incomplete)])):
    """see `numeric_column`."""
    @property
    def name(self): ...

class _BucketizedColumn(_DenseColumn, _CategoricalColumn, NamedTuple('_BucketizedColumn', [('source_column', Incomplete), ('boundaries', Incomplete)])):
    """See `bucketized_column`."""
    @property
    def name(self): ...

class _EmbeddingColumn(_DenseColumn, _SequenceDenseColumn, NamedTuple('_EmbeddingColumn', [('categorical_column', Incomplete), ('dimension', Incomplete), ('combiner', Incomplete), ('layer_creator', Incomplete), ('ckpt_to_load_from', Incomplete), ('tensor_name_in_ckpt', Incomplete), ('max_norm', Incomplete), ('trainable', Incomplete), ('use_safe_embedding_lookup', Incomplete)])):
    """See `embedding_column`."""
    def __new__(cls, categorical_column, dimension, combiner, layer_creator, ckpt_to_load_from, tensor_name_in_ckpt, max_norm, trainable, use_safe_embedding_lookup: bool = True): ...
    @property
    def name(self): ...

class _SharedEmbeddingColumn(_DenseColumn, _SequenceDenseColumn, NamedTuple('_SharedEmbeddingColumn', [('categorical_column', Incomplete), ('dimension', Incomplete), ('combiner', Incomplete), ('initializer', Incomplete), ('shared_embedding_collection_name', Incomplete), ('ckpt_to_load_from', Incomplete), ('tensor_name_in_ckpt', Incomplete), ('max_norm', Incomplete), ('trainable', Incomplete), ('use_safe_embedding_lookup', Incomplete)])):
    """See `embedding_column`."""
    @property
    def name(self): ...

class _HashedCategoricalColumn(_CategoricalColumn, NamedTuple('_HashedCategoricalColumn', [('key', Incomplete), ('hash_bucket_size', Incomplete), ('dtype', Incomplete)])):
    """see `categorical_column_with_hash_bucket`."""
    @property
    def name(self): ...

class _VocabularyFileCategoricalColumn(_CategoricalColumn, NamedTuple('_VocabularyFileCategoricalColumn', [('key', Incomplete), ('vocabulary_file', Incomplete), ('vocabulary_size', Incomplete), ('num_oov_buckets', Incomplete), ('dtype', Incomplete), ('default_value', Incomplete)])):
    """See `categorical_column_with_vocabulary_file`."""
    @property
    def name(self): ...

class _VocabularyListCategoricalColumn(_CategoricalColumn, NamedTuple('_VocabularyListCategoricalColumn', [('key', Incomplete), ('vocabulary_list', Incomplete), ('dtype', Incomplete), ('default_value', Incomplete), ('num_oov_buckets', Incomplete)])):
    """See `categorical_column_with_vocabulary_list`."""
    @property
    def name(self): ...

class _IdentityCategoricalColumn(_CategoricalColumn, NamedTuple('_IdentityCategoricalColumn', [('key', Incomplete), ('num_buckets', Incomplete), ('default_value', Incomplete)])):
    """See `categorical_column_with_identity`."""
    @property
    def name(self): ...

class _WeightedCategoricalColumn(_CategoricalColumn, NamedTuple('_WeightedCategoricalColumn', [('categorical_column', Incomplete), ('weight_feature_key', Incomplete), ('dtype', Incomplete)])):
    """See `weighted_categorical_column`."""
    @property
    def name(self): ...

class _CrossedColumn(_CategoricalColumn, NamedTuple('_CrossedColumn', [('keys', Incomplete), ('hash_bucket_size', Incomplete), ('hash_key', Incomplete)])):
    """See `crossed_column`."""
    @property
    def name(self): ...

class _IndicatorColumn(_DenseColumn, _SequenceDenseColumn, NamedTuple('_IndicatorColumn', [('categorical_column', Incomplete)])):
    """Represents a one-hot column for use in deep networks.

  Args:
    categorical_column: A `_CategoricalColumn` which is created by
      `categorical_column_with_*` function.
  """
    @property
    def name(self): ...

class _SequenceCategoricalColumn(_CategoricalColumn, NamedTuple('_SequenceCategoricalColumn', [('categorical_column', Incomplete)])):
    """Represents sequences of categorical data."""
    @property
    def name(self): ...
