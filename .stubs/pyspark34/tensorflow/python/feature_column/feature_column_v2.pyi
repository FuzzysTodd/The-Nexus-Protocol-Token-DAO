import abc
from _typeshed import Incomplete
from tensorflow.python.data.ops import readers as readers
from tensorflow.python.eager import context as context
from tensorflow.python.feature_column import feature_column as fc_old
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, embedding_ops as embedding_ops, init_ops as init_ops, lookup_ops as lookup_ops, math_ops as math_ops, parsing_ops as parsing_ops, sparse_ops as sparse_ops, string_ops as string_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.trackable import autotrackable as autotrackable, data_structures as data_structures
from tensorflow.python.training import checkpoint_utils as checkpoint_utils
from tensorflow.python.util import deprecation as deprecation, nest as nest, tf_inspect as tf_inspect
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import NamedTuple

class StateManager:
    """Manages the state associated with FeatureColumns.

  Some `FeatureColumn`s create variables or resources to assist their
  computation. The `StateManager` is responsible for creating and storing these
  objects since `FeatureColumn`s are supposed to be stateless configuration
  only.
  """
    def create_variable(self, feature_column, name, shape, dtype: Incomplete | None = None, trainable: bool = True, use_resource: bool = True, initializer: Incomplete | None = None) -> None:
        """Creates a new variable.

    Args:
      feature_column: A `FeatureColumn` object this variable corresponds to.
      name: variable name.
      shape: variable shape.
      dtype: The type of the variable. Defaults to `self.dtype` or `float32`.
      trainable: Whether this variable is trainable or not.
      use_resource: If true, we use resource variables. Otherwise we use
        RefVariable.
      initializer: initializer instance (callable).

    Returns:
      The created variable.
    """
    def add_variable(self, feature_column, var) -> None:
        """Adds an existing variable to the state.

    Args:
      feature_column: A `FeatureColumn` object to associate this variable with.
      var: The variable.
    """
    def get_variable(self, feature_column, name) -> None:
        """Returns an existing variable.

    Args:
      feature_column: A `FeatureColumn` object this variable corresponds to.
      name: variable name.
    """
    def add_resource(self, feature_column, name, resource) -> None:
        """Creates a new resource.

    Resources can be things such as tables, variables, trackables, etc.

    Args:
      feature_column: A `FeatureColumn` object this resource corresponds to.
      name: Name of the resource.
      resource: The resource.

    Returns:
      The created resource.
    """
    def has_resource(self, feature_column, name) -> None:
        """Returns true iff a resource with same name exists.

    Resources can be things such as tables, variables, trackables, etc.

    Args:
      feature_column: A `FeatureColumn` object this variable corresponds to.
      name: Name of the resource.
    """
    def get_resource(self, feature_column, name) -> None:
        """Returns an already created resource.

    Resources can be things such as tables, variables, trackables, etc.

    Args:
      feature_column: A `FeatureColumn` object this variable corresponds to.
      name: Name of the resource.
    """

class _StateManagerImpl(StateManager):
    """Manages the state of DenseFeatures and LinearLayer.

  Some `FeatureColumn`s create variables or resources to assist their
  computation. The `StateManager` is responsible for creating and storing these
  objects since `FeatureColumn`s are supposed to be stateless configuration
  only.
  """
    def __init__(self, layer, trainable) -> None:
        """Creates an _StateManagerImpl object.

    Args:
      layer: The input layer this state manager is associated with.
      trainable: Whether by default, variables created are trainable or not.
    """
    def create_variable(self, feature_column, name, shape, dtype: Incomplete | None = None, trainable: bool = True, use_resource: bool = True, initializer: Incomplete | None = None):
        """Creates a new variable.

    Args:
      feature_column: A `FeatureColumn` object this variable corresponds to.
      name: variable name.
      shape: variable shape.
      dtype: The type of the variable. Defaults to `self.dtype` or `float32`.
      trainable: Whether this variable is trainable or not.
      use_resource: If true, we use resource variables. Otherwise we use
        RefVariable.
      initializer: initializer instance (callable).

    Returns:
      The created variable.
    """
    def get_variable(self, feature_column, name):
        """Returns an existing variable.

    Args:
      feature_column: A `FeatureColumn` object this variable corresponds to.
      name: variable name.
    """
    def add_resource(self, feature_column, resource_name, resource) -> None:
        """Creates a new resource.

    Resources can be things such as tables, variables, trackables, etc.

    Args:
      feature_column: A `FeatureColumn` object this resource corresponds to.
      resource_name: Name of the resource.
      resource: The resource.

    Returns:
      The created resource.
    """
    def has_resource(self, feature_column, resource_name):
        """Returns true iff a resource with same name exists.

    Resources can be things such as tables, variables, trackables, etc.

    Args:
      feature_column: A `FeatureColumn` object this variable corresponds to.
      resource_name: Name of the resource.
    """
    def get_resource(self, feature_column, resource_name):
        """Returns an already created resource.

    Resources can be things such as tables, variables, trackables, etc.

    Args:
      feature_column: A `FeatureColumn` object this variable corresponds to.
      resource_name: Name of the resource.
    """

def make_parse_example_spec_v2(feature_columns):
    '''Creates parsing spec dictionary from input feature_columns.

  The returned dictionary can be used as arg \'features\' in
  `tf.io.parse_example`.

  Typical usage example:

  ```python
  # Define features and transformations
  feature_a = tf.feature_column.categorical_column_with_vocabulary_file(...)
  feature_b = tf.feature_column.numeric_column(...)
  feature_c_bucketized = tf.feature_column.bucketized_column(
      tf.feature_column.numeric_column("feature_c"), ...)
  feature_a_x_feature_c = tf.feature_column.crossed_column(
      columns=["feature_a", feature_c_bucketized], ...)

  feature_columns = set(
      [feature_b, feature_c_bucketized, feature_a_x_feature_c])
  features = tf.io.parse_example(
      serialized=serialized_examples,
      features=tf.feature_column.make_parse_example_spec(feature_columns))
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
      should be instances of classes derived from `FeatureColumn`.

  Returns:
    A dict mapping each feature key to a `FixedLenFeature` or `VarLenFeature`
    value.

  Raises:
    ValueError: If any of the given `feature_columns` is not a `FeatureColumn`
      instance.
  '''
def embedding_column(categorical_column, dimension, combiner: str = 'mean', initializer: Incomplete | None = None, ckpt_to_load_from: Incomplete | None = None, tensor_name_in_ckpt: Incomplete | None = None, max_norm: Incomplete | None = None, trainable: bool = True, use_safe_embedding_lookup: bool = True):
    """`DenseColumn` that converts from sparse, categorical input.

  Use this when your inputs are sparse, but you want to convert them to a dense
  representation (e.g., to feed to a DNN).

  Inputs must be a `CategoricalColumn` created by any of the
  `categorical_column_*` function. Here is an example of using
  `embedding_column` with `DNNClassifier`:

  ```python
  video_id = categorical_column_with_identity(
      key='video_id', num_buckets=1000000, default_value=0)
  columns = [embedding_column(video_id, 9),...]

  estimator = tf.estimator.DNNClassifier(feature_columns=columns, ...)

  label_column = ...
  def input_fn():
    features = tf.io.parse_example(
        ..., features=make_parse_example_spec(columns + [label_column]))
    labels = features.pop(label_column.name)
    return features, labels

  estimator.train(input_fn=input_fn, steps=100)
  ```

  Here is an example using `embedding_column` with model_fn:

  ```python
  def model_fn(features, ...):
    video_id = categorical_column_with_identity(
        key='video_id', num_buckets=1000000, default_value=0)
    columns = [embedding_column(video_id, 9),...]
    dense_tensor = input_layer(features, columns)
    # Form DNN layers, calculate loss, and return EstimatorSpec.
    ...
  ```

  Args:
    categorical_column: A `CategoricalColumn` created by a
      `categorical_column_with_*` function. This column produces the sparse IDs
      that are inputs to the embedding lookup.
    dimension: An integer specifying dimension of the embedding, must be > 0.
    combiner: A string specifying how to reduce if there are multiple entries in
      a single row. Currently 'mean', 'sqrtn' and 'sum' are supported, with
      'mean' the default. 'sqrtn' often achieves good accuracy, in particular
      with bag-of-words columns. Each of this can be thought as example level
      normalizations on the column. For more information, see
      `tf.embedding_lookup_sparse`.
    initializer: A variable initializer function to be used in embedding
      variable initialization. If not specified, defaults to
      `truncated_normal_initializer` with mean `0.0` and standard deviation
      `1/sqrt(dimension)`.
    ckpt_to_load_from: String representing checkpoint name/pattern from which to
      restore column weights. Required if `tensor_name_in_ckpt` is not `None`.
    tensor_name_in_ckpt: Name of the `Tensor` in `ckpt_to_load_from` from which
      to restore the column weights. Required if `ckpt_to_load_from` is not
      `None`.
    max_norm: If not `None`, embedding values are l2-normalized to this value.
    trainable: Whether or not the embedding is trainable. Default is True.
    use_safe_embedding_lookup: If true, uses safe_embedding_lookup_sparse
      instead of embedding_lookup_sparse. safe_embedding_lookup_sparse ensures
      there are no empty rows and all weights and ids are positive at the
      expense of extra compute cost. This only applies to rank 2 (NxM) shaped
      input tensors. Defaults to true, consider turning off if the above checks
      are not needed. Note that having empty rows will not trigger any error
      though the output result might be 0 or omitted.

  Returns:
    `DenseColumn` that converts from sparse input.

  Raises:
    ValueError: if `dimension` not > 0.
    ValueError: if exactly one of `ckpt_to_load_from` and `tensor_name_in_ckpt`
      is specified.
    ValueError: if `initializer` is specified and is not callable.
    RuntimeError: If eager execution is enabled.
  """
def shared_embedding_columns(categorical_columns, dimension, combiner: str = 'mean', initializer: Incomplete | None = None, shared_embedding_collection_name: Incomplete | None = None, ckpt_to_load_from: Incomplete | None = None, tensor_name_in_ckpt: Incomplete | None = None, max_norm: Incomplete | None = None, trainable: bool = True, use_safe_embedding_lookup: bool = True):
    """List of dense columns that convert from sparse, categorical input.

  This is similar to `embedding_column`, except that it produces a list of
  embedding columns that share the same embedding weights.

  Use this when your inputs are sparse and of the same type (e.g. watched and
  impression video IDs that share the same vocabulary), and you want to convert
  them to a dense representation (e.g., to feed to a DNN).

  Inputs must be a list of categorical columns created by any of the
  `categorical_column_*` function. They must all be of the same type and have
  the same arguments except `key`. E.g. they can be
  categorical_column_with_vocabulary_file with the same vocabulary_file. Some or
  all columns could also be weighted_categorical_column.

  Here is an example embedding of two features for a DNNClassifier model:

  ```python
  watched_video_id = categorical_column_with_vocabulary_file(
      'watched_video_id', video_vocabulary_file, video_vocabulary_size)
  impression_video_id = categorical_column_with_vocabulary_file(
      'impression_video_id', video_vocabulary_file, video_vocabulary_size)
  columns = shared_embedding_columns(
      [watched_video_id, impression_video_id], dimension=10)

  estimator = tf.estimator.DNNClassifier(feature_columns=columns, ...)

  label_column = ...
  def input_fn():
    features = tf.io.parse_example(
        ..., features=make_parse_example_spec(columns + [label_column]))
    labels = features.pop(label_column.name)
    return features, labels

  estimator.train(input_fn=input_fn, steps=100)
  ```

  Here is an example using `shared_embedding_columns` with model_fn:

  ```python
  def model_fn(features, ...):
    watched_video_id = categorical_column_with_vocabulary_file(
        'watched_video_id', video_vocabulary_file, video_vocabulary_size)
    impression_video_id = categorical_column_with_vocabulary_file(
        'impression_video_id', video_vocabulary_file, video_vocabulary_size)
    columns = shared_embedding_columns(
        [watched_video_id, impression_video_id], dimension=10)
    dense_tensor = input_layer(features, columns)
    # Form DNN layers, calculate loss, and return EstimatorSpec.
    ...
  ```

  Args:
    categorical_columns: List of categorical columns created by a
      `categorical_column_with_*` function. These columns produce the sparse IDs
      that are inputs to the embedding lookup. All columns must be of the same
      type and have the same arguments except `key`. E.g. they can be
      categorical_column_with_vocabulary_file with the same vocabulary_file.
      Some or all columns could also be weighted_categorical_column.
    dimension: An integer specifying dimension of the embedding, must be > 0.
    combiner: A string specifying how to reduce if there are multiple entries in
      a single row. Currently 'mean', 'sqrtn' and 'sum' are supported, with
      'mean' the default. 'sqrtn' often achieves good accuracy, in particular
      with bag-of-words columns. Each of this can be thought as example level
      normalizations on the column. For more information, see
      `tf.embedding_lookup_sparse`.
    initializer: A variable initializer function to be used in embedding
      variable initialization. If not specified, defaults to
      `truncated_normal_initializer` with mean `0.0` and standard deviation
      `1/sqrt(dimension)`.
    shared_embedding_collection_name: Optional name of the collection where
      shared embedding weights are added. If not given, a reasonable name will
      be chosen based on the names of `categorical_columns`. This is also used
      in `variable_scope` when creating shared embedding weights.
    ckpt_to_load_from: String representing checkpoint name/pattern from which to
      restore column weights. Required if `tensor_name_in_ckpt` is not `None`.
    tensor_name_in_ckpt: Name of the `Tensor` in `ckpt_to_load_from` from which
      to restore the column weights. Required if `ckpt_to_load_from` is not
      `None`.
    max_norm: If not `None`, each embedding is clipped if its l2-norm is larger
      than this value, before combining.
    trainable: Whether or not the embedding is trainable. Default is True.
    use_safe_embedding_lookup: If true, uses safe_embedding_lookup_sparse
      instead of embedding_lookup_sparse. safe_embedding_lookup_sparse ensures
      there are no empty rows and all weights and ids are positive at the
      expense of extra compute cost. This only applies to rank 2 (NxM) shaped
      input tensors. Defaults to true, consider turning off if the above checks
      are not needed. Note that having empty rows will not trigger any error
      though the output result might be 0 or omitted.

  Returns:
    A list of dense columns that converts from sparse input. The order of
    results follows the ordering of `categorical_columns`.

  Raises:
    ValueError: if `dimension` not > 0.
    ValueError: if any of the given `categorical_columns` is of different type
      or has different arguments than the others.
    ValueError: if exactly one of `ckpt_to_load_from` and `tensor_name_in_ckpt`
      is specified.
    ValueError: if `initializer` is specified and is not callable.
    RuntimeError: if eager execution is enabled.
  """
def shared_embedding_columns_v2(categorical_columns, dimension, combiner: str = 'mean', initializer: Incomplete | None = None, shared_embedding_collection_name: Incomplete | None = None, ckpt_to_load_from: Incomplete | None = None, tensor_name_in_ckpt: Incomplete | None = None, max_norm: Incomplete | None = None, trainable: bool = True, use_safe_embedding_lookup: bool = True):
    """List of dense columns that convert from sparse, categorical input.

  This is similar to `embedding_column`, except that it produces a list of
  embedding columns that share the same embedding weights.

  Use this when your inputs are sparse and of the same type (e.g. watched and
  impression video IDs that share the same vocabulary), and you want to convert
  them to a dense representation (e.g., to feed to a DNN).

  Inputs must be a list of categorical columns created by any of the
  `categorical_column_*` function. They must all be of the same type and have
  the same arguments except `key`. E.g. they can be
  categorical_column_with_vocabulary_file with the same vocabulary_file. Some or
  all columns could also be weighted_categorical_column.

  Here is an example embedding of two features for a DNNClassifier model:

  ```python
  watched_video_id = categorical_column_with_vocabulary_file(
      'watched_video_id', video_vocabulary_file, video_vocabulary_size)
  impression_video_id = categorical_column_with_vocabulary_file(
      'impression_video_id', video_vocabulary_file, video_vocabulary_size)
  columns = shared_embedding_columns(
      [watched_video_id, impression_video_id], dimension=10)

  estimator = tf.estimator.DNNClassifier(feature_columns=columns, ...)

  label_column = ...
  def input_fn():
    features = tf.io.parse_example(
        ..., features=make_parse_example_spec(columns + [label_column]))
    labels = features.pop(label_column.name)
    return features, labels

  estimator.train(input_fn=input_fn, steps=100)
  ```

  Here is an example using `shared_embedding_columns` with model_fn:

  ```python
  def model_fn(features, ...):
    watched_video_id = categorical_column_with_vocabulary_file(
        'watched_video_id', video_vocabulary_file, video_vocabulary_size)
    impression_video_id = categorical_column_with_vocabulary_file(
        'impression_video_id', video_vocabulary_file, video_vocabulary_size)
    columns = shared_embedding_columns(
        [watched_video_id, impression_video_id], dimension=10)
    dense_tensor = input_layer(features, columns)
    # Form DNN layers, calculate loss, and return EstimatorSpec.
    ...
  ```

  Args:
    categorical_columns: List of categorical columns created by a
      `categorical_column_with_*` function. These columns produce the sparse IDs
      that are inputs to the embedding lookup. All columns must be of the same
      type and have the same arguments except `key`. E.g. they can be
      categorical_column_with_vocabulary_file with the same vocabulary_file.
      Some or all columns could also be weighted_categorical_column.
    dimension: An integer specifying dimension of the embedding, must be > 0.
    combiner: A string specifying how to reduce if there are multiple entries in
      a single row. Currently 'mean', 'sqrtn' and 'sum' are supported, with
      'mean' the default. 'sqrtn' often achieves good accuracy, in particular
      with bag-of-words columns. Each of this can be thought as example level
      normalizations on the column. For more information, see
      `tf.embedding_lookup_sparse`.
    initializer: A variable initializer function to be used in embedding
      variable initialization. If not specified, defaults to
      `truncated_normal_initializer` with mean `0.0` and standard deviation
      `1/sqrt(dimension)`.
    shared_embedding_collection_name: Optional collective name of these columns.
      If not given, a reasonable name will be chosen based on the names of
      `categorical_columns`.
    ckpt_to_load_from: String representing checkpoint name/pattern from which to
      restore column weights. Required if `tensor_name_in_ckpt` is not `None`.
    tensor_name_in_ckpt: Name of the `Tensor` in `ckpt_to_load_from` from which
      to restore the column weights. Required if `ckpt_to_load_from` is not
      `None`.
    max_norm: If not `None`, each embedding is clipped if its l2-norm is larger
      than this value, before combining.
    trainable: Whether or not the embedding is trainable. Default is True.
    use_safe_embedding_lookup: If true, uses safe_embedding_lookup_sparse
      instead of embedding_lookup_sparse. safe_embedding_lookup_sparse ensures
      there are no empty rows and all weights and ids are positive at the
      expense of extra compute cost. This only applies to rank 2 (NxM) shaped
      input tensors. Defaults to true, consider turning off if the above checks
      are not needed. Note that having empty rows will not trigger any error
      though the output result might be 0 or omitted.

  Returns:
    A list of dense columns that converts from sparse input. The order of
    results follows the ordering of `categorical_columns`.

  Raises:
    ValueError: if `dimension` not > 0.
    ValueError: if any of the given `categorical_columns` is of different type
      or has different arguments than the others.
    ValueError: if exactly one of `ckpt_to_load_from` and `tensor_name_in_ckpt`
      is specified.
    ValueError: if `initializer` is specified and is not callable.
    RuntimeError: if eager execution is enabled.
  """
def numeric_column(key, shape=(1,), default_value: Incomplete | None = None, dtype=..., normalizer_fn: Incomplete | None = None):
    '''Represents real valued or numerical features.

  Example:

  Assume we have data with two features `a` and `b`.

  >>> data = {\'a\': [15, 9, 17, 19, 21, 18, 25, 30],
  ...    \'b\': [5.0, 6.4, 10.5, 13.6, 15.7, 19.9, 20.3 , 0.0]}

  Let us represent the features `a` and `b` as numerical features.

  >>> a = tf.feature_column.numeric_column(\'a\')
  >>> b = tf.feature_column.numeric_column(\'b\')

  Feature column describe a set of transformations to the inputs.

  For example, to "bucketize" feature `a`, wrap the `a` column in a
  `feature_column.bucketized_column`.
  Providing `5` bucket boundaries, the bucketized_column api
  will bucket this feature in total of `6` buckets.

  >>> a_buckets = tf.feature_column.bucketized_column(a,
  ...    boundaries=[10, 15, 20, 25, 30])

  Create a `DenseFeatures` layer which will apply the transformations
  described by the set of `tf.feature_column` objects:

  >>> feature_layer = tf.keras.layers.DenseFeatures([a_buckets, b])
  >>> print(feature_layer(data))
  tf.Tensor(
  [[ 0.   0.   1.   0.   0.   0.   5. ]
   [ 1.   0.   0.   0.   0.   0.   6.4]
   [ 0.   0.   1.   0.   0.   0.  10.5]
   [ 0.   0.   1.   0.   0.   0.  13.6]
   [ 0.   0.   0.   1.   0.   0.  15.7]
   [ 0.   0.   1.   0.   0.   0.  19.9]
   [ 0.   0.   0.   0.   1.   0.  20.3]
   [ 0.   0.   0.   0.   0.   1.   0. ]], shape=(8, 7), dtype=float32)

  Args:
    key: A unique string identifying the input feature. It is used as the column
      name and the dictionary key for feature parsing configs, feature `Tensor`
      objects, and feature columns.
    shape: An iterable of integers specifies the shape of the `Tensor`. An
      integer can be given which means a single dimension `Tensor` with given
      width. The `Tensor` representing the column will have the shape of
      [batch_size] + `shape`.
    default_value: A single value compatible with `dtype` or an iterable of
      values compatible with `dtype` which the column takes on during
      `tf.Example` parsing if data is missing. A default value of `None` will
      cause `tf.io.parse_example` to fail if an example does not contain this
      column. If a single value is provided, the same value will be applied as
      the default value for every item. If an iterable of values is provided,
      the shape of the `default_value` should be equal to the given `shape`.
    dtype: defines the type of values. Default value is `tf.float32`. Must be a
      non-quantized, real integer or floating point type.
    normalizer_fn: If not `None`, a function that can be used to normalize the
      value of the tensor after `default_value` is applied for parsing.
      Normalizer function takes the input `Tensor` as its argument, and returns
      the output `Tensor`. (e.g. lambda x: (x - 3.0) / 4.2). Please note that
      even though the most common use case of this function is normalization, it
      can be used for any kind of Tensorflow transformations.

  Returns:
    A `NumericColumn`.

  Raises:
    TypeError: if any dimension in shape is not an int
    ValueError: if any dimension in shape is not a positive integer
    TypeError: if `default_value` is an iterable but not compatible with `shape`
    TypeError: if `default_value` is not compatible with `dtype`.
    ValueError: if `dtype` is not convertible to `tf.float32`.
  '''
def bucketized_column(source_column, boundaries):
    """Represents discretized dense input bucketed by `boundaries`.

  Buckets include the left boundary, and exclude the right boundary. Namely,
  `boundaries=[0., 1., 2.]` generates buckets `(-inf, 0.)`, `[0., 1.)`,
  `[1., 2.)`, and `[2., +inf)`.

  For example, if the inputs are

  ```python
  boundaries = [0, 10, 100]
  input tensor = [[-5, 10000]
                  [150,   10]
                  [5,    100]]
  ```

  then the output will be

  ```python
  output = [[0, 3]
            [3, 2]
            [1, 3]]
  ```

  Example:

  ```python
  price = tf.feature_column.numeric_column('price')
  bucketized_price = tf.feature_column.bucketized_column(
      price, boundaries=[...])
  columns = [bucketized_price, ...]
  features = tf.io.parse_example(
      ..., features=tf.feature_column.make_parse_example_spec(columns))
  dense_tensor = tf.keras.layers.DenseFeatures(columns)(features)
  ```

  A `bucketized_column` can also be crossed with another categorical column
  using `crossed_column`:

  ```python
  price = tf.feature_column.numeric_column('price')
  # bucketized_column converts numerical feature to a categorical one.
  bucketized_price = tf.feature_column.bucketized_column(
      price, boundaries=[...])
  # 'keywords' is a string feature.
  price_x_keywords = tf.feature_column.crossed_column(
      [bucketized_price, 'keywords'], 50K)
  columns = [price_x_keywords, ...]
  features = tf.io.parse_example(
      ..., features=tf.feature_column.make_parse_example_spec(columns))
  dense_tensor = tf.keras.layers.DenseFeatures(columns)(features)
  linear_model = tf.keras.experimental.LinearModel(units=...)(dense_tensor)
  ```

  Args:
    source_column: A one-dimensional dense column which is generated with
      `numeric_column`.
    boundaries: A sorted list or tuple of floats specifying the boundaries.

  Returns:
    A `BucketizedColumn`.

  Raises:
    ValueError: If `source_column` is not a numeric column, or if it is not
      one-dimensional.
    ValueError: If `boundaries` is not a sorted list or tuple.
  """
def categorical_column_with_hash_bucket(key, hash_bucket_size, dtype=...):
    '''Represents sparse feature where ids are set by hashing.

  Use this when your sparse features are in string or integer format, and you
  want to distribute your inputs into a finite number of buckets by hashing.
  output_id = Hash(input_feature_string) % bucket_size for string type input.
  For int type input, the value is converted to its string representation first
  and then hashed by the same formula.

  For input dictionary `features`, `features[key]` is either `Tensor` or
  `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int
  and `\'\'` for string, which will be dropped by this feature column.

  Example:

  ```python
  import tensorflow as tf
  keywords = tf.feature_column.categorical_column_with_hash_bucket("keywords",
  10000)
  columns = [keywords]
  features = {\'keywords\': tf.constant([[\'Tensorflow\', \'Keras\', \'RNN\', \'LSTM\',
  \'CNN\'], [\'LSTM\', \'CNN\', \'Tensorflow\', \'Keras\', \'RNN\'], [\'CNN\', \'Tensorflow\',
  \'LSTM\', \'Keras\', \'RNN\']])}
  linear_prediction, _, _ = tf.compat.v1.feature_column.linear_model(features,
  columns)

  # or
  import tensorflow as tf
  keywords = tf.feature_column.categorical_column_with_hash_bucket("keywords",
  10000)
  keywords_embedded = tf.feature_column.embedding_column(keywords, 16)
  columns = [keywords_embedded]
  features = {\'keywords\': tf.constant([[\'Tensorflow\', \'Keras\', \'RNN\', \'LSTM\',
  \'CNN\'], [\'LSTM\', \'CNN\', \'Tensorflow\', \'Keras\', \'RNN\'], [\'CNN\', \'Tensorflow\',
  \'LSTM\', \'Keras\', \'RNN\']])}
  input_layer = tf.keras.layers.DenseFeatures(columns)
  dense_tensor = input_layer(features)
  ```

  Args:
    key: A unique string identifying the input feature. It is used as the column
      name and the dictionary key for feature parsing configs, feature `Tensor`
      objects, and feature columns.
    hash_bucket_size: An int > 1. The number of buckets.
    dtype: The type of features. Only string and integer types are supported.

  Returns:
    A `HashedCategoricalColumn`.

  Raises:
    ValueError: `hash_bucket_size` is not greater than 1.
    ValueError: `dtype` is neither string nor integer.
  '''
def categorical_column_with_vocabulary_file(key, vocabulary_file, vocabulary_size: Incomplete | None = None, num_oov_buckets: int = 0, default_value: Incomplete | None = None, dtype=...):
    """A `CategoricalColumn` with a vocabulary file.

  Use this when your inputs are in string or integer format, and you have a
  vocabulary file that maps each value to an integer ID. By default,
  out-of-vocabulary values are ignored. Use either (but not both) of
  `num_oov_buckets` and `default_value` to specify how to include
  out-of-vocabulary values.

  For input dictionary `features`, `features[key]` is either `Tensor` or
  `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int
  and `''` for string, which will be dropped by this feature column.

  Example with `num_oov_buckets`:
  File '/us/states.txt' contains 50 lines, each with a 2-character U.S. state
  abbreviation. All inputs with values in that file are assigned an ID 0-49,
  corresponding to its line number. All other values are hashed and assigned an
  ID 50-54.

  ```python
  import tensorflow as tf
  states = tf.feature_column.categorical_column_with_vocabulary_file(
    key='states', vocabulary_file='states.txt', vocabulary_size=5,
    num_oov_buckets=1)
  columns = [states]
  features = {'states':tf.constant([['california', 'georgia', 'michigan',
  'texas', 'new york'], ['new york', 'georgia', 'california', 'michigan',
  'texas']])}
  linear_prediction = tf.compat.v1.feature_column.linear_model(features,
  columns)
  ```

  Example with `default_value`:
  File '/us/states.txt' contains 51 lines - the first line is 'XX', and the
  other 50 each have a 2-character U.S. state abbreviation. Both a literal 'XX'
  in input, and other values missing from the file, will be assigned ID 0. All
  others are assigned the corresponding line number 1-50.

  ```python
  import tensorflow as tf
  states = tf.feature_column.categorical_column_with_vocabulary_file(
    key='states', vocabulary_file='states.txt', vocabulary_size=6,
    default_value=0)
  columns = [states]
  features = {'states':tf.constant([['california', 'georgia', 'michigan',
  'texas', 'new york'], ['new york', 'georgia', 'california', 'michigan',
  'texas']])}
  linear_prediction = tf.compat.v1.feature_column.linear_model(features,
  columns)
  ```

  And to make an embedding with either:

  ```python
  import tensorflow as tf
  states = tf.feature_column.categorical_column_with_vocabulary_file(
    key='states', vocabulary_file='states.txt', vocabulary_size=5,
    num_oov_buckets=1)
  columns = [tf.feature_column.embedding_column(states, 3)]
  features = {'states':tf.constant([['california', 'georgia', 'michigan',
  'texas', 'new york'], ['new york', 'georgia', 'california', 'michigan',
  'texas']])}
  input_layer = tf.keras.layers.DenseFeatures(columns)
  dense_tensor = input_layer(features)
  ```

  Args:
    key: A unique string identifying the input feature. It is used as the column
      name and the dictionary key for feature parsing configs, feature `Tensor`
      objects, and feature columns.
    vocabulary_file: The vocabulary file name.
    vocabulary_size: Number of the elements in the vocabulary. This must be no
      greater than length of `vocabulary_file`, if less than length, later
      values are ignored. If None, it is set to the length of `vocabulary_file`.
    num_oov_buckets: Non-negative integer, the number of out-of-vocabulary
      buckets. All out-of-vocabulary inputs will be assigned IDs in the range
      `[vocabulary_size, vocabulary_size+num_oov_buckets)` based on a hash of
      the input value. A positive `num_oov_buckets` can not be specified with
      `default_value`.
    default_value: The integer ID value to return for out-of-vocabulary feature
      values, defaults to `-1`. This can not be specified with a positive
      `num_oov_buckets`.
    dtype: The type of features. Only string and integer types are supported.

  Returns:
    A `CategoricalColumn` with a vocabulary file.

  Raises:
    ValueError: `vocabulary_file` is missing or cannot be opened.
    ValueError: `vocabulary_size` is missing or < 1.
    ValueError: `num_oov_buckets` is a negative integer.
    ValueError: `num_oov_buckets` and `default_value` are both specified.
    ValueError: `dtype` is neither string nor integer.
  """
def categorical_column_with_vocabulary_file_v2(key, vocabulary_file, vocabulary_size: Incomplete | None = None, dtype=..., default_value: Incomplete | None = None, num_oov_buckets: int = 0, file_format: Incomplete | None = None):
    """A `CategoricalColumn` with a vocabulary file.

  Use this when your inputs are in string or integer format, and you have a
  vocabulary file that maps each value to an integer ID. By default,
  out-of-vocabulary values are ignored. Use either (but not both) of
  `num_oov_buckets` and `default_value` to specify how to include
  out-of-vocabulary values.

  For input dictionary `features`, `features[key]` is either `Tensor` or
  `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int
  and `''` for string, which will be dropped by this feature column.

  Example with `num_oov_buckets`:
  File `'/us/states.txt'` contains 50 lines, each with a 2-character U.S. state
  abbreviation. All inputs with values in that file are assigned an ID 0-49,
  corresponding to its line number. All other values are hashed and assigned an
  ID 50-54.

  ```python
  states = categorical_column_with_vocabulary_file(
      key='states', vocabulary_file='/us/states.txt', vocabulary_size=50,
      num_oov_buckets=5)
  columns = [states, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  linear_prediction = linear_model(features, columns)
  ```

  Example with `default_value`:
  File `'/us/states.txt'` contains 51 lines - the first line is `'XX'`, and the
  other 50 each have a 2-character U.S. state abbreviation. Both a literal
  `'XX'` in input, and other values missing from the file, will be assigned
  ID 0. All others are assigned the corresponding line number 1-50.

  ```python
  states = categorical_column_with_vocabulary_file(
      key='states', vocabulary_file='/us/states.txt', vocabulary_size=51,
      default_value=0)
  columns = [states, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  linear_prediction, _, _ = linear_model(features, columns)
  ```

  And to make an embedding with either:

  ```python
  columns = [embedding_column(states, 3),...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  dense_tensor = input_layer(features, columns)
  ```

  Args:
    key: A unique string identifying the input feature. It is used as the column
      name and the dictionary key for feature parsing configs, feature `Tensor`
      objects, and feature columns.
    vocabulary_file: The vocabulary file name.
    vocabulary_size: Number of the elements in the vocabulary. This must be no
      greater than length of `vocabulary_file`, if less than length, later
      values are ignored. If None, it is set to the length of `vocabulary_file`.
    dtype: The type of features. Only string and integer types are supported.
    default_value: The integer ID value to return for out-of-vocabulary feature
      values, defaults to `-1`. This can not be specified with a positive
      `num_oov_buckets`.
    num_oov_buckets: Non-negative integer, the number of out-of-vocabulary
      buckets. All out-of-vocabulary inputs will be assigned IDs in the range
      `[vocabulary_size, vocabulary_size+num_oov_buckets)` based on a hash of
      the input value. A positive `num_oov_buckets` can not be specified with
      `default_value`.
    file_format: The format of the vocabulary file. The format is 'text' by
      default unless `vocabulary_file` is a string which ends in 'tfrecord.gz'.
      Accepted alternative value for `file_format` is 'tfrecord_gzip'.

  Returns:
    A `CategoricalColumn` with a vocabulary file.

  Raises:
    ValueError: `vocabulary_file` is missing or cannot be opened.
    ValueError: `vocabulary_size` is missing or < 1.
    ValueError: `num_oov_buckets` is a negative integer.
    ValueError: `num_oov_buckets` and `default_value` are both specified.
    ValueError: `dtype` is neither string nor integer.
  """
def categorical_column_with_vocabulary_list(key, vocabulary_list, dtype: Incomplete | None = None, default_value: int = -1, num_oov_buckets: int = 0):
    """A `CategoricalColumn` with in-memory vocabulary.

  Use this when your inputs are in string or integer format, and you have an
  in-memory vocabulary mapping each value to an integer ID. By default,
  out-of-vocabulary values are ignored. Use either (but not both) of
  `num_oov_buckets` and `default_value` to specify how to include
  out-of-vocabulary values.

  For input dictionary `features`, `features[key]` is either `Tensor` or
  `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int
  and `''` for string, which will be dropped by this feature column.

  Example with `num_oov_buckets`:
  In the following example, each input in `vocabulary_list` is assigned an ID
  0-3 corresponding to its index (e.g., input 'B' produces output 2). All other
  inputs are hashed and assigned an ID 4-5.

  ```python
  colors = categorical_column_with_vocabulary_list(
      key='colors', vocabulary_list=('R', 'G', 'B', 'Y'),
      num_oov_buckets=2)
  columns = [colors, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  linear_prediction, _, _ = linear_model(features, columns)
  ```

  Example with `default_value`:
  In the following example, each input in `vocabulary_list` is assigned an ID
  0-4 corresponding to its index (e.g., input 'B' produces output 3). All other
  inputs are assigned `default_value` 0.


  ```python
  colors = categorical_column_with_vocabulary_list(
      key='colors', vocabulary_list=('X', 'R', 'G', 'B', 'Y'), default_value=0)
  columns = [colors, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  linear_prediction, _, _ = linear_model(features, columns)
  ```

  And to make an embedding with either:

  ```python
  columns = [embedding_column(colors, 3),...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  dense_tensor = input_layer(features, columns)
  ```

  Args:
    key: A unique string identifying the input feature. It is used as the column
      name and the dictionary key for feature parsing configs, feature `Tensor`
      objects, and feature columns.
    vocabulary_list: An ordered iterable defining the vocabulary. Each feature
      is mapped to the index of its value (if present) in `vocabulary_list`.
      Must be castable to `dtype`.
    dtype: The type of features. Only string and integer types are supported. If
      `None`, it will be inferred from `vocabulary_list`.
    default_value: The integer ID value to return for out-of-vocabulary feature
      values, defaults to `-1`. This can not be specified with a positive
      `num_oov_buckets`.
    num_oov_buckets: Non-negative integer, the number of out-of-vocabulary
      buckets. All out-of-vocabulary inputs will be assigned IDs in the range
      `[len(vocabulary_list), len(vocabulary_list)+num_oov_buckets)` based on a
      hash of the input value. A positive `num_oov_buckets` can not be specified
      with `default_value`.

  Returns:
    A `CategoricalColumn` with in-memory vocabulary.

  Raises:
    ValueError: if `vocabulary_list` is empty, or contains duplicate keys.
    ValueError: `num_oov_buckets` is a negative integer.
    ValueError: `num_oov_buckets` and `default_value` are both specified.
    ValueError: if `dtype` is not integer or string.
  """
def categorical_column_with_identity(key, num_buckets, default_value: Incomplete | None = None):
    """A `CategoricalColumn` that returns identity values.

  Use this when your inputs are integers in the range `[0, num_buckets)`, and
  you want to use the input value itself as the categorical ID. Values outside
  this range will result in `default_value` if specified, otherwise it will
  fail.

  Typically, this is used for contiguous ranges of integer indexes, but
  it doesn't have to be. This might be inefficient, however, if many of IDs
  are unused. Consider `categorical_column_with_hash_bucket` in that case.

  For input dictionary `features`, `features[key]` is either `Tensor` or
  `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int
  and `''` for string, which will be dropped by this feature column.

  In the following examples, each input in the range `[0, 1000000)` is assigned
  the same value. All other inputs are assigned `default_value` 0. Note that a
  literal 0 in inputs will result in the same default ID.

  Linear model:

  ```python
  import tensorflow as tf
  video_id = tf.feature_column.categorical_column_with_identity(
      key='video_id', num_buckets=1000000, default_value=0)
  columns = [video_id]
  features = {'video_id': tf.sparse.from_dense([[2, 85, 0, 0, 0],
  [33,78, 2, 73, 1]])}
  linear_prediction = tf.compat.v1.feature_column.linear_model(features,
  columns)
  ```

  Embedding for a DNN model:

  ```python
  import tensorflow as tf
  video_id = tf.feature_column.categorical_column_with_identity(
      key='video_id', num_buckets=1000000, default_value=0)
  columns = [tf.feature_column.embedding_column(video_id, 9)]
  features = {'video_id': tf.sparse.from_dense([[2, 85, 0, 0, 0],
  [33,78, 2, 73, 1]])}
  input_layer = tf.keras.layers.DenseFeatures(columns)
  dense_tensor = input_layer(features)
  ```

  Args:
    key: A unique string identifying the input feature. It is used as the column
      name and the dictionary key for feature parsing configs, feature `Tensor`
      objects, and feature columns.
    num_buckets: Range of inputs and outputs is `[0, num_buckets)`.
    default_value: If set, values outside of range `[0, num_buckets)` will be
      replaced with this value. If not set, values >= num_buckets will cause a
      failure while values < 0 will be dropped.

  Returns:
    A `CategoricalColumn` that returns identity values.

  Raises:
    ValueError: if `num_buckets` is less than one.
    ValueError: if `default_value` is not in range `[0, num_buckets)`.
  """
def indicator_column(categorical_column):
    '''Represents multi-hot representation of given categorical column.

  - For DNN model, `indicator_column` can be used to wrap any
    `categorical_column_*` (e.g., to feed to DNN). Consider to Use
    `embedding_column` if the number of buckets/unique(values) are large.

  - For Wide (aka linear) model, `indicator_column` is the internal
    representation for categorical column when passing categorical column
    directly (as any element in feature_columns) to `linear_model`. See
    `linear_model` for details.

  ```python
  name = indicator_column(categorical_column_with_vocabulary_list(
      \'name\', [\'bob\', \'george\', \'wanda\']))
  columns = [name, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  dense_tensor = input_layer(features, columns)

  dense_tensor == [[1, 0, 0]]  # If "name" bytes_list is ["bob"]
  dense_tensor == [[1, 0, 1]]  # If "name" bytes_list is ["bob", "wanda"]
  dense_tensor == [[2, 0, 0]]  # If "name" bytes_list is ["bob", "bob"]
  ```

  Args:
    categorical_column: A `CategoricalColumn` which is created by
      `categorical_column_with_*` or `crossed_column` functions.

  Returns:
    An `IndicatorColumn`.

  Raises:
    ValueError: If `categorical_column` is not CategoricalColumn type.
  '''
def weighted_categorical_column(categorical_column, weight_feature_key, dtype=...):
    '''Applies weight values to a `CategoricalColumn`.

  Use this when each of your sparse inputs has both an ID and a value. For
  example, if you\'re representing text documents as a collection of word
  frequencies, you can provide 2 parallel sparse input features (\'terms\' and
  \'frequencies\' below).

  Example:

  Input `tf.Example` objects:

  ```proto
  [
    features {
      feature {
        key: "terms"
        value {bytes_list {value: "very" value: "model"}}
      }
      feature {
        key: "frequencies"
        value {float_list {value: 0.3 value: 0.1}}
      }
    },
    features {
      feature {
        key: "terms"
        value {bytes_list {value: "when" value: "course" value: "human"}}
      }
      feature {
        key: "frequencies"
        value {float_list {value: 0.4 value: 0.1 value: 0.2}}
      }
    }
  ]
  ```

  ```python
  categorical_column = categorical_column_with_hash_bucket(
      column_name=\'terms\', hash_bucket_size=1000)
  weighted_column = weighted_categorical_column(
      categorical_column=categorical_column, weight_feature_key=\'frequencies\')
  columns = [weighted_column, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  linear_prediction, _, _ = linear_model(features, columns)
  ```

  This assumes the input dictionary contains a `SparseTensor` for key
  \'terms\', and a `SparseTensor` for key \'frequencies\'. These 2 tensors must have
  the same indices and dense shape.

  Args:
    categorical_column: A `CategoricalColumn` created by
      `categorical_column_with_*` functions.
    weight_feature_key: String key for weight values.
    dtype: Type of weights, such as `tf.float32`. Only float and integer weights
      are supported.

  Returns:
    A `CategoricalColumn` composed of two sparse features: one represents id,
    the other represents weight (value) of the id feature in that example.

  Raises:
    ValueError: if `dtype` is not convertible to float.
  '''
def crossed_column(keys, hash_bucket_size, hash_key: Incomplete | None = None):
    '''Returns a column for performing crosses of categorical features.

  Crossed features will be hashed according to `hash_bucket_size`. Conceptually,
  the transformation can be thought of as:
    Hash(cartesian product of features) % `hash_bucket_size`

  For example, if the input features are:

  * SparseTensor referred by first key:

    ```python
    shape = [2, 2]
    {
        [0, 0]: "a"
        [1, 0]: "b"
        [1, 1]: "c"
    }
    ```

  * SparseTensor referred by second key:

    ```python
    shape = [2, 1]
    {
        [0, 0]: "d"
        [1, 0]: "e"
    }
    ```

  then crossed feature will look like:

  ```python
   shape = [2, 2]
  {
      [0, 0]: Hash64("d", Hash64("a")) % hash_bucket_size
      [1, 0]: Hash64("e", Hash64("b")) % hash_bucket_size
      [1, 1]: Hash64("e", Hash64("c")) % hash_bucket_size
  }
  ```

  Here is an example to create a linear model with crosses of string features:

  ```python
  keywords_x_doc_terms = crossed_column([\'keywords\', \'doc_terms\'], 50K)
  columns = [keywords_x_doc_terms, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  linear_prediction = linear_model(features, columns)
  ```

  You could also use vocabulary lookup before crossing:

  ```python
  keywords = categorical_column_with_vocabulary_file(
      \'keywords\', \'/path/to/vocabulary/file\', vocabulary_size=1K)
  keywords_x_doc_terms = crossed_column([keywords, \'doc_terms\'], 50K)
  columns = [keywords_x_doc_terms, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  linear_prediction = linear_model(features, columns)
  ```

  If an input feature is of numeric type, you can use
  `categorical_column_with_identity`, or `bucketized_column`, as in the example:

  ```python
  # vertical_id is an integer categorical feature.
  vertical_id = categorical_column_with_identity(\'vertical_id\', 10K)
  price = numeric_column(\'price\')
  # bucketized_column converts numerical feature to a categorical one.
  bucketized_price = bucketized_column(price, boundaries=[...])
  vertical_id_x_price = crossed_column([vertical_id, bucketized_price], 50K)
  columns = [vertical_id_x_price, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  linear_prediction = linear_model(features, columns)
  ```

  To use crossed column in DNN model, you need to add it in an embedding column
  as in this example:

  ```python
  vertical_id_x_price = crossed_column([vertical_id, bucketized_price], 50K)
  vertical_id_x_price_embedded = embedding_column(vertical_id_x_price, 10)
  dense_tensor = input_layer(features, [vertical_id_x_price_embedded, ...])
  ```

  Args:
    keys: An iterable identifying the features to be crossed. Each element can
      be either:
      * string: Will use the corresponding feature which must be of string type.
      * `CategoricalColumn`: Will use the transformed tensor produced by this
        column. Does not support hashed categorical column.
    hash_bucket_size: An int > 1. The number of buckets.
    hash_key: Specify the hash_key that will be used by the `FingerprintCat64`
      function to combine the crosses fingerprints on SparseCrossOp (optional).

  Returns:
    A `CrossedColumn`.

  Raises:
    ValueError: If `len(keys) < 2`.
    ValueError: If any of the keys is neither a string nor `CategoricalColumn`.
    ValueError: If any of the keys is `HashedCategoricalColumn`.
    ValueError: If `hash_bucket_size < 1`.
  '''

class FeatureColumn(metaclass=abc.ABCMeta):
    '''Represents a feature column abstraction.

  WARNING: Do not subclass this layer unless you know what you are doing:
  the API is subject to future changes.

  To distinguish between the concept of a feature family and a specific binary
  feature within a family, we refer to a feature family like "country" as a
  feature column. For example, we can have a feature in a `tf.Example` format:
    {key: "country",  value: [ "US" ]}
  In this example the value of feature is "US" and "country" refers to the
  column of the feature.

  This class is an abstract class. Users should not create instances of this.
  '''
    @property
    @abc.abstractmethod
    def name(self):
        """Returns string. Used for naming."""
    def __lt__(self, other):
        '''Allows feature columns to be sorted in Python 3 as they are in Python 2.

    Feature columns need to occasionally be sortable, for example when used as
    keys in a features dictionary passed to a layer.

    In CPython, `__lt__` must be defined for all objects in the
    sequence being sorted.

    If any objects in the sequence being sorted do not have an `__lt__` method
    compatible with feature column objects (such as strings), then CPython will
    fall back to using the `__gt__` method below.
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
    @abc.abstractmethod
    def transform_feature(self, transformation_cache, state_manager):
        """Returns intermediate representation (usually a `Tensor`).

    Uses `transformation_cache` to create an intermediate representation
    (usually a `Tensor`) that other feature columns can use.

    Example usage of `transformation_cache`:
    Let's say a Feature column depends on raw feature ('raw') and another
    `FeatureColumn` (input_fc). To access corresponding `Tensor`s,
    transformation_cache will be used as follows:

    ```python
    raw_tensor = transformation_cache.get('raw', state_manager)
    fc_tensor = transformation_cache.get(input_fc, state_manager)
    ```

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.

    Returns:
      Transformed feature `Tensor`.
    """
    @property
    @abc.abstractmethod
    def parse_example_spec(self):
        """Returns a `tf.Example` parsing spec as dict.

    It is used for get_parsing_spec for `tf.io.parse_example`. Returned spec is
    a dict from keys ('string') to `VarLenFeature`, `FixedLenFeature`, and other
    supported objects. Please check documentation of `tf.io.parse_example` for
    all supported spec objects.

    Let's say a Feature column depends on raw feature ('raw') and another
    `FeatureColumn` (input_fc). One possible implementation of
    parse_example_spec is as follows:

    ```python
    spec = {'raw': tf.io.FixedLenFeature(...)}
    spec.update(input_fc.parse_example_spec)
    return spec
    ```
    """
    def create_state(self, state_manager) -> None:
        """Uses the `state_manager` to create state for the FeatureColumn.

    Args:
      state_manager: A `StateManager` to create / access resources such as
        lookup tables and variables.
    """
    @property
    @abc.abstractmethod
    def parents(self):
        """Returns a list of immediate raw feature and FeatureColumn dependencies.

    For example:
    # For the following feature columns
    a = numeric_column('f1')
    c = crossed_column(a, 'f2')
    # The expected parents are:
    a.parents = ['f1']
    c.parents = [a, 'f2']
    """
    def get_config(self):
        """Returns the config of the feature column.

    A FeatureColumn config is a Python dictionary (serializable) containing the
    configuration of a FeatureColumn. The same FeatureColumn can be
    reinstantiated later from this configuration.

    The config of a feature column does not include information about feature
    columns depending on it nor the FeatureColumn class name.

    Example with (de)serialization practices followed in this file:
    ```python
    class SerializationExampleFeatureColumn(
        FeatureColumn, collections.namedtuple(
            'SerializationExampleFeatureColumn',
            ('dimension', 'parent', 'dtype', 'normalizer_fn'))):

      def get_config(self):
        # Create a dict from the namedtuple.
        # Python attribute literals can be directly copied from / to the config.
        # For example 'dimension', assuming it is an integer literal.
        config = dict(zip(self._fields, self))

        # (De)serialization of parent FeatureColumns should use the provided
        # (de)serialize_feature_column() methods that take care of de-duping.
        config['parent'] = serialize_feature_column(self.parent)

        # Many objects provide custom (de)serialization e.g: for tf.DType
        # tf.DType.name, tf.as_dtype() can be used.
        config['dtype'] = self.dtype.name

        # Non-trivial dependencies should be Keras-(de)serializable.
        config['normalizer_fn'] = generic_utils.serialize_keras_object(
            self.normalizer_fn)

        return config

      @classmethod
      def from_config(cls, config, custom_objects=None, columns_by_name=None):
        # This should do the inverse transform from `get_config` and construct
        # the namedtuple.
        kwargs = config.copy()
        kwargs['parent'] = deserialize_feature_column(
            config['parent'], custom_objects, columns_by_name)
        kwargs['dtype'] = dtypes.as_dtype(config['dtype'])
        kwargs['normalizer_fn'] = generic_utils.deserialize_keras_object(
          config['normalizer_fn'], custom_objects=custom_objects)
        return cls(**kwargs)

    ```
    Returns:
      A serializable Dict that can be used to deserialize the object with
      from_config.
    """
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None, columns_by_name: Incomplete | None = None):
        """Creates a FeatureColumn from its config.

    This method should be the reverse of `get_config`, capable of instantiating
    the same FeatureColumn from the config dictionary. See `get_config` for an
    example of common (de)serialization practices followed in this file.

    TODO(b/118939620): This is a private method until consensus is reached on
    supporting object deserialization deduping within Keras.

    Args:
      config: A Dict config acquired with `get_config`.
      custom_objects: Optional dictionary mapping names (strings) to custom
        classes or functions to be considered during deserialization.
      columns_by_name: A Dict[String, FeatureColumn] of existing columns in
        order to avoid duplication. Should be passed to any calls to
        deserialize_feature_column().

    Returns:
      A FeatureColumn for the input config.
    """

class DenseColumn(FeatureColumn, metaclass=abc.ABCMeta):
    """Represents a column which can be represented as `Tensor`.

  Some examples of this type are: numeric_column, embedding_column,
  indicator_column.
  """
    @property
    @abc.abstractmethod
    def variable_shape(self):
        """`TensorShape` of `get_dense_tensor`, without batch dimension."""
    @abc.abstractmethod
    def get_dense_tensor(self, transformation_cache, state_manager):
        """Returns a `Tensor`.

    The output of this function will be used by model-builder-functions. For
    example the pseudo code of `input_layer` will be like:

    ```python
    def input_layer(features, feature_columns, ...):
      outputs = [fc.get_dense_tensor(...) for fc in feature_columns]
      return tf.concat(outputs)
    ```

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.

    Returns:
      `Tensor` of shape [batch_size] + `variable_shape`.
    """

def is_feature_column_v2(feature_columns):
    """Returns True if all feature columns are V2."""

class CategoricalColumn(FeatureColumn, metaclass=abc.ABCMeta):
    """Represents a categorical feature.

  A categorical feature typically handled with a `tf.sparse.SparseTensor` of
  IDs.
  """

    class IdWeightPair(NamedTuple):
        id_tensor: Incomplete
        weight_tensor: Incomplete
    @property
    @abc.abstractmethod
    def num_buckets(self):
        """Returns number of buckets in this sparse feature."""
    @abc.abstractmethod
    def get_sparse_tensors(self, transformation_cache, state_manager):
        """Returns an IdWeightPair.

    `IdWeightPair` is a pair of `SparseTensor`s which represents ids and
    weights.

    `IdWeightPair.id_tensor` is typically a `batch_size` x `num_buckets`
    `SparseTensor` of `int64`. `IdWeightPair.weight_tensor` is either a
    `SparseTensor` of `float` or `None` to indicate all weights should be
    taken to be 1. If specified, `weight_tensor` must have exactly the same
    shape and indices as `sp_ids`. Expected `SparseTensor` is same as parsing
    output of a `VarLenFeature` which is a ragged matrix.

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.
    """

class SequenceDenseColumn(FeatureColumn, metaclass=abc.ABCMeta):
    """Represents dense sequence data."""

    class TensorSequenceLengthPair(NamedTuple):
        dense_tensor: Incomplete
        sequence_length: Incomplete
    @abc.abstractmethod
    def get_sequence_dense_tensor(self, transformation_cache, state_manager):
        """Returns a `TensorSequenceLengthPair`.

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.
    """

class FeatureTransformationCache:
    '''Handles caching of transformations while building the model.

  `FeatureColumn` specifies how to digest an input column to the network. Some
  feature columns require data transformations. This class caches those
  transformations.

  Some features may be used in more than one place. For example, one can use a
  bucketized feature by itself and a cross with it. In that case we
  should create only one bucketization op instead of creating ops for each
  feature column separately. To handle re-use of transformed columns,
  `FeatureTransformationCache` caches all previously transformed columns.

  Example:
  We\'re trying to use the following `FeatureColumn`s:

  ```python
  bucketized_age = fc.bucketized_column(fc.numeric_column("age"), ...)
  keywords = fc.categorical_column_with_hash_buckets("keywords", ...)
  age_X_keywords = fc.crossed_column([bucketized_age, "keywords"])
  ... = linear_model(features,
                          [bucketized_age, keywords, age_X_keywords]
  ```

  If we transform each column independently, then we\'ll get duplication of
  bucketization (one for cross, one for bucketization itself).
  The `FeatureTransformationCache` eliminates this duplication.
  '''
    def __init__(self, features) -> None:
        """Creates a `FeatureTransformationCache`.

    Args:
      features: A mapping from feature column to objects that are `Tensor` or
        `SparseTensor`, or can be converted to same via
        `sparse_tensor.convert_to_tensor_or_sparse_tensor`. A `string` key
        signifies a base feature (not-transformed). A `FeatureColumn` key means
        that this `Tensor` is the output of an existing `FeatureColumn` which
        can be reused.
    """
    def get(self, key, state_manager, training: Incomplete | None = None):
        """Returns a `Tensor` for the given key.

    A `str` key is used to access a base feature (not-transformed). When a
    `FeatureColumn` is passed, the transformed feature is returned if it
    already exists, otherwise the given `FeatureColumn` is asked to provide its
    transformed output, which is then cached.

    Args:
      key: a `str` or a `FeatureColumn`.
      state_manager: A StateManager object that holds the FeatureColumn state.
      training: Boolean indicating whether to the column is being used in
        training mode. This argument is passed to the transform_feature method
        of any `FeatureColumn` that takes a `training` argument. For example, if
        a `FeatureColumn` performed dropout, it could expose a `training`
        argument to control whether the dropout should be applied.

    Returns:
      The transformed `Tensor` corresponding to the `key`.

    Raises:
      ValueError: if key is not found or a transformed `Tensor` cannot be
        computed.
    """

class NumericColumn(DenseColumn, fc_old._DenseColumn, NamedTuple('NumericColumn', [('key', Incomplete), ('shape', Incomplete), ('default_value', Incomplete), ('dtype', Incomplete), ('normalizer_fn', Incomplete)])):
    """see `numeric_column`."""
    @property
    def name(self):
        """See `FeatureColumn` base class."""
    @property
    def parse_example_spec(self):
        """See `FeatureColumn` base class."""
    def transform_feature(self, transformation_cache, state_manager):
        """See `FeatureColumn` base class.

    In this case, we apply the `normalizer_fn` to the input tensor.

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.

    Returns:
      Normalized input tensor.
    Raises:
      ValueError: If a SparseTensor is passed in.
    """
    @property
    def variable_shape(self):
        """See `DenseColumn` base class."""
    def get_dense_tensor(self, transformation_cache, state_manager):
        """Returns dense `Tensor` representing numeric feature.

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.

    Returns:
      Dense `Tensor` created within `transform_feature`.
    """
    @property
    def parents(self):
        """See 'FeatureColumn` base class."""
    def get_config(self):
        """See 'FeatureColumn` base class."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None, columns_by_name: Incomplete | None = None):
        """See 'FeatureColumn` base class."""

class BucketizedColumn(DenseColumn, CategoricalColumn, fc_old._DenseColumn, fc_old._CategoricalColumn, NamedTuple('BucketizedColumn', [('source_column', Incomplete), ('boundaries', Incomplete)])):
    """See `bucketized_column`."""
    @property
    def name(self):
        """See `FeatureColumn` base class."""
    @property
    def parse_example_spec(self):
        """See `FeatureColumn` base class."""
    def transform_feature(self, transformation_cache, state_manager):
        """Returns bucketized categorical `source_column` tensor."""
    @property
    def variable_shape(self):
        """See `DenseColumn` base class."""
    def get_dense_tensor(self, transformation_cache, state_manager):
        """Returns one hot encoded dense `Tensor`."""
    @property
    def num_buckets(self):
        """See `CategoricalColumn` base class."""
    def get_sparse_tensors(self, transformation_cache, state_manager):
        """Converts dense inputs to SparseTensor so downstream code can use it."""
    @property
    def parents(self):
        """See 'FeatureColumn` base class."""
    def get_config(self):
        """See 'FeatureColumn` base class."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None, columns_by_name: Incomplete | None = None):
        """See 'FeatureColumn` base class."""

class EmbeddingColumn(DenseColumn, SequenceDenseColumn, fc_old._DenseColumn, fc_old._SequenceDenseColumn, NamedTuple('EmbeddingColumn', [('categorical_column', Incomplete), ('dimension', Incomplete), ('combiner', Incomplete), ('initializer', Incomplete), ('ckpt_to_load_from', Incomplete), ('tensor_name_in_ckpt', Incomplete), ('max_norm', Incomplete), ('trainable', Incomplete), ('use_safe_embedding_lookup', Incomplete)])):
    """See `embedding_column`."""
    def __new__(cls, categorical_column, dimension, combiner, initializer, ckpt_to_load_from, tensor_name_in_ckpt, max_norm, trainable, use_safe_embedding_lookup: bool = True): ...
    @property
    def name(self):
        """See `FeatureColumn` base class."""
    @property
    def parse_example_spec(self):
        """See `FeatureColumn` base class."""
    def transform_feature(self, transformation_cache, state_manager):
        """Transforms underlying `categorical_column`."""
    @property
    def variable_shape(self):
        """See `DenseColumn` base class."""
    def create_state(self, state_manager) -> None:
        """Creates the embedding lookup variable."""
    def get_dense_tensor(self, transformation_cache, state_manager):
        """Returns tensor after doing the embedding lookup.

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.

    Returns:
      Embedding lookup tensor.

    Raises:
      ValueError: `categorical_column` is SequenceCategoricalColumn.
    """
    def get_sequence_dense_tensor(self, transformation_cache, state_manager):
        """See `SequenceDenseColumn` base class."""
    @property
    def parents(self):
        """See 'FeatureColumn` base class."""
    def get_config(self):
        """See 'FeatureColumn` base class."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None, columns_by_name: Incomplete | None = None):
        """See 'FeatureColumn` base class."""

class SharedEmbeddingColumnCreator(autotrackable.AutoTrackable):
    """Class that creates a `SharedEmbeddingColumn`."""
    def __init__(self, dimension, initializer, ckpt_to_load_from, tensor_name_in_ckpt, num_buckets, trainable, name: str = 'shared_embedding_column_creator', use_safe_embedding_lookup: bool = True) -> None: ...
    def __call__(self, categorical_column, combiner, max_norm): ...
    @property
    def embedding_weights(self): ...
    @property
    def dimension(self): ...

class SharedEmbeddingColumn(DenseColumn, SequenceDenseColumn, fc_old._DenseColumn, fc_old._SequenceDenseColumn, NamedTuple('SharedEmbeddingColumn', [('categorical_column', Incomplete), ('shared_embedding_column_creator', Incomplete), ('combiner', Incomplete), ('max_norm', Incomplete), ('use_safe_embedding_lookup', Incomplete)])):
    """See `embedding_column`."""
    def __new__(cls, categorical_column, shared_embedding_column_creator, combiner, max_norm, use_safe_embedding_lookup: bool = True): ...
    @property
    def name(self):
        """See `FeatureColumn` base class."""
    @property
    def parse_example_spec(self):
        """See `FeatureColumn` base class."""
    def transform_feature(self, transformation_cache, state_manager):
        """See `FeatureColumn` base class."""
    @property
    def variable_shape(self):
        """See `DenseColumn` base class."""
    def get_dense_tensor(self, transformation_cache, state_manager):
        """Returns the embedding lookup result."""
    def get_sequence_dense_tensor(self, transformation_cache, state_manager):
        """See `SequenceDenseColumn` base class."""
    @property
    def parents(self):
        """See 'FeatureColumn` base class."""

class HashedCategoricalColumn(CategoricalColumn, fc_old._CategoricalColumn, NamedTuple('HashedCategoricalColumn', [('key', Incomplete), ('hash_bucket_size', Incomplete), ('dtype', Incomplete)])):
    """see `categorical_column_with_hash_bucket`."""
    @property
    def name(self):
        """See `FeatureColumn` base class."""
    @property
    def parse_example_spec(self):
        """See `FeatureColumn` base class."""
    def transform_feature(self, transformation_cache, state_manager):
        """Hashes the values in the feature_column."""
    @property
    def num_buckets(self):
        """Returns number of buckets in this sparse feature."""
    def get_sparse_tensors(self, transformation_cache, state_manager):
        """See `CategoricalColumn` base class."""
    @property
    def parents(self):
        """See 'FeatureColumn` base class."""
    def get_config(self):
        """See 'FeatureColumn` base class."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None, columns_by_name: Incomplete | None = None):
        """See 'FeatureColumn` base class."""

class VocabularyFileCategoricalColumn(CategoricalColumn, fc_old._CategoricalColumn, NamedTuple('VocabularyFileCategoricalColumn', [('key', Incomplete), ('vocabulary_file', Incomplete), ('vocabulary_size', Incomplete), ('num_oov_buckets', Incomplete), ('dtype', Incomplete), ('default_value', Incomplete), ('file_format', Incomplete)])):
    """See `categorical_column_with_vocabulary_file`."""
    def __new__(cls, key, vocabulary_file, vocabulary_size, num_oov_buckets, dtype, default_value, file_format: Incomplete | None = None): ...
    @property
    def name(self):
        """See `FeatureColumn` base class."""
    @property
    def parse_example_spec(self):
        """See `FeatureColumn` base class."""
    def transform_feature(self, transformation_cache, state_manager):
        """Creates a lookup table for the vocabulary."""
    @property
    def num_buckets(self):
        """Returns number of buckets in this sparse feature."""
    def get_sparse_tensors(self, transformation_cache, state_manager):
        """See `CategoricalColumn` base class."""
    @property
    def parents(self):
        """See 'FeatureColumn` base class."""
    def get_config(self):
        """See 'FeatureColumn` base class."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None, columns_by_name: Incomplete | None = None):
        """See 'FeatureColumn` base class."""

class VocabularyListCategoricalColumn(CategoricalColumn, fc_old._CategoricalColumn, NamedTuple('VocabularyListCategoricalColumn', [('key', Incomplete), ('vocabulary_list', Incomplete), ('dtype', Incomplete), ('default_value', Incomplete), ('num_oov_buckets', Incomplete)])):
    """See `categorical_column_with_vocabulary_list`."""
    @property
    def name(self):
        """See `FeatureColumn` base class."""
    @property
    def parse_example_spec(self):
        """See `FeatureColumn` base class."""
    def transform_feature(self, transformation_cache, state_manager):
        """Creates a lookup table for the vocabulary list."""
    @property
    def num_buckets(self):
        """Returns number of buckets in this sparse feature."""
    def get_sparse_tensors(self, transformation_cache, state_manager):
        """See `CategoricalColumn` base class."""
    @property
    def parents(self):
        """See 'FeatureColumn` base class."""
    def get_config(self):
        """See 'FeatureColumn` base class."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None, columns_by_name: Incomplete | None = None):
        """See 'FeatureColumn` base class."""

class IdentityCategoricalColumn(CategoricalColumn, fc_old._CategoricalColumn, NamedTuple('IdentityCategoricalColumn', [('key', Incomplete), ('number_buckets', Incomplete), ('default_value', Incomplete)])):
    """See `categorical_column_with_identity`."""
    @property
    def name(self):
        """See `FeatureColumn` base class."""
    @property
    def parse_example_spec(self):
        """See `FeatureColumn` base class."""
    def transform_feature(self, transformation_cache, state_manager):
        """Returns a SparseTensor with identity values."""
    @property
    def num_buckets(self):
        """Returns number of buckets in this sparse feature."""
    def get_sparse_tensors(self, transformation_cache, state_manager):
        """See `CategoricalColumn` base class."""
    @property
    def parents(self):
        """See 'FeatureColumn` base class."""
    def get_config(self):
        """See 'FeatureColumn` base class."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None, columns_by_name: Incomplete | None = None):
        """See 'FeatureColumn` base class."""

class WeightedCategoricalColumn(CategoricalColumn, fc_old._CategoricalColumn, NamedTuple('WeightedCategoricalColumn', [('categorical_column', Incomplete), ('weight_feature_key', Incomplete), ('dtype', Incomplete)])):
    """See `weighted_categorical_column`."""
    @property
    def name(self):
        """See `FeatureColumn` base class."""
    @property
    def parse_example_spec(self):
        """See `FeatureColumn` base class."""
    @property
    def num_buckets(self):
        """See `DenseColumn` base class."""
    def transform_feature(self, transformation_cache, state_manager):
        """Applies weights to tensor generated from `categorical_column`'."""
    def get_sparse_tensors(self, transformation_cache, state_manager):
        """See `CategoricalColumn` base class."""
    @property
    def parents(self):
        """See 'FeatureColumn` base class."""
    def get_config(self):
        """See 'FeatureColumn` base class."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None, columns_by_name: Incomplete | None = None):
        """See 'FeatureColumn` base class."""

class CrossedColumn(CategoricalColumn, fc_old._CategoricalColumn, NamedTuple('CrossedColumn', [('keys', Incomplete), ('hash_bucket_size', Incomplete), ('hash_key', Incomplete)])):
    """See `crossed_column`."""
    @property
    def name(self):
        """See `FeatureColumn` base class."""
    @property
    def parse_example_spec(self):
        """See `FeatureColumn` base class."""
    def transform_feature(self, transformation_cache, state_manager):
        """Generates a hashed sparse cross from the input tensors."""
    @property
    def num_buckets(self):
        """Returns number of buckets in this sparse feature."""
    def get_sparse_tensors(self, transformation_cache, state_manager):
        """See `CategoricalColumn` base class."""
    @property
    def parents(self):
        """See 'FeatureColumn` base class."""
    def get_config(self):
        """See 'FeatureColumn` base class."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None, columns_by_name: Incomplete | None = None):
        """See 'FeatureColumn` base class."""

class IndicatorColumn(DenseColumn, SequenceDenseColumn, fc_old._DenseColumn, fc_old._SequenceDenseColumn, NamedTuple('IndicatorColumn', [('categorical_column', Incomplete)])):
    """Represents a one-hot column for use in deep networks.

  Args:
    categorical_column: A `CategoricalColumn` which is created by
      `categorical_column_with_*` function.
  """
    @property
    def name(self):
        """See `FeatureColumn` base class."""
    def transform_feature(self, transformation_cache, state_manager):
        """Returns dense `Tensor` representing feature.

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.

    Returns:
      Transformed feature `Tensor`.

    Raises:
      ValueError: if input rank is not known at graph building time.
    """
    @property
    def parse_example_spec(self):
        """See `FeatureColumn` base class."""
    @property
    def variable_shape(self):
        """Returns a `TensorShape` representing the shape of the dense `Tensor`."""
    def get_dense_tensor(self, transformation_cache, state_manager):
        """Returns dense `Tensor` representing feature.

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.

    Returns:
      Dense `Tensor` created within `transform_feature`.

    Raises:
      ValueError: If `categorical_column` is a `SequenceCategoricalColumn`.
    """
    def get_sequence_dense_tensor(self, transformation_cache, state_manager):
        """See `SequenceDenseColumn` base class."""
    @property
    def parents(self):
        """See 'FeatureColumn` base class."""
    def get_config(self):
        """See 'FeatureColumn` base class."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None, columns_by_name: Incomplete | None = None):
        """See 'FeatureColumn` base class."""

class SequenceCategoricalColumn(CategoricalColumn, fc_old._SequenceCategoricalColumn, NamedTuple('SequenceCategoricalColumn', [('categorical_column', Incomplete)])):
    """Represents sequences of categorical data."""
    @property
    def name(self):
        """See `FeatureColumn` base class."""
    @property
    def parse_example_spec(self):
        """See `FeatureColumn` base class."""
    def transform_feature(self, transformation_cache, state_manager):
        """See `FeatureColumn` base class."""
    @property
    def num_buckets(self):
        """Returns number of buckets in this sparse feature."""
    def get_sparse_tensors(self, transformation_cache, state_manager):
        """Returns an IdWeightPair.

    `IdWeightPair` is a pair of `SparseTensor`s which represents ids and
    weights.

    `IdWeightPair.id_tensor` is typically a `batch_size` x `num_buckets`
    `SparseTensor` of `int64`. `IdWeightPair.weight_tensor` is either a
    `SparseTensor` of `float` or `None` to indicate all weights should be
    taken to be 1. If specified, `weight_tensor` must have exactly the same
    shape and indices as `sp_ids`. Expected `SparseTensor` is same as parsing
    output of a `VarLenFeature` which is a ragged matrix.

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.
    """
    @property
    def parents(self):
        """See 'FeatureColumn` base class."""
    def get_config(self):
        """See 'FeatureColumn` base class."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None, columns_by_name: Incomplete | None = None):
        """See 'FeatureColumn` base class."""
