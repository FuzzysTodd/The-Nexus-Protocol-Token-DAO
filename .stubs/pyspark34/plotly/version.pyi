from ._version import get_versions as get_versions
from ._widget_version import __frontend_version__ as __frontend_version__
from _typeshed import Incomplete

__version__: Incomplete

def stable_semver():
    """
    Get the stable portion of the semantic version string (the first three
    numbers), without any of the trailing labels

    '3.0.0rc11' -> '3.0.0'
    """
