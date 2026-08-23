from _typeshed import Incomplete
from hashlib import sha256, sha384, sha512
from paramiko.common import byte_chr as byte_chr
from paramiko.message import Message as Message
from paramiko.ssh_exception import SSHException as SSHException

c_MSG_KEXECDH_INIT: Incomplete
c_MSG_KEXECDH_REPLY: Incomplete

class KexNistp256:
    name: str
    hash_algo = sha256
    curve: Incomplete
    transport: Incomplete
    P: int
    Q_C: Incomplete
    Q_S: Incomplete
    def __init__(self, transport) -> None: ...
    def start_kex(self) -> None: ...
    def parse_next(self, ptype, m): ...

class KexNistp384(KexNistp256):
    name: str
    hash_algo = sha384
    curve: Incomplete

class KexNistp521(KexNistp256):
    name: str
    hash_algo = sha512
    curve: Incomplete
