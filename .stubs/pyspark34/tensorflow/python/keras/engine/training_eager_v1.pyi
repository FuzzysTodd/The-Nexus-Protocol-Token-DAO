from _typeshed import Incomplete
from tensorflow.python.eager.backprop import GradientTape as GradientTape
from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import training_utils as training_utils, training_utils_v1 as training_utils_v1
from tensorflow.python.keras.mixed_precision import loss_scale_optimizer as loss_scale_optimizer
from tensorflow.python.keras.utils import losses_utils as losses_utils
from tensorflow.python.ops import math_ops as math_ops
from tensorflow.python.util import nest as nest

def train_on_batch(model, inputs, targets, sample_weights: Incomplete | None = None, output_loss_metrics: Incomplete | None = None):
    """Calculates the loss and gradient updates for one input batch.

  Args:
      model: Model whose loss has to be calculated.
      inputs: Input batch data.
      targets: Target batch data.
      sample_weights: Sample weight batch data.
      output_loss_metrics: List of metrics that are used to aggregated output
        loss values.

  Returns:
      Dict with three items:
        'total_loss': list with a single tensor for overall loss,
        'output_losses': list of tensors for loss corresponding to each of the
          model output. Could be a empty list when model has only one output.
        'metrics': list of tensors for metric specified.
  """
def test_on_batch(model, inputs, targets, sample_weights: Incomplete | None = None, output_loss_metrics: Incomplete | None = None):
    """Calculates the loss for one input batch.

  Args:
      model: Model whose loss has to be calculated.
      inputs: Input batch data.
      targets: Target batch data.
      sample_weights: Sample weight batch data.
      output_loss_metrics: List of metrics that are used to aggregated output
        loss values.

  Returns:
      Dict with three items:
        'total_loss': single tensor for overall loss,
        'output_losses': list of tensors for loss corresponding to each of the
          model output. Could be a empty list when model has only one output.
        'metrics': list of tensors for metric specified.
  """
