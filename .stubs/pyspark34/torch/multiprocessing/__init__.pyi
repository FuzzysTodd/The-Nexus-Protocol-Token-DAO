from multiprocessing import *

__all__ = ['set_sharing_strategy', 'get_sharing_strategy', 'get_all_sharing_strategies']

def set_sharing_strategy(new_strategy) -> None:
    """Sets the strategy for sharing CPU tensors.

    Args:
        new_strategy (str): Name of the selected strategy. Should be one of
            the values returned by :func:`get_all_sharing_strategies()`.
    """
def get_sharing_strategy():
    """Returns the current strategy for sharing CPU tensors."""
def get_all_sharing_strategies():
    """Returns a set of sharing strategies supported on a current system."""
