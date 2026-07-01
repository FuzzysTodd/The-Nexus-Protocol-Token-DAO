from .base_channel import BaseChannel as BaseChannel
from .log_utils import LogType as LogType, nni_log as nni_log
from _typeshed import Incomplete

class AMLChannel(BaseChannel):
    args: Incomplete
    run: Incomplete
    current_message_index: int
    def __init__(self, args) -> None: ...
