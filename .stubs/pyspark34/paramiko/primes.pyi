from _typeshed import Incomplete
from paramiko import util as util
from paramiko.common import byte_mask as byte_mask
from paramiko.ssh_exception import SSHException as SSHException

class ModulusPack:
    """
    convenience object for holding the contents of the /etc/ssh/moduli file,
    on systems that have such a file.
    """
    pack: Incomplete
    discarded: Incomplete
    def __init__(self) -> None: ...
    def read_file(self, filename) -> None:
        """
        :raises IOError: passed from any file operations that fail.
        """
    def get_modulus(self, min, prefer, max): ...
