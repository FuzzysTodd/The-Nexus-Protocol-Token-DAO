import numpy as np
from ...api.base import ExplainerMixin as ExplainerMixin
from ...api.templates import FeatureValueExplanation as FeatureValueExplanation
from ...provider import JobLibProvider as JobLibProvider
from ...utils._clean_simple import clean_dimensions as clean_dimensions, clean_init_score_and_X as clean_init_score_and_X, typify_classification as typify_classification
from ...utils._clean_x import preclean_X as preclean_X
from ...utils._compressed_dataset import bin_native_by_dimension as bin_native_by_dimension
from ...utils._explanation import gen_global_selector as gen_global_selector, gen_local_selector as gen_local_selector, gen_name_from_class as gen_name_from_class, gen_perf_dicts as gen_perf_dicts
from ...utils._histogram import make_all_histogram_edges as make_all_histogram_edges
from ...utils._link import inv_link as inv_link
from ...utils._native import Native as Native
from ...utils._preprocessor import construct_bins as construct_bins
from ...utils._privacy import calc_classic_noise_multi as calc_classic_noise_multi, calc_gdp_noise_multi as calc_gdp_noise_multi, validate_eps_delta as validate_eps_delta
from ...utils._rank_interactions import rank_interactions as rank_interactions
from ...utils._seed import normalize_initial_seed as normalize_initial_seed
from ...utils._unify_data import unify_data as unify_data
from ._bin import ebm_decision_function as ebm_decision_function, ebm_decision_function_and_explain as ebm_decision_function_and_explain, eval_terms as eval_terms, make_bin_weights as make_bin_weights
from ._boost import boost as boost
from ._tensor import remove_last as remove_last, trim_tensor as trim_tensor
from ._utils import deduplicate_bins as deduplicate_bins, generate_term_names as generate_term_names, generate_term_types as generate_term_types, jsonify_item as jsonify_item, jsonify_lists as jsonify_lists, make_bag as make_bag, order_terms as order_terms, process_terms as process_terms, remove_unused_higher_bins as remove_unused_higher_bins
from _typeshed import Incomplete
from sklearn.base import BaseEstimator, ClassifierMixin, RegressorMixin
from typing import Dict, List, Mapping, Sequence, Tuple

class EBMExplanation(FeatureValueExplanation):
    """Visualizes specifically for EBM."""
    explanation_type: Incomplete
    def __init__(self, explanation_type, internal_obj, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, name: Incomplete | None = None, selector: Incomplete | None = None) -> None:
        """Initializes class.

        Args:
            explanation_type:  Type of explanation.
            internal_obj: A jsonable object that backs the explanation.
            feature_names: List of feature names.
            feature_types: List of feature types.
            name: User-defined name of explanation.
            selector: A dataframe whose indices correspond to explanation entries.
        """
    def visualize(self, key: Incomplete | None = None):
        """Provides interactive visualizations.

        Args:
            key: Either a scalar or list
                that indexes the internal object for sub-plotting.
                If an overall visualization is requested, pass None.

        Returns:
            A Plotly figure.
        """

def is_private(estimator):
    """Return True if the given estimator is a differentially private EBM estimator
    Parameters
    ----------
    estimator : estimator instance
        Estimator object to test.
    Returns
    -------
    out : bool
        True if estimator is a differentially private EBM estimator and False otherwise.
    """

class EBMModel(BaseEstimator):
    """Base class for all EBMs"""
    feature_names: Incomplete
    feature_types: Incomplete
    max_bins: Incomplete
    max_interaction_bins: Incomplete
    interactions: Incomplete
    exclude: Incomplete
    validation_size: Incomplete
    outer_bags: Incomplete
    inner_bags: Incomplete
    learning_rate: Incomplete
    greediness: Incomplete
    smoothing_rounds: Incomplete
    max_rounds: Incomplete
    early_stopping_rounds: Incomplete
    early_stopping_tolerance: Incomplete
    min_samples_leaf: Incomplete
    max_leaves: Incomplete
    objective: Incomplete
    n_jobs: Incomplete
    random_state: Incomplete
    epsilon: Incomplete
    delta: Incomplete
    composition: Incomplete
    bin_budget_frac: Incomplete
    privacy_bounds: Incomplete
    privacy_target_min: Incomplete
    privacy_target_max: Incomplete
    def __init__(self, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, max_bins: int = 256, max_interaction_bins: int = 32, interactions: int = 10, exclude=[], validation_size: float = 0.15, outer_bags: int = 8, inner_bags: int = 0, learning_rate: float = 0.01, greediness: float = 0.0, smoothing_rounds: int = 0, max_rounds: int = 5000, early_stopping_rounds: int = 50, early_stopping_tolerance: float = 0.0001, min_samples_leaf: int = 2, max_leaves: int = 3, objective: Incomplete | None = None, n_jobs: int = -2, random_state: int = 42, epsilon: int = 1, delta: float = 1e-05, composition: str = 'gdp', bin_budget_frac: float = 0.1, privacy_bounds: Incomplete | None = None, privacy_target_min: Incomplete | None = None, privacy_target_max: Incomplete | None = None) -> None: ...
    n_features_in_: Incomplete
    term_names_: Incomplete
    noise_scale_binning_: Incomplete
    noise_scale_boosting_: Incomplete
    histogram_edges_: Incomplete
    histogram_weights_: Incomplete
    unique_val_counts_: Incomplete
    classes_: Incomplete
    min_target_: Incomplete
    max_target_: Incomplete
    bins_: Incomplete
    feature_names_in_: Incomplete
    feature_types_in_: Incomplete
    feature_bounds_: Incomplete
    term_features_: Incomplete
    bin_weights_: Incomplete
    bagged_scores_: Incomplete
    term_scores_: Incomplete
    standard_deviations_: Incomplete
    intercept_: Incomplete
    link_: Incomplete
    link_param_: Incomplete
    bag_weights_: Incomplete
    breakpoint_iteration_: Incomplete
    has_fitted_: bool
    def fit(self, X, y, sample_weight: Incomplete | None = None, bags: Incomplete | None = None, init_score: Incomplete | None = None):
        """Fits model to provided samples.

        Args:
            X: Numpy array for training samples.
            y: Numpy array as training labels.
            sample_weight: Optional array of weights per sample. Should be same length as X and y.
            bags: Optional bag definitions. The first dimension should have length equal to the number of outer_bags.
                The second dimension should have length equal to the number of samples. The contents should be
                +1 for training, -1 for validation, and 0 if not included in the bag. Numbers other than 1 indicate
                how many times to include the sample in the training or validation sets.
            init_score: Optional. Either a model that can generate scores or per-sample initialization score.
                If samples scores it should be the same length as X.

        Returns:
            Itself.
        """
    def decision_function(self, X, init_score: Incomplete | None = None):
        """Predict scores from model before calling the link function.

        Args:
            X: Numpy array for samples.
            init_score: Optional. Either a model that can generate scores or per-sample initialization score.
                If samples scores it should be the same length as X.

        Returns:
            The sum of the additive term contributions.
        """
    def explain_global(self, name: Incomplete | None = None):
        """Provides global explanation for model.

        Args:
            name: User-defined explanation name.

        Returns:
            An explanation object,
            visualizing feature-value pairs as horizontal bar chart.
        """
    def explain_local(self, X, y: Incomplete | None = None, name: Incomplete | None = None, init_score: Incomplete | None = None):
        """Provides local explanations for provided samples.

        Args:
            X: Numpy array for X to explain.
            y: Numpy vector for y to explain.
            name: User-defined explanation name.
            init_score: Optional. Either a model that can generate scores or per-sample initialization score.
                If samples scores it should be the same length as X.

        Returns:
            An explanation object, visualizing feature-value pairs
            for each sample as horizontal bar charts.
        """
    def term_importances(self, importance_type: str = 'avg_weight'):
        """Provides the term importances

        Args:
            importance_type: the type of term importance requested ('avg_weight', 'min_max')

        Returns:
            An array term importances with one importance per additive term
        """
    def monotonize(self, term, increasing: str = 'auto', passthrough: float = 0.0):
        """Adjusts a term to be monotone using isotonic regression. An important consideration
        is that this function only adjusts a single term and will not modify pairwise terms.
        When a feature needs to be globally monotonic, any pairwise terms that include the feature
        should be excluded from the model.

        Args:
            term: Index or name of the term to monotonize
            increasing: 'auto' or bool. 'auto' decides direction based on Spearman correlation estimate.
            passthrough: the process of monotonization can result in a change to the mean response
                of the model. If passthrough is set to 0.0 then the model's mean response to the
                training set will not change. If passthrough is set to 1.0 then any change to the
                mean response made by monotonization will be passed through to self.intercept_.
                Values between 0 and 1 will result in that percentage being passed through.

        Returns:
            Itself.
        """

class ExplainableBoostingClassifier(EBMModel, ClassifierMixin, ExplainerMixin):
    '''An Explainable Boosting Classifier

    Parameters
    ----------
    feature_names : list of str, default=None
        List of feature names.
    feature_types : list of FeatureType, default=None

        List of feature types. FeatureType can be:

            - `None`: Auto-detect
            - `\'quantile\'`: Continuous with equal density bins
            - `\'rounded_quantile\'`: Continuous with quantile bins, but the cut values are rounded when possible
            - `\'uniform\'`: Continuous with equal width bins
            - `\'winsorized\'`: Continuous with equal width bins, but the leftmost and rightmost cut are chosen by quantiles
            - `\'continuous\'`: Use the default binning for continuous features, which is \'quantile\' currently
            - `[List of float]`: Continuous with specified cut values. Eg: [5.5, 8.75]
            - `[List of str]`: Ordinal categorical where the order has meaning. Eg: ["low", "medium", "high"]
            - `\'ordinal\'`: Ordinal categorical where the order is determined by sorting the feature strings
            - `\'nominal\'`: Categorical where the order has no meaning. Eg: country names
    max_bins : int, default=256
        Max number of bins per feature for the main effects stage.
    max_interaction_bins : int, default=32
        Max number of bins per feature for interaction terms.
    interactions : int, float, or list of tuples of feature indices, default=10

        Interaction terms to be included in the model. Options are:

            - Integer (1 <= interactions): Count of interactions to be automatically selected
            - Percentage (interactions < 1.0): Determine the integer count of interactions by multiplying the number of features by this percentage
            - List of tuples: The tuples contain the indices of the features within the additive term
    exclude : \'mains\' or list of tuples of feature indices|names, default=[]
        Features or terms to be excluded.
    validation_size : int or float, default=0.15

        Validation set size. Used for early stopping during boosting, and is needed to create outer bags.

            - Integer (1 <= validation_size): Count of samples to put in the validation sets
            - Percentage (validation_size < 1.0): Percentage of the data to put in the validation sets
            - 0: Turns off early stopping. Outer bags have no utility. Error bounds will be eliminated
    outer_bags : int, default=8
        Number of outer bags. Outer bags are used to generate error bounds and help with smoothing the graphs.
    inner_bags : int, default=0
        Number of inner bags. 0 turns off inner bagging.
    learning_rate : float, default=0.01
        Learning rate for boosting.
    greediness : float, default=0.0
        Percentage of rounds where boosting is greedy instead of round-robin. Greedy rounds are intermixed with cyclic rounds.
    smoothing_rounds : int, default=0
        Number of initial highly regularized rounds to set the basic shape of the main effect feature graphs.
    max_rounds : int, default=5000
        Total number of boosting rounds with n_terms boosting steps per round.
    early_stopping_rounds : int, default=50
        Number of rounds with no improvement to trigger early stopping. 0 turns off
        early stopping and boosting will occur for exactly max_rounds.
    early_stopping_tolerance : float, default=1e-4
        Tolerance that dictates the smallest delta required to be considered an improvement.
    min_samples_leaf : int, default=2
        Minimum number of samples allowed in the leaves.
    max_leaves : int, default=3
        Maximum number of leaves allowed in each tree.
    objective : str, default="log_loss"
        The objective to optimize.
    n_jobs : int, default=-2
        Number of jobs to run in parallel. Negative integers are interpreted as following joblib\'s formula
        (n_cpus + 1 + n_jobs), just like scikit-learn. Eg: -2 means using all threads except 1.
    random_state : int or None, default=42
        Random state. None uses device_random and generates non-repeatable sequences.

    Attributes
    ----------
    classes\\_ : array of bool, int, or unicode with shape ``(n_classes,)``
        The class labels.
    n_features_in\\_ : int
        Number of features.
    feature_names_in\\_ : List of str
        Resolved feature names. Names can come from feature_names, X, or be auto-generated.
    feature_types_in\\_ : List of str
        Resolved feature types. Can be: \'continuous\', \'nominal\', or \'ordinal\'.
    bins\\_ : List[Union[List[Dict[str, int]], List[array of float with shape ``(n_cuts,)``]]]
        Per-feature list that defines how to bin each feature. Each feature in the list contains
        a list of binning resolutions. The first item in the binning resolution list is for binning
        main effect features. If there are more items in the binning resolution list, they define the
        binning for successive levels of resolutions. The item at index 1, if it exists, defines the
        binning for pairs. The last binning resolution defines the bins for all successive interaction levels.
        If the binning resolution list contains dictionaries, then the feature is either a \'nominal\' or
        \'ordinal\' categorical. If the binning resolution list contains arrays, then the feature is \'continuous\'
        and the arrays will contain float cut points that separate continuous values into bins.
    feature_bounds\\_ : array of float with shape ``(n_features, 2)``
        min/max bounds for each feature. feature_bounds_[feature_index, 0] is the min value of the feature
        and feature_bounds_[feature_index, 1] is the max value of the feature. Categoricals have min & max
        values of NaN.
    histogram_edges\\_ : List of None or array of float with shape ``(n_hist_edges,)``
        Per-feature list of the histogram edges. Categorical features contain None within the List
        at their feature index.
    histogram_weights\\_ : List of array of float with shape ``(n_hist_bins,)``
        Per-feature list of the total sample weights within each feature\'s histogram bins.
    unique_val_counts\\_ : array of int with shape ``(n_features,)``
        Per-feature count of the number of unique feature values.
    term_features\\_ : List of tuples of feature indices
        Additive terms used in the model and their component feature indices.
    term_names\\_ : List of str
        List of term names.
    bin_weights\\_ : List of array of float with shape ``(n_feature0_bins, ..., n_featureN_bins)``
        Per-term list of the total sample weights in each term\'s tensor bins.
    bagged_scores\\_ : List of array of float with shape ``(n_outer_bags, n_feature0_bins, ..., n_featureN_bins, n_classes)`` or ``(n_outer_bags, n_feature0_bins, ..., n_featureN_bins)``
        Per-term list of the bagged model scores.
        The last dimension of length n_classes is dropped for binary classification.
    term_scores\\_ : List of array of float with shape ``(n_feature0_bins, ..., n_featureN_bins, n_classes)`` or ``(n_feature0_bins, ..., n_featureN_bins)``
        Per-term list of the model scores.
        The last dimension of length n_classes is dropped for binary classification.
    standard_deviations\\_ : List of array of float with shape ``(n_feature0_bins, ..., n_featureN_bins, n_classes)`` or ``(n_feature0_bins, ..., n_featureN_bins)``
        Per-term list of the standard deviations of the bagged model scores.
        The last dimension of length n_classes is dropped for binary classification.
    link\\_ : str
        Link function used to convert the predictions or targets into linear space
        additive scores and vice versa via the inverse link. Possible values include:
        "custom_classification", "logit", "probit", "cloglog", "loglog", "cauchit"
    link_param\\_ : float
        Float value that can be used by the link function. For classification it is only used by "custom_classification".
    bag_weights\\_ : array of float with shape ``(n_outer_bags,)``
        Per-bag record of the total weight within each bag.
    breakpoint_iteration\\_ : array of int with shape ``(n_stages, n_outer_bags)``
        The number of boosting rounds performed within each stage until either early stopping, or the max_rounds was reached.
        Normally, the count of main effects boosting rounds will be in breakpoint_iteration_[0],
        and the count of interaction boosting rounds will be in breakpoint_iteration_[1].
    intercept\\_ : array of float with shape ``(n_classes,)`` or ``(1,)``
        Intercept of the model. Binary classification is shape ``(1,)``, and multiclass is shape ``(n_classes,)``.
    '''
    n_features_in_: int
    term_names_: List[str]
    bins_: List[List[Dict[str, int]] | List[np.ndarray]]
    feature_names_in_: List[str]
    feature_types_in_: List[str]
    feature_bounds_: np.ndarray
    term_features_: List[Tuple[int, ...]]
    bin_weights_: List[np.ndarray]
    bagged_scores_: List[np.ndarray]
    term_scores_: List[np.ndarray]
    standard_deviations_: List[np.ndarray]
    link_: str
    link_param_: float
    bag_weights_: np.ndarray
    breakpoint_iteration_: np.ndarray
    histogram_edges_: List[None | np.ndarray]
    histogram_weights_: List[np.ndarray]
    unique_val_counts_: np.ndarray
    classes_: np.ndarray
    intercept_: np.ndarray
    available_explanations: Incomplete
    explainer_type: str
    def __init__(self, feature_names: Sequence[None | str] | None = None, feature_types: Sequence[None | str | Sequence[str] | Sequence[float]] | None = None, max_bins: int = 256, max_interaction_bins: int = 32, interactions: int | float | Sequence[int | str | Sequence[int | str]] | None = 10, exclude: Sequence[int | str | Sequence[int | str]] | None = [], validation_size: int | float | None = 0.15, outer_bags: int = 8, inner_bags: int | None = 0, learning_rate: float = 0.01, greediness: float | None = 0.0, smoothing_rounds: int | None = 0, max_rounds: int | None = 5000, early_stopping_rounds: int | None = 50, early_stopping_tolerance: float | None = 0.0001, min_samples_leaf: int | None = 2, max_leaves: int = 3, objective: str = 'log_loss', n_jobs: int | None = -2, random_state: int | None = 42) -> None: ...
    def predict_proba(self, X, init_score: Incomplete | None = None):
        """Probability estimates on provided samples.

        Args:
            X: Numpy array for samples.
            init_score: Optional. Either a model that can generate scores or per-sample initialization score.
                If samples scores it should be the same length as X.

        Returns:
            Probability estimate of sample for each class.
        """
    def predict(self, X, init_score: Incomplete | None = None):
        """Predicts on provided samples.

        Args:
            X: Numpy array for samples.
            init_score: Optional. Either a model that can generate scores or per-sample initialization score.
                If samples scores it should be the same length as X.

        Returns:
            Predicted class label per sample.
        """
    def predict_and_contrib(self, X, output: str = 'probabilities', init_score: Incomplete | None = None):
        """Predicts on provided samples, returning predictions and explanations for each sample.

        Args:
            X: Numpy array for samples.
            output: Prediction type to output (i.e. one of 'probabilities', 'labels', 'logits')
            init_score: Optional. Either a model that can generate scores or per-sample initialization score.
                If samples scores it should be the same length as X.

        Returns:
            Predictions and local explanations for each sample.
        """

class ExplainableBoostingRegressor(EBMModel, RegressorMixin, ExplainerMixin):
    '''An Explainable Boosting Regressor

    Parameters
    ----------
    feature_names : list of str, default=None
        List of feature names.
    feature_types : list of FeatureType, default=None

        List of feature types. FeatureType can be:

            - `None`: Auto-detect
            - `\'quantile\'`: Continuous with equal density bins
            - `\'rounded_quantile\'`: Continuous with quantile bins, but the cut values are rounded when possible
            - `\'uniform\'`: Continuous with equal width bins
            - `\'winsorized\'`: Continuous with equal width bins, but the leftmost and rightmost cut are chosen by quantiles
            - `\'continuous\'`: Use the default binning for continuous features, which is \'quantile\' currently
            - `[List of float]`: Continuous with specified cut values. Eg: [5.5, 8.75]
            - `[List of str]`: Ordinal categorical where the order has meaning. Eg: ["low", "medium", "high"]
            - `\'ordinal\'`: Ordinal categorical where the order is determined by sorting the feature strings
            - `\'nominal\'`: Categorical where the order has no meaning. Eg: country names
    max_bins : int, default=256
        Max number of bins per feature for the main effects stage.
    max_interaction_bins : int, default=32
        Max number of bins per feature for interaction terms.
    interactions : int, float, or list of tuples of feature indices, default=10

        Interaction terms to be included in the model. Options are:

            - Integer (1 <= interactions): Count of interactions to be automatically selected
            - Percentage (interactions < 1.0): Determine the integer count of interactions by multiplying the number of features by this percentage
            - List of tuples: The tuples contain the indices of the features within the additive term
    exclude : \'mains\' or list of tuples of feature indices|names, default=[]
        Features or terms to be excluded.
    validation_size : int or float, default=0.15

        Validation set size. Used for early stopping during boosting, and is needed to create outer bags.

            - Integer (1 <= validation_size): Count of samples to put in the validation sets
            - Percentage (validation_size < 1.0): Percentage of the data to put in the validation sets
            - 0: Turns off early stopping. Outer bags have no utility. Error bounds will be eliminated
    outer_bags : int, default=8
        Number of outer bags. Outer bags are used to generate error bounds and help with smoothing the graphs.
    inner_bags : int, default=0
        Number of inner bags. 0 turns off inner bagging.
    learning_rate : float, default=0.01
        Learning rate for boosting.
    greediness : float, default=0.0
        Percentage of rounds where boosting is greedy instead of round-robin. Greedy rounds are intermixed with cyclic rounds.
    smoothing_rounds : int, default=0
        Number of initial highly regularized rounds to set the basic shape of the main effect feature graphs.
    max_rounds : int, default=5000
        Total number of boosting rounds with n_terms boosting steps per round.
    early_stopping_rounds : int, default=50
        Number of rounds with no improvement to trigger early stopping. 0 turns off
        early stopping and boosting will occur for exactly max_rounds.
    early_stopping_tolerance : float, default=1e-4
        Tolerance that dictates the smallest delta required to be considered an improvement.
    min_samples_leaf : int, default=2
        Minimum number of samples allowed in the leaves.
    max_leaves : int, default=3
        Maximum number of leaves allowed in each tree.
    objective : str, default="rmse"
        The objective to optimize. Options include: "rmse",
        "poisson_deviance", "tweedie_deviance:variance_power=1.5", "gamma_deviance",
        "pseudo_huber:delta=1.0", "rmse_log" (rmse with a log link function)
    n_jobs : int, default=-2
        Number of jobs to run in parallel. Negative integers are interpreted as following joblib\'s formula
        (n_cpus + 1 + n_jobs), just like scikit-learn. Eg: -2 means using all threads except 1.
    random_state : int or None, default=42
        Random state. None uses device_random and generates non-repeatable sequences.

    Attributes
    ----------
    n_features_in\\_ : int
        Number of features.
    feature_names_in\\_ : List of str
        Resolved feature names. Names can come from feature_names, X, or be auto-generated.
    feature_types_in\\_ : List of str
        Resolved feature types. Can be: \'continuous\', \'nominal\', or \'ordinal\'.
    bins\\_ : List[Union[List[Dict[str, int]], List[array of float with shape ``(n_cuts,)``]]]
        Per-feature list that defines how to bin each feature. Each feature in the list contains
        a list of binning resolutions. The first item in the binning resolution list is for binning
        main effect features. If there are more items in the binning resolution list, they define the
        binning for successive levels of resolutions. The item at index 1, if it exists, defines the
        binning for pairs. The last binning resolution defines the bins for all successive interaction levels.
        If the binning resolution list contains dictionaries, then the feature is either a \'nominal\' or
        \'ordinal\' categorical. If the binning resolution list contains arrays, then the feature is \'continuous\'
        and the arrays will contain float cut points that separate continuous values into bins.
    feature_bounds\\_ : array of float with shape ``(n_features, 2)``
        min/max bounds for each feature. feature_bounds_[feature_index, 0] is the min value of the feature
        and feature_bounds_[feature_index, 1] is the max value of the feature. Categoricals have min & max
        values of NaN.
    histogram_edges\\_ : List of None or array of float with shape ``(n_hist_edges,)``
        Per-feature list of the histogram edges. Categorical features contain None within the List
        at their feature index.
    histogram_weights\\_ : List of array of float with shape ``(n_hist_bins,)``
        Per-feature list of the total sample weights within each feature\'s histogram bins.
    unique_val_counts\\_ : array of int with shape ``(n_features,)``
        Per-feature count of the number of unique feature values.
    term_features\\_ : List of tuples of feature indices
        Additive terms used in the model and their component feature indices.
    term_names\\_ : List of str
        List of term names.
    bin_weights\\_ : List of array of float with shape ``(n_feature0_bins, ..., n_featureN_bins)``
        Per-term list of the total sample weights in each term\'s tensor bins.
    bagged_scores\\_ : List of array of float with shape ``(n_outer_bags, n_feature0_bins, ..., n_featureN_bins)``
        Per-term list of the bagged model scores.
    term_scores\\_ : List of array of float with shape ``(n_feature0_bins, ..., n_featureN_bins)``
        Per-term list of the model scores.
    standard_deviations\\_ : List of array of float with shape ``(n_feature0_bins, ..., n_featureN_bins)``
        Per-term list of the standard deviations of the bagged model scores.
    link\\_ : str
        Link function used to convert the predictions or targets into linear space
        additive scores and vice versa via the inverse link. Possible values include:
        "custom_regression", "power", "identity", "log", "inverse", "inverse_square", "sqrt"
    link_param\\_ : float
        Float value that can be used by the link function. The primary use is for the power link.
    bag_weights\\_ : array of float with shape ``(n_outer_bags,)``
        Per-bag record of the total weight within each bag.
    breakpoint_iteration\\_ : array of int with shape ``(n_stages, n_outer_bags)``
        The number of boosting rounds performed within each stage until either early stopping, or the max_rounds was reached.
        Normally, the count of main effects boosting rounds will be in breakpoint_iteration_[0],
        and the count of interaction boosting rounds will be in breakpoint_iteration_[1].
    intercept\\_ : float
        Intercept of the model.
    min_target\\_ : float
        The minimum value found in \'y\'.
    max_target\\_ : float
        The maximum value found in \'y\'.
    '''
    n_features_in_: int
    term_names_: List[str]
    bins_: List[List[Dict[str, int]] | List[np.ndarray]]
    feature_names_in_: List[str]
    feature_types_in_: List[str]
    feature_bounds_: np.ndarray
    term_features_: List[Tuple[int, ...]]
    bin_weights_: List[np.ndarray]
    bagged_scores_: List[np.ndarray]
    term_scores_: List[np.ndarray]
    standard_deviations_: List[np.ndarray]
    link_: str
    link_param_: float
    bag_weights_: np.ndarray
    breakpoint_iteration_: np.ndarray
    histogram_edges_: List[None | np.ndarray]
    histogram_weights_: List[np.ndarray]
    unique_val_counts_: np.ndarray
    intercept_: float
    min_target_: float
    max_target_: float
    available_explanations: Incomplete
    explainer_type: str
    def __init__(self, feature_names: Sequence[None | str] | None = None, feature_types: Sequence[None | str | Sequence[str] | Sequence[float]] | None = None, max_bins: int = 256, max_interaction_bins: int = 32, interactions: int | float | Sequence[int | str | Sequence[int | str]] | None = 10, exclude: Sequence[int | str | Sequence[int | str]] | None = [], validation_size: int | float | None = 0.15, outer_bags: int = 8, inner_bags: int | None = 0, learning_rate: float = 0.01, greediness: float | None = 0.0, smoothing_rounds: int | None = 0, max_rounds: int | None = 5000, early_stopping_rounds: int | None = 50, early_stopping_tolerance: float | None = 0.0001, min_samples_leaf: int | None = 2, max_leaves: int = 3, objective: str = 'rmse', n_jobs: int | None = -2, random_state: int | None = 42) -> None: ...
    def predict(self, X, init_score: Incomplete | None = None):
        """Predicts on provided samples.

        Args:
            X: Numpy array for samples.
            init_score: Optional. Either a model that can generate scores or per-sample initialization score.
                If samples scores it should be the same length as X.

        Returns:
            Predicted class label per sample.
        """
    def predict_and_contrib(self, X, init_score: Incomplete | None = None):
        """Predicts on provided samples, returning predictions and explanations for each sample.

        Args:
            X: Numpy array for samples.
            init_score: Optional. Either a model that can generate scores or per-sample initialization score.
                If samples scores it should be the same length as X.

        Returns:
            Predictions and local explanations for each sample.
        """

class DPExplainableBoostingClassifier(EBMModel, ClassifierMixin, ExplainerMixin):
    '''Differentially Private Explainable Boosting Classifier. Note that many arguments are defaulted differently than regular EBMs.

    Parameters
    ----------
    feature_names : list of str, default=None
        List of feature names.
    feature_types : list of FeatureType, default=None

        List of feature types. For DP-EBMs, feature_types should be fully specified.
        The auto-detector, if used, examines the data and is not included in the privacy budget.
        If auto-detection is used, a privacy warning will be issued.
        FeatureType can be:

            - `None`: Auto-detect (privacy budget is not respected!).
            - `\'continuous\'`: Use private continuous binning.
            - `[List of str]`: Ordinal categorical where the order has meaning. Eg: ["low", "medium", "high"]. Uses private categorical binning.
            - `\'ordinal\'`: Ordinal categorical where the order is determined by sorting the feature strings. Uses private categorical binning.
            - `\'nominal\'`: Categorical where the order has no meaning. Eg: country names. Uses private categorical binning.
    max_bins : int, default=32
        Max number of bins per feature.
    exclude : list of tuples of feature indices|names, default=[]
        Features to be excluded.
    validation_size : int or float, default=0

        Validation set size. A validation set is needed if outer bags or error bars are desired.

            - Integer (1 <= validation_size): Count of samples to put in the validation sets
            - Percentage (validation_size < 1.0): Percentage of the data to put in the validation sets
            - 0: Outer bags have no utility and error bounds will be eliminated
    outer_bags : int, default=1
        Number of outer bags. Outer bags are used to generate error bounds and help with smoothing the graphs.
    learning_rate : float, default=0.01
        Learning rate for boosting.
    max_rounds : int, default=300
        Total number of boosting rounds with n_terms boosting steps per round.
    max_leaves : int, default=3
        Maximum number of leaves allowed in each tree.
    n_jobs : int, default=-2
        Number of jobs to run in parallel. Negative integers are interpreted as following joblib\'s formula
        (n_cpus + 1 + n_jobs), just like scikit-learn. Eg: -2 means using all threads except 1.
    random_state : int or None, default=None
        Random state. None uses device_random and generates non-repeatable sequences.
        Should be set to \'None\' for privacy, but can be set to an integer for testing and repeatability.
    epsilon: float, default=1.0
        Total privacy budget to be spent.
    delta: float, default=1e-5
        Additive component of differential privacy guarantee. Should be smaller than 1/n_training_samples.
    composition: {\'gdp\', \'classic\'}, default=\'gdp\'
        Method of tracking noise aggregation.
    bin_budget_frac: float, default=0.1
        Percentage of total epsilon budget to use for private binning.
    privacy_bounds: Union[np.ndarray, Mapping[Union[int, str], Tuple[float, float]]], default=None
        Specifies known min/max values for each feature.
        If None, DP-EBM shows a warning and uses the data to determine these values.

    Attributes
    ----------
    classes\\_ : array of bool, int, or unicode with shape ``(2,)``
        The class labels. DPExplainableBoostingClassifier only supports binary classification, so there are 2 classes.
    n_features_in\\_ : int
        Number of features.
    feature_names_in\\_ : List of str
        Resolved feature names. Names can come from feature_names, X, or be auto-generated.
    feature_types_in\\_ : List of str
        Resolved feature types. Can be: \'continuous\', \'nominal\', or \'ordinal\'.
    bins\\_ : List[Union[List[Dict[str, int]], List[array of float with shape ``(n_cuts,)``]]]
        Per-feature list that defines how to bin each feature. Each feature in the list contains
        a list of binning resolutions. The first item in the binning resolution list is for binning
        main effect features. If there are more items in the binning resolution list, they define the
        binning for successive levels of resolutions. The item at index 1, if it exists, defines the
        binning for pairs. The last binning resolution defines the bins for all successive interaction levels.
        If the binning resolution list contains dictionaries, then the feature is either a \'nominal\' or
        \'ordinal\' categorical. If the binning resolution list contains arrays, then the feature is \'continuous\'
        and the arrays will contain float cut points that separate continuous values into bins.
    feature_bounds\\_ : array of float with shape ``(n_features, 2)``
        min/max bounds for each feature. feature_bounds_[feature_index, 0] is the min value of the feature
        and feature_bounds_[feature_index, 1] is the max value of the feature. Categoricals have min & max
        values of NaN.
    term_features\\_ : List of tuples of feature indices
        Additive terms used in the model and their component feature indices.
    term_names\\_ : List of str
        List of term names.
    bin_weights\\_ : List of array of float with shape ``(n_bins)``
        Per-term list of the total sample weights in each term\'s bins.
    bagged_scores\\_ : List of array of float with shape ``(n_outer_bags, n_bins)``
        Per-term list of the bagged model scores.
    term_scores\\_ : List of array of float with shape ``(n_bins)``
        Per-term list of the model scores.
    standard_deviations\\_ : List of array of float with shape ``(n_bins)``
        Per-term list of the standard deviations of the bagged model scores.
    link\\_ : str
        Link function used to convert the predictions or targets into linear space
        additive scores and vice versa via the inverse link. Possible values include:
        "custom_classification", "logit", "probit", "cloglog", "loglog", "cauchit"
    link_param\\_ : float
        Float value that can be used by the link function. For classification it is only used by "custom_classification".
    bag_weights\\_ : array of float with shape ``(n_outer_bags,)``
        Per-bag record of the total weight within each bag.
    breakpoint_iteration\\_ : array of int with shape ``(n_stages, n_outer_bags)``
        The number of boosting rounds performed within each stage. Normally, the count of main effects
        boosting rounds will be in breakpoint_iteration_[0].
    intercept\\_ : array of float with shape ``(1,)``
        Intercept of the model.
    noise_scale_binning\\_ : float
        The noise scale during binning.
    noise_scale_boosting\\_ : float
        The noise scale during boosting.
    '''
    n_features_in_: int
    term_names_: List[str]
    bins_: List[List[Dict[str, int]] | List[np.ndarray]]
    feature_names_in_: List[str]
    feature_types_in_: List[str]
    feature_bounds_: np.ndarray
    term_features_: List[Tuple[int, ...]]
    bin_weights_: List[np.ndarray]
    bagged_scores_: List[np.ndarray]
    term_scores_: List[np.ndarray]
    standard_deviations_: List[np.ndarray]
    link_: str
    link_param_: float
    bag_weights_: np.ndarray
    breakpoint_iteration_: np.ndarray
    noise_scale_binning_: float
    noise_scale_boosting_: float
    classes_: np.ndarray
    intercept_: np.ndarray
    available_explanations: Incomplete
    explainer_type: str
    def __init__(self, feature_names: Sequence[None | str] | None = None, feature_types: Sequence[None | str | Sequence[str] | Sequence[float]] | None = None, max_bins: int = 32, exclude: Sequence[int | str | Sequence[int | str]] | None = [], validation_size: int | float | None = 0, outer_bags: int = 1, learning_rate: float = 0.01, max_rounds: int | None = 300, max_leaves: int = 3, n_jobs: int | None = -2, random_state: int | None = None, epsilon: float = 1.0, delta: float = 1e-05, composition: str = 'gdp', bin_budget_frac: float = 0.1, privacy_bounds: np.ndarray | Mapping[int | str, Tuple[float, float]] | None = None) -> None: ...
    def predict_proba(self, X, init_score: Incomplete | None = None):
        """Probability estimates on provided samples.

        Args:
            X: Numpy array for samples.
            init_score: Optional. Either a model that can generate scores or per-sample initialization score.
                If samples scores it should be the same length as X.

        Returns:
            Probability estimate of sample for each class.
        """
    def predict(self, X, init_score: Incomplete | None = None):
        """Predicts on provided samples.

        Args:
            X: Numpy array for samples.
            init_score: Optional. Either a model that can generate scores or per-sample initialization score.
                If samples scores it should be the same length as X.

        Returns:
            Predicted class label per sample.
        """

class DPExplainableBoostingRegressor(EBMModel, RegressorMixin, ExplainerMixin):
    '''Differentially Private Explainable Boosting Regressor. Note that many arguments are defaulted differently than regular EBMs.

    Parameters
    ----------
    feature_names : list of str, default=None
        List of feature names.
    feature_types : list of FeatureType, default=None

        List of feature types. For DP-EBMs, feature_types should be fully specified.
        The auto-detector, if used, examines the data and is not included in the privacy budget.
        If auto-detection is used, a privacy warning will be issued.
        FeatureType can be:

            - `None`: Auto-detect (privacy budget is not respected!).
            - `\'continuous\'`: Use private continuous binning.
            - `[List of str]`: Ordinal categorical where the order has meaning. Eg: ["low", "medium", "high"]. Uses private categorical binning.
            - `\'ordinal\'`: Ordinal categorical where the order is determined by sorting the feature strings. Uses private categorical binning.
            - `\'nominal\'`: Categorical where the order has no meaning. Eg: country names. Uses private categorical binning.
    max_bins : int, default=32
        Max number of bins per feature.
    exclude : list of tuples of feature indices|names, default=[]
        Features to be excluded.
    validation_size : int or float, default=0

        Validation set size. A validation set is needed if outer bags or error bars are desired.

            - Integer (1 <= validation_size): Count of samples to put in the validation sets
            - Percentage (validation_size < 1.0): Percentage of the data to put in the validation sets
            - 0: Outer bags have no utility and error bounds will be eliminated
    outer_bags : int, default=1
        Number of outer bags. Outer bags are used to generate error bounds and help with smoothing the graphs.
    learning_rate : float, default=0.01
        Learning rate for boosting.
    max_rounds : int, default=300
        Total number of boosting rounds with n_terms boosting steps per round.
    max_leaves : int, default=3
        Maximum number of leaves allowed in each tree.
    n_jobs : int, default=-2
        Number of jobs to run in parallel. Negative integers are interpreted as following joblib\'s formula
        (n_cpus + 1 + n_jobs), just like scikit-learn. Eg: -2 means using all threads except 1.
    random_state : int or None, default=None
        Random state. None uses device_random and generates non-repeatable sequences.
        Should be set to \'None\' for privacy, but can be set to an integer for testing and repeatability.
    epsilon: float, default=1.0
        Total privacy budget to be spent.
    delta: float, default=1e-5
        Additive component of differential privacy guarantee. Should be smaller than 1/n_training_samples.
    composition: {\'gdp\', \'classic\'}, default=\'gdp\'
        Method of tracking noise aggregation.
    bin_budget_frac: float, default=0.1
        Percentage of total epsilon budget to use for private binning.
    privacy_bounds: Union[np.ndarray, Mapping[Union[int, str], Tuple[float, float]]], default=None
        Specifies known min/max values for each feature.
        If None, DP-EBM shows a warning and uses the data to determine these values.
    privacy_target_min: float, default=None
        Known target minimum. \'y\' values will be clipped to this min.
        If None, DP-EBM shows a warning and uses the data to determine this value.
    privacy_target_max: float, default=None
        Known target maximum. \'y\' values will be clipped to this max.
        If None, DP-EBM shows a warning and uses the data to determine this value.

    Attributes
    ----------
    n_features_in\\_ : int
        Number of features.
    feature_names_in\\_ : List of str
        Resolved feature names. Names can come from feature_names, X, or be auto-generated.
    feature_types_in\\_ : List of str
        Resolved feature types. Can be: \'continuous\', \'nominal\', or \'ordinal\'.
    bins\\_ : List[Union[List[Dict[str, int]], List[array of float with shape ``(n_cuts,)``]]]
        Per-feature list that defines how to bin each feature. Each feature in the list contains
        a list of binning resolutions. The first item in the binning resolution list is for binning
        main effect features. If there are more items in the binning resolution list, they define the
        binning for successive levels of resolutions. The item at index 1, if it exists, defines the
        binning for pairs. The last binning resolution defines the bins for all successive interaction levels.
        If the binning resolution list contains dictionaries, then the feature is either a \'nominal\' or
        \'ordinal\' categorical. If the binning resolution list contains arrays, then the feature is \'continuous\'
        and the arrays will contain float cut points that separate continuous values into bins.
    feature_bounds\\_ : array of float with shape ``(n_features, 2)``
        min/max bounds for each feature. feature_bounds_[feature_index, 0] is the min value of the feature
        and feature_bounds_[feature_index, 1] is the max value of the feature. Categoricals have min & max
        values of NaN.
    term_features\\_ : List of tuples of feature indices
        Additive terms used in the model and their component feature indices.
    term_names\\_ : List of str
        List of term names.
    bin_weights\\_ : List of array of float with shape ``(n_bins)``
        Per-term list of the total sample weights in each term\'s bins.
    bagged_scores\\_ : List of array of float with shape ``(n_outer_bags, n_bins)``
        Per-term list of the bagged model scores.
    term_scores\\_ : List of array of float with shape ``(n_bins)``
        Per-term list of the model scores.
    standard_deviations\\_ : List of array of float with shape ``(n_bins)``
        Per-term list of the standard deviations of the bagged model scores.
    link\\_ : str
        Link function used to convert the predictions or targets into linear space
        additive scores and vice versa via the inverse link. Possible values include:
        "custom_regression", "power", "identity", "log", "inverse", "inverse_square", "sqrt"
    link_param\\_ : float
        Float value that can be used by the link function. The primary use is for the power link.
    bag_weights\\_ : array of float with shape ``(n_outer_bags,)``
        Per-bag record of the total weight within each bag.
    breakpoint_iteration\\_ : array of int with shape ``(n_stages, n_outer_bags)``
        The number of boosting rounds performed within each stage. Normally, the count of main effects
        boosting rounds will be in breakpoint_iteration_[0].
    intercept\\_ : float
        Intercept of the model.
    min_target\\_ : float
        The minimum value found in \'y\', or privacy_target_min if provided.
    max_target\\_ : float
        The maximum value found in \'y\', or privacy_target_max if provided.
    noise_scale_binning\\_ : float
        The noise scale during binning.
    noise_scale_boosting\\_ : float
        The noise scale during boosting.
    '''
    n_features_in_: int
    term_names_: List[str]
    bins_: List[List[Dict[str, int]] | List[np.ndarray]]
    feature_names_in_: List[str]
    feature_types_in_: List[str]
    feature_bounds_: np.ndarray
    term_features_: List[Tuple[int, ...]]
    bin_weights_: List[np.ndarray]
    bagged_scores_: List[np.ndarray]
    term_scores_: List[np.ndarray]
    standard_deviations_: List[np.ndarray]
    link_: str
    link_param_: float
    bag_weights_: np.ndarray
    breakpoint_iteration_: np.ndarray
    noise_scale_binning_: float
    noise_scale_boosting_: float
    intercept_: float
    min_target_: float
    max_target_: float
    available_explanations: Incomplete
    explainer_type: str
    def __init__(self, feature_names: Sequence[None | str] | None = None, feature_types: Sequence[None | str | Sequence[str] | Sequence[float]] | None = None, max_bins: int = 32, exclude: Sequence[int | str | Sequence[int | str]] | None = [], validation_size: int | float | None = 0, outer_bags: int = 1, learning_rate: float = 0.01, max_rounds: int | None = 300, max_leaves: int = 3, n_jobs: int | None = -2, random_state: int | None = None, epsilon: float = 1.0, delta: float = 1e-05, composition: str = 'gdp', bin_budget_frac: float = 0.1, privacy_bounds: np.ndarray | Mapping[int | str, Tuple[float, float]] | None = None, privacy_target_min: float | None = None, privacy_target_max: float | None = None) -> None: ...
    def predict(self, X, init_score: Incomplete | None = None):
        """Predicts on provided samples.

        Args:
            X: Numpy array for samples.
            init_score: Optional. Either a model that can generate scores or per-sample initialization score.
                If samples scores it should be the same length as X.

        Returns:
            Predicted class label per sample.
        """
