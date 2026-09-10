import io
from ..constants import HF_HUB_DISABLE_PROGRESS_BARS as HF_HUB_DISABLE_PROGRESS_BARS
from pathlib import Path
from tqdm.auto import tqdm as old_tqdm
from typing import Iterator

def disable_progress_bars() -> None:
    """
    Disable globally progress bars used in `huggingface_hub` except if `HF_HUB_DISABLE_PROGRESS_BARS` environment
    variable has been set.

    Use [`~utils.enable_progress_bars`] to re-enable them.
    """
def enable_progress_bars() -> None:
    """
    Enable globally progress bars used in `huggingface_hub` except if `HF_HUB_DISABLE_PROGRESS_BARS` environment
    variable has been set.

    Use [`~utils.disable_progress_bars`] to disable them.
    """
def are_progress_bars_disabled() -> bool:
    """Return whether progress bars are globally disabled or not.

    Progress bars used in `huggingface_hub` can be enable or disabled globally using [`~utils.enable_progress_bars`]
    and [`~utils.disable_progress_bars`] or by setting `HF_HUB_DISABLE_PROGRESS_BARS` as environment variable.
    """

class tqdm(old_tqdm):
    """
    Class to override `disable` argument in case progress bars are globally disabled.

    Taken from https://github.com/tqdm/tqdm/issues/619#issuecomment-619639324.
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def __delattr__(self, attr: str) -> None:
        """Fix for https://github.com/huggingface/huggingface_hub/issues/1603"""

def tqdm_stream_file(path: Path | str) -> Iterator[io.BufferedReader]:
    '''
    Open a file as binary and wrap the `read` method to display a progress bar when it\'s streamed.

    First implemented in `transformers` in 2019 but removed when switched to git-lfs. Used in `huggingface_hub` to show
    progress bar when uploading an LFS file to the Hub. See github.com/huggingface/transformers/pull/2078#discussion_r354739608
    for implementation details.

    Note: currently implementation handles only files stored on disk as it is the most common use case. Could be
          extended to stream any `BinaryIO` object but we might have to debug some corner cases.

    Example:
    ```py
    >>> with tqdm_stream_file("config.json") as f:
    >>>     requests.put(url, data=f)
    config.json: 100%|█████████████████████████| 8.19k/8.19k [00:02<00:00, 3.72kB/s]
    ```
    '''
