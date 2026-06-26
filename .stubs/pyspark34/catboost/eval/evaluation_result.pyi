from .. import CatBoostError as CatBoostError
from ..core import metric_description_or_str_to_str as metric_description_or_str_to_str
from ..utils import compute_wx_test as compute_wx_test
from _typeshed import Incomplete
from enum import Enum

def calc_wilcoxon_test(baseline, test): ...

class ScoreType(Enum):
    Abs: str
    Rel: str

class ScoreConfig:
    """
        Config to present human-friendly evaluation results.
    """
    type: Incomplete
    multiplier: Incomplete
    score_level: Incomplete
    interval_level: Incomplete
    overfit_overfit_iterations_info: Incomplete
    def __init__(self, score_type=..., multiplier: int = 100, score_level: float = 0.01, interval_level: float = 0.01, overfit_iterations_info: bool = True) -> None:
        """

        :param score_type: type of score. For abs difference score will be (baseline - test).mean(),
        for relative it's ((baseline - test) / baseline).mean()
        :param multiplier: multiplier to print score
        :param score_level: WX-test level. Will be used to make if tested case significantly better or worse
        :param interval_level: level to compute score confidence interval
        :param overfit_iterations_info: if information about overfit iterations should be preserved
        """
    @staticmethod
    def abs_score(level: float = 0.01): ...
    @staticmethod
    def rel_score(level: float = 0.01): ...

def calc_bootstrap_ci_for_mean(samples, level: float = 0.05, tries: int = 999):
    """
    Count confidence intervals for difference each two samples.

    Args:
        :param samples: samples
        :param level: (float) Level for the confidence interval.
        :param tries: bootstrap samples to use
        :return: (left, right) border of confidence interval

    """

class CaseEvaluationResult:
    """
        CaseEvaluationResults stores aggregated statistics for one EvaluationCase and one metric.
    """
    def __init__(self, case, metric_description, eval_step) -> None: ...
    def __eq__(self, other): ...
    def get_case(self):
        """
            ExecutionCases for this result
        """
    def get_fold_ids(self):
        """

        :return: FoldsIds for which this caseResult was calculated
        """
    def get_best_metric_for_fold(self, fold):
        """

        :param fold: id of fold to get result
        :return: best metric value, best metric iteration
        """
    def get_best_iterations(self):
        """

        :return: pandas Series with best iterations on all folds
        """
    def get_best_metrics(self):
        """

        :return: pandas series with best metric values
        """
    def get_fold_curve(self, fold):
        """

        :param fold:
        :return: fold learning curve (test scores on every eval_period iteration)
        """
    def get_metric_description(self):
        """

        :return: Metric used to build this CaseEvaluationResult
        """
    def get_eval_step(self):
        """

        :return: step which was used for metric computations
        """
    def count_under_and_over_fits(self, overfit_border: float = 0.15, underfit_border: float = 0.95):
        """

        :param overfit_border: min fraction of iterations until overfitting starts one expects all models to have
        :param underfit_border: border, after which there should be no best_metric_scores
        :return: #models with best_metric > underfit_border * iter_count, #models, with best_metric > overfit_border
        """
    def estimate_fit_quality(self):
        """

        :return: Simple sanity check that all models overfit and not too fast
        """
    def create_learning_curves_plot(self, offset: Incomplete | None = None):
        """

        :param offset: First iteration to plot
        :return: plotly Figure with learning curves for each fold
        """

class MetricEvaluationResult:
    """
        Evaluation result for one metric.
        Stores all ExecutionCases with specified metric scores
        Computes human-friendly tables with results and some plots
    """
    def __init__(self, case_results) -> None: ...
    def get_baseline_case(self):
        """

        :return: ExecutionCases used as a baseline (with everything else is compared)
        """
    def get_cases(self):
        """

        :return: Cases which are compared
        """
    def get_metric_description(self):
        """

        :return: Metric for which results were calculated
        """
    def get_baseline_comparison(self, score_config: Incomplete | None = None):
        """
        Method to get human-friendly table with model comparisons.

        Returns baseline vs all other computed cases result
        :param score_config: Config to present human-friendly score, optional. Instance of ScoreConfig
        :return: pandas DataFrame. Each row is related to one ExecutionCase.
        Each row describes how better (or worse) this case is compared to baseline.
        """
    def get_case_comparison(self, case, score_config: Incomplete | None = None):
        """
        Method to get human-friendly table with model comparisons.
        Same as get_baseline_comparison(), but with other non-baseline case specified as baseline

        :param case: use specified case as baseline
        :param score_config:
        :return: pandas DataFrame. Each row is related to one ExecutionCase.
        Each row describes how better (or worse) this case is compared to baseline.
        """
    def change_baseline_case(self, case) -> None:
        """

        :param case: new baseline case
        :return:
        """
    def get_case_result(self, case):
        """

        :param case:
        :return: CaseEvaluationResult. Scores and other information about single execution case
        """
    def get_fold_ids(self):
        """

        :return: Folds ids which we used for computing this evaluation result
        """
    def get_eval_step(self): ...
    def create_fold_learning_curves(self, fold, offset: Incomplete | None = None):
        """

        :param fold: FoldId to plot
        :param offset: first iteration to plot
        :return: plotly figure for all cases on specified fold
        """
    def __eq__(self, other): ...

class EvaluationResults:
    def __init__(self, metric_results) -> None: ...
    def get_metric_results(self, metric):
        """

        :param metric:
        :return: MetricEvaluationResult for specified metric
        """
    def get_metrics(self):
        """

        :return: Names of the metrics which were computed
        """
    def get_results(self):
        """

        :return: Results are the map from metric names to computed results (instance of MetricEvaluationResult)
         on this fold
        """
    def set_baseline_case(self, case) -> None:
        """
            Could be used to change baseline cases for already computed results
        """
