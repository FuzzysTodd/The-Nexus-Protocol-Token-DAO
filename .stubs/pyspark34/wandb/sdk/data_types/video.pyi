import numpy as np
from . import _dtypes
from ..wandb_run import Run as LocalRun
from ._private import MEDIA_TMP as MEDIA_TMP
from .base_types.media import BatchableMedia as BatchableMedia
from _typeshed import Incomplete
from io import BytesIO
from typing import Any, Sequence, TextIO
from wandb import util as util
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.lib import filesystem as filesystem, runid as runid

def write_gif_with_image_io(clip: Any, filename: str, fps: int | None = None) -> None: ...

class Video(BatchableMedia):
    '''Format a video for logging to W&B.

    Arguments:
        data_or_path: (numpy array, string, io)
            Video can be initialized with a path to a file or an io object.
            The format must be "gif", "mp4", "webm" or "ogg".
            The format must be specified with the format argument.
            Video can be initialized with a numpy tensor.
            The numpy tensor must be either 4 dimensional or 5 dimensional.
            Channels should be (time, channel, height, width) or
            (batch, time, channel, height width)
        caption: (string) caption associated with the video for display
        fps: (int) frames per second for video. Default is 4.
        format: (string) format of video, necessary if initializing with path or io object.

    Examples:
        ### Log a numpy array as a video
        <!--yeadoc-test:log-video-numpy-->
        ```python
        import numpy as np
        import wandb

        wandb.init()
        # axes are (time, channel, height, width)
        frames = np.random.randint(low=0, high=256, size=(10, 3, 100, 100), dtype=np.uint8)
        wandb.log({"video": wandb.Video(frames, fps=4)})
        ```
    '''
    EXTS: Incomplete
    data: Incomplete
    def __init__(self, data_or_path: np.ndarray | str | TextIO | BytesIO, caption: str | None = None, fps: int = 4, format: str | None = None) -> None: ...
    def encode(self) -> None: ...
    @classmethod
    def get_media_subdir(cls) -> str: ...
    def to_json(self, run_or_artifact: LocalRun | Artifact) -> dict: ...
    @classmethod
    def seq_to_json(cls, seq: Sequence['BatchableMedia'], run: LocalRun, key: str, step: int | str) -> dict: ...

class _VideoFileType(_dtypes.Type):
    name: str
    types: Incomplete
