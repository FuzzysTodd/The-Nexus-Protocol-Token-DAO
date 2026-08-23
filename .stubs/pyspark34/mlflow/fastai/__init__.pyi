from _typeshed import Incomplete
from mlflow import pyfunc as pyfunc
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.utils.autologging_utils import autologging_integration as autologging_integration, batch_metrics_logger as batch_metrics_logger, log_fn_args_as_params as log_fn_args_as_params, safe_patch as safe_patch
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import write_to as write_to
from typing import Any, Dict

FLAVOR_NAME: str

def get_default_pip_requirements(include_cloudpickle: bool = False):
    """
    :return: A list of default pip requirements for MLflow Models produced by this flavor.
             Calls to :func:`save_model()` and :func:`log_model()` produce a pip environment
             that, at minimum, contains these requirements.
    """
def get_default_conda_env(include_cloudpickle: bool = False):
    """
    :return: The default Conda environment for MLflow Models produced by calls to
             :func:`save_model()` and :func:`log_model()`.
    """
def save_model(fastai_learner, path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, mlflow_model: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, **kwargs):
    '''
    Save a fastai Learner to a path on the local file system.

    :param fastai_learner: fastai Learner to be saved.
    :param path: Local path where the model is to be saved.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param mlflow_model: MLflow model config this flavor is being added to.

    :param signature: :py:class:`ModelSignature <mlflow.models.ModelSignature>`
                      describes model input and output :py:class:`Schema <mlflow.types.Schema>`.
                      The model signature can be :py:func:`inferred <mlflow.models.infer_signature>`
                      from datasets with valid model input (e.g. the training dataset with target
                      column omitted) and valid model output (e.g. model predictions generated on
                      the training dataset), for example:

                      .. code-block:: python

                        from mlflow.models import infer_signature

                        train = df.drop_column("target_label")
                        predictions = ...  # compute model predictions
                        signature = infer_signature(train, predictions)
    :param input_example: Input example provides one or several instances of valid
                          model input. The example can be used as a hint of what data to feed the
                          model. The given example will be converted to a Pandas DataFrame and then
                          serialized to json using the Pandas split-oriented format. Bytes are
                          base64-encoded.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.

    :param kwargs: kwargs to pass to ``Learner.save`` method.

    .. code-block:: python
        :caption: Example

        import os

        import mlflow.fastai

        # Create a fastai Learner model
        model = ...

        # Start MLflow session and save model to current working directory
        with mlflow.start_run():
            model.fit(epochs, learning_rate)
            mlflow.fastai.save_model(model, "model")

        # Load saved model for inference
        model_uri = "{}/{}".format(os.getcwd(), "model")
        loaded_model = mlflow.fastai.load_model(model_uri)
        results = loaded_model.predict(predict_data)
    '''
def log_model(fastai_learner, artifact_path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, await_registration_for=..., pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, **kwargs):
    '''
    Log a fastai model as an MLflow artifact for the current run.

    :param fastai_learner: Fastai model (an instance of `fastai.Learner`_) to be saved.
    :param artifact_path: Run-relative artifact path.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param registered_model_name: This argument may change or be removed in a
                                  future release without warning. If given, create a model
                                  version under ``registered_model_name``, also creating a
                                  registered model if one with the given name does not exist.

    :param signature: :py:class:`ModelSignature <mlflow.models.ModelSignature>`
                      describes model input and output :py:class:`Schema <mlflow.types.Schema>`.
                      The model signature can be :py:func:`inferred <mlflow.models.infer_signature>`
                      from datasets with valid model input (e.g. the training dataset with target
                      column omitted) and valid model output (e.g. model predictions generated on
                      the training dataset), for example:

                      .. code-block:: python

                        from mlflow.models import infer_signature

                        train = df.drop_column("target_label")
                        predictions = ...  # compute model predictions
                        signature = infer_signature(train, predictions)
    :param input_example: Input example provides one or several instances of valid
                          model input. The example can be used as a hint of what data to feed the
                          model. The given example will be converted to a Pandas DataFrame and then
                          serialized to json using the Pandas split-oriented format. Bytes are
                          base64-encoded.

    :param kwargs: kwargs to pass to `fastai.Learner.export`_ method.
    :param await_registration_for: Number of seconds to wait for the model version to finish
                            being created and is in ``READY`` status. By default, the function
                            waits for five minutes. Specify 0 or None to skip waiting.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.

    .. code-block:: python
        :caption: Example

        import fastai.vision as vis
        import mlflow.fastai
        from mlflow import MlflowClient


        def main(epochs=5, learning_rate=0.01):
            # Download and untar the MNIST data set
            path = vis.untar_data(vis.URLs.MNIST_SAMPLE)

            # Prepare, transform, and normalize the data
            data = vis.ImageDataBunch.from_folder(
                path, ds_tfms=(vis.rand_pad(2, 28), []), bs=64
            )
            data.normalize(vis.imagenet_stats)

            # Create the CNN Learner model
            model = vis.cnn_learner(data, vis.models.resnet18, metrics=vis.accuracy)

            # Start MLflow session and log model
            with mlflow.start_run() as run:
                model.fit(epochs, learning_rate)
                mlflow.fastai.log_model(model, "model")

            # fetch the logged model artifacts
            artifacts = [
                f.path for f in MlflowClient().list_artifacts(run.info.run_id, "model")
            ]
            print("artifacts: {}".format(artifacts))


        main()

    .. code-block:: text
        :caption: Output

        artifacts: [\'model/MLmodel\', \'model/conda.yaml\', \'model/model.fastai\']
    '''

class _FastaiModelWrapper:
    learner: Incomplete
    def __init__(self, learner) -> None: ...
    def predict(self, dataframe, params: Dict[str, Any] | None = None):
        """
        :param dataframe: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """

def load_model(model_uri, dst_path: Incomplete | None = None):
    '''
    Load a fastai model from a local file or a run.

    :param model_uri: The location, in URI format, of the MLflow model. For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/tracking.html#
                      artifact-locations>`_.
    :param dst_path: The local filesystem path to which to download the model artifact.
                     This directory must already exist. If unspecified, a local output
                     path will be created.

    :return: A fastai model (an instance of `fastai.Learner`_).

    .. code-block:: python
        :caption: Example

        import mlflow.fastai

        # Define the Learner model
        model = ...

        # log the fastai Leaner model
        with mlflow.start_run() as run:
            model.fit(epochs, learning_rate)
            mlflow.fastai.log_model(model, "model")

        # Load the model for scoring
        model_uri = "runs:/{}/model".format(run.info.run_id)
        loaded_model = mlflow.fastai.load_model(model_uri)
        results = loaded_model.predict(predict_data)
    '''
def autolog(log_models: bool = True, log_datasets: bool = True, disable: bool = False, exclusive: bool = False, disable_for_unsupported_versions: bool = False, silent: bool = False, registered_model_name: Incomplete | None = None, extra_tags: Incomplete | None = None):
    '''
    Enable automatic logging from Fastai to MLflow.
    Logs loss and any other metrics specified in the fit
    function, and optimizer data as parameters. Model checkpoints
    are logged as artifacts to a \'models\' directory.

    MLflow will also log the parameters of the
    `EarlyStoppingCallback <https://docs.fast.ai/callback.tracker.html#EarlyStoppingCallback>`_
    and `OneCycleScheduler <https://docs.fast.ai/callback.schedule.html#ParamScheduler>`_ callbacks

    :param log_models: If ``True``, trained models are logged as MLflow model artifacts.
                       If ``False``, trained models are not logged.
    :param log_datasets: If ``True``, dataset information is logged to MLflow Tracking.
                         If ``False``, dataset information is not logged.
    :param disable: If ``True``, disables the Fastai autologging integration. If ``False``,
                    enables the Fastai autologging integration.
    :param exclusive: If ``True``, autologged content is not logged to user-created fluent runs.
                      If ``False``, autologged content is logged to the active fluent run,
                      which may be user-created.
    :param disable_for_unsupported_versions: If ``True``, disable autologging for versions of
                      fastai that have not been tested against this version of the MLflow client
                      or are incompatible.
    :param silent: If ``True``, suppress all event logs and warnings from MLflow during Fastai
                   autologging. If ``False``, show all events and warnings during Fastai
                   autologging.
    :param registered_model_name: If given, each time a model is trained, it is registered as a
                                  new model version of the registered model with this name.
                                  The registered model is created if it does not already exist.
    :param extra_tags: A dictionary of extra tags to set on each managed run created by autologging.

    .. code-block:: python
        :caption: Example

        # This is a modified example from
        # https://github.com/mlflow/mlflow/tree/master/examples/fastai
        # demonstrating autolog capabilities.

        import fastai.vision as vis
        import mlflow.fastai
        from mlflow import MlflowClient


        def print_auto_logged_info(r):
            tags = {k: v for k, v in r.data.tags.items() if not k.startswith("mlflow.")}
            artifacts = [f.path for f in MlflowClient().list_artifacts(r.info.run_id, "model")]
            print("run_id: {}".format(r.info.run_id))
            print("artifacts: {}".format(artifacts))
            print("params: {}".format(r.data.params))
            print("metrics: {}".format(r.data.metrics))
            print("tags: {}".format(tags))


        def main(epochs=5, learning_rate=0.01):
            # Download and untar the MNIST data set
            path = vis.untar_data(vis.URLs.MNIST_SAMPLE)

            # Prepare, transform, and normalize the data
            data = vis.ImageDataBunch.from_folder(
                path, ds_tfms=(vis.rand_pad(2, 28), []), bs=64
            )
            data.normalize(vis.imagenet_stats)

            # Create CNN the Learner model
            model = vis.cnn_learner(data, vis.models.resnet18, metrics=vis.accuracy)

            # Enable auto logging
            mlflow.fastai.autolog()

            # Start MLflow session
            with mlflow.start_run() as run:
                model.fit(epochs, learning_rate)

            # fetch the auto logged parameters, metrics, and artifacts
            print_auto_logged_info(mlflow.get_run(run_id=run.info.run_id))


        main()

    .. code-block:: text
        :caption: output

        run_id: 5a23dcbcaa334637814dbce7a00b2f6a
        artifacts: [\'model/MLmodel\', \'model/conda.yaml\', \'model/model.fastai\']
        params: {\'wd\': \'None\',
                 \'bn_wd\': \'True\',
                 \'opt_func\': \'Adam\',
                 \'epochs\': \'5\', \'
                 train_bn\': \'True\',
                 \'num_layers\': \'60\',
                 \'lr\': \'0.01\',
                 \'true_wd\': \'True\'}
        metrics: {\'train_loss\': 0.024,
                  \'accuracy\': 0.99214,
                  \'valid_loss\': 0.021}
        # Tags model summary omitted too long
        tags: {...}

    .. figure:: ../_static/images/fastai_autolog.png

        Fastai autologged MLflow entities
    '''
