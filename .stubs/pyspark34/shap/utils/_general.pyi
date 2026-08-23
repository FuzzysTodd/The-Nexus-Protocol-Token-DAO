from _typeshed import Incomplete
from collections.abc import Generator

import_errors: Incomplete

def assert_import(package_name) -> None: ...
def record_import_error(package_name, msg, e) -> None: ...
def shapley_coefficients(n): ...
def convert_name(ind, shap_values, input_names): ...
def potential_interactions(shap_values_column, shap_values_matrix):
    """ Order other features by how much interaction they seem to have with the feature at the given index.

    This just bins the SHAP values for a feature along that feature's value. For true Shapley interaction
    index values for SHAP see the interaction_contribs option implemented in XGBoost.
    """
def approximate_interactions(index, shap_values, X, feature_names: Incomplete | None = None):
    """ Order other features by how much interaction they seem to have with the feature at the given index.

    This just bins the SHAP values for a feature along that feature's value. For true Shapley interaction
    index values for SHAP see the interaction_contribs option implemented in XGBoost.
    """
def encode_array_if_needed(arr, dtype=...): ...
def sample(X, nsamples: int = 100, random_state: int = 0): ...
def safe_isinstance(obj, class_path_str):
    """
    Acts as a safe version of isinstance without having to explicitly
    import packages which may not exist in the users environment.

    Checks if obj is an instance of type specified by class_path_str.

    Parameters
    ----------
    obj: Any
        Some object you want to test against
    class_path_str: str or list
        A string or list of strings specifying full class paths
        Example: `sklearn.ensemble.RandomForestRegressor`

    Returns
    --------
    bool: True if isinstance is true and the package exists, False otherwise
    """
def format_value(s, format_str):
    """ Strips trailing zeros and uses a unicode minus sign.
    """
def ordinal_str(n):
    """ Converts a number to and ordinal string.
    """

class OpChain:
    """ A way to represent a set of dot chained operations on an object without actually running them.
    """
    def __init__(self, root_name: str = '') -> None: ...
    def apply(self, obj):
        """ Applies all our ops to the given object.
        """
    def __call__(self, *args, **kwargs):
        """ Update the args for the previous operation.
        """
    def __getitem__(self, item): ...
    def __getattr__(self, name): ...

def suppress_stderr() -> Generator[None, None, None]: ...
