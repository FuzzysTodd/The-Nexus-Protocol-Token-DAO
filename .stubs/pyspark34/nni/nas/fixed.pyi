from .utils import ContextStack as ContextStack
from collections.abc import Generator
from pathlib import Path
from typing import Any, Dict

def fixed_arch(fixed_arch: str | Path | Dict[str, Any], verbose: bool = True):
    """
    Load architecture from ``fixed_arch`` and apply to model. This should be used as a context manager. For example,

    .. code-block:: python

        with fixed_arch('/path/to/export.json'):
            model = Model(3, 224, 224)

    Parameters
    ----------
    fixed_arc : str, Path or dict
        Path to the JSON that stores the architecture, or dict that stores the exported architecture.
    verbose : bool
        Print log messages if set to True

    Returns
    -------
    ContextStack
        Context manager that provides a fixed architecture when creates the model.
    """
def no_fixed_arch() -> Generator[None, None, None]:
    """
    Ignore the ``fixed_arch()`` context.

    This is useful in creating a search space within a ``fixed_arch()`` context.
    Under the hood, it only disables the most recent one fixed context, which means,
    if it's currently in a nested with-fixed-arch context, multiple ``no_fixed_arch()`` contexts is required.

    Examples
    --------
    >>> with fixed_arch(arch_dict):
    ...     with no_fixed_arch():
    ...         model_space = ModelSpace()
    """
