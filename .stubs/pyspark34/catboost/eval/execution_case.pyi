from .. import CatBoostError as CatBoostError
from ..eval.factor_utils import FactorUtils as FactorUtils
from _typeshed import Incomplete

class ExecutionCase:
    def __init__(self, params, label: Incomplete | None = None, ignored_features: Incomplete | None = None, learning_rate: Incomplete | None = None) -> None:
        """
            Instances of this class are cases which will be compared during evaluation
            Params are CatBoost params
            label is a string which will be used for plots and other visualisations
            ignored_features is a set of additional feature indices to ignore
        """
    def get_params(self): ...
    def get_label(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
