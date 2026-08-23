from _typeshed import Incomplete

class FeatureSelector:
    selected_features_: Incomplete
    X: Incomplete
    y: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def fit(self, X, y, **kwargs) -> None:
        """
        Fit the training data to FeatureSelector

        Paramters
        ---------
        X : array-like numpy matrix
            The training input samples, which shape is [n_samples, n_features].
        y: array-like numpy matrix
            The target values (class labels in classification, real numbers in
            regression). Which shape is [n_samples].
        """
    def get_selected_features(self):
        """
        Fit the training data to FeatureSelector

        Returns
        -------
        list :
                Return the index of imprtant feature.
        """
