from mlflow.utils.autologging_utils.safety import *
from mlflow.utils.autologging_utils.events import *
from mlflow.utils.autologging_utils.client import *
from _typeshed import Incomplete
from collections.abc import Generator
from mlflow.entities import Metric as Metric
from mlflow.tracking.client import MlflowClient as MlflowClient
from mlflow.utils.autologging_utils.events import AutologgingEventLogger as AutologgingEventLogger
from mlflow.utils.autologging_utils.logging_and_warnings import set_mlflow_events_and_warnings_behavior_globally as set_mlflow_events_and_warnings_behavior_globally, set_non_mlflow_warnings_behavior_for_current_thread as set_non_mlflow_warnings_behavior_for_current_thread
from mlflow.utils.autologging_utils.safety import revert_patches as revert_patches, update_wrapper_extended as update_wrapper_extended
from mlflow.utils.autologging_utils.versioning import FLAVOR_TO_MODULE_NAME_AND_VERSION_INFO_KEY as FLAVOR_TO_MODULE_NAME_AND_VERSION_INFO_KEY, get_min_max_version_and_pip_release as get_min_max_version_and_pip_release, is_flavor_supported_for_associated_package_versions as is_flavor_supported_for_associated_package_versions
from mlflow.utils.validation import MAX_METRICS_PER_BATCH as MAX_METRICS_PER_BATCH
from typing import List

INPUT_EXAMPLE_SAMPLE_ROWS: int
ENSURE_AUTOLOGGING_ENABLED_TEXT: str
AUTOLOGGING_CONF_KEY_IS_GLOBALLY_CONFIGURED: str
AUTOLOGGING_INTEGRATIONS: Incomplete

def get_mlflow_run_params_for_fn_args(fn, args, kwargs, unlogged: Incomplete | None = None):
    """
    Given arguments explicitly passed to a function, generate a dictionary of MLflow Run
    parameter key / value pairs.

    :param fn: function whose parameters are to be logged
    :param args: arguments explicitly passed into fn. If `fn` is defined on a class,
                 `self` should not be part of `args`; the caller is responsible for
                 filtering out `self` before calling this function.
    :param kwargs: kwargs explicitly passed into fn
    :param unlogged: parameters not to be logged
    :return: A dictionary of MLflow Run parameter key / value pairs.
    """
def log_fn_args_as_params(fn, args, kwargs, unlogged: Incomplete | None = None) -> None:
    """
    Log arguments explicitly passed to a function as MLflow Run parameters to the current active
    MLflow Run.

    :param fn: function whose parameters are to be logged
    :param args: arguments explicitly passed into fn. If `fn` is defined on a class,
                 `self` should not be part of `args`; the caller is responsible for
                 filtering out `self` before calling this function.
    :param kwargs: kwargs explicitly passed into fn
    :param unlogged: parameters not to be logged
    :return: None
    """

class InputExampleInfo:
    """
    Stores info about the input example collection before it is needed.

    For example, in xgboost and lightgbm, an InputExampleInfo object is attached to the dataset,
    where its value is read later by the train method.

    Exactly one of input_example or error_msg should be populated.
    """
    input_example: Incomplete
    error_msg: Incomplete
    def __init__(self, input_example: Incomplete | None = None, error_msg: Incomplete | None = None) -> None: ...

def resolve_input_example_and_signature(get_input_example, infer_model_signature, log_input_example, log_model_signature, logger):
    """
    Handles the logic of calling functions to gather the input example and infer the model
    signature.

    :param get_input_example: function which returns an input example, usually sliced from a
                              dataset. This function can raise an exception, its message will be
                              shown to the user in a warning in the logs.
    :param infer_model_signature: function which takes an input example and returns the signature
                                  of the inputs and outputs of the model. This function can raise
                                  an exception, its message will be shown to the user in a warning
                                  in the logs.
    :param log_input_example: whether to log errors while collecting the input example, and if it
                              succeeds, whether to return the input example to the user. We collect
                              it even if this parameter is False because it is needed for inferring
                              the model signature.
    :param log_model_signature: whether to infer and return the model signature.
    :param logger: the logger instance used to log warnings to the user during input example
                   collection and model signature inference.

    :return: A tuple of input_example and signature. Either or both could be None based on the
             values of log_input_example and log_model_signature.
    """

class BatchMetricsLogger:
    """
    The BatchMetricsLogger will log metrics in batch against an mlflow run.
    If run_id is passed to to constructor then all recording and logging will
    happen against that run_id.
    If no run_id is passed into constructor, then the run ID will be fetched
    from `mlflow.active_run()` each time `record_metrics()` or `flush()` is called; in this
    case, callers must ensure that an active run is present before invoking
    `record_metrics()` or `flush()`.
    """
    run_id: Incomplete
    client: Incomplete
    data: Incomplete
    total_training_time: int
    total_log_batch_time: int
    previous_training_timestamp: Incomplete
    def __init__(self, run_id: Incomplete | None = None, tracking_uri: Incomplete | None = None) -> None: ...
    def flush(self) -> None:
        """
        The metrics accumulated by BatchMetricsLogger will be batch logged to an MLFlow run.
        """
    def record_metrics(self, metrics, step: Incomplete | None = None) -> None:
        """
        Submit a set of metrics to be logged. The metrics may not be immediately logged, as this
        class will batch them in order to not increase execution time too much by logging
        frequently.

        :param metrics: dictionary containing key, value pairs of metrics to be logged.
        :param step: the training step that the metrics correspond to.
        """

def batch_metrics_logger(run_id) -> Generator[Incomplete, None, None]:
    """
    Context manager that yields a BatchMetricsLogger object, which metrics can be logged against.
    The BatchMetricsLogger keeps metrics in a list until it decides they should be logged, at
    which point the accumulated metrics will be batch logged. The BatchMetricsLogger ensures
    that logging imposes no more than a 10% overhead on the training, where the training is
    measured by adding up the time elapsed between consecutive calls to record_metrics.

    If logging a batch fails, a warning will be emitted and subsequent metrics will continue to
    be collected.

    Once the context is closed, any metrics that have yet to be logged will be logged.

    :param run_id: ID of the run that the metrics will be logged to.
    """
def gen_autologging_package_version_requirements_doc(integration_name):
    """
    :return: A document note string saying the compatibility for the specified autologging
             integration's associated package versions.
    """
def autologging_integration(name):
    """
    **All autologging integrations should be decorated with this wrapper.**

    Wraps an autologging function in order to store its configuration arguments. This enables
    patch functions to broadly obey certain configurations (e.g., disable=True) without
    requiring specific logic to be present in each autologging integration.
    """
def get_autologging_config(flavor_name, config_key, default_value: Incomplete | None = None):
    """
    Returns a desired config value for a specified autologging integration.
    Returns `None` if specified `flavor_name` has no recorded configs.
    If `config_key` is not set on the config object, default value is returned.

    :param flavor_name: An autologging integration flavor name.
    :param config_key: The key for the desired config value.
    :param default_value: The default_value to return
    """
def autologging_is_disabled(integration_name):
    """
    Returns a boolean flag of whether the autologging integration is disabled.

    :param integration_name: An autologging integration flavor name.
    """
def disable_autologging() -> Generator[None, None, None]:
    """
    Context manager that temporarily disables autologging globally for all integrations upon
    entry and restores the previous autologging configuration upon exit.
    """
def disable_discrete_autologging(flavors_to_disable: List[str]) -> None:
    """
    Context manager for disabling specific autologging integrations temporarily while another
    flavor's autologging is activated. This context wrapper is useful in the event that, for
    example, a particular library calls upon another library within a training API that has a
    current MLflow autologging integration.
    For instance, the transformers library's Trainer class, when running metric scoring,
    builds a sklearn model and runs evaluations as part of its accuracy scoring. Without this
    temporary autologging disabling, a new run will be generated that contains a sklearn model
    that holds no use for tracking purposes as it is only used during the metric evaluation phase
    of training.
    :param flavors_to_disable: A list of flavors that need to be temporarily disabled while
                               executing another flavor's autologging to prevent spurious run
                               logging of unrelated models, metrics, and parameters.
    """
def get_instance_method_first_arg_value(method, call_pos_args, call_kwargs):
    """
    Get instance method first argument value (exclude the `self` argument).
    :param method A `cls.method` object which includes the `self` argument.
    :param call_pos_args: positional arguments excluding the first `self` argument.
    :param call_kwargs: keywords arguments.
    """
def get_method_call_arg_value(arg_index, arg_name, default_value, call_pos_args, call_kwargs):
    """
    Get argument value for a method call.
    :param arg_index: the argument index in the function signature. start from 0.
    :param arg_name: the argument name in the function signature.
    :param default_value: default argument value.
    :param call_pos_args: the positional argument values in the method call.
    :param call_kwargs: the keyword argument values in the method call.
    """
