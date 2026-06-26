from _typeshed import Incomplete
from keras.engine.base_layer import Layer as Layer
from keras.saving.legacy import serialization as serialization

class _BaseFeaturesLayer(Layer):
    """Base class for DenseFeatures and SequenceFeatures.

    Defines common methods and helpers.

    Args:
      feature_columns: An iterable containing the FeatureColumns to use as
        inputs to your model.
      expected_column_type: Expected class for provided feature columns.
      trainable:  Boolean, whether the layer's variables will be updated via
        gradient descent during training.
      name: Name to give to the DenseFeatures.
      **kwargs: Keyword arguments to construct a layer.

    Raises:
      ValueError: if an item in `feature_columns` doesn't match
        `expected_column_type`.
    """
    def __init__(self, feature_columns, expected_column_type, trainable, name, partitioner: Incomplete | None = None, **kwargs) -> None: ...
    def build(self, _) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...
