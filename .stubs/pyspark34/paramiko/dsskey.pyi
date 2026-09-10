from _typeshed import Incomplete
from paramiko import util as util
from paramiko.ber import BER as BER, BERException as BERException
from paramiko.common import zero_byte as zero_byte
from paramiko.message import Message as Message
from paramiko.pkey import PKey as PKey
from paramiko.ssh_exception import SSHException as SSHException

class DSSKey(PKey):
    """
    Representation of a DSS key which can be used to sign an verify SSH2
    data.
    """
    name: str
    p: Incomplete
    q: Incomplete
    g: Incomplete
    y: Incomplete
    x: Incomplete
    public_blob: Incomplete
    size: Incomplete
    def __init__(self, msg: Incomplete | None = None, data: Incomplete | None = None, filename: Incomplete | None = None, password: Incomplete | None = None, vals: Incomplete | None = None, file_obj: Incomplete | None = None) -> None: ...
    def asbytes(self): ...
    def get_name(self): ...
    def get_bits(self): ...
    def can_sign(self): ...
    def sign_ssh_data(self, data, algorithm: Incomplete | None = None): ...
    def verify_ssh_sig(self, data, msg): ...
    def write_private_key_file(self, filename, password: Incomplete | None = None) -> None: ...
    def write_private_key(self, file_obj, password: Incomplete | None = None) -> None: ...
    @staticmethod
    def generate(bits: int = 1024, progress_func: Incomplete | None = None):
        """
        Generate a new private DSS key.  This factory function can be used to
        generate a new host key or authentication key.

        :param int bits: number of bits the generated key should be.
        :param progress_func: Unused
        :return: new `.DSSKey` private key
        """
