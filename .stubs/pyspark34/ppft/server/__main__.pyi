import hashlib
import ppft as pp
from _typeshed import Incomplete

copyright: Incomplete
__version__: Incomplete
version: Incomplete
LISTEN_SOCKET_TIMEOUT: int
STAT_SIGNAL: Incomplete
sha_new = hashlib.sha1

class _NetworkServer(pp.Server):
    """Network Server Class
    """
    host: Incomplete
    bcast: Incomplete
    port: Incomplete
    timeout: Incomplete
    ncon: int
    last_con_time: Incomplete
    ncon_lock: Incomplete
    def __init__(self, ncpus: str = 'autodetect', interface: str = '0.0.0.0', broadcast: str = '255.255.255.255', port: Incomplete | None = None, secret: Incomplete | None = None, timeout: Incomplete | None = None, restart: bool = False, proto: int = 2, socket_timeout: int = 3600, pid_file: Incomplete | None = None) -> None: ...
    def ncon_add(self, val) -> None:
        """Keeps track of the number of connections and time of the last one"""
    def check_timeout(self) -> None:
        """Checks if timeout happened and shutdowns server if it did"""
    ssocket: Incomplete
    def listen(self) -> None:
        """Initiates listenting to incoming connections"""
    def crun(self, csocket) -> None:
        """Authenticates client and handles its jobs"""
    def broadcast(self) -> None:
        """Initiaates auto-discovery mechanism"""

def parse_config(file_loc):
    """
    Parses a config file in a very forgiving way.
    """
def print_usage() -> None:
    """Prints help"""
def create_network_server(argv): ...
def signal_handler(signum, stack) -> None: ...
