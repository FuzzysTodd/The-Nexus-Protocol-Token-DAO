from _typeshed import Incomplete
from mlflow import pyfunc as pyfunc
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.utils.annotations import deprecated as deprecated
from mlflow.utils.autologging_utils import autologging_integration as autologging_integration, batch_metrics_logger as batch_metrics_logger, safe_patch as safe_patch
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import write_to as write_to
from typing import Any, Dict

FLAVOR_NAME: str

def load_model(model_uri, ctx, dst_path: Incomplete | None = None):
    '''
    Load a Gluon model from a local file or a run.

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
    :param ctx: Either CPU or GPU.
    :param dst_path: The local filesystem path to which to download the model artifact.
                     This directory must already exist. If unspecified, a local output
                     path will be created.

    :return: A Gluon model instance.

    .. code-block:: python
        :caption: Example

        # Load persisted model as a Gluon model, make inferences against an NDArray
        model = mlflow.gluon.load_model("runs:/" + gluon_random_data_run.info.run_id + "/model")
        model(nd.array(np.random.rand(1000, 1, 32)))
    '''

class _GluonModelWrapper:
    gluon_model: Incomplete
    def __init__(self, gluon_model) -> None: ...
    def predict(self, data, params: Dict[str, Any] | None = None):
        """
        :param data: Either a pandas DataFrame or a numpy array containing input array values.
                     If the input is a DataFrame, it will be converted to an array first by a
                     `ndarray = df.values`.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions. If the input is a pandas.DataFrame, the predictions are returned
                 in a pandas.DataFrame. If the input is a numpy array, the predictions are returned
                 as either a numpy.ndarray or a plain list for hybrid models.


        """

def save_model(gluon_model, path, mlflow_model: Incomplete | None = None, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None):
    """
    Save a Gluon model to a path on the local file system.

    :param gluon_model: Gluon model to be saved. Must be already hybridized.
    :param path: Local path where the model is to be saved.
    :param mlflow_model: MLflow model config this flavor is being added to.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param signature: {{ signature }}
    :param input_example: {{ input_example }}
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.

    .. code-block:: python
        :caption: Example

        from mxnet.gluon import Trainer
        from mxnet.gluon.contrib import estimator
        from mxnet.gluon.loss import SoftmaxCrossEntropyLoss
        from mxnet.gluon.nn import HybridSequential
        from mxnet.metric import Accuracy
        import mlflow

        # Build, compile, and train your model
        gluon_model_path = ...
        net = HybridSequential()
        with net.name_scope():
            ...
        net.hybridize()
        net.collect_params().initialize()
        softmax_loss = SoftmaxCrossEntropyLoss()
        trainer = Trainer(net.collect_params())
        est = estimator.Estimator(
            net=net, loss=softmax_loss, metrics=Accuracy(), trainer=trainer
        )
        est.fit(train_data=train_data, epochs=100, val_data=validation_data)
        # Save the model as an MLflow Model
        mlflow.gluon.save_model(net, gluon_model_path)
    """
def get_default_pip_requirements():
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
def log_model(gluon_model, artifact_path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None):
    '''
    Log a Gluon model as an MLflow artifact for the current run.

    :param gluon_model: Gluon model to be saved. Must be already hybridized.
    :param artifact_path: Run-relative artifact path.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param registered_model_name: If given, create a model version under
                                  ``registered_model_name``, also creating a registered model if one
                                  with the given name does not exist.
    :param signature: {{ signature }}
    :param input_example: {{ input_example }}
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.

    .. code-block:: python
        :caption: Example

        from mxnet.gluon import Trainer
        from mxnet.gluon.contrib import estimator
        from mxnet.gluon.loss import SoftmaxCrossEntropyLoss
        from mxnet.gluon.nn import HybridSequential
        from mxnet.metric import Accuracy
        import mlflow

        # Build, compile, and train your model
        net = HybridSequential()
        with net.name_scope():
            ...
        net.hybridize()
        net.collect_params().initialize()
        softmax_loss = SoftmaxCrossEntropyLoss()
        trainer = Trainer(net.collect_params())
        est = estimator.Estimator(
            net=net, loss=softmax_loss, metrics=Accuracy(), trainer=trainer
        )
        # Log metrics and log the model
        with mlflow.start_run():
            est.fit(train_data=train_data, epochs=100, val_data=validation_data)
            mlflow.gluon.log_model(net, "model")
    '''
def autolog(log_models: bool = True, log_datasets: bool = True, disable: bool = False, exclusive: bool = False, disable_for_unsupported_versions: bool = False, silent: bool = False, registered_model_name: Incomplete | None = None):
    """
    Enables (or disables) and configures autologging from Gluon to MLflow.
    Logs loss and any other metrics specified in the fit
    function, and optimizer data as parameters. Model checkpoints
    are logged as artifacts to a 'models' directory.

    :param log_models: If ``True``, trained models are logged as MLflow model artifacts.
                       If ``False``, trained models are not logged.
    :param log_datasets: If ``True``, dataset information is logged to MLflow Tracking.
                         If ``False``, dataset information is not logged.
    :param disable: If ``True``, disables the MXNet Gluon autologging integration. If ``False``,
                    enables the MXNet Gluon autologging integration.
    :param exclusive: If ``True``, autologged content is not logged to user-created fluent runs.
                      If ``False``, autologged content is logged to the active fluent run,
                      which may be user-created.
    :param disable_for_unsupported_versions: If ``True``, disable autologging for versions of
                      gluon that have not been tested against this version of the MLflow client
                      or are incompatible.
    :param silent: If ``True``, suppress all event logs and warnings from MLflow during MXNet Gluon
                   autologging. If ``False``, show all events and warnings during MXNet Gluon
                   autologging.
    :param registered_model_name: If given, each time a model is trained, it is registered as a
                                  new model version of the registered model with this name.
                                  The registered model is created if it does not already exist.
    """
