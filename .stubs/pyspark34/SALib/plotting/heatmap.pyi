from _typeshed import Incomplete
from typing import Dict

__all__ = ['heatmap']

def heatmap(sp: Dict, metric: str, index: str, title: str = None, ax: Incomplete | None = None):
    """Plot a heatmap of the target metric.

    Parameters
    ----------
    sp : object, SALib ProblemSpec
    metric : str, metric to plot. Defaults to first metric/result output if `None`.
    index : str, sensitivity indices to plot ('S1', 'ST', etc). Displays all if `None`.
    title : str, plot title to use
    ax : axes object, matplotlib axes object to assign figure to.

    Returns
    -------
    ax : matplotlib axes object
    """
