from .. import CatBoostError as CatBoostError
from ..eval.evaluation_result import CaseEvaluationResult as CaseEvaluationResult
from ..eval.log_config import get_eval_logger as get_eval_logger
from ..eval.utils import make_dirs_if_not_exists as make_dirs_if_not_exists
from ._fold_model import FoldModel as FoldModel

class FoldModelsHandler:
    """
    Class that is responsible for learning models and computing their metrics
    """
    def __init__(self, metrics, cases, thread_count, eval_step, remove_models) -> None:
        """
        Args:
            :param remove_models: Set true if you want models to be removed after applying them.

        """
    def proceed(self, splitter, fold_size, folds_count, fold_offset):
        """
        Run all processes to gain stats. It applies algorithms to fold files that gains from learning. It keeps
        stats inside models and models are stored in DataFrame. Columns are matched to the different algos and rows to
        the folds.

        Args:
            :param splitter: Splitter entity.
            :param fold_size: The size of fold.
            :param folds_count: Count of golds.
            :param fold_offset: The offset (count of folds that we want to skip).
            :return: return dict: keys metric to CaseEvaluationResult

        """
