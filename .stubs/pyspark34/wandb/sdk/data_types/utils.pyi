from ..wandb_run import Run as LocalRun
from .base_types.media import BatchableMedia as BatchableMedia, Media as Media
from .base_types.wb_value import WBValue as WBValue
from .plotly import Plotly as Plotly
from _typeshed import Incomplete
from typing import Sequence
from wandb import util as util

ValToJsonType: Incomplete

def history_dict_to_json(run: LocalRun | None, payload: dict, step: int | None = None, ignore_copy_err: bool | None = None) -> dict: ...
def val_to_json(run: LocalRun | None, key: str, val: ValToJsonType, namespace: str | int | None = None, ignore_copy_err: bool | None = None) -> Sequence | dict: ...
