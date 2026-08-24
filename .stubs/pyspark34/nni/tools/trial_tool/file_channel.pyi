from .base_channel import BaseChannel as BaseChannel
from _typeshed import Incomplete

command_path: str
runner_commands_file_name_prefix: str
manager_commands_file_name: str

class FileChannel(BaseChannel):
    node_id: Incomplete
    out_file: Incomplete
    in_file: Incomplete
    in_offset: int
    in_cache: bytes
    def __init__(self, args) -> None: ...
