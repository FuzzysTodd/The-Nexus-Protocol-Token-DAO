from ..public import PanelMetricsHelper as PanelMetricsHelper, Run as Run
from .runset import Runset as Runset
from .util import Attr as Attr, Base as Base, Panel as Panel, nested_get as nested_get, nested_set as nested_set
from _typeshed import Incomplete

class LineKey:
    key: Incomplete
    def __init__(self, key: str) -> None: ...
    def __hash__(self) -> int: ...
    @classmethod
    def from_run(cls, run: Run, metric: str) -> LineKey: ...
    @classmethod
    def from_panel_agg(cls, runset: Runset, panel: Panel, metric: str) -> LineKey: ...
    @classmethod
    def from_runset_agg(cls, runset: Runset, metric: str) -> LineKey: ...

class PCColumn(Base):
    metric: str
    name: str | None
    ascending: bool | None
    log_scale: bool | None
    panel_metrics_helper: Incomplete
    def __init__(self, metric, name: Incomplete | None = None, ascending: Incomplete | None = None, log_scale: Incomplete | None = None, *args, **kwargs) -> None: ...
    @classmethod
    def from_json(cls, spec): ...
