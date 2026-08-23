from _typeshed import Incomplete
from paramiko.message import Message as Message
from paramiko.pkey import OPENSSH_AUTH_MAGIC as OPENSSH_AUTH_MAGIC, PKey as PKey
from paramiko.ssh_exception import PasswordRequiredException as PasswordRequiredException, SSHException as SSHException
from paramiko.util import b as b

class Ed25519Key(PKey):
    """
    Representation of an `Ed25519 <https://ed25519.cr.yp.to/>`_ key.

    .. note::
        Ed25519 key support was added to OpenSSH in version 6.5.

    .. versionadded:: 2.2
    .. versionchanged:: 2.3
        Added a ``file_obj`` parameter to match other key classes.
    """
    name: str
    public_blob: Incomplete
    def __init__(self, msg: Incomplete | None = None, data: Incomplete | None = None, filename: Incomplete | None = None, password: Incomplete | None = None, file_obj: Incomplete | None = None) -> None: ...
    def asbytes(self): ...
    def get_name(self): ...
    def get_bits(self): ...
    def can_sign(self): ...
    def sign_ssh_data(self, data, algorithm: Incomplete | None = None): ...
    def verify_ssh_sig(self, data, msg): ...
