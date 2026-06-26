from . import constants as constants
from .fginitialize import PrepareData as PrepareData
from _typeshed import Incomplete
from nni.feature_engineering.feature_selector import FeatureSelector as FeatureSelector
from sklearn.base import BaseEstimator
from sklearn.feature_selection import SelectorMixin

class FeatureGradientSelector(FeatureSelector, BaseEstimator, SelectorMixin):
    order: Incomplete
    penalty: Incomplete
    n_features: Incomplete
    max_features: Incomplete
    learning_rate: Incomplete
    init: Incomplete
    n_epochs: Incomplete
    shuffle: Incomplete
    batch_size: Incomplete
    target_batch_size: Incomplete
    max_time: Incomplete
    dftol_stop: int
    freltol_stop: int
    classification: Incomplete
    ordinal: Incomplete
    balanced: Incomplete
    preprocess: Incomplete
    soft_grouping: Incomplete
    verbose: Incomplete
    device: Incomplete
    model_: Incomplete
    scores_: Incomplete
    def __init__(self, order: int = 4, penalty: int = 1, n_features: Incomplete | None = None, max_features: Incomplete | None = None, learning_rate: float = 0.1, init: str = 'zero', n_epochs: int = 1, shuffle: bool = True, batch_size: int = 1000, target_batch_size: int = 1000, max_time=..., classification: bool = True, ordinal: bool = False, balanced: bool = True, preprocess: str = 'zscore', soft_grouping: bool = False, verbose: int = 0, device: str = 'cpu') -> None:
        '''
            FeatureGradientSelector is a class that selects features for a machine
            learning model using a gradient based search.

            Parameters
            ----------
            order : int
                What order of interactions to include. Higher orders
                may be more accurate but increase the run time. 12 is the maximum allowed order.
            penatly : int
                Constant that multiplies the regularization term.
            n_features: int
                If None, will automatically choose number of features based on search.
                Otherwise, number of top features to select.
            max_features : int
                If not None, will use the \'elbow method\' to determine the number of features
                with max_features as the upper limit.
            learning_rate : float
            init : str
                How to initialize the vector of scores. \'zero\' is the default.
                Options: {\'zero\', \'on\', \'off\', \'onhigh\', \'offhigh\', \'sklearn\'}
            n_epochs : int
                number of epochs to run
            shuffle : bool
                Shuffle "rows" prior to an epoch.
            batch_size : int
                Nnumber of "rows" to process at a time
            target_batch_size : int
                Number of "rows" to accumulate gradients over.
                Useful when many rows will not fit into memory but are needed for accurate estimation.
            classification : bool
                If True, problem is classification, else regression.
            ordinal : bool
                If True, problem is ordinal classification. Requires classification to be True.
            balanced : bool
                If true, each class is weighted equally in optimization, otherwise
                weighted is done via support of each class. Requires classification to be True.
            prerocess : str
                \'zscore\' which refers to centering and normalizing data to unit variance or
                \'center\' which only centers the data to 0 mean
            soft_grouping : bool
                if True, groups represent features that come from the same source.
                Used to encourage sparsity of groups and features within groups.
            verbose : int
                Controls the verbosity when fitting. Set to 0 for no printing
                1 or higher for printing every verbose number of gradient steps.
            device : str
                \'cpu\' to run on CPU and \'cuda\' to run on GPU. Runs much faster on GPU
        '''
    def partial_fit(self, X, y, n_classes: Incomplete | None = None, groups: Incomplete | None = None):
        """
        Select Features via a gradient based search on (X, y) on the given samples.
        Can be called repeatedly with different X and y to handle streaming datasets.

        Parameters
        ----------
        X : array-like
            Shape = [n_samples, n_features]
            The training input samples.
        y :  array-like
            Shape = [n_samples]
            The target values (class labels in classification, real numbers in
            regression).
        n_classes : int
            Number of classes
            Classes across all calls to partial_fit.
            Can be obtained by via `np.unique(y_all).shape[0]`, where y_all is the
            target vector of the entire dataset.
            This argument is expected for the first call to partial_fit,
            otherwise will assume all classes are present in the batch of y given.
            It will be ignored in the subsequent calls.
            Note that y doesn't need to contain all labels in `classes`.
        groups : array-like
            Optional, shape = [n_features]
            Groups of columns that must be selected as a unit
            e.g. [0, 0, 1, 2] specifies the first two columns are part of a group.
            This argument is expected for the first call to partial_fit,
            otherwise will assume all classes are present in the batch of y given.
            It will be ignored in the subsequent calls.
        """
    def fit(self, X, y, groups: Incomplete | None = None):
        """
        Select Features via a gradient based search on (X, y).

        Parameters
        ----------
        X : array-like
            Shape = [n_samples, n_features]
            The training input samples.
        y : array-like
            Shape = [n_samples]
            The target values (class labels in classification, real numbers in
            regression).
        groups : array-like
            Optional, shape = [n_features]
            Groups of columns that must be selected as a unit
            e.g. [0, 0, 1, 2] specifies the first two columns are part of a group.
        """
    def get_selected_features(self): ...
    def transform(self, X):
        """
        Returns selected features from X.

        Paramters
        ---------
        X: array-like
            Shape = [n_samples, n_features]
            The training input samples.
        """
    def get_support(self, indices: bool = False):
        """
        Get a mask, or integer index, of the features selected.

        Parameters
        ----------
        indices : bool
            Default False
            If True, the return value will be an array of integers, rather than a boolean mask.

        Returns
        -------
        list :
            returns support: An index that selects the retained features from a feature vector.
            If indices is False, this is a boolean array of shape [# input features],
            in which an element is True iff its corresponding feature is selected for retention.
            If indices is True, this is an integer array of shape [# output features] whose values
            are indices into the input feature vector.
        """
    def inverse_transform(self, X):
        """
        Returns transformed X to the original number of column.
        This operation is lossy and all columns not in the transformed data
        will be returned as columns of 0s.
        """
    def get_params(self, deep: bool = True):
        """
        Get parameters for this estimator.
        """
    def set_params(self, **params):
        """
        Set the parameters of this estimator.
        """
    def fit_transform(self, X, y):
        """
        Select features and then return X with the selected features.

        Parameters
        ----------
        X : array-like
            Shape = [n_samples, n_features]
            The training input samples.
        y : array-like
            Shape = [n_samples]
            The target values (class labels in classification, real numbers in
            regression).
        """
    def set_n_features(self, n, groups: Incomplete | None = None):
        """
        Set the number of features to return after fitting.
        """
    def set_top_percentile(self, percentile, groups: Incomplete | None = None):
        """
        Set the percentile of features to return after fitting.
        """
