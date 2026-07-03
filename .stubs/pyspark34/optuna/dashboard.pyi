import bokeh.document
import bokeh.models.widgets
import bokeh.plotting
import optuna.study
import optuna.trial
from _typeshed import Incomplete
from optuna._imports import try_import as try_import
from optuna._study_direction import StudyDirection as StudyDirection
from typing import Any, Dict, List

class _CompleteTrialsWidget:
    trial_ids: Incomplete
    direction: Incomplete
    cds: Incomplete
    best_value: Incomplete
    def __init__(self, trials: List[optuna.trial.FrozenTrial], direction: StudyDirection) -> None: ...
    def create_figure(self) -> bokeh.plotting.Figure: ...
    def update(self, new_trials: List[optuna.trial.FrozenTrial]) -> None: ...

class _AllTrialsWidget:
    cds: Incomplete
    def __init__(self, trials: List[optuna.trial.FrozenTrial]) -> None: ...
    def create_table(self) -> bokeh.models.widgets.DataTable: ...
    def update(self, old_trials: List[optuna.trial.FrozenTrial], new_trials: List[optuna.trial.FrozenTrial]) -> None: ...
    @staticmethod
    def trials_to_dict(trials: List[optuna.trial.FrozenTrial]) -> Dict[str, List[Any]]: ...

class _DashboardApp:
    study: Incomplete
    launch_update_thread: Incomplete
    lock: Incomplete
    def __init__(self, study: optuna.study.Study, launch_update_thread: bool) -> None: ...
    doc: Incomplete
    current_trials: Incomplete
    new_trials: Incomplete
    complete_trials_widget: Incomplete
    all_trials_widget: Incomplete
    stop_event: Incomplete
    def __call__(self, doc: bokeh.document.Document) -> None: ...
    def thread_loop(self) -> None: ...
    def update_callback(self) -> Any: ...
