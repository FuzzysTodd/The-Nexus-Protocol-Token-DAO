import abc
from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.saved_model import signature_def_utils as signature_def_utils

class ExportOutput(metaclass=abc.ABCMeta):
    """Represents an output of a model that can be served.

  These typically correspond to model heads.
  """
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def as_signature_def(self, receiver_tensors):
        """Generate a SignatureDef proto for inclusion in a MetaGraphDef.

    The SignatureDef will specify outputs as described in this ExportOutput,
    and will use the provided receiver_tensors as inputs.

    Args:
      receiver_tensors: a `Tensor`, or a dict of string to `Tensor`, specifying
        input nodes that will be fed.
    """

class ClassificationOutput(ExportOutput):
    """Represents the output of a classification head.

  Either classes or scores or both must be set.

  The classes `Tensor` must provide string labels, not integer class IDs.

  If only classes is set, it is interpreted as providing top-k results in
  descending order.

  If only scores is set, it is interpreted as providing a score for every class
  in order of class ID.

  If both classes and scores are set, they are interpreted as zipped, so each
  score corresponds to the class at the same index.  Clients should not depend
  on the order of the entries.
  """
    def __init__(self, scores: Incomplete | None = None, classes: Incomplete | None = None) -> None:
        """Constructor for `ClassificationOutput`.

    Args:
      scores: A float `Tensor` giving scores (sometimes but not always
          interpretable as probabilities) for each class.  May be `None`, but
          only if `classes` is set.  Interpretation varies-- see class doc.
      classes: A string `Tensor` giving predicted class labels.  May be `None`,
          but only if `scores` is set.  Interpretation varies-- see class doc.

    Raises:
      ValueError: if neither classes nor scores is set, or one of them is not a
          `Tensor` with the correct dtype.
    """
    @property
    def scores(self): ...
    @property
    def classes(self): ...
    def as_signature_def(self, receiver_tensors): ...

class RegressionOutput(ExportOutput):
    """Represents the output of a regression head."""
    def __init__(self, value) -> None:
        """Constructor for `RegressionOutput`.

    Args:
      value: a float `Tensor` giving the predicted values.  Required.

    Raises:
      ValueError: if the value is not a `Tensor` with dtype tf.float32.
    """
    @property
    def value(self): ...
    def as_signature_def(self, receiver_tensors): ...

class PredictOutput(ExportOutput):
    """Represents the output of a generic prediction head.

  A generic prediction need not be either a classification or a regression.

  Named outputs must be provided as a dict from string to `Tensor`,
  """
    def __init__(self, outputs) -> None:
        """Constructor for PredictOutput.

    Args:
      outputs: A `Tensor` or a dict of string to `Tensor` representing the
        predictions.

    Raises:
      ValueError: if the outputs is not dict, or any of its keys are not
          strings, or any of its values are not `Tensor`s.
    """
    @property
    def outputs(self): ...
    def as_signature_def(self, receiver_tensors): ...

class _SupervisedOutput(ExportOutput, metaclass=abc.ABCMeta):
    """Represents the output of a supervised training or eval process."""
    __metaclass__ = abc.ABCMeta
    LOSS_NAME: str
    PREDICTIONS_NAME: str
    METRICS_NAME: str
    METRIC_VALUE_SUFFIX: str
    METRIC_UPDATE_SUFFIX: str
    def __init__(self, loss: Incomplete | None = None, predictions: Incomplete | None = None, metrics: Incomplete | None = None) -> None:
        """Constructor for SupervisedOutput (ie, Train or Eval output).

    Args:
      loss: dict of Tensors or single Tensor representing calculated loss.
      predictions: dict of Tensors or single Tensor representing model
        predictions.
      metrics: Dict of metric results keyed by name.
        The values of the dict can be one of the following:
        (1) instance of `Metric` class.
        (2) (metric_value, update_op) tuples, or a single tuple.
        metric_value must be a Tensor, and update_op must be a Tensor or Op.

    Raises:
      ValueError: if any of the outputs' dict keys are not strings or tuples of
        strings or the values are not Tensors (or Operations in the case of
        update_op).
    """
    @property
    def loss(self): ...
    @property
    def predictions(self): ...
    @property
    def metrics(self): ...
    def as_signature_def(self, receiver_tensors): ...

class TrainOutput(_SupervisedOutput):
    """Represents the output of a supervised training process.

  This class generates the appropriate signature def for exporting
  training output by type-checking and wrapping loss, predictions, and metrics
  values.
  """
class EvalOutput(_SupervisedOutput):
    """Represents the output of a supervised eval process.

  This class generates the appropriate signature def for exporting
  eval output by type-checking and wrapping loss, predictions, and metrics
  values.
  """
