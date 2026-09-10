from . import _dtypes
from ..wandb_run import Run as LocalRun
from ._private import MEDIA_TMP as MEDIA_TMP
from .base_types.media import BatchableMedia as BatchableMedia
from _typeshed import Incomplete
from typing import Sequence, TextIO
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.lib import filesystem as filesystem, runid as runid

class Html(BatchableMedia):
    """Wandb class for arbitrary html.

    Arguments:
        data: (string or io object) HTML to display in wandb
        inject: (boolean) Add a stylesheet to the HTML object.  If set
            to False the HTML will pass through unchanged.
    """
    html: Incomplete
    def __init__(self, data: str | TextIO, inject: bool = True) -> None: ...
    def inject_head(self) -> None: ...
    @classmethod
    def get_media_subdir(cls) -> str: ...
    def to_json(self, run_or_artifact: LocalRun | Artifact) -> dict: ...
    @classmethod
    def from_json(cls, json_obj: dict, source_artifact: Artifact) -> Html: ...
    @classmethod
    def seq_to_json(cls, seq: Sequence['BatchableMedia'], run: LocalRun, key: str, step: int | str) -> dict: ...

class _HtmlFileType(_dtypes.Type):
    name: str
    types: Incomplete
