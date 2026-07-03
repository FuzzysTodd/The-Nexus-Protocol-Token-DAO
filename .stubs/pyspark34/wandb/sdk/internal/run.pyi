from .. import wandb_run as wandb_run

class InternalRun(wandb_run.Run):
    def __init__(self, run_obj, settings, datatypes_cb) -> None: ...
