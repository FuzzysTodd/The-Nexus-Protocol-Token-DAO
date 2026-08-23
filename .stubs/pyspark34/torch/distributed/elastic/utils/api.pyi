import socket
from typing import Any, List

def get_env_variable_or_raise(env_name: str) -> str:
    """
    Tries to retrieve environment variable. Raises ``ValueError``
    if no environment variable found.

    Args:
        env_name (str): Name of the env variable
    """
def get_socket_with_port() -> socket.socket: ...

class macros:
    """
    Defines simple macros for caffe2.distributed.launch cmd args substitution
    """
    local_rank: str
    @staticmethod
    def substitute(args: List[Any], local_rank: str) -> List[str]: ...
