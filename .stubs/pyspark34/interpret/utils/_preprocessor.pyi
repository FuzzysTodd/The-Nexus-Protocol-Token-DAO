from ._clean_simple import clean_dimensions as clean_dimensions
from ._clean_x import preclean_X as preclean_X, unify_columns as unify_columns, unify_feature_names as unify_feature_names
from ._native import Native as Native
from ._privacy import calc_classic_noise_multi as calc_classic_noise_multi, calc_gdp_noise_multi as calc_gdp_noise_multi, private_categorical_binning as private_categorical_binning, private_numeric_binning as private_numeric_binning, validate_eps_delta as validate_eps_delta
from ._seed import increment_seed as increment_seed, normalize_initial_seed as normalize_initial_seed
from _typeshed import Incomplete
from sklearn.base import BaseEstimator, TransformerMixin

class EBMPreprocessor(BaseEstimator, TransformerMixin):
    """Transformer that preprocesses data to be ready before EBM."""
    feature_names: Incomplete
    feature_types: Incomplete
    max_bins: Incomplete
    binning: Incomplete
    min_samples_bin: Incomplete
    min_unique_continuous: Incomplete
    random_state: Incomplete
    epsilon: Incomplete
    delta: Incomplete
    composition: Incomplete
    privacy_bounds: Incomplete
    def __init__(self, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, max_bins: int = 256, binning: str = 'quantile', min_samples_bin: int = 1, min_unique_continuous: int = 0, random_state: Incomplete | None = None, epsilon: Incomplete | None = None, delta: Incomplete | None = None, composition: Incomplete | None = None, privacy_bounds: Incomplete | None = None) -> None:
        '''Initializes EBM preprocessor.

        Args:
            feature_names: Feature names as list.
            feature_types: Feature types as list, for example "continuous" or "nominal".
            max_bins: Max number of bins to process numeric features.
            binning: Strategy to compute bins: "quantile", "rounded_quantile", "uniform", or "private".
            min_samples_bin: minimum number of samples to put into a quantile or rounded_quantile bin
            min_unique_continuous: number of unique numbers required before a feature is considered continuous
            random_state: Random state.
            epsilon: Privacy budget parameter. Only applicable when binning is "private".
            delta: Privacy budget parameter. Only applicable when binning is "private".
            composition: Method of tracking noise aggregation. Must be one of \'classic\' or \'gdp\'.
            privacy_bounds: User specified min/max values for numeric features. Only applicable when binning is "private".
        '''
    feature_names_in_: Incomplete
    feature_types_in_: Incomplete
    bins_: Incomplete
    bin_weights_: Incomplete
    feature_bounds_: Incomplete
    histogram_weights_: Incomplete
    missing_val_counts_: Incomplete
    unique_val_counts_: Incomplete
    noise_scale_: Incomplete
    has_fitted_: bool
    def fit(self, X, y: Incomplete | None = None, sample_weight: Incomplete | None = None):
        """Fits transformer to provided samples.

        Args:
            X: Numpy array for training samples.
            y: Unused. Only included for scikit-learn compatibility
            sample_weight: Per-sample weights

        Returns:
            Itself.
        """
    def transform(self, X):
        """Transform on provided samples.

        Args:
            X: Numpy array for samples.

        Returns:
            Transformed numpy array.
        """
    def fit_transform(self, X, y: Incomplete | None = None, sample_weight: Incomplete | None = None):
        """Fits and Transform on provided samples.

        Args:
            X: Numpy array for samples.
            y: Unused. Only included for scikit-learn compatibility
            sample_weight: Per-sample weights

        Returns:
            Transformed numpy array.
        """

def construct_bins(X, y, sample_weight, feature_names_given, feature_types_given, max_bins_leveled, binning: str = 'quantile', min_samples_bin: int = 1, min_unique_continuous: int = 0, random_state: Incomplete | None = None, epsilon: Incomplete | None = None, delta: Incomplete | None = None, composition: Incomplete | None = None, privacy_bounds: Incomplete | None = None): ...
