import types
from optuna import distributions as distributions, exceptions as exceptions, importance as importance, integration as integration, logging as logging, multi_objective as multi_objective, pruners as pruners, samplers as samplers, storages as storages, study as study, trial as trial, version as version, visualization as visualization
from optuna.exceptions import TrialPruned as TrialPruned
from optuna.study import Study as Study, copy_study as copy_study, create_study as create_study, delete_study as delete_study, get_all_study_summaries as get_all_study_summaries, load_study as load_study
from optuna.trial import Trial as Trial, create_trial as create_trial
from optuna.version import __version__ as __version__
from typing import Any, TYPE_CHECKING as TYPE_CHECKING

__all__ = ['Study', 'TYPE_CHECKING', 'Trial', 'TrialPruned', '__version__', 'copy_study', 'create_study', 'create_trial', 'delete_study', 'distributions', 'exceptions', 'get_all_study_summaries', 'importance', 'integration', 'load_study', 'logging', 'multi_objective', 'pruners', 'samplers', 'storages', 'study', 'trial', 'version', 'visualization']

class _LazyImport(types.ModuleType):
    """Module wrapper for lazy import.

    This class wraps specified module and lazily import it when they are actually accessed.
    Otherwise, `import optuna` becomes slower because it imports all submodules and
    their dependencies (e.g., bokeh) all at once.
    Within this project's usage, importlib override this module's attribute on the first
    access and the imported submodule is directly accessed from the second access.

    Args:
        name: Name of module to apply lazy import.
    """
    def __init__(self, name: str) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
