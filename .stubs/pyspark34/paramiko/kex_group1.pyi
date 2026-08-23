from _typeshed import Incomplete
from hashlib import sha1
from paramiko import util as util
from paramiko.common import byte_chr as byte_chr, byte_mask as byte_mask, max_byte as max_byte, zero_byte as zero_byte
from paramiko.message import Message as Message
from paramiko.ssh_exception import SSHException as SSHException

c_MSG_KEXDH_INIT: Incomplete
c_MSG_KEXDH_REPLY: Incomplete
b7fffffffffffffff: Incomplete
b0000000000000000: Incomplete

class KexGroup1:
    P: int
    G: int
    name: str
    hash_algo = sha1
    transport: Incomplete
    x: int
    e: int
    f: int
    def __init__(self, transport) -> None: ...
    def start_kex(self) -> None: ...
    def parse_next(self, ptype, m): ...
