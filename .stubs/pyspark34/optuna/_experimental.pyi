from optuna.exceptions import ExperimentalWarning as ExperimentalWarning
from typing import Any

def experimental(version: str, name: str | None = None) -> Any:
    """Decorate class or function as experimental.

    Args:
        version: The first version that supports the target feature.
        name: The name of the feature. Defaults to the function or class name. Optional.
    """
