from _typeshed import Incomplete
from nni.tuner import Tuner

__all__ = ['GridSearchTuner']

class GridSearchTuner(Tuner):
    """
    Grid search tuner divides search space into evenly spaced grid, and performs brute-force traverse.

    Recommended when the search space is small, or if you want to find strictly optimal hyperparameters.

    **Implementation**

    The original grid search approach performs an exhaustive search through a space consists of ``choice`` and ``randint``.

    NNI's implementation extends grid search to support all search spaces types.

    When the search space contains continuous parameters like ``normal`` and ``loguniform``,
    grid search tuner works in following steps:

    1. Divide the search space into a grid.
    2. Perform an exhaustive searth through the grid.
    3. Subdivide the grid into a finer-grained new grid.
    4. Goto step 2, until experiment end.

    As a deterministic algorithm, grid search has no argument.

    Examples
    --------

    .. code-block::

        config.tuner.name = 'GridSearch'
    """
    space: Incomplete
    grid: Incomplete
    vector: Incomplete
    epoch_bar: Incomplete
    divisions: Incomplete
    history: Incomplete
    def __init__(self, optimize_mode: Incomplete | None = None) -> None: ...
    def update_search_space(self, space) -> None: ...
    def generate_parameters(self, *args, **kwargs): ...
    def receive_trial_result(self, *args, **kwargs) -> None: ...
    def import_data(self, data) -> None: ...
