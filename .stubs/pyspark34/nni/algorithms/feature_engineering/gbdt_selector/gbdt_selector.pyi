from _typeshed import Incomplete
from nni.feature_engineering.feature_selector import FeatureSelector as FeatureSelector

class GBDTSelector(FeatureSelector):
    selected_features_: Incomplete
    X: Incomplete
    y: Incomplete
    feature_importance: Incomplete
    lgb_params: Incomplete
    eval_ratio: Incomplete
    early_stopping_rounds: Incomplete
    importance_type: Incomplete
    num_boost_round: Incomplete
    model: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def fit(self, X, y, **kwargs) -> None:
        """
        Fit the training data to FeatureSelector

        Paramters
        ---------
        X : array-like numpy matrix
            The training input samples, which shape is [n_samples, n_features].
        y : array-like numpy matrix
            The target values (class labels in classification, real numbers in
            regression). Which shape is [n_samples].
        lgb_params : dict
            Parameters of lightgbm
        eval_ratio : float
            The ratio of data size. It's used for split the eval data and train data from self.X.
        early_stopping_rounds : int
            The early stopping setting in lightgbm.
        importance_type : str
            Supporting type is 'gain' or 'split'.
        num_boost_round : int
            num_boost_round in lightgbm.
        """
    def get_selected_features(self, topk):
        """
        Fit the training data to FeatureSelector

        Returns
        -------
        list :
                Return the index of imprtant feature.
        """
