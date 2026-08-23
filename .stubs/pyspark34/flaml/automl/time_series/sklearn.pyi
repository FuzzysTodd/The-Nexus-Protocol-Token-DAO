import pandas as pd
from _typeshed import Incomplete
from pandas import to_datetime as to_datetime

class PD: ...

def make_lag_features(X: pd.DataFrame, y: pd.Series, lags: int):
    """Transform input data X, y into autoregressive form - shift
    them appropriately based on horizon and create `lags` columns.

    Parameters
    ----------
    X : pandas.DataFrame
        Input features.

    y : array_like, (1d)
        Target vector.

    horizon : int
        length of X for `predict` method

    Returns
    -------
    pandas.DataFrame
        shifted dataframe with `lags` columns
    """

class SklearnWrapper:
    fit_params: Incomplete
    lags: Incomplete
    horizon: Incomplete
    models: Incomplete
    pca_features: Incomplete
    norm: Incomplete
    pca: Incomplete
    def __init__(self, model_class: type, horizon: int, lags: int, init_params: dict = None, fit_params: dict = None, pca_features: bool = False) -> None: ...
    def fit(self, X: pd.DataFrame, y: pd.Series, **kwargs): ...
    def predict(self, X, X_train: Incomplete | None = None, y_train: Incomplete | None = None): ...
