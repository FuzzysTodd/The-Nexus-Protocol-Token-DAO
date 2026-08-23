from pip._internal.utils.logging import get_indentation as get_indentation
from pip._vendor.rich.progress import BarColumn as BarColumn, DownloadColumn as DownloadColumn, FileSizeColumn as FileSizeColumn, Progress as Progress, ProgressColumn as ProgressColumn, SpinnerColumn as SpinnerColumn, TextColumn as TextColumn, TimeElapsedColumn as TimeElapsedColumn, TimeRemainingColumn as TimeRemainingColumn, TransferSpeedColumn as TransferSpeedColumn
from typing import Callable, Iterable, Iterator

DownloadProgressRenderer = Callable[[Iterable[bytes]], Iterator[bytes]]

def get_download_progress_renderer(*, bar_type: str, size: int | None = None) -> DownloadProgressRenderer:
    '''Get an object that can be used to render the download progress.

    Returns a callable, that takes an iterable to "wrap".
    '''
