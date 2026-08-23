import pickle
from _typeshed import Incomplete
from mlflow import pyfunc as pyfunc
from mlflow.data.code_dataset_source import CodeDatasetSource as CodeDatasetSource
from mlflow.data.numpy_dataset import from_numpy as from_numpy
from mlflow.data.pandas_dataset import from_pandas as from_pandas
from mlflow.entities.dataset_input import DatasetInput as DatasetInput
from mlflow.entities.input_tag import InputTag as InputTag
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.protos.databricks_pb2 import INTERNAL_ERROR as INTERNAL_ERROR, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.tracking.client import MlflowClient as MlflowClient
from mlflow.utils import gorilla as gorilla
from mlflow.utils.autologging_utils import INPUT_EXAMPLE_SAMPLE_ROWS as INPUT_EXAMPLE_SAMPLE_ROWS, MlflowAutologgingQueueingClient as MlflowAutologgingQueueingClient, autologging_integration as autologging_integration, disable_autologging as disable_autologging, get_autologging_config as get_autologging_config, get_instance_method_first_arg_value as get_instance_method_first_arg_value, resolve_input_example_and_signature as resolve_input_example_and_signature, safe_patch as safe_patch, update_wrapper_extended as update_wrapper_extended
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import write_to as write_to
from mlflow.utils.mlflow_tags import MLFLOW_AUTOLOGGING as MLFLOW_AUTOLOGGING, MLFLOW_DATASET_CONTEXT as MLFLOW_DATASET_CONTEXT
from typing import Any, Dict

FLAVOR_NAME: str
SERIALIZATION_FORMAT_PICKLE: str
SERIALIZATION_FORMAT_CLOUDPICKLE: str
SUPPORTED_SERIALIZATION_FORMATS: Incomplete

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
def save_model(sk_model, path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, mlflow_model: Incomplete | None = None, serialization_format=..., signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, pyfunc_predict_fn: str = 'predict', metadata: Incomplete | None = None):
    '''
    Save a scikit-learn model to a path on the local file system. Produces an MLflow Model
    containing the following flavors:

        - :py:mod:`mlflow.sklearn`
        - :py:mod:`mlflow.pyfunc`. NOTE: This flavor is only included for scikit-learn models
          that define `predict()`, since `predict()` is required for pyfunc model inference.

    :param sk_model: scikit-learn model to be saved.
    :param path: Local path where the model is to be saved.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param mlflow_model: :py:mod:`mlflow.models.Model` this flavor is being added to.
    :param serialization_format: The format in which to serialize the model. This should be one of
                                 the formats listed in
                                 ``mlflow.sklearn.SUPPORTED_SERIALIZATION_FORMATS``. The Cloudpickle
                                 format, ``mlflow.sklearn.SERIALIZATION_FORMAT_CLOUDPICKLE``,
                                 provides better cross-system compatibility by identifying and
                                 packaging code dependencies with the serialized model.

    :param signature: {{ signature }}
    :param input_example: {{ input_example }}
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param pyfunc_predict_fn: The name of the prediction function to use for inference with the
           pyfunc representation of the resulting MLflow Model; e.g. ``"predict_proba"``.
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.

    .. code-block:: python
        :caption: Example

        import mlflow.sklearn
        from sklearn.datasets import load_iris
        from sklearn import tree

        iris = load_iris()
        sk_model = tree.DecisionTreeClassifier()
        sk_model = sk_model.fit(iris.data, iris.target)

        # Save the model in cloudpickle format
        # set path to location for persistence
        sk_path_dir_1 = ...
        mlflow.sklearn.save_model(
            sk_model,
            sk_path_dir_1,
            serialization_format=mlflow.sklearn.SERIALIZATION_FORMAT_CLOUDPICKLE,
        )

        # save the model in pickle format
        # set path to location for persistence
        sk_path_dir_2 = ...
        mlflow.sklearn.save_model(
            sk_model,
            sk_path_dir_2,
            serialization_format=mlflow.sklearn.SERIALIZATION_FORMAT_PICKLE,
        )
    '''
def log_model(sk_model, artifact_path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, serialization_format=..., registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, await_registration_for=..., pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, pyfunc_predict_fn: str = 'predict', metadata: Incomplete | None = None):
    '''
    Log a scikit-learn model as an MLflow artifact for the current run. Produces an MLflow Model
    containing the following flavors:

        - :py:mod:`mlflow.sklearn`
        - :py:mod:`mlflow.pyfunc`. NOTE: This flavor is only included for scikit-learn models
          that define `predict()`, since `predict()` is required for pyfunc model inference.

    :param sk_model: scikit-learn model to be saved.
    :param artifact_path: Run-relative artifact path.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param serialization_format: The format in which to serialize the model. This should be one of
                                 the formats listed in
                                 ``mlflow.sklearn.SUPPORTED_SERIALIZATION_FORMATS``. The Cloudpickle
                                 format, ``mlflow.sklearn.SERIALIZATION_FORMAT_CLOUDPICKLE``,
                                 provides better cross-system compatibility by identifying and
                                 packaging code dependencies with the serialized model.
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
    :param pyfunc_predict_fn: The name of the prediction function to use for inference with the
           pyfunc representation of the resulting MLflow Model; e.g. ``"predict_proba"``.
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.

    .. code-block:: python
        :caption: Example

        import mlflow
        import mlflow.sklearn
        from mlflow.models import infer_signature
        from sklearn.datasets import load_iris
        from sklearn import tree

        with mlflow.start_run():
            # load dataset and train model
            iris = load_iris()
            sk_model = tree.DecisionTreeClassifier()
            sk_model = sk_model.fit(iris.data, iris.target)

            # log model params
            mlflow.log_param("criterion", sk_model.criterion)
            mlflow.log_param("splitter", sk_model.splitter)
            signature = infer_signature(iris.data, sk_model.predict(iris.data))

            # log model
            mlflow.sklearn.log_model(sk_model, "sk_models", signature=signature)

    '''

class _SklearnModelWrapper:
    sklearn_model: Incomplete
    def __init__(self, sklearn_model) -> None: ...
    def predict(self, data, params: Dict[str, Any] | None = None):
        """
        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """
    def predict_proba(self, *args, **kwargs): ...
    def score(self, *args, **kwargs): ...

class _SklearnCustomModelPicklingError(pickle.PicklingError):
    """
    Exception for describing error raised during pickling custom sklearn estimator
    """
    original_exception: Incomplete
    def __init__(self, sk_model, original_exception) -> None:
        """
        :param sk_model: The custom sklearn model to be pickled
        :param original_exception: The original exception raised
        """

def load_model(model_uri, dst_path: Incomplete | None = None):
    '''
    Load a scikit-learn model from a local file or a run.

    :param model_uri: The location, in URI format, of the MLflow model, for example:

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

    :return: A scikit-learn model.

    .. code-block:: python
        :caption: Example

        import mlflow.sklearn

        sk_model = mlflow.sklearn.load_model("runs:/96771d893a5e46159d9f3b49bf9013e2/sk_models")

        # use Pandas DataFrame to make predictions
        pandas_df = ...
        predictions = sk_model.predict(pandas_df)
    '''

class _AutologgingMetricsManager:
    '''
    This class is designed for holding information which is used by autologging metrics
    It will hold information of:
    (1) a map of "prediction result object id" to a tuple of dataset name(the dataset is
       the one which generate the prediction result) and run_id.
       Note: We need this map instead of setting the run_id into the "prediction result object"
       because the object maybe a numpy array which does not support additional attribute
       assignment.
    (2) _log_post_training_metrics_enabled flag, in the following method scope:
       `model.fit` and `model.score`, in order to avoid nested/duplicated autologging metric, when
       run into these scopes, we need temporarily disable the metric autologging.
    (3) _eval_dataset_info_map, it is a double level map:
       `_eval_dataset_info_map[run_id][eval_dataset_var_name]` will get a list, each
       element in the list is an id of "eval_dataset" instance.
       This data structure is used for:
        * generating unique dataset name key when autologging metric. For each eval dataset object,
          if they have the same eval_dataset_var_name, but object ids are different,
          then they will be assigned different name (via appending index to the
          eval_dataset_var_name) when autologging.
    (4) _metric_api_call_info, it is a double level map:
       `_metric_api_call_info[run_id][metric_name]` wil get a list of tuples, each tuple is:
         (logged_metric_key, metric_call_command_string)
        each call command string is like `metric_fn(arg1, arg2, ...)`
        This data structure is used for:
         * storing the call arguments dict for each metric call, we need log them into metric_info
           artifact file.

    Note: this class is not thread-safe.
    Design rule for this class:
     Because this class instance is a global instance, in order to prevent memory leak, it should
     only holds IDs and other small objects references. This class internal data structure should
     avoid reference to user dataset variables or model variables.
    '''
    def __init__(self) -> None: ...
    def should_log_post_training_metrics(self):
        """
        Check whether we should run patching code for autologging post training metrics.
        This checking should surround the whole patched code due to the safe guard checking,
        See following note.

        Note: It includes checking `_SklearnTrainingSession.is_active()`, This is a safe guarding
        for meta-estimator (e.g. GridSearchCV) case:
          running GridSearchCV.fit, the nested `estimator.fit` will be called in parallel,
          but, the _autolog_training_status is a global status without thread-safe lock protecting.
          This safe guarding will prevent code run into this case.
        """
    def disable_log_post_training_metrics(self): ...
    @staticmethod
    def get_run_id_for_model(model): ...
    @staticmethod
    def is_metric_value_loggable(metric_value):
        """
        check whether the specified `metric_value` is a numeric value which can be logged
        as an MLflow metric.
        """
    def register_model(self, model, run_id) -> None:
        """
        In `patched_fit`, we need register the model with the run_id used in `patched_fit`
        So that in following metric autologging, the metric will be logged into the registered
        run_id
        """
    @staticmethod
    def gen_name_with_index(name, index): ...
    def register_prediction_input_dataset(self, model, eval_dataset):
        '''
        Register prediction input dataset into eval_dataset_info_map, it will do:
         1. inspect eval dataset var name.
         2. check whether eval_dataset_info_map already registered this eval dataset.
            will check by object id.
         3. register eval dataset with id.
         4. return eval dataset name with index.

        Note: this method include inspecting argument variable name.
         So should be called directly from the "patched method", to ensure it capture
         correct argument variable name.
        '''
    def register_prediction_result(self, run_id, eval_dataset_name, predict_result) -> None:
        """
        Register the relationship
         id(prediction_result) --> (eval_dataset_name, run_id)
        into map `_pred_result_id_to_dataset_name_and_run_id`
        """
    @staticmethod
    def gen_metric_call_command(self_obj, metric_fn, *call_pos_args, **call_kwargs):
        '''
        Generate metric function call command string like `metric_fn(arg1, arg2, ...)`
        Note: this method include inspecting argument variable name.
         So should be called directly from the "patched method", to ensure it capture
         correct argument variable name.

        :param self_obj: If the metric_fn is a method of an instance (e.g. `model.score`),
           the `self_obj` represent the instance.
        :param metric_fn: metric function.
        :param call_pos_args: the positional arguments of the metric function call. If `metric_fn`
          is instance method, then the `call_pos_args` should exclude the first `self` argument.
        :param call_kwargs: the keyword arguments of the metric function call.
        '''
    def register_metric_api_call(self, run_id, metric_name, dataset_name, call_command):
        '''
        This method will do:
        (1) Generate and return metric key, format is:
          {metric_name}[-{call_index}]_{eval_dataset_name}
          metric_name is generated by metric function name, if multiple calls on the same
          metric API happen, the following calls will be assigned with an increasing "call index".
        (2) Register the metric key with the "call command" information into
          `_AUTOLOGGING_METRICS_MANAGER`. See doc of `gen_metric_call_command` method for
          details of "call command".
        '''
    def get_run_id_and_dataset_name_for_metric_api_call(self, call_pos_args, call_kwargs):
        """
        Given a metric api call (include the called metric function, and call arguments)
        Register the call information (arguments dict) into the `metric_api_call_arg_dict_list_map`
        and return a tuple of (run_id, eval_dataset_name)
        """
    def log_post_training_metric(self, run_id, key, value):
        """
        Log the metric into the specified mlflow run.
        and it will also update the metric_info artifact if needed.
        """

def autolog(log_input_examples: bool = False, log_model_signatures: bool = True, log_models: bool = True, log_datasets: bool = True, disable: bool = False, exclusive: bool = False, disable_for_unsupported_versions: bool = False, silent: bool = False, max_tuning_runs: int = 5, log_post_training_metrics: bool = True, serialization_format=..., registered_model_name: Incomplete | None = None, pos_label: Incomplete | None = None, extra_tags: Incomplete | None = None) -> None:
    '''
    Enables (or disables) and configures autologging for scikit-learn estimators.

    **When is autologging performed?**
      Autologging is performed when you call:

      - ``estimator.fit()``
      - ``estimator.fit_predict()``
      - ``estimator.fit_transform()``

    **Logged information**
      **Parameters**
        - Parameters obtained by ``estimator.get_params(deep=True)``. Note that ``get_params``
          is called with ``deep=True``. This means when you fit a meta estimator that chains
          a series of estimators, the parameters of these child estimators are also logged.

      **Training metrics**
        - A training score obtained by ``estimator.score``. Note that the training score is
          computed using parameters given to ``fit()``.
        - Common metrics for classifier:

          - `precision score`_

          .. _precision score:
              https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html

          - `recall score`_

          .. _recall score:
              https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html

          - `f1 score`_

          .. _f1 score:
              https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html

          - `accuracy score`_

          .. _accuracy score:
              https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html

          If the classifier has method ``predict_proba``, we additionally log:

          - `log loss`_

          .. _log loss:
              https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html

          - `roc auc score`_

          .. _roc auc score:
              https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html

        - Common metrics for regressor:

          - `mean squared error`_

          .. _mean squared error:
              https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html

          - root mean squared error

          - `mean absolute error`_

          .. _mean absolute error:
              https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html

          - `r2 score`_

          .. _r2 score:
              https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html

      .. _post training metrics:

      **Post training metrics**
        When users call metric APIs after model training, MLflow tries to capture the metric API
        results and log them as MLflow metrics to the Run associated with the model. The following
        types of scikit-learn metric APIs are supported:

        - model.score
        - metric APIs defined in the `sklearn.metrics` module

        For post training metrics autologging, the metric key format is:
        "{metric_name}[-{call_index}]_{dataset_name}"

        - If the metric function is from `sklearn.metrics`, the MLflow "metric_name" is the
          metric function name. If the metric function is `model.score`, then "metric_name" is
          "{model_class_name}_score".
        - If multiple calls are made to the same scikit-learn metric API, each subsequent call
          adds a "call_index" (starting from 2) to the metric key.
        - MLflow uses the prediction input dataset variable name as the "dataset_name" in the
          metric key. The "prediction input dataset variable" refers to the variable which was
          used as the first argument of the associated `model.predict` or `model.score` call.
          Note: MLflow captures the "prediction input dataset" instance in the outermost call
          frame and fetches the variable name in the outermost call frame. If the "prediction
          input dataset" instance is an intermediate expression without a defined variable
          name, the dataset name is set to "unknown_dataset". If multiple "prediction input
          dataset" instances have the same variable name, then subsequent ones will append an
          index (starting from 2) to the inspected dataset name.

        **Limitations**
           - MLflow can only map the original prediction result object returned by a model
             prediction API (including predict / predict_proba / predict_log_proba / transform,
             but excluding fit_predict / fit_transform.) to an MLflow run.
             MLflow cannot find run information
             for other objects derived from a given prediction result (e.g. by copying or selecting
             a subset of the prediction result). scikit-learn metric APIs invoked on derived objects
             do not log metrics to MLflow.
           - Autologging must be enabled before scikit-learn metric APIs are imported from
             `sklearn.metrics`. Metric APIs imported before autologging is enabled do not log
             metrics to MLflow runs.
           - If user define a scorer which is not based on metric APIs in `sklearn.metrics`, then
             then post training metric autologging for the scorer is invalid.

        **Tags**
          - An estimator class name (e.g. "LinearRegression").
          - A fully qualified estimator class name
            (e.g. "sklearn.linear_model._base.LinearRegression").

        **Artifacts**
          - An MLflow Model with the :py:mod:`mlflow.sklearn` flavor containing a fitted estimator
            (logged by :py:func:`mlflow.sklearn.log_model()`). The Model also contains the
            :py:mod:`mlflow.pyfunc` flavor when the scikit-learn estimator defines `predict()`.
          - For post training metrics API calls, a "metric_info.json" artifact is logged. This is a
            JSON object whose keys are MLflow post training metric names
            (see "Post training metrics" section for the key format) and whose values are the
            corresponding metric call commands that produced the metrics, e.g.
            ``accuracy_score(y_true=test_iris_y, y_pred=pred_iris_y, normalize=False)``.

    **How does autologging work for meta estimators?**
      When a meta estimator (e.g. `Pipeline`_, `GridSearchCV`_) calls ``fit()``, it internally calls
      ``fit()`` on its child estimators. Autologging does NOT perform logging on these constituent
      ``fit()`` calls.

      **Parameter search**
          In addition to recording the information discussed above, autologging for parameter
          search meta estimators (`GridSearchCV`_ and `RandomizedSearchCV`_) records child runs
          with metrics for each set of explored parameters, as well as artifacts and parameters
          for the best model (if available).

    **Supported estimators**
      - All estimators obtained by `sklearn.utils.all_estimators`_ (including meta estimators).
      - `Pipeline`_
      - Parameter search estimators (`GridSearchCV`_ and `RandomizedSearchCV`_)

    .. _sklearn.utils.all_estimators:
        https://scikit-learn.org/stable/modules/generated/sklearn.utils.all_estimators.html

    .. _Pipeline:
        https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html

    .. _GridSearchCV:
        https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html

    .. _RandomizedSearchCV:
        https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html

    **Example**

    `See more examples <https://github.com/mlflow/mlflow/blob/master/examples/sklearn_autolog>`_

    .. code-block:: python

        from pprint import pprint
        import numpy as np
        from sklearn.linear_model import LinearRegression
        import mlflow
        from mlflow import MlflowClient


        def fetch_logged_data(run_id):
            client = MlflowClient()
            data = client.get_run(run_id).data
            tags = {k: v for k, v in data.tags.items() if not k.startswith("mlflow.")}
            artifacts = [f.path for f in client.list_artifacts(run_id, "model")]
            return data.params, data.metrics, tags, artifacts


        # enable autologging
        mlflow.sklearn.autolog()

        # prepare training data
        X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
        y = np.dot(X, np.array([1, 2])) + 3

        # train a model
        model = LinearRegression()
        with mlflow.start_run() as run:
            model.fit(X, y)

        # fetch logged data
        params, metrics, tags, artifacts = fetch_logged_data(run.info.run_id)

        pprint(params)
        # {\'copy_X\': \'True\',
        #  \'fit_intercept\': \'True\',
        #  \'n_jobs\': \'None\',
        #  \'normalize\': \'False\'}

        pprint(metrics)
        # {\'training_score\': 1.0,
        #  \'training_mean_absolute_error\': 2.220446049250313e-16,
        #  \'training_mean_squared_error\': 1.9721522630525295e-31,
        #  \'training_r2_score\': 1.0,
        #  \'training_root_mean_squared_error\': 4.440892098500626e-16}

        pprint(tags)
        # {\'estimator_class\': \'sklearn.linear_model._base.LinearRegression\',
        #  \'estimator_name\': \'LinearRegression\'}

        pprint(artifacts)
        # [\'model/MLmodel\', \'model/conda.yaml\', \'model/model.pkl\']

    :param log_input_examples: If ``True``, input examples from training datasets are collected and
                               logged along with scikit-learn model artifacts during training. If
                               ``False``, input examples are not logged.
                               Note: Input examples are MLflow model attributes
                               and are only collected if ``log_models`` is also ``True``.
    :param log_model_signatures: If ``True``,
                                 :py:class:`ModelSignatures <mlflow.models.ModelSignature>`
                                 describing model inputs and outputs are collected and logged along
                                 with scikit-learn model artifacts during training. If ``False``,
                                 signatures are not logged.
                                 Note: Model signatures are MLflow model attributes
                                 and are only collected if ``log_models`` is also ``True``.
    :param log_models: If ``True``, trained models are logged as MLflow model artifacts.
                       If ``False``, trained models are not logged.
                       Input examples and model signatures, which are attributes of MLflow models,
                       are also omitted when ``log_models`` is ``False``.
    :param log_datasets: If ``True``, train and validation dataset information is logged to MLflow
                         Tracking if applicable. If ``False``, dataset information is not logged.
    :param disable: If ``True``, disables the scikit-learn autologging integration. If ``False``,
                    enables the scikit-learn autologging integration.
    :param exclusive: If ``True``, autologged content is not logged to user-created fluent runs.
                      If ``False``, autologged content is logged to the active fluent run,
                      which may be user-created.
    :param disable_for_unsupported_versions: If ``True``, disable autologging for versions of
                      scikit-learn that have not been tested against this version of the MLflow
                      client or are incompatible.
    :param silent: If ``True``, suppress all event logs and warnings from MLflow during scikit-learn
                   autologging. If ``False``, show all events and warnings during scikit-learn
                   autologging.
    :param max_tuning_runs: The maximum number of child Mlflow runs created for hyperparameter
                            search estimators. To create child runs for the best `k` results from
                            the search, set `max_tuning_runs` to `k`. The default value is to track
                            the best 5 search parameter sets. If `max_tuning_runs=None`, then
                            a child run is created for each search parameter set. Note: The best k
                            results is based on ordering in `rank_test_score`. In the case of
                            multi-metric evaluation with a custom scorer, the first scorer’s
                            `rank_test_score_<scorer_name>` will be used to select the best k
                            results. To change metric used for selecting best k results, change
                            ordering of dict passed as `scoring` parameter for estimator.
    :param log_post_training_metrics: If ``True``, post training metrics are logged. Defaults to
                                      ``True``. See the `post training metrics`_ section for more
                                      details.
    :param serialization_format: The format in which to serialize the model. This should be one of
                                 the following: ``mlflow.sklearn.SERIALIZATION_FORMAT_PICKLE`` or
                                 ``mlflow.sklearn.SERIALIZATION_FORMAT_CLOUDPICKLE``.
    :param registered_model_name: If given, each time a model is trained, it is registered as a
                                  new model version of the registered model with this name.
                                  The registered model is created if it does not already exist.
    :param pos_label: If given, used as the positive label to compute binary classification
                      training metrics such as precision, recall, f1, etc. This parameter should
                      only be set for binary classification model. If used for multi-label model,
                      the training metrics calculation will fail and the training metrics won\'t
                      be logged. If used for regression model, the parameter will be ignored.
    :param extra_tags: A dictionary of extra tags to set on each managed run created by autologging.
    '''
