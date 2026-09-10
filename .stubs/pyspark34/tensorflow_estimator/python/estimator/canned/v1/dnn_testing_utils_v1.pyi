import tensorflow as tf
from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import estimator as estimator, model_fn as model_fn
from tensorflow_estimator.python.estimator.canned import metric_keys as metric_keys, prediction_keys as prediction_keys
from tensorflow_estimator.python.estimator.inputs import numpy_io as numpy_io
from tensorflow_estimator.python.estimator.mode_keys import ModeKeys as ModeKeys

LEARNING_RATE_NAME: str
HIDDEN_WEIGHTS_NAME_PATTERN: str
HIDDEN_BIASES_NAME_PATTERN: str
BATCH_NORM_BETA_NAME_PATTERN: str
BATCH_NORM_GAMMA_NAME_PATTERN: str
BATCH_NORM_MEAN_NAME_PATTERN: str
BATCH_NORM_VARIANCE_NAME_PATTERN: str
LOGITS_WEIGHTS_NAME: str
LOGITS_BIASES_NAME: str
OCCUPATION_EMBEDDING_NAME: str
CITY_EMBEDDING_NAME: str

def assert_close(expected, actual, rtol: float = 0.0001, message: str = '', name: str = 'assert_close'): ...
def create_checkpoint(weights_and_biases, global_step, model_dir, batch_norm_vars: Incomplete | None = None) -> None:
    """Create checkpoint file with provided model weights.

  Args:
    weights_and_biases: Iterable of tuples of weight and bias values.
    global_step: Initial global step to save in checkpoint.
    model_dir: Directory into which checkpoint is saved.
    batch_norm_vars: Variables used for batch normalization.
  """
def mock_head(testcase, hidden_units, logits_dimension, expected_logits):
    """Returns a mock head that validates logits values and variable names."""
def mock_optimizer(testcase, hidden_units, expected_loss: Incomplete | None = None):
    """Creates a mock optimizer to test the train method.

  Args:
    testcase: A TestCase instance.
    hidden_units: Iterable of integer sizes for the hidden layers.
    expected_loss: If given, will assert the loss value.

  Returns:
    A mock Optimizer.
  """

class BaseDNNModelFnTest:
    """Tests that _dnn_model_fn passes expected logits to mock head."""
    def __init__(self, dnn_model_fn, fc_impl=...) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_one_dim_logits(self) -> None:
        """Tests one-dimensional logits.

    input_layer = [[10]]
    hidden_layer_0 = [[relu(0.6*10 +0.1), relu(0.5*10 -0.1)]] = [[6.1, 4.9]]
    hidden_layer_1 = [[relu(1*6.1 -0.8*4.9 +0.2), relu(0.8*6.1 -1*4.9 -0.1)]]
                   = [[relu(2.38), relu(-0.12)]] = [[2.38, 0]]
    logits = [[-1*2.38 +1*0 +0.3]] = [[-2.08]]
    """
    def test_multi_dim_logits(self) -> None:
        """Tests multi-dimensional logits.

    input_layer = [[10]]
    hidden_layer_0 = [[relu(0.6*10 +0.1), relu(0.5*10 -0.1)]] = [[6.1, 4.9]]
    hidden_layer_1 = [[relu(1*6.1 -0.8*4.9 +0.2), relu(0.8*6.1 -1*4.9 -0.1)]]
                   = [[relu(2.38), relu(-0.12)]] = [[2.38, 0]]
    logits = [[-1*2.38 +0.3, 1*2.38 -0.3, 0.5*2.38]]
           = [[-2.08, 2.08, 1.19]]
    """
    def test_multi_example_multi_dim_logits(self) -> None:
        """Tests multiple examples and multi-dimensional logits.

    input_layer = [[10], [5]]
    hidden_layer_0 = [[relu(0.6*10 +0.1), relu(0.5*10 -0.1)],
                      [relu(0.6*5 +0.1), relu(0.5*5 -0.1)]]
                   = [[6.1, 4.9], [3.1, 2.4]]
    hidden_layer_1 = [[relu(1*6.1 -0.8*4.9 +0.2), relu(0.8*6.1 -1*4.9 -0.1)],
                      [relu(1*3.1 -0.8*2.4 +0.2), relu(0.8*3.1 -1*2.4 -0.1)]]
                   = [[2.38, 0], [1.38, 0]]
    logits = [[-1*2.38 +0.3, 1*2.38 -0.3, 0.5*2.38],
              [-1*1.38 +0.3, 1*1.38 -0.3, 0.5*1.38]]
           = [[-2.08, 2.08, 1.19], [-1.08, 1.08, 0.69]]
    """
    def test_multi_dim_input_one_dim_logits(self) -> None:
        """Tests multi-dimensional inputs and one-dimensional logits.

    input_layer = [[10, 8]]
    hidden_layer_0 = [[relu(0.6*10 -0.6*8 +0.1), relu(0.5*10 -0.5*8 -0.1)]]
                   = [[1.3, 0.9]]
    hidden_layer_1 = [[relu(1*1.3 -0.8*0.9 + 0.2), relu(0.8*1.3 -1*0.9 -0.2)]]
                   = [[0.78, relu(-0.06)]] = [[0.78, 0]]
    logits = [[-1*0.78 +1*0 +0.3]] = [[-0.48]]
    """
    def test_multi_dim_input_multi_dim_logits(self) -> None:
        """Tests multi-dimensional inputs and multi-dimensional logits.

    input_layer = [[10, 8]]
    hidden_layer_0 = [[relu(0.6*10 -0.6*8 +0.1), relu(0.5*10 -0.5*8 -0.1)]]
                   = [[1.3, 0.9]]
    hidden_layer_1 = [[relu(1*1.3 -0.8*0.9 + 0.2), relu(0.8*1.3 -1*0.9 -0.2)]]
                   = [[0.78, relu(-0.06)]] = [[0.78, 0]]
    logits = [[-1*0.78 + 0.3, 1*0.78 -0.3, 0.5*0.78]] = [[-0.48, 0.48, 0.39]]
    """
    def test_multi_feature_column_multi_dim_logits(self) -> None:
        """Tests multiple feature columns and multi-dimensional logits.

    All numbers are the same as test_multi_dim_input_multi_dim_logits. The only
    difference is that the input consists of two 1D feature columns, instead of
    one 2D feature column.
    """
    def test_multi_feature_column_mix_multi_dim_logits(self) -> None:
        """Tests multiple feature columns and multi-dimensional logits.

    All numbers are the same as test_multi_dim_input_multi_dim_logits. The only
    difference is that the input consists of two 1D feature columns, instead of
    one 2D feature column.
    """
    def test_features_tensor_raises_value_error(self) -> None:
        """Tests that passing a Tensor for features raises a ValueError."""

class BaseDNNLogitFnTest:
    """Tests correctness of logits calculated from _dnn_logit_fn_builder."""
    def __init__(self, dnn_logit_fn_builder, fc_impl=...) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_one_dim_logits(self) -> None:
        """Tests one-dimensional logits.

    input_layer = [[10]]
    hidden_layer_0 = [[relu(0.6*10 +0.1), relu(0.5*10 -0.1)]] = [[6.1, 4.9]]
    hidden_layer_1 = [[relu(1*6.1 -0.8*4.9 +0.2), relu(0.8*6.1 -1*4.9 -0.1)]]
                   = [[relu(2.38), relu(-0.12)]] = [[2.38, 0]]
    logits = [[-1*2.38 +1*0 +0.3]] = [[-2.08]]
    """
    def test_one_dim_logits_with_batch_norm(self) -> None:
        """Tests one-dimensional logits.

    input_layer = [[10]]
    hidden_layer_0 = [[relu(0.6*10 +1), relu(0.5*10 -1)]] = [[7, 4]]
    hidden_layer_0 = [[relu(0.6*20 +1), relu(0.5*20 -1)]] = [[13, 9]]

    batch_norm_0, training (epsilon = 0.001):
      mean1 = 1/2*(7+13) = 10,
      variance1 = 1/2*(3^2+3^2) = 9
      x11 = (7-10)/sqrt(9+0.001) = -0.999944449,
      x21 = (13-10)/sqrt(9+0.001) = 0.999944449,

      mean2 = 1/2*(4+9) = 6.5,
      variance2 = 1/2*(2.5^2+.2.5^2) = 6.25
      x12 = (4-6.5)/sqrt(6.25+0.001) = -0.99992001,
      x22 = (9-6.5)/sqrt(6.25+0.001) = 0.99992001,

    logits = [[-1*(-0.999944449) + 2*(-0.99992001) + 0.3],
              [-1*0.999944449 + 2*0.99992001 + 0.3]]
           = [[-0.699895571],[1.299895571]]

    batch_norm_0, not training (epsilon = 0.001):
      moving_mean1 = 0, moving_variance1 = 1
      x11 = (7-0)/sqrt(1+0.001) = 6.996502623,
      x21 = (13-0)/sqrt(1+0.001) = 12.993504871,
      moving_mean2 = 0, moving_variance2 = 1
      x12 = (4-0)/sqrt(1+0.001) = 3.998001499,
      x22 = (9-0)/sqrt(1+0.001) = 8.995503372,

    logits = [[-1*6.996502623 + 2*3.998001499 + 0.3],
              [-1*12.993504871 + 2*8.995503372 + 0.3]]
           = [[1.299500375],[5.297501873]]
    """
    def test_multi_dim_logits(self) -> None:
        """Tests multi-dimensional logits.

    input_layer = [[10]]
    hidden_layer_0 = [[relu(0.6*10 +0.1), relu(0.5*10 -0.1)]] = [[6.1, 4.9]]
    hidden_layer_1 = [[relu(1*6.1 -0.8*4.9 +0.2), relu(0.8*6.1 -1*4.9 -0.1)]]
                   = [[relu(2.38), relu(-0.12)]] = [[2.38, 0]]
    logits = [[-1*2.38 +0.3, 1*2.38 -0.3, 0.5*2.38]]
           = [[-2.08, 2.08, 1.19]]
    """
    def test_multi_example_multi_dim_logits(self) -> None:
        """Tests multiple examples and multi-dimensional logits.

    input_layer = [[10], [5]]
    hidden_layer_0 = [[relu(0.6*10 +0.1), relu(0.5*10 -0.1)],
                      [relu(0.6*5 +0.1), relu(0.5*5 -0.1)]]
                   = [[6.1, 4.9], [3.1, 2.4]]
    hidden_layer_1 = [[relu(1*6.1 -0.8*4.9 +0.2), relu(0.8*6.1 -1*4.9 -0.1)],
                      [relu(1*3.1 -0.8*2.4 +0.2), relu(0.8*3.1 -1*2.4 -0.1)]]
                   = [[2.38, 0], [1.38, 0]]
    logits = [[-1*2.38 +0.3, 1*2.38 -0.3, 0.5*2.38],
              [-1*1.38 +0.3, 1*1.38 -0.3, 0.5*1.38]]
           = [[-2.08, 2.08, 1.19], [-1.08, 1.08, 0.69]]
    """
    def test_multi_dim_input_one_dim_logits(self) -> None:
        """Tests multi-dimensional inputs and one-dimensional logits.

    input_layer = [[10, 8]]
    hidden_layer_0 = [[relu(0.6*10 -0.6*8 +0.1), relu(0.5*10 -0.5*8 -0.1)]]
                   = [[1.3, 0.9]]
    hidden_layer_1 = [[relu(1*1.3 -0.8*0.9 + 0.2), relu(0.8*1.3 -1*0.9 -0.2)]]
                   = [[0.78, relu(-0.06)]] = [[0.78, 0]]
    logits = [[-1*0.78 +1*0 +0.3]] = [[-0.48]]
    """
    def test_multi_dim_input_multi_dim_logits(self) -> None:
        """Tests multi-dimensional inputs and multi-dimensional logits.

    input_layer = [[10, 8]]
    hidden_layer_0 = [[relu(0.6*10 -0.6*8 +0.1), relu(0.5*10 -0.5*8 -0.1)]]
                   = [[1.3, 0.9]]
    hidden_layer_1 = [[relu(1*1.3 -0.8*0.9 + 0.2), relu(0.8*1.3 -1*0.9 -0.2)]]
                   = [[0.78, relu(-0.06)]] = [[0.78, 0]]
    logits = [[-1*0.78 + 0.3, 1*0.78 -0.3, 0.5*0.78]] = [[-0.48, 0.48, 0.39]]
    """
    def test_multi_feature_column_multi_dim_logits(self) -> None:
        """Tests multiple feature columns and multi-dimensional logits.

    All numbers are the same as test_multi_dim_input_multi_dim_logits. The only
    difference is that the input consists of two 1D feature columns, instead of
    one 2D feature column.
    """
    def test_multi_feature_column_mix_multi_dim_logits(self) -> None:
        """Tests multiple feature columns and multi-dimensional logits.

    All numbers are the same as test_multi_dim_input_multi_dim_logits. The only
    difference is that the input consists of two 1D feature columns, instead of
    one 2D feature column.
    """

class BaseDNNWarmStartingTest:
    def __init__(self, _dnn_classifier_fn, _dnn_regressor_fn, fc_impl=...) -> None: ...
    def setUp(self): ...
    def tearDown(self) -> None: ...
    def assertAllNotClose(self, t1, t2) -> None:
        """Helper assert for arrays."""
    def test_classifier_basic_warm_starting(self) -> None:
        """Tests correctness of DNNClassifier default warm-start."""
    def test_regressor_basic_warm_starting(self) -> None:
        """Tests correctness of DNNRegressor default warm-start."""
    def test_warm_starting_selective_variables(self) -> None:
        """Tests selecting variables to warm-start."""
    def test_warm_starting_with_vocab_remapping_and_partitioning(self) -> None:
        """Tests warm-starting with vocab remapping and partitioning."""
    def test_warm_starting_with_naming_change(self) -> None:
        """Tests warm-starting with a Tensor name remapping."""

class BaseDNNClassifierEvaluateTest:
    def __init__(self, dnn_classifier_fn, fc_impl=...) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_one_dim(self):
        """Asserts evaluation metrics for one-dimensional input and logits."""
    def test_multi_dim(self):
        """Asserts evaluation metrics for multi-dimensional input and logits."""
    def test_float_labels(self):
        """Asserts evaluation metrics for float labels in binary classification."""
    def test_multi_dim_weights(self):
        """Tests evaluation with weights."""

class BaseDNNRegressorEvaluateTest:
    def __init__(self, dnn_regressor_fn, fc_impl=...) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_one_dim(self):
        """Asserts evaluation metrics for one-dimensional input and logits."""
    def test_multi_dim(self):
        """Asserts evaluation metrics for multi-dimensional input and logits."""
    def test_multi_dim_weights(self):
        """Asserts evaluation metrics for multi-dimensional input and logits."""

class BaseDNNClassifierPredictTest:
    def __init__(self, dnn_classifier_fn, fc_impl=...) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_one_dim_without_label_vocabulary(self): ...
    def test_one_dim_with_label_vocabulary(self): ...
    def test_multi_dim_with_3_classes_but_no_label_vocab(self): ...
    def test_multi_dim_with_3_classes_and_label_vocab(self): ...

class BaseDNNRegressorPredictTest:
    def __init__(self, dnn_regressor_fn, fc_impl=...) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_one_dim(self) -> None:
        """Asserts predictions for one-dimensional input and logits."""
    def test_multi_dim(self) -> None:
        """Asserts predictions for multi-dimensional input and logits."""

class _SummaryHook(tf.compat.v1.train.SessionRunHook):
    """Saves summaries every N steps."""
    def __init__(self) -> None: ...
    def begin(self) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...
    def summaries(self): ...

class BaseDNNClassifierTrainTest:
    def __init__(self, dnn_classifier_fn, fc_impl=...) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_from_scratch_with_default_optimizer_binary(self): ...
    def test_from_scratch_with_default_optimizer_multi_class(self): ...
    def test_from_scratch_validate_summary(self): ...
    def test_binary_classification(self): ...
    def test_binary_classification_float_labels(self): ...
    def test_multi_class(self): ...

class BaseDNNRegressorTrainTest:
    def __init__(self, dnn_regressor_fn, fc_impl=...) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_from_scratch_with_default_optimizer(self): ...
    def test_from_scratch(self): ...
    def test_one_dim(self):
        """Asserts train loss for one-dimensional input and logits."""
    def test_multi_dim(self):
        """Asserts train loss for multi-dimensional input and logits."""
