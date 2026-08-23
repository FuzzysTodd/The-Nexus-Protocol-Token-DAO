import hashlib
from _typeshed import Incomplete
from paramiko.common import byte_chr as byte_chr
from paramiko.message import Message as Message
from paramiko.ssh_exception import SSHException as SSHException

c_MSG_KEXECDH_INIT: Incomplete
c_MSG_KEXECDH_REPLY: Incomplete

class KexCurve25519:
    hash_algo = hashlib.sha256
    transport: Incomplete
    key: Incomplete
    def __init__(self, transport) -> None: ...
    @classmethod
    def is_available(cls): ...
    def start_kex(self) -> None: ...
    def parse_next(self, ptype, m): ...
