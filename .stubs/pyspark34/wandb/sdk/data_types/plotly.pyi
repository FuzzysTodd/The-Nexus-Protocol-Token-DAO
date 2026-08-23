import matplotlib
import plotly
from ..wandb_run import Run as LocalRun
from ._private import MEDIA_TMP as MEDIA_TMP
from .base_types.media import Media as Media
from .base_types.wb_value import WBValue as WBValue
from .image import Image as Image
from _typeshed import Incomplete
from wandb import util as util
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.lib import runid as runid

ValToJsonType: Incomplete

class Plotly(Media):
    """Wandb class for plotly plots.

    Arguments:
        val: matplotlib or plotly figure
    """
    @classmethod
    def make_plot_media(cls, val: plotly.Figure | matplotlib.artist.Artist) -> Image | Plotly: ...
    def __init__(self, val: plotly.Figure | matplotlib.artist.Artist) -> None: ...
    @classmethod
    def get_media_subdir(cls) -> str: ...
    def to_json(self, run_or_artifact: LocalRun | Artifact) -> dict: ...
