from _typeshed import Incomplete
from pyspark.ml.param.shared import Params

class HasArbitraryParamsDict(Params):
    """
    This is a Params based class that is extended by _SparkXGBParams
    and holds the variable to store the **kwargs parts of the XGBoost
    input.
    """
    arbitrary_params_dict: Incomplete

class HasBaseMarginCol(Params):
    """
    This is a Params based class that is extended by _SparkXGBParams
    and holds the variable to store the base margin column part of XGboost.
    """
    base_margin_col: Incomplete

class HasFeaturesCols(Params):
    """
    Mixin for param features_cols: a list of feature column names.
    This parameter is taken effect only when use_gpu is enabled.
    """
    features_cols: Incomplete
    def __init__(self) -> None: ...

class HasEnableSparseDataOptim(Params):
    """
    This is a Params based class that is extended by _SparkXGBParams
    and holds the variable to store the boolean config of enabling sparse data optimization.
    """
    enable_sparse_data_optim: Incomplete
    def __init__(self) -> None: ...

class HasQueryIdCol(Params):
    """
    Mixin for param qid_col: query id column name.
    """
    qid_col: Incomplete
