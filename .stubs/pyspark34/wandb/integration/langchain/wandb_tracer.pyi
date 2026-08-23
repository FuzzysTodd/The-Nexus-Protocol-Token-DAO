from _typeshed import Incomplete
from langchain.callbacks.tracers import WandbTracer
from wandb.sdk.lib import deprecate as deprecate

langchain: Incomplete

class WandbTracer(WandbTracer):
    def __init__(self, *args, **kwargs) -> None: ...
