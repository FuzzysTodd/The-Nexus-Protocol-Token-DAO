import wandb
from _typeshed import Incomplete
from typing import List

FileSubtypes: Incomplete

class RunQueueItemFileSaver:
    run_queue_item_id: Incomplete
    run: Incomplete
    def __init__(self, agent_run: wandb.sdk.wandb_run.Run | wandb.sdk.lib.RunDisabled | None, run_queue_item_id: str) -> None: ...
    def save_contents(self, contents: str, fname: str, file_sub_type: FileSubtypes) -> List[str] | None: ...
