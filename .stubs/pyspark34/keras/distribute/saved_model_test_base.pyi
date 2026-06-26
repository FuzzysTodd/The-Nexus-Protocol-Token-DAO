import tensorflow.compat.v2 as tf
from _typeshed import Incomplete
from absl.testing import parameterized
from keras.distribute import model_combinations as model_combinations

PREDICT_STEPS: int
simple_models: Incomplete
strategies: Incomplete

def simple_models_with_strategies(): ...
def simple_models_with_strategy_pairs(): ...
def tfmodule_models_with_strategies(): ...
def tfmodule_models_with_strategy_pairs(): ...
def load_and_run_with_saved_model_api(distribution, saved_dir, predict_dataset, output_name):
    """Loads a saved_model using tf.saved_model API, and runs it."""

class TestSavedModelBase(tf.test.TestCase, parameterized.TestCase):
    """Base class for testing saving/loading with DS."""
    def setUp(self) -> None: ...
    def run_test_save_no_strategy_restore_strategy(self, model_and_input, distribution) -> None:
        """Save a model without DS, and restore it with DS."""
    def run_test_save_strategy_restore_no_strategy(self, model_and_input, distribution, save_in_scope) -> None:
        """Save a model with DS, and restore it without DS."""
    def run_test_save_strategy_restore_strategy(self, model_and_input, distribution_for_saving, distribution_for_restoring, save_in_scope) -> None:
        """Save a model with DS, and restore it with potentially different
        DS."""
    def run_test_save_strategy(self, model_and_input, distribution, save_in_scope):
        """Save a model with DS."""
