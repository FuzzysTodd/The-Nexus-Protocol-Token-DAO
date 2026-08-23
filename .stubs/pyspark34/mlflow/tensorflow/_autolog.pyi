from _typeshed import Incomplete
from mlflow.utils.autologging_utils import ExceptionSafeClass as ExceptionSafeClass, INPUT_EXAMPLE_SAMPLE_ROWS as INPUT_EXAMPLE_SAMPLE_ROWS
from tensorflow.keras.callbacks import Callback, TensorBoard

class _TensorBoard(TensorBoard, metaclass=ExceptionSafeClass): ...

class __MLflowTfKeras2Callback(Callback, metaclass=ExceptionSafeClass):
    """
    Callback for auto-logging parameters and metrics in TensorFlow >= 2.0.0.
    Records model structural information as params when training starts.
    """
    metrics_logger: Incomplete
    log_every_n_steps: Incomplete
    def __init__(self, metrics_logger, log_every_n_steps) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def on_train_begin(self, logs: Incomplete | None = None) -> None: ...
    def on_epoch_end(self, epoch, logs: Incomplete | None = None) -> None: ...

def extract_input_example_from_tf_input_fn(input_fn):
    """
    Extracts sample data from dict (str -> ndarray),
    ``tensorflow.Tensor`` or ``tensorflow.data.Dataset`` type.

    :param input_fn: Tensorflow's input function used for train method
    :return: a slice (of limit ``mlflow.utils.autologging_utils.INPUT_EXAMPLE_SAMPLE_ROWS``)
             of the input of type `np.ndarray`.
             Returns `None` if the return type of ``input_fn`` is unsupported.
    """
def extract_tf_keras_input_example(input_training_data):
    """
    Generates a sample ndarray or dict (str -> ndarray)
    from the input type 'x' for keras ``fit`` or ``fit_generator``

    :param input_training_data: Keras input function used for ``fit`` or
                                ``fit_generator`` methods
    :return: a slice of type ndarray or
             dict (str -> ndarray) limited to
             ``mlflow.utils.autologging_utils.INPUT_EXAMPLE_SAMPLE_ROWS``.
             Throws ``MlflowException`` exception, if input_training_data is unsupported.
             Returns `None` if the type of input_training_data is unsupported.
    """
