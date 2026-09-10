from _typeshed import Incomplete
from mlflow.data.code_dataset_source import CodeDatasetSource as CodeDatasetSource
from mlflow.data.spark_dataset import SparkDataset as SparkDataset
from mlflow.entities import Metric as Metric, Param as Param
from mlflow.entities.dataset_input import DatasetInput as DatasetInput
from mlflow.entities.input_tag import InputTag as InputTag
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.tracking.client import MlflowClient as MlflowClient
from mlflow.utils.autologging_utils import INPUT_EXAMPLE_SAMPLE_ROWS as INPUT_EXAMPLE_SAMPLE_ROWS, autologging_integration as autologging_integration, get_method_call_arg_value as get_method_call_arg_value, resolve_input_example_and_signature as resolve_input_example_and_signature, safe_patch as safe_patch
from mlflow.utils.file_utils import TempDir as TempDir
from mlflow.utils.mlflow_tags import MLFLOW_AUTOLOGGING as MLFLOW_AUTOLOGGING, MLFLOW_DATASET_CONTEXT as MLFLOW_DATASET_CONTEXT, MLFLOW_PARENT_RUN_ID as MLFLOW_PARENT_RUN_ID
from mlflow.utils.rest_utils import MlflowHostCreds as MlflowHostCreds, augmented_raise_for_status as augmented_raise_for_status, http_request as http_request
from mlflow.utils.time_utils import get_current_time_millis as get_current_time_millis
from mlflow.utils.validation import MAX_ENTITY_KEY_LENGTH as MAX_ENTITY_KEY_LENGTH, MAX_PARAMS_TAGS_PER_BATCH as MAX_PARAMS_TAGS_PER_BATCH, MAX_PARAM_VAL_LENGTH as MAX_PARAM_VAL_LENGTH
from typing import NamedTuple

AUTOLOGGING_INTEGRATION_NAME: str

class _AutologgingEstimatorMetadata(NamedTuple):
    hierarchy: Incomplete
    uid_to_indexed_name_map: Incomplete
    param_search_estimators: Incomplete

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
       `Estimator.fit`, `Model.transform`, `Evaluator.evaluate`,
       in order to avoid nested/duplicated autologging metric, when run into these scopes,
       we need temporarily disable the metric autologging.
    (3) _eval_dataset_info_map, it is a double level map:
       `_eval_dataset_info_map[run_id][eval_dataset_var_name]` will get a list, each
       element in the list is an id of "eval_dataset" instance.
       This data structure is used for:
        * generating unique dataset name key when autologging metric. For each eval dataset object,
          if they have the same eval_dataset_var_name, but object ids are different,
          then they will be assigned different name (via appending index to the
          eval_dataset_var_name) when autologging.
    (4) _evaluator_call_info, it is a double level map:
       `_metric_api_call_info[run_id][metric_name]` wil get a list of tuples, each tuple is:
         (logged_metric_key, evaluator_information)
        Evaluator information includes evaluator class name and params, these information
        will also be logged into "metric_info.json" artifacts.

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

        Note: It includes checking `_SparkTrainingSession.is_active()`, This is a safe guarding
        for meta-estimator (e.g. CrossValidator/TrainValidationSplit) case:
          running CrossValidator.fit, the nested `estimator.fit` will be called in parallel,
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
    def get_run_id_and_dataset_name_for_evaluator_call(self, pred_result_dataset):
        """
        Given a registered prediction result dataset object,
        return a tuple of (run_id, eval_dataset_name)
        """
    def gen_evaluator_info(self, evaluator):
        """
        Generate evaluator information, include evaluator class name and params.
        """
    def register_evaluator_call(self, run_id, metric_name, dataset_name, evaluator_info):
        """
        Register the `Evaluator.evaluate` call, including register the evaluator information
        (See doc of `gen_evaluator_info` method) into the corresponding run_id and metric_name
        entry in the registry table.
        """
    def log_post_training_metric(self, run_id, key, value):
        """
        Log the metric into the specified mlflow run.
        and it will also update the metric_info artifact if needed.
        """

def autolog(log_models: bool = True, log_datasets: bool = True, disable: bool = False, exclusive: bool = False, disable_for_unsupported_versions: bool = False, silent: bool = False, log_post_training_metrics: bool = True, registered_model_name: Incomplete | None = None, log_input_examples: bool = False, log_model_signatures: bool = True, log_model_allowlist: Incomplete | None = None, extra_tags: Incomplete | None = None):
    '''
    Enables (or disables) and configures autologging for pyspark ml estimators.
    This method is not threadsafe.
    This API requires Spark 3.0 or above.

    **When is autologging performed?**
      Autologging is performed when you call ``Estimator.fit`` except for estimators (featurizers)
      under ``pyspark.ml.feature``.

    **Logged information**
      **Parameters**
        - Parameters obtained by ``estimator.params``. If a param value is also an ``Estimator``,
          then params in the the wrapped estimator will also be logged, the nested param key
          will be `{estimator_uid}.{param_name}`

      **Tags**
        - An estimator class name (e.g. "LinearRegression").
        - A fully qualified estimator class name
          (e.g. "pyspark.ml.regression.LinearRegression").

      .. _post training metrics:

      **Post training metrics**
        When users call evaluator APIs after model training, MLflow tries to capture the
        `Evaluator.evaluate` results and log them as MLflow metrics to the Run associated with
        the model. All pyspark ML evaluators are supported.

        For post training metrics autologging, the metric key format is:
        "{metric_name}[-{call_index}]_{dataset_name}"

        - The metric name is the name returned by `Evaluator.getMetricName()`
        - If multiple calls are made to the same pyspark ML evaluator metric, each subsequent call
          adds a "call_index" (starting from 2) to the metric key.
        - MLflow uses the prediction input dataset variable name as the "dataset_name" in the
          metric key. The "prediction input dataset variable" refers to the variable which was
          used as the `dataset` argument of `model.transform` call.
          Note: MLflow captures the "prediction input dataset" instance in the outermost call
          frame and fetches the variable name in the outermost call frame. If the "prediction
          input dataset" instance is an intermediate expression without a defined variable
          name, the dataset name is set to "unknown_dataset". If multiple "prediction input
          dataset" instances have the same variable name, then subsequent ones will append an
          index (starting from 2) to the inspected dataset name.

        **Limitations**
          - MLflow cannot find run information for other objects derived from a given prediction
            result (e.g. by doing some transformation on the prediction result dataset).

      **Artifacts**
        - An MLflow Model with the :py:mod:`mlflow.spark` flavor containing a fitted estimator
          (logged by :py:func:`mlflow.spark.log_model()`). Note that large models may not be
          autologged for performance and storage space considerations, and autologging for
          Pipelines and hyperparameter tuning meta-estimators (e.g. CrossValidator) is not yet
          supported.
          See ``log_models`` param below for details.
        - For post training metrics API calls, a "metric_info.json" artifact is logged. This is a
          JSON object whose keys are MLflow post training metric names
          (see "Post training metrics" section for the key format) and whose values are the
          corresponding evaluator information, including evaluator class name and evaluator params.

    **How does autologging work for meta estimators?**
          When a meta estimator (e.g. `Pipeline`_, `CrossValidator`_, `TrainValidationSplit`_,
          `OneVsRest`_)
          calls ``fit()``, it internally calls ``fit()`` on its child estimators. Autologging
          does NOT perform logging on these constituent ``fit()`` calls.

          A "estimator_info.json" artifact is logged, which includes a `hierarchy` entry
          describing the hierarchy of the meta estimator. The hierarchy includes expanded
          entries for all nested stages, such as nested pipeline stages.

      **Parameter search**
          In addition to recording the information discussed above, autologging for parameter
          search meta estimators (`CrossValidator`_ and `TrainValidationSplit`_) records child runs
          with metrics for each set of explored parameters, as well as artifacts and parameters
          for the best model and the best parameters (if available).
          For better readability, the "estimatorParamMaps" param in parameter search estimator
          will be recorded inside "estimator_info" artifact, see following description.
          Inside "estimator_info.json" artifact, in addition to the "hierarchy", records 2 more
          items: "tuning_parameter_map_list": a list contains all parameter maps used in tuning,
          and "tuned_estimator_parameter_map": the parameter map of the tuned estimator.
          Records a "best_parameters.json" artifacts, contains the best parameter it searched out.
          Records a "search_results.csv" artifacts, contains search results, it is a table with
          2 columns: "params" and "metric".

    .. _OneVsRest:
        https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.classification.OneVsRest.html#pyspark.ml.classification.OneVsRest
    .. _Pipeline:
        https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.Pipeline.html#pyspark.ml.Pipeline
    .. _CrossValidator:
        https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.tuning.CrossValidator.html#pyspark.ml.tuning.CrossValidator
    .. _TrainValidationSplit:
        https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.tuning.TrainValidationSplit.html#pyspark.ml.tuning.TrainValidationSplit

    :param log_models: If ``True``, if trained models are in allowlist, they are logged as MLflow
                       model artifacts. If ``False``, trained models are not logged.
                       Note: the built-in allowlist excludes some models (e.g. ALS models) which
                       can be large. To specify a custom allowlist, create a file containing a
                       newline-delimited list of fully-qualified estimator classnames, and set
                       the "spark.mlflow.pysparkml.autolog.logModelAllowlistFile" Spark config
                       to the path of your allowlist file.
    :param log_datasets: If ``True``, dataset information is logged to MLflow Tracking.
                         If ``False``, dataset information is not logged.
    :param disable: If ``True``, disables the scikit-learn autologging integration. If ``False``,
                    enables the pyspark ML autologging integration.
    :param exclusive: If ``True``, autologged content is not logged to user-created fluent runs.
                      If ``False``, autologged content is logged to the active fluent run,
                      which may be user-created.
    :param disable_for_unsupported_versions: If ``True``, disable autologging for versions of
                      pyspark that have not been tested against this version of the MLflow
                      client or are incompatible.
    :param silent: If ``True``, suppress all event logs and warnings from MLflow during pyspark ML
                   autologging. If ``False``, show all events and warnings during pyspark ML
                   autologging.
    :param log_post_training_metrics: If ``True``, post training metrics are logged. Defaults to
                                      ``True``. See the `post training metrics`_ section for more
                                      details.
    :param registered_model_name: If given, each time a model is trained, it is registered as a
                                  new model version of the registered model with this name.
                                  The registered model is created if it does not already exist.
    :param log_input_examples: If ``True``, input examples from training datasets are collected and
                               logged along with pyspark ml model artifacts during training. If
                               ``False``, input examples are not logged.
    :param log_model_signatures: If ``True``,
                                 :py:class:`ModelSignatures <mlflow.models.ModelSignature>`
                                 describing model inputs and outputs are collected and logged along
                                 with spark ml pipeline/estimator artifacts during training.
                                 If ``False`` signatures are not logged.

                                 .. warning::

                                    Currently, only scalar Spark data types are supported. If
                                    model inputs/outputs contain non-scalar Spark data types such
                                    as ``pyspark.ml.linalg.Vector``, signatures are not logged.
    :param log_model_allowlist: If given, it overrides the default log model allowlist in mlflow.
                                This takes precedence over the spark configuration of
                                "spark.mlflow.pysparkml.autolog.logModelAllowlistFile".

    **The default log model allowlist in mlflow**
        .. literalinclude:: ../../../mlflow/pyspark/ml/log_model_allowlist.txt
           :language: text

    :param extra_tags: A dictionary of extra tags to set on each managed run created by autologging.
    '''
