from _typeshed import Incomplete
from paramiko.common import four_byte as four_byte
from paramiko.message import Message as Message
from paramiko.pkey import PKey as PKey
from paramiko.ssh_exception import SSHException as SSHException
from paramiko.util import deflate_long as deflate_long

class _ECDSACurve:
    """
    Represents a specific ECDSA Curve (nistp256, nistp384, etc).

    Handles the generation of the key format identifier and the selection of
    the proper hash function. Also grabs the proper curve from the 'ecdsa'
    package.
    """
    nist_name: Incomplete
    key_length: Incomplete
    key_format_identifier: Incomplete
    hash_object: Incomplete
    curve_class: Incomplete
    def __init__(self, curve_class, nist_name) -> None: ...

class _ECDSACurveSet:
    """
    A collection to hold the ECDSA curves. Allows querying by oid and by key
    format identifier. The two ways in which ECDSAKey needs to be able to look
    up curves.
    """
    ecdsa_curves: Incomplete
    def __init__(self, ecdsa_curves) -> None: ...
    def get_key_format_identifier_list(self): ...
    def get_by_curve_class(self, curve_class): ...
    def get_by_key_format_identifier(self, key_format_identifier): ...
    def get_by_key_length(self, key_length): ...

class ECDSAKey(PKey):
    """
    Representation of an ECDSA key which can be used to sign and verify SSH2
    data.
    """
    verifying_key: Incomplete
    signing_key: Incomplete
    public_blob: Incomplete
    ecdsa_curve: Incomplete
    def __init__(self, msg: Incomplete | None = None, data: Incomplete | None = None, filename: Incomplete | None = None, password: Incomplete | None = None, vals: Incomplete | None = None, file_obj: Incomplete | None = None, validate_point: bool = True) -> None: ...
    @classmethod
    def identifiers(cls): ...
    @classmethod
    def supported_key_format_identifiers(cls): ...
    def asbytes(self): ...
    def get_name(self): ...
    def get_bits(self): ...
    def can_sign(self): ...
    def sign_ssh_data(self, data, algorithm: Incomplete | None = None): ...
    def verify_ssh_sig(self, data, msg): ...
    def write_private_key_file(self, filename, password: Incomplete | None = None) -> None: ...
    def write_private_key(self, file_obj, password: Incomplete | None = None) -> None: ...
    @classmethod
    def generate(cls, curve=..., progress_func: Incomplete | None = None, bits: Incomplete | None = None):
        """
        Generate a new private ECDSA key.  This factory function can be used to
        generate a new host key or authentication key.

        :param progress_func: Not used for this type of key.
        :returns: A new private key (`.ECDSAKey`) object
        """
