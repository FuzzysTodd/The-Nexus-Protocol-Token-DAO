from _typeshed import Incomplete
from mlflow import pyfunc as pyfunc
from mlflow.data.code_dataset_source import CodeDatasetSource as CodeDatasetSource
from mlflow.data.numpy_dataset import from_numpy as from_numpy
from mlflow.data.pandas_dataset import from_pandas as from_pandas
from mlflow.entities.dataset_input import DatasetInput as DatasetInput
from mlflow.entities.input_tag import InputTag as InputTag
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature, infer_signature as infer_signature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.utils.autologging_utils import ENSURE_AUTOLOGGING_ENABLED_TEXT as ENSURE_AUTOLOGGING_ENABLED_TEXT, INPUT_EXAMPLE_SAMPLE_ROWS as INPUT_EXAMPLE_SAMPLE_ROWS, InputExampleInfo as InputExampleInfo, MlflowAutologgingQueueingClient as MlflowAutologgingQueueingClient, autologging_integration as autologging_integration, batch_metrics_logger as batch_metrics_logger, get_mlflow_run_params_for_fn_args as get_mlflow_run_params_for_fn_args, picklable_exception_safe_function as picklable_exception_safe_function, resolve_input_example_and_signature as resolve_input_example_and_signature, safe_patch as safe_patch
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import write_to as write_to
from mlflow.utils.mlflow_tags import MLFLOW_DATASET_CONTEXT as MLFLOW_DATASET_CONTEXT
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
def save_model(lgb_model, path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, mlflow_model: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None):
    '''
    Save a LightGBM model to a path on the local file system.

    :param lgb_model: LightGBM model (an instance of `lightgbm.Booster`_) or
                      models that implement the `scikit-learn API`_  to be saved.
    :param path: Local path where the model is to be saved.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param mlflow_model: :py:mod:`mlflow.models.Model` this flavor is being added to.
    :param signature: {{ signature }}
    :param input_example: {{ input_example }}
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.

    .. code-block:: python
        :caption: Example

        from pathlib import Path
        from lightgbm import LGBMClassifier
        from sklearn import datasets
        import mlflow

        # Load iris dataset
        X, y = datasets.load_iris(return_X_y=True, as_frame=True)

        # Initialize our model
        model = LGBMClassifier(objective="multiclass", random_state=42)

        # Train the model
        model.fit(X, y)

        # Save the model
        path = "model"
        mlflow.lightgbm.save_model(model, path)

        # Load model for inference
        loaded_model = mlflow.lightgbm.load_model(Path.cwd() / path)
        print(loaded_model.predict(X[:5]))

    .. code-block:: text
        :caption: Output

        [0 0 0 0 0]
    '''
def log_model(lgb_model, artifact_path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, await_registration_for=..., pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, **kwargs):
    '''
    Log a LightGBM model as an MLflow artifact for the current run.

    :param lgb_model: LightGBM model (an instance of `lightgbm.Booster`_) or
                      models that implement the `scikit-learn API`_  to be saved.
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
    :param await_registration_for: Number of seconds to wait for the model version to finish
                            being created and is in ``READY`` status. By default, the function
                            waits for five minutes. Specify 0 or None to skip waiting.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :param kwargs: kwargs to pass to `lightgbm.Booster.save_model`_ method.
    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.

    .. code-block:: python
        :caption: Example

        from lightgbm import LGBMClassifier
        from sklearn import datasets
        import mlflow
        from mlflow.models import infer_signature

        # Load iris dataset
        X, y = datasets.load_iris(return_X_y=True, as_frame=True)

        # Initialize our model
        model = LGBMClassifier(objective="multiclass", random_state=42)

        # Train the model
        model.fit(X, y)

        # Create model signature
        predictions = model.predict(X)
        signature = infer_signature(X, predictions)

        # Log the model
        artifact_path = "model"
        with mlflow.start_run():
            model_info = mlflow.lightgbm.log_model(model, artifact_path, signature=signature)

        # Fetch the logged model artifacts
        print(f"run_id: {run.info.run_id}")
        client = mlflow.MlflowClient()
        artifacts = [f.path for f in client.list_artifacts(run.info.run_id, artifact_path)]
        print(f"artifacts: {artifacts}")

    .. code-block:: text
        :caption: Output

        artifacts: [\'model/MLmodel\',
                    \'model/conda.yaml\',
                    \'model/model.pkl\',
                    \'model/python_env.yaml\',
                    \'model/requirements.txt\']
    '''
def load_model(model_uri, dst_path: Incomplete | None = None):
    '''
    Load a LightGBM model from a local file or a run.

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

    :return: A LightGBM model (an instance of `lightgbm.Booster`_) or a LightGBM scikit-learn
             model, depending on the saved model class specification.

    .. code-block:: python
        :caption: Example

        from lightgbm import LGBMClassifier
        from sklearn import datasets
        import mlflow

        # Auto log all MLflow entities
        mlflow.lightgbm.autolog()

        # Load iris dataset
        X, y = datasets.load_iris(return_X_y=True, as_frame=True)

        # Initialize our model
        model = LGBMClassifier(objective="multiclass", random_state=42)

        # Train the model
        model.fit(X, y)

        # Load model for inference
        model_uri = f"runs:/{mlflow.last_active_run().info.run_id}/model"
        loaded_model = mlflow.lightgbm.load_model(model_uri)
        print(loaded_model.predict(X[:5]))

    .. code-block:: text
        :caption: Output

        [0 0 0 0 0]
    '''

class _LGBModelWrapper:
    lgb_model: Incomplete
    def __init__(self, lgb_model) -> None: ...
    def predict(self, dataframe, params: Dict[str, Any] | None = None):
        """
        :param dataframe: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """

def autolog(log_input_examples: bool = False, log_model_signatures: bool = True, log_models: bool = True, log_datasets: bool = True, disable: bool = False, exclusive: bool = False, disable_for_unsupported_versions: bool = False, silent: bool = False, registered_model_name: Incomplete | None = None, extra_tags: Incomplete | None = None):
    '''
    Enables (or disables) and configures autologging from LightGBM to MLflow. Logs the following:

    - parameters specified in `lightgbm.train`_.
    - metrics on each iteration (if ``valid_sets`` specified).
    - metrics at the best iteration (if ``early_stopping_rounds`` specified or ``early_stopping``
        callback is set).
    - feature importance (both "split" and "gain") as JSON files and plots.
    - trained model, including:
        - an example of valid input.
        - inferred signature of the inputs and outputs of the model.

    Note that the `scikit-learn API`_ is now supported.

    :param log_input_examples: If ``True``, input examples from training datasets are collected and
                               logged along with LightGBM model artifacts during training. If
                               ``False``, input examples are not logged.
                               Note: Input examples are MLflow model attributes
                               and are only collected if ``log_models`` is also ``True``.
    :param log_model_signatures: If ``True``,
                                 :py:class:`ModelSignatures <mlflow.models.ModelSignature>`
                                 describing model inputs and outputs are collected and logged along
                                 with LightGBM model artifacts during training. If ``False``,
                                 signatures are not logged.
                                 Note: Model signatures are MLflow model attributes
                                 and are only collected if ``log_models`` is also ``True``.
    :param log_models: If ``True``, trained models are logged as MLflow model artifacts.
                       If ``False``, trained models are not logged.
                       Input examples and model signatures, which are attributes of MLflow models,
                       are also omitted when ``log_models`` is ``False``.
    :param log_datasets: If ``True``, train and validation dataset information is logged to MLflow
                         Tracking if applicable. If ``False``, dataset information is not logged.
    :param disable: If ``True``, disables the LightGBM autologging integration. If ``False``,
                    enables the LightGBM autologging integration.
    :param exclusive: If ``True``, autologged content is not logged to user-created fluent runs.
                      If ``False``, autologged content is logged to the active fluent run,
                      which may be user-created.
    :param disable_for_unsupported_versions: If ``True``, disable autologging for versions of
                      lightgbm that have not been tested against this version of the MLflow client
                      or are incompatible.
    :param silent: If ``True``, suppress all event logs and warnings from MLflow during LightGBM
                   autologging. If ``False``, show all events and warnings during LightGBM
                   autologging.
    :param registered_model_name: If given, each time a model is trained, it is registered as a
                                  new model version of the registered model with this name.
                                  The registered model is created if it does not already exist.
    :param extra_tags: A dictionary of extra tags to set on each managed run created by autologging.

    .. code-block:: python
        :caption: Example

        import mlflow
        from lightgbm import LGBMClassifier
        from sklearn import datasets


        def print_auto_logged_info(run):
            tags = {k: v for k, v in run.data.tags.items() if not k.startswith("mlflow.")}
            artifacts = [
                f.path for f in mlflow.MlflowClient().list_artifacts(run.info.run_id, "model")
            ]
            feature_importances = [
                f.path
                for f in mlflow.MlflowClient().list_artifacts(run.info.run_id)
                if f.path != "model"
            ]
            print(f"run_id: {run.info.run_id}")
            print(f"artifacts: {artifacts}")
            print(f"feature_importances: {feature_importances}")
            print(f"params: {run.data.params}")
            print(f"metrics: {run.data.metrics}")
            print(f"tags: {tags}")


        # Load iris dataset
        X, y = datasets.load_iris(return_X_y=True, as_frame=True)

        # Initialize our model
        model = LGBMClassifier(objective="multiclass", random_state=42)

        # Auto log all MLflow entities
        mlflow.lightgbm.autolog()

        # Train the model
        with mlflow.start_run() as run:
            model.fit(X, y)

        # fetch the auto logged parameters and metrics
        print_auto_logged_info(mlflow.get_run(run_id=run.info.run_id))

    .. code-block:: text
        :caption: Output

        run_id: e08dd59d57a74971b68cf78a724dfaf6
        artifacts: [\'model/MLmodel\',
                    \'model/conda.yaml\',
                    \'model/model.pkl\',
                    \'model/python_env.yaml\',
                    \'model/requirements.txt\']
        feature_importances: [\'feature_importance_gain.json\',
                              \'feature_importance_gain.png\',
                              \'feature_importance_split.json\',
                              \'feature_importance_split.png\']
        params: {\'boosting_type\': \'gbdt\',
                 \'categorical_feature\': \'auto\',
                 \'colsample_bytree\': \'1.0\',
                 ...
                 \'verbose_eval\': \'warn\'}
        metrics: {}
        tags: {}
    '''
