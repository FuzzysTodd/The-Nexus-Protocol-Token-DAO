__all__ = ['is_available']

def is_available() -> bool:
    """Returns whether visualization with plotly is available or not.

    .. note::

        :mod:`~optuna.visualization` module depends on plotly version 4.0.0 or higher. If a
        supported version of plotly isn't installed in your environment, this function will return
        :obj:`False`. In such case, please execute ``$ pip install -U plotly>=4.0.0`` to install
        plotly.

    Returns:
        :obj:`True` if visualization with plotly is available, :obj:`False` otherwise.
    """
