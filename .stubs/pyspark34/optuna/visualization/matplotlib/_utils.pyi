__all__ = ['is_available']

def is_available() -> bool:
    """Returns whether visualization with Matplotlib is available or not.

    .. note::

        :mod:`~optuna.visualization.matplotlib` module depends on Matplotlib version 3.0.0 or
        higher. If a supported version of Matplotlib isn't installed in your environment, this
        function will return :obj:`False`. In such a case, please execute ``$ pip install -U
        matplotlib>=3.0.0`` to install Matplotlib.

    Returns:
        :obj:`True` if visualization with Matplotlib is available, :obj:`False` otherwise.
    """
