import threading
from ..core import Format as Format, image_as_uint as image_as_uint
from _typeshed import Incomplete

logger: Incomplete
CAM_FORMAT: str

def download(directory: Incomplete | None = None, force_download: bool = False) -> None: ...
def get_exe():
    """Wrapper for imageio_ffmpeg.get_ffmpeg_exe()"""

class FfmpegFormat(Format):
    """Read/Write ImageResources using FFMPEG.

    See :mod:`imageio.plugins.ffmpeg`
    """
    class Reader(Format.Reader):
        def count_frames(self):
            """Count the number of frames. Note that this can take a few
            seconds for large files. Also note that it counts the number
            of frames in the original video and does not take a given fps
            into account.
            """
    class Writer(Format.Writer):
        def set_meta_data(self, meta) -> None: ...

class FrameCatcher(threading.Thread):
    """Thread to keep reading the frame data from stdout. This is
    useful when streaming from a webcam. Otherwise, if the user code
    does not grab frames fast enough, the buffer will fill up, leading
    to lag, and ffmpeg can also stall (experienced on Linux). The
    get_frame() method always returns the last available image.
    """
    daemon: bool
    def __init__(self, gen) -> None: ...
    def stop_me(self) -> None: ...
    def get_frame(self): ...
    def run(self) -> None: ...

def parse_device_names(ffmpeg_output):
    """Parse the output of the ffmpeg -list-devices command"""
