from .base_channel import BaseChannel as BaseChannel
from .log_utils import LogType as LogType, nni_log as nni_log
from _typeshed import Incomplete

class WebChannel(BaseChannel):
    node_id: Incomplete
    args: Incomplete
    client: Incomplete
    in_cache: bytes
    timeout: int
    def __init__(self, args) -> None: ...
