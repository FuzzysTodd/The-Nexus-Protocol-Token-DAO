from typing import Any
from wandb.sdk.launch.sweeps.scheduler import LOG_PREFIX as LOG_PREFIX, RunState as RunState, Scheduler as Scheduler, SweepRun as SweepRun

class SweepScheduler(Scheduler):
    """A controller/agent that populates a Launch RunQueue from a sweeps RunQueue."""
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
