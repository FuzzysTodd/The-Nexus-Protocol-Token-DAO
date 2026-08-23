from _typeshed import Incomplete
from keras.distribute import keras_correctness_test_base as keras_correctness_test_base
from keras.layers.rnn import gru as gru, gru_v1 as gru_v1, lstm as lstm, lstm_v1 as lstm_v1
from keras.mixed_precision import policy as policy
from keras.testing_infra import test_utils as test_utils

class _DistributionStrategyRnnModelCorrectnessTest(keras_correctness_test_base.TestDistributionStrategyEmbeddingModelCorrectnessBase):
    def get_model(self, max_words: int = 10, initial_weights: Incomplete | None = None, distribution: Incomplete | None = None, input_shapes: Incomplete | None = None): ...

class DistributionStrategyGruModelCorrectnessTest(_DistributionStrategyRnnModelCorrectnessTest):
    def test_gru_model_correctness(self, distribution, use_numpy, use_validation_data) -> None: ...

class DistributionStrategyLstmModelCorrectnessTest(_DistributionStrategyRnnModelCorrectnessTest):
    def test_lstm_model_correctness(self, distribution, use_numpy, use_validation_data) -> None: ...
    def test_lstm_model_correctness_mixed_precision(self, distribution, use_numpy, use_validation_data) -> None: ...
