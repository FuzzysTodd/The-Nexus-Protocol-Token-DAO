from _typeshed import Incomplete
from hashlib import sha1, sha256
from paramiko import util as util
from paramiko.common import DEBUG as DEBUG, byte_chr as byte_chr, byte_mask as byte_mask, byte_ord as byte_ord
from paramiko.message import Message as Message
from paramiko.ssh_exception import SSHException as SSHException

c_MSG_KEXDH_GEX_REQUEST_OLD: Incomplete
c_MSG_KEXDH_GEX_GROUP: Incomplete
c_MSG_KEXDH_GEX_INIT: Incomplete
c_MSG_KEXDH_GEX_REPLY: Incomplete
c_MSG_KEXDH_GEX_REQUEST: Incomplete

class KexGex:
    name: str
    min_bits: int
    max_bits: int
    preferred_bits: int
    hash_algo = sha1
    transport: Incomplete
    p: Incomplete
    q: Incomplete
    g: Incomplete
    x: Incomplete
    e: Incomplete
    f: Incomplete
    old_style: bool
    def __init__(self, transport) -> None: ...
    def start_kex(self, _test_old_style: bool = False) -> None: ...
    def parse_next(self, ptype, m): ...

class KexGexSHA256(KexGex):
    name: str
    hash_algo = sha256
