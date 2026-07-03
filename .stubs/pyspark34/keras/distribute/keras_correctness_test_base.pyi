import keras
import tensorflow.compat.v2 as tf
from _typeshed import Incomplete
from absl.testing import parameterized
from keras.distribute import distributed_training_utils as distributed_training_utils
from keras.distribute.strategy_combinations import all_strategies as all_strategies, multi_worker_mirrored_strategies as multi_worker_mirrored_strategies, strategies_minus_tpu as strategies_minus_tpu
from keras.mixed_precision import policy as policy
from keras.utils import data_utils as data_utils

def eager_mode_test_configuration(): ...
def graph_mode_test_configuration(): ...
def all_strategy_and_input_config_combinations(): ...
def all_strategy_and_input_config_combinations_eager(): ...
def strategy_minus_tpu_and_input_config_combinations_eager(): ...
def strategies_for_embedding_models():
    """Returns distribution strategies to test for embedding models.

    Since embedding models take longer to train, we disregard DefaultStrategy
    in order to prevent testing timeouts.
    """
def test_combinations_for_embedding_model(): ...
def test_combinations_with_tpu_strategies_graph(): ...
def multi_worker_mirrored_eager(): ...
def multi_worker_mirrored_eager_and_graph(): ...

class MaybeDistributionScope:
    """Provides a context allowing no distribution strategy."""
    def __init__(self, distribution) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def batch_wrapper(dataset, batch_size, repeat: Incomplete | None = None): ...
def get_batch_size(global_batch_size, distribution): ...
def get_data_size(data):
    """Gets the size of data in list, tuple, dict, or a numpy array."""
def get_shapes(data): ...
def get_correctness_test_inputs(use_numpy, use_validation_data, with_distribution, x_train, y_train, x_eval, y_eval, x_predict, training_epochs):
    """Generates the inputs for correctness check when enable Keras with DS."""
def fit_eval_and_predict(initial_weights, input_fn, model_fn, distribution: Incomplete | None = None, is_stateful_model: bool = False):
    """Generates results for fit/predict/evaluate for given model."""
def compare_results(results_with_ds, results_without_ds, distribution, testcase, partial_last_batch: Incomplete | None = None):
    """Compares results of model compiled with/without distribution strategy."""
def should_skip_tpu_with_eager(distribution): ...

class LearningRateBatchScheduler(keras.callbacks.Callback):
    """Scheduler that dynamically sets the learning rate of model."""
    def __init__(self, update_freq: Incomplete | None = None) -> None: ...
    def on_batch_begin(self, batch, logs: Incomplete | None = None) -> None: ...

class TestDistributionStrategyCorrectnessBase(tf.test.TestCase, parameterized.TestCase):
    """Model agnostic testing infra to test correctness of Keras models."""
    use_numpy: Incomplete
    use_validation_data: Incomplete
    with_batch_norm: Incomplete
    def set_up_test_config(self, use_numpy: bool = False, use_validation_data: bool = False, with_batch_norm: Incomplete | None = None) -> None: ...
    def get_data(self): ...
    def get_data_with_partial_last_batch(self) -> None: ...
    def get_data_with_partial_last_batch_eval(self) -> None: ...
    def get_input_for_correctness_test(self, **kwargs):
        """Generates inputs that are dictionaries.

        We only provide a default implementation of this method here. If you
        need more customized way of providing input to your model, overwrite
        this method.

        Args:
          **kwargs: key word arguments about how to create the input
            dictionaries

        Returns:
          Three dictionaries representing the input for fit(), evaluate() and
          predict()
        """
    def get_model(self, distribution: Incomplete | None = None, input_shapes: Incomplete | None = None) -> None: ...
    def run_correctness_test(self, distribution, use_numpy, use_validation_data, with_batch_norm: Incomplete | None = None, is_stateful_model: bool = False, partial_last_batch: Incomplete | None = None, training_epochs: int = 2) -> None: ...
    def get_input_for_dynamic_lr_test(self, **kwargs):
        """Generates inputs that are dictionaries.

        We only provide a default implementation of this method here. If you
        need more customized way of providing input to your model, overwrite
        this method.

        Args:
          **kwargs: key word arguments about how to create the input
            dictionaries

        Returns:
          Three dictionaries representing the input for fit(), evaluate() and
          predict()
        """
    def run_dynamic_lr_test(self, distribution) -> None: ...

class TestDistributionStrategyEmbeddingModelCorrectnessBase(TestDistributionStrategyCorrectnessBase):
    """Base class to test correctness of Keras models with embedding layers."""
    def get_data(self, count=..., min_words: int = 5, max_words: int = 10, max_word_id: int = 19, num_classes: int = 2): ...
