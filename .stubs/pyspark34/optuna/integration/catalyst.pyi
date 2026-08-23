from catalyst.dl import OptunaPruningCallback
from optuna._deprecated import deprecated as deprecated
from optuna._imports import try_import as try_import

OptunaPruningCallback = object

class CatalystPruningCallback(OptunaPruningCallback):
    """Catalyst callback to prune unpromising trials.

    This class is an alias to Catalyst's
    `OptunaPruningCallback <https://catalyst-team.github.io/catalyst/api/callbacks.html?highlight=optuna#catalyst.callbacks.optuna.OptunaPruningCallback>`_.

    See the Catalyst's documentation for the detailed description.
    """
