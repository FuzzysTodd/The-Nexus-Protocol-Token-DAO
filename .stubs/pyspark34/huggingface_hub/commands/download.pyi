from _typeshed import Incomplete
from argparse import Namespace, _SubParsersAction
from huggingface_hub import logging as logging
from huggingface_hub._snapshot_download import snapshot_download as snapshot_download
from huggingface_hub.commands import BaseHuggingfaceCLICommand as BaseHuggingfaceCLICommand
from huggingface_hub.constants import HF_HUB_ENABLE_HF_TRANSFER as HF_HUB_ENABLE_HF_TRANSFER
from huggingface_hub.file_download import hf_hub_download as hf_hub_download
from huggingface_hub.utils import disable_progress_bars as disable_progress_bars, enable_progress_bars as enable_progress_bars

logger: Incomplete

class DownloadCommand(BaseHuggingfaceCLICommand):
    @staticmethod
    def register_subcommand(parser: _SubParsersAction): ...
    token: Incomplete
    repo_id: Incomplete
    filenames: Incomplete
    repo_type: Incomplete
    revision: Incomplete
    include: Incomplete
    exclude: Incomplete
    cache_dir: Incomplete
    local_dir: Incomplete
    force_download: Incomplete
    resume_download: Incomplete
    quiet: Incomplete
    local_dir_use_symlinks: Incomplete
    def __init__(self, args: Namespace) -> None: ...
    def run(self) -> None: ...
