from _typeshed import Incomplete
from argparse import Namespace, _SubParsersAction
from huggingface_hub import logging as logging
from huggingface_hub._commit_scheduler import CommitScheduler as CommitScheduler
from huggingface_hub.commands import BaseHuggingfaceCLICommand as BaseHuggingfaceCLICommand
from huggingface_hub.constants import HF_HUB_ENABLE_HF_TRANSFER as HF_HUB_ENABLE_HF_TRANSFER
from huggingface_hub.hf_api import HfApi as HfApi
from huggingface_hub.utils import disable_progress_bars as disable_progress_bars, enable_progress_bars as enable_progress_bars

logger: Incomplete

class UploadCommand(BaseHuggingfaceCLICommand):
    @staticmethod
    def register_subcommand(parser: _SubParsersAction): ...
    repo_id: Incomplete
    repo_type: Incomplete
    revision: Incomplete
    private: Incomplete
    include: Incomplete
    exclude: Incomplete
    delete: Incomplete
    commit_message: Incomplete
    commit_description: Incomplete
    create_pr: Incomplete
    api: Incomplete
    quiet: Incomplete
    every: Incomplete
    local_path: Incomplete
    path_in_repo: Incomplete
    def __init__(self, args: Namespace) -> None: ...
    def run(self) -> None: ...
