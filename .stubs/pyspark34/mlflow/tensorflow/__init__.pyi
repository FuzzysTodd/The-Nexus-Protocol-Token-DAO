from _typeshed import Incomplete
from mlflow import pyfunc as pyfunc
from mlflow.data.code_dataset_source import CodeDatasetSource as CodeDatasetSource
from mlflow.data.numpy_dataset import from_numpy as from_numpy
from mlflow.data.tensorflow_dataset import from_tensorflow as from_tensorflow
from mlflow.entities import Metric as Metric
from mlflow.exceptions import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, MlflowException as MlflowException
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature, infer_signature as infer_signature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.tracking.client import MlflowClient as MlflowClient
from mlflow.types.schema import TensorSpec as TensorSpec
from mlflow.utils import is_iterator as is_iterator
from mlflow.utils.autologging_utils import PatchFunction as PatchFunction, autologging_integration as autologging_integration, batch_metrics_logger as batch_metrics_logger, get_autologging_config as get_autologging_config, log_fn_args_as_params as log_fn_args_as_params, picklable_exception_safe_function as picklable_exception_safe_function, resolve_input_example_and_signature as resolve_input_example_and_signature, safe_patch as safe_patch
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import write_to as write_to
from mlflow.utils.time_utils import get_current_time_millis as get_current_time_millis
from typing import Any, Dict, NamedTuple

FLAVOR_NAME: str

def get_default_pip_requirements(include_cloudpickle: bool = False):
    """
    :return: A list of default pip requirements for MLflow Models produced by this flavor.
             Calls to :func:`save_model()` and :func:`log_model()` produce a pip environment
             that, at minimum, contains these requirements.
    """
def get_default_conda_env():
    """
    :return: The default Conda environment for MLflow Models produced by calls to
             :func:`save_model()` and :func:`log_model()`.
    """
def log_model(model, artifact_path, custom_objects: Incomplete | None = None, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, registered_model_name: Incomplete | None = None, await_registration_for=..., pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, saved_model_kwargs: Incomplete | None = None, keras_model_kwargs: Incomplete | None = None, metadata: Incomplete | None = None):
    '''
    Log a TF2 core model (inheriting tf.Module) or a Keras model in MLflow Model format.

    .. note::

        If you log a Keras or TensorFlow model without a signature, inference with
        :py:func:`mlflow.pyfunc.spark_udf()` will not work unless the model\'s pyfunc
        representation accepts pandas DataFrames as inference inputs.

        You can infer a model\'s signature by calling the :py:func:`mlflow.models.infer_signature()`
        API on features from the model\'s test dataset. You can also manually create a model
        signature, for example:

        .. code-block:: python
            :caption: Example of creating signature for saving TensorFlow and `tf.Keras` models

            from mlflow.types.schema import Schema, TensorSpec
            from mlflow.models import ModelSignature
            import numpy as np

            input_schema = Schema(
                [
                    TensorSpec(np.dtype(np.uint64), (-1, 5), "field1"),
                    TensorSpec(np.dtype(np.float32), (-1, 3, 2), "field2"),
                ]
            )
            # Create the signature for a model that requires 2 inputs:
            #  - Input with name "field1", shape (-1, 5), type "np.uint64"
            #  - Input with name "field2", shape (-1, 3, 2), type "np.float32"
            signature = ModelSignature(inputs=input_schema)

    :param model: The TF2 core model (inheriting tf.Module) or Keras model to be saved.
    :param artifact_path: The run-relative path to which to log model artifacts.
    :param custom_objects: A Keras ``custom_objects`` dictionary mapping names (strings) to
                           custom classes or functions associated with the Keras model. MLflow saves
                           these custom layers using CloudPickle and restores them automatically
                           when the model is loaded with :py:func:`mlflow.tensorflow.load_model` and
                           :py:func:`mlflow.pyfunc.load_model`.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param registered_model_name: If given, create a model version under
                                  ``registered_model_name``, also creating a registered model if one
                                  with the given name does not exist.

    :param signature: {{ signature }}
    :param input_example: {{ input_example }}
    :param await_registration_for: Number of seconds to wait for the model version to finish
                            being created and is in ``READY`` status. By default, the function
                            waits for five minutes. Specify 0 or None to skip waiting.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param saved_model_kwargs: a dict of kwargs to pass to ``tensorflow.saved_model.save`` method.
    :param keras_model_kwargs: a dict of kwargs to pass to ``keras_model.save`` method.
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.
    '''
def save_model(model, path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, mlflow_model: Incomplete | None = None, custom_objects: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, saved_model_kwargs: Incomplete | None = None, keras_model_kwargs: Incomplete | None = None, metadata: Incomplete | None = None):
    '''
    Save a TF2 core model (inheriting tf.Module) or Keras model in MLflow Model format to a path on
    the local file system.

    .. note::
        If you save a Keras or TensorFlow model without a signature, inference with
        :py:func:`mlflow.pyfunc.spark_udf()` will not work unless the model\'s pyfunc
        representation accepts pandas DataFrames as inference inputs.
        You can infer a model\'s signature by calling the :py:func:`mlflow.models.infer_signature()`
        API on features from the model\'s test dataset. You can also manually create a model
        signature, for example:

        .. code-block:: python
            :caption: Example of creating signature for saving TensorFlow and `tf.Keras` models

            from mlflow.types.schema import Schema, TensorSpec
            from mlflow.models import ModelSignature
            import numpy as np

            input_schema = Schema(
                [
                    TensorSpec(np.dtype(np.uint64), (-1, 5), "field1"),
                    TensorSpec(np.dtype(np.float32), (-1, 3, 2), "field2"),
                ]
            )
            # Create the signature for a model that requires 2 inputs:
            #  - Input with name "field1", shape (-1, 5), type "np.uint64"
            #  - Input with name "field2", shape (-1, 3, 2), type "np.float32"
            signature = ModelSignature(inputs=input_schema)

    :param model: The Keras model or Tensorflow module to be saved.
    :param path: Local path where the MLflow model is to be saved.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param mlflow_model: MLflow model configuration to which to add the ``tensorflow`` flavor.
    :param custom_objects: A Keras ``custom_objects`` dictionary mapping names (strings) to
                           custom classes or functions associated with the Keras model. MLflow saves
                           these custom layers using CloudPickle and restores them automatically
                           when the model is loaded with :py:func:`mlflow.tensorflow.load_model` and
                           :py:func:`mlflow.pyfunc.load_model`.
    :param signature: {{ signature }}
    :param input_example: {{ input_example }}
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param saved_model_kwargs: a dict of kwargs to pass to ``tensorflow.saved_model.save`` method
                               if the model to be saved is a Tensorflow module.
    :param keras_model_kwargs: a dict of kwargs to pass to ``model.save`` method if the model
                               to be saved is a keras model.
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    '''
def load_model(model_uri, dst_path: Incomplete | None = None, saved_model_kwargs: Incomplete | None = None, keras_model_kwargs: Incomplete | None = None):
    '''
    Load an MLflow model that contains the TensorFlow flavor from the specified path.

    :param model_uri: The location, in URI format, of the MLflow model. For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``models:/<model_name>/<model_version>``
                      - ``models:/<model_name>/<stage>``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                      artifact-locations>`_.
    :param dst_path: The local filesystem path to which to download the model artifact.
                     This directory must already exist. If unspecified, a local output
                     path will be created.
    :param saved_model_kwargs: kwargs to pass to ``tensorflow.saved_model.load`` method.
                               Only available when you are loading a tensorflow2 core model.
    :param keras_model_kwargs: kwargs to pass to ``keras.models.load_model`` method.
                               Only available when you are loading a Keras model.

    :return: A callable graph (tf.function) that takes inputs and returns inferences.

    .. code-block:: python
        :caption: Example

        import mlflow
        import tensorflow as tf

        tf_graph = tf.Graph()
        tf_sess = tf.Session(graph=tf_graph)
        with tf_graph.as_default():
            signature_definition = mlflow.tensorflow.load_model(
                model_uri="model_uri", tf_sess=tf_sess
            )
            input_tensors = [
                tf_graph.get_tensor_by_name(input_signature.name)
                for _, input_signature in signature_definition.inputs.items()
            ]
            output_tensors = [
                tf_graph.get_tensor_by_name(output_signature.name)
                for _, output_signature in signature_definition.outputs.items()
            ]
    '''

class _TF2Wrapper:
    """
    Wrapper class that exposes a TensorFlow model for inference via a ``predict`` function such that
    ``predict(data: pandas.DataFrame) -> pandas.DataFrame``. For TensorFlow versions >= 2.0.0.
    """
    model: Incomplete
    infer: Incomplete
    def __init__(self, model, infer) -> None:
        """
        :param model: A Tensorflow SavedModel.
        :param infer: Tensorflow function returned by a saved model that is used for inference.
        """
    def predict(self, data, params: Dict[str, Any] | None = None):
        """
        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """

class _TF2ModuleWrapper:
    model: Incomplete
    signature: Incomplete
    def __init__(self, model, signature) -> None: ...
    def predict(self, data, params: Dict[str, Any] | None = None):
        """
        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """

class _KerasModelWrapper:
    keras_model: Incomplete
    signature: Incomplete
    def __init__(self, keras_model, signature) -> None: ...
    def predict(self, data, params: Dict[str, Any] | None = None):
        """
        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """

class _TensorBoardLogDir(NamedTuple):
    location: Incomplete
    is_temp: Incomplete

def autolog(every_n_iter: int = 1, log_models: bool = True, log_datasets: bool = True, disable: bool = False, exclusive: bool = False, disable_for_unsupported_versions: bool = False, silent: bool = False, registered_model_name: Incomplete | None = None, log_input_examples: bool = False, log_model_signatures: bool = True, saved_model_kwargs: Incomplete | None = None, keras_model_kwargs: Incomplete | None = None, extra_tags: Incomplete | None = None):
    """
    Enables autologging for ``tf.keras`` and ``keras``.
    Note that only ``tensorflow>=2.3`` are supported.
    As an example, try running the
    `Keras/TensorFlow example <https://github.com/mlflow/mlflow/blob/master/examples/keras/train.py>`_.

    For each TensorFlow module, autologging captures the following information:

    **tf.keras**
     - **Metrics** and **Parameters**

      - Training loss; validation loss; user-specified metrics
      - ``fit()`` or ``fit_generator()`` parameters; optimizer name; learning rate; epsilon

     - **Artifacts**

      - Model summary on training start
      - `MLflow Model <https://mlflow.org/docs/latest/models.html>`_ (Keras model)
      - TensorBoard logs on training end

    **tf.keras.callbacks.EarlyStopping**
     - **Metrics** and **Parameters**

      - Metrics from the ``EarlyStopping`` callbacks: ``stopped_epoch``, ``restored_epoch``,
        ``restore_best_weight``, etc
      - ``fit()`` or ``fit_generator()`` parameters associated with ``EarlyStopping``:
        ``min_delta``, ``patience``, ``baseline``, ``restore_best_weights``, etc

    Refer to the autologging tracking documentation for more
    information on `TensorFlow workflows
    <https://www.mlflow.org/docs/latest/tracking.html#tensorflow-and-keras-experimental>`_.

    :param every_n_iter: The frequency with which metrics should be logged. For example, a value of
                         100 will log metrics at step 0, 100, 200, etc.
    :param log_models: If ``True``, trained models are logged as MLflow model artifacts.
                       If ``False``, trained models are not logged.
    :param log_datasets: If ``True``, dataset information is logged to MLflow Tracking.
                         If ``False``, dataset information is not logged.
    :param disable: If ``True``, disables the TensorFlow autologging integration. If ``False``,
                    enables the TensorFlow integration autologging integration.
    :param exclusive: If ``True``, autologged content is not logged to user-created fluent runs.
                      If ``False``, autologged content is logged to the active fluent run,
                      which may be user-created.
    :param disable_for_unsupported_versions: If ``True``, disable autologging for versions of
                      tensorflow that have not been tested against this version of the MLflow
                      client or are incompatible.
    :param silent: If ``True``, suppress all event logs and warnings from MLflow during TensorFlow
                   autologging. If ``False``, show all events and warnings during TensorFlow
                   autologging.
    :param registered_model_name: If given, each time a model is trained, it is registered as a
                                  new model version of the registered model with this name.
                                  The registered model is created if it does not already exist.
    :param log_input_examples: If ``True``, input examples from training datasets are collected and
                               logged along with tf/keras model artifacts during training. If
                               ``False``, input examples are not logged.
    :param log_model_signatures: If ``True``,
                                 :py:class:`ModelSignatures <mlflow.models.ModelSignature>`
                                 describing model inputs and outputs are collected and logged along
                                 with tf/keras model artifacts during training. If ``False``,
                                 signatures are not logged. Note that logging TensorFlow models
                                 with signatures changes their pyfunc inference behavior when
                                 Pandas DataFrames are passed to ``predict()``.
                                 When a signature is present, an ``np.ndarray``
                                 (for single-output models) or a mapping from
                                 ``str`` -> ``np.ndarray`` (for multi-output models) is returned;
                                 when a signature is not present, a Pandas DataFrame is returned.
    :param saved_model_kwargs: a dict of kwargs to pass to ``tensorflow.saved_model.save`` method.
    :param keras_model_kwargs: a dict of kwargs to pass to ``keras_model.save`` method.
    :param extra_tags: A dictionary of extra tags to set on each managed run created by autologging.
    """
