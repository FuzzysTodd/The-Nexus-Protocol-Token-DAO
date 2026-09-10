from .. import CatBoost as CatBoost, CatBoostError as CatBoostError
from ._fold_models_handler import FoldModelsHandler as FoldModelsHandler
from .evaluation_result import EvaluationResults as EvaluationResults, MetricEvaluationResult as MetricEvaluationResult
from .execution_case import ExecutionCase as ExecutionCase
from .factor_utils import FactorUtils as FactorUtils, LabelMode as LabelMode
from _typeshed import Incomplete
from enum import Enum

class EvalType(Enum):
    """
        Type of feature evaluation:
            All: All factors presented
            SeqRem:  Each factor while other presented
            SeqAdd:  Each factor while other removed
            SeqAddAndAll:  SeqAdd + All
    """
    All: str
    SeqRem: str
    SeqAdd: str
    SeqAddAndAll: str

class CatboostEvaluation:
    def __init__(self, path_to_dataset, fold_size, fold_count, column_description, fold_offset: int = 0, group_column: Incomplete | None = None, working_dir: Incomplete | None = None, remove_models: bool = True, delimiter: str = '\t', has_header: bool = False, partition_random_seed: int = 0, min_fold_count: int = 1) -> None:
        """
        Args:
            :param path_to_dataset: (str) Path to the dataset to be used for evaluation.
            :param fold_size: (int) Size of the folds in cross-validation.
            :param fold_count: (int) Number of times we get a new fold, learn a model and check results as if
            there wouldn't be any offset. If there'are some offset it means that the real count of folds will
            be smaller.
            :param column_description: (str) Path to the file where column description is placed.
            :param fold_offset: (int) Number of folds we skip before begin to make cross-validation.
            :param group_column: (int) GroupId column index in the dataset file.
            'None' value means absence of grouping information in the dataset (it's the default).
            :param working_dir: Working dir for temporary files
            :param remove_models: (bool) Set true if you want models to be removed after applying them.
            :param delimiter: (str) Field delimiter used in dataset files.
            :param has_header: (bool) Set true if you want to skip first line in dataset files.
            :param partition_random_seed: (int) The seed for random value generator used for getting permutations for
             cross-validation.
            :param min_fold_count: (int) Minimun amount of folds dataset can be cut to.
        """
    def get_working_dir(self): ...
    def eval_features(self, learn_config, features_to_eval, loss_function: Incomplete | None = None, eval_type=..., eval_metrics: Incomplete | None = None, thread_count: int = -1, eval_step: Incomplete | None = None, label_mode=...):
        """ Evaluate features.
            Args:
            learn_config: dict with params or instance of CatBoost. In second case instance params will be used
            features_to_eval: list of indices of features to evaluate
            loss_function: one of CatBoost loss functions, get it from learn_config if not specified
            eval_type: Type of feature evaluate (All, SeqAdd, SeqRem)
            eval_metrics: Additional metrics to calculate
            thread_count: thread_count to use. If not none will override learn_config values
            Returns
            -------
            result : Instance of EvaluationResult class
        """
    def eval_cases(self, baseline_case, compare_cases, eval_metrics, thread_count: int = -1, eval_step: int = 1):
        """More flexible evaluation of any cases.
            Args:
            baseline_case: Execution case used for baseline
            compare_cases: List of cases to compare
            eval_metrics: Metrics to calculate
            thread_count: thread_count to use.  Will override one in cases
            Returns
            -------
            result : Instance of EvaluationResult class
        """
