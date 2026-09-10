import tensorflow.compat.v2 as tf
from _typeshed import Incomplete
from collections.abc import Generator
from keras.feature_column import dense_features as dense_features
from keras.utils import tf_contextlib as tf_contextlib

class DenseFeatures(dense_features.DenseFeatures):
    '''A layer that produces a dense `Tensor` based on given `feature_columns`.

    Generally a single example in training data is described with
    FeatureColumns.  At the first layer of the model, this column oriented data
    should be converted to a single `Tensor`.

    This layer can be called multiple times with different features.

    This is the V2 version of this layer that uses name_scopes to create
    variables instead of variable_scopes. But this approach currently lacks
    support for partitioned variables. In that case, use the V1 version instead.

    Example:

    ```python
    price = tf.feature_column.numeric_column(\'price\')
    keywords_embedded = tf.feature_column.embedding_column(
        tf.feature_column.categorical_column_with_hash_bucket("keywords",
                                                              10000),
        dimensions=16)
    columns = [price, keywords_embedded, ...]
    feature_layer = tf.keras.layers.DenseFeatures(columns)

    features = tf.io.parse_example(
        ..., features=tf.feature_column.make_parse_example_spec(columns))
    dense_tensor = feature_layer(features)
    for units in [128, 64, 32]:
      dense_tensor = tf.keras.layers.Dense(units, activation=\'relu\')(
        dense_tensor)
    prediction = tf.keras.layers.Dense(1)(dense_tensor)
    ```
    '''
    def __init__(self, feature_columns, trainable: bool = True, name: Incomplete | None = None, **kwargs) -> None:
        """Creates a DenseFeatures object.

        Args:
          feature_columns: An iterable containing the FeatureColumns to use as
            inputs to your model. All items should be instances of classes
            derived from `DenseColumn` such as `numeric_column`,
            `embedding_column`, `bucketized_column`, `indicator_column`. If you
            have categorical features, you can wrap them with an
            `embedding_column` or `indicator_column`.
          trainable:  Boolean, whether the layer's variables will be updated via
            gradient descent during training.
          name: Name to give to the DenseFeatures.
          **kwargs: Keyword arguments to construct a layer.

        Raises:
          ValueError: if an item in `feature_columns` is not a `DenseColumn`.
        """
    def build(self, _) -> None: ...

class _StateManagerImplV2(tf.__internal__.feature_column.StateManager):
    """Manages the state of DenseFeatures."""
    def create_variable(self, feature_column, name, shape, dtype: Incomplete | None = None, trainable: bool = True, use_resource: bool = True, initializer: Incomplete | None = None): ...

def no_manual_dependency_tracking_scope(obj) -> Generator[None, None, None]:
    '''A context that disables manual dependency tracking for the given `obj`.

    Sometimes library methods might track objects on their own and we might want
    to disable that and do the tracking on our own. One can then use this
    context manager to disable the tracking the library method does and do your
    own tracking.

    For example:

    class TestLayer(tf.keras.Layer):
      def build():
        with no_manual_dependency_tracking_scope(self):
          var = self.add_weight("name1")  # Creates a var and doesn\'t track it
        # We track variable with name `name2`
        self._track_trackable("name2", var)

    Args:
      obj: A trackable object.

    Yields:
      a scope in which the object doesn\'t track dependencies manually.
    '''
