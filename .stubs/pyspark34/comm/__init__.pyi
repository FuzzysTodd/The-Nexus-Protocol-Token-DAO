from .base_comm import BaseComm
from _typeshed import Incomplete

__all__ = ['create_comm', 'get_comm_manager', '__version__']

__version__: str

class DummyComm(BaseComm):
    def publish_msg(self, msg_type, data: Incomplete | None = None, metadata: Incomplete | None = None, buffers: Incomplete | None = None, **keys) -> None: ...

create_comm: Incomplete
get_comm_manager: Incomplete
