from _typeshed import Incomplete
from keras.engine import data_adapter as data_adapter
from keras.models import Model as Model
from keras.saving.legacy.serialization import serialize_keras_object as serialize_keras_object
from keras.saving.object_registration import register_keras_serializable as register_keras_serializable

class SharpnessAwareMinimization(Model):
    """Sharpness aware minimization (SAM) training flow.

    Sharpness-aware minimization (SAM) is a technique that improves the model
    generalization and provides robustness to label noise. Mini-batch splitting
    is proven to improve the SAM's performance, so users can control how mini
    batches are split via setting the `num_batch_splits` argument.

    Args:
      model: `tf.keras.Model` instance. The inner model that does the
        forward-backward pass.
      rho: float, defaults to 0.05. The gradients scaling factor.
      num_batch_splits: int, defaults to None. The number of mini batches to
        split into from each data batch. If None, batches are not split into
        sub-batches.
      name: string, defaults to None. The name of the SAM model.

    Reference:
      [Pierre Foret et al., 2020](https://arxiv.org/abs/2010.01412)
    """
    model: Incomplete
    rho: Incomplete
    num_batch_splits: Incomplete
    def __init__(self, model, rho: float = 0.05, num_batch_splits: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
    def train_step(self, data):
        """The logic of one SAM training step.

        Args:
          data: A nested structure of `Tensor`s. It should be of structure
            (x, y, sample_weight) or (x, y).

        Returns:
          A dict mapping metric names to running average values.
        """
    def call(self, inputs):
        """Forward pass of SAM.

        SAM delegates the forward pass call to the wrapped model.

        Args:
          inputs: Tensor. The model inputs.

        Returns:
          A Tensor, the outputs of the wrapped model for given `inputs`.
        """
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...
