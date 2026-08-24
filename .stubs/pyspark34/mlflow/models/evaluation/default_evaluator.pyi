import mlflow
import pandas as pd
from _typeshed import Incomplete
from mlflow import MlflowClient as MlflowClient
from mlflow.entities.metric import Metric as Metric
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models.evaluation.artifacts import CsvEvaluationArtifact as CsvEvaluationArtifact, ImageEvaluationArtifact as ImageEvaluationArtifact, JsonEvaluationArtifact as JsonEvaluationArtifact, NumpyEvaluationArtifact as NumpyEvaluationArtifact
from mlflow.models.evaluation.base import EvaluationResult as EvaluationResult, ModelEvaluator as ModelEvaluator
from mlflow.models.utils import plot_lines as plot_lines
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.utils.file_utils import TempDir as TempDir
from mlflow.utils.proto_json_utils import NumpyEncoder as NumpyEncoder
from mlflow.utils.time_utils import get_current_time_millis as get_current_time_millis
from typing import Callable, NamedTuple

class _Curve(NamedTuple):
    plot_fn: Incomplete
    plot_fn_args: Incomplete
    auc: Incomplete

class _CustomMetric(NamedTuple):
    """
    A namedtuple representing a custom metric function and its properties.

    function : the custom metric function
    name : the name of the custom metric function
    index : the index of the function in the ``custom_metrics`` argument of mlflow.evaluate
    """
    function: Callable
    name: str
    index: int

class _CustomArtifact(NamedTuple):
    """
    A namedtuple representing a custom artifact function and its properties.

    function : the custom artifact function
    name : the name of the custom artifact function
    index : the index of the function in the ``custom_artifacts`` argument of mlflow.evaluate
    artifacts_dir : the path to a temporary directory to store produced artifacts of the function
    """
    function: Callable
    name: str
    index: int
    artifacts_dir: str

class DefaultEvaluator(ModelEvaluator):
    client: Incomplete
    def __init__(self) -> None: ...
    def can_evaluate(self, *, model_type, evaluator_config, **kwargs): ...
    dataset: Incomplete
    run_id: Incomplete
    model_type: Incomplete
    evaluator_config: Incomplete
    feature_names: Incomplete
    custom_metrics: Incomplete
    custom_artifacts: Incomplete
    y: Incomplete
    pos_label: Incomplete
    sample_weights: Incomplete
    def evaluate(self, *, model: mlflow.pyfunc.PyFuncModel, model_type, dataset, run_id, evaluator_config, custom_metrics: Incomplete | None = None, custom_artifacts: Incomplete | None = None, baseline_model: Incomplete | None = None, **kwargs): ...
    @property
    def X(self) -> pd.DataFrame:
        """
        The features (`X`) portion of the dataset, guarded against accidental mutations.
        """
    class _MutationGuardedData:
        """
        Wrapper around a data object that requires explicit API calls to obtain either a copy
        of the data object, or, in cases where the caller can guaranteed that the object will not
        be mutated, the original data object.
        """
        def __init__(self, data) -> None:
            """
            :param data: A data object, such as a Pandas DataFrame, numPy array, or list.
            """
        def copy_to_avoid_mutation(self):
            """
            Obtain a copy of the data. This method should be called every time the data needs
            to be used in a context where it may be subsequently mutated, guarding against
            accidental reuse after mutation.

            :return: A copy of the data object.
            """
        def get_original(self):
            """
            Obtain the original data object. This method should only be called if the caller
            can guarantee that it will not mutate the data during subsequent operations.

            :return: The original data object.
            """
