import enum
import typing
from _typeshed import Incomplete
from cryptography import utils as utils
from cryptography.exceptions import UnsupportedAlgorithm as UnsupportedAlgorithm
from cryptography.hazmat.primitives import hashes as hashes
from cryptography.hazmat.primitives.asymmetric import dsa as dsa, ec as ec, ed25519 as ed25519, padding as padding, rsa as rsa
from cryptography.hazmat.primitives.ciphers import AEADDecryptionContext as AEADDecryptionContext, Cipher as Cipher, algorithms as algorithms, modes as modes
from cryptography.hazmat.primitives.serialization import Encoding as Encoding, KeySerializationEncryption as KeySerializationEncryption, NoEncryption as NoEncryption, PrivateFormat as PrivateFormat, PublicFormat as PublicFormat
from dataclasses import dataclass

@dataclass
class _SSHCipher:
    alg: typing.Type[algorithms.AES]
    key_len: int
    mode: typing.Type[modes.CTR] | typing.Type[modes.CBC] | typing.Type[modes.GCM]
    block_len: int
    iv_len: int
    tag_len: int | None
    is_aead: bool
    def __init__(self, alg, key_len, mode, block_len, iv_len, tag_len, is_aead) -> None: ...

class _FragList:
    """Build recursive structure without data copy."""
    flist: typing.List[bytes]
    def __init__(self, init: typing.List[bytes] | None = None) -> None: ...
    def put_raw(self, val: bytes) -> None:
        """Add plain bytes"""
    def put_u32(self, val: int) -> None:
        """Big-endian uint32"""
    def put_u64(self, val: int) -> None:
        """Big-endian uint64"""
    def put_sshstr(self, val: bytes | _FragList) -> None:
        """Bytes prefixed with u32 length"""
    def put_mpint(self, val: int) -> None:
        """Big-endian bigint prefixed with u32 length"""
    def size(self) -> int:
        """Current number of bytes"""
    def render(self, dstbuf: memoryview, pos: int = 0) -> int:
        """Write into bytearray"""
    def tobytes(self) -> bytes:
        """Return as bytes"""

class _SSHFormatRSA:
    """Format for RSA keys.

    Public:
        mpint e, n
    Private:
        mpint n, e, d, iqmp, p, q
    """
    def get_public(self, data: memoryview):
        """RSA public fields"""
    def load_public(self, data: memoryview) -> typing.Tuple[rsa.RSAPublicKey, memoryview]:
        """Make RSA public key from data."""
    def load_private(self, data: memoryview, pubfields) -> typing.Tuple[rsa.RSAPrivateKey, memoryview]:
        """Make RSA private key from data."""
    def encode_public(self, public_key: rsa.RSAPublicKey, f_pub: _FragList) -> None:
        """Write RSA public key"""
    def encode_private(self, private_key: rsa.RSAPrivateKey, f_priv: _FragList) -> None:
        """Write RSA private key"""

class _SSHFormatDSA:
    """Format for DSA keys.

    Public:
        mpint p, q, g, y
    Private:
        mpint p, q, g, y, x
    """
    def get_public(self, data: memoryview) -> typing.Tuple[typing.Tuple, memoryview]:
        """DSA public fields"""
    def load_public(self, data: memoryview) -> typing.Tuple[dsa.DSAPublicKey, memoryview]:
        """Make DSA public key from data."""
    def load_private(self, data: memoryview, pubfields) -> typing.Tuple[dsa.DSAPrivateKey, memoryview]:
        """Make DSA private key from data."""
    def encode_public(self, public_key: dsa.DSAPublicKey, f_pub: _FragList) -> None:
        """Write DSA public key"""
    def encode_private(self, private_key: dsa.DSAPrivateKey, f_priv: _FragList) -> None:
        """Write DSA private key"""

class _SSHFormatECDSA:
    """Format for ECDSA keys.

    Public:
        str curve
        bytes point
    Private:
        str curve
        bytes point
        mpint secret
    """
    ssh_curve_name: Incomplete
    curve: Incomplete
    def __init__(self, ssh_curve_name: bytes, curve: ec.EllipticCurve) -> None: ...
    def get_public(self, data: memoryview) -> typing.Tuple[typing.Tuple, memoryview]:
        """ECDSA public fields"""
    def load_public(self, data: memoryview) -> typing.Tuple[ec.EllipticCurvePublicKey, memoryview]:
        """Make ECDSA public key from data."""
    def load_private(self, data: memoryview, pubfields) -> typing.Tuple[ec.EllipticCurvePrivateKey, memoryview]:
        """Make ECDSA private key from data."""
    def encode_public(self, public_key: ec.EllipticCurvePublicKey, f_pub: _FragList) -> None:
        """Write ECDSA public key"""
    def encode_private(self, private_key: ec.EllipticCurvePrivateKey, f_priv: _FragList) -> None:
        """Write ECDSA private key"""

class _SSHFormatEd25519:
    """Format for Ed25519 keys.

    Public:
        bytes point
    Private:
        bytes point
        bytes secret_and_point
    """
    def get_public(self, data: memoryview) -> typing.Tuple[typing.Tuple, memoryview]:
        """Ed25519 public fields"""
    def load_public(self, data: memoryview) -> typing.Tuple[ed25519.Ed25519PublicKey, memoryview]:
        """Make Ed25519 public key from data."""
    def load_private(self, data: memoryview, pubfields) -> typing.Tuple[ed25519.Ed25519PrivateKey, memoryview]:
        """Make Ed25519 private key from data."""
    def encode_public(self, public_key: ed25519.Ed25519PublicKey, f_pub: _FragList) -> None:
        """Write Ed25519 public key"""
    def encode_private(self, private_key: ed25519.Ed25519PrivateKey, f_priv: _FragList) -> None:
        """Write Ed25519 private key"""

SSHPrivateKeyTypes: Incomplete

def load_ssh_private_key(data: bytes, password: bytes | None, backend: typing.Any = None) -> SSHPrivateKeyTypes:
    """Load private key from OpenSSH custom encoding."""

SSHPublicKeyTypes: Incomplete
SSHCertPublicKeyTypes: Incomplete

class SSHCertificateType(enum.Enum):
    USER: int
    HOST: int

class SSHCertificate:
    def __init__(self, _nonce: memoryview, _public_key: SSHPublicKeyTypes, _serial: int, _cctype: int, _key_id: memoryview, _valid_principals: typing.List[bytes], _valid_after: int, _valid_before: int, _critical_options: typing.Dict[bytes, bytes], _extensions: typing.Dict[bytes, bytes], _sig_type: memoryview, _sig_key: memoryview, _inner_sig_type: memoryview, _signature: memoryview, _tbs_cert_body: memoryview, _cert_key_type: bytes, _cert_body: memoryview) -> None: ...
    @property
    def nonce(self) -> bytes: ...
    def public_key(self) -> SSHCertPublicKeyTypes: ...
    @property
    def serial(self) -> int: ...
    @property
    def type(self) -> SSHCertificateType: ...
    @property
    def key_id(self) -> bytes: ...
    @property
    def valid_principals(self) -> typing.List[bytes]: ...
    @property
    def valid_before(self) -> int: ...
    @property
    def valid_after(self) -> int: ...
    @property
    def critical_options(self) -> typing.Dict[bytes, bytes]: ...
    @property
    def extensions(self) -> typing.Dict[bytes, bytes]: ...
    def signature_key(self) -> SSHCertPublicKeyTypes: ...
    def public_bytes(self) -> bytes: ...
    def verify_cert_signature(self) -> None: ...

def load_ssh_public_identity(data: bytes) -> SSHCertificate | SSHPublicKeyTypes: ...
def load_ssh_public_key(data: bytes, backend: typing.Any = None) -> SSHPublicKeyTypes: ...
def serialize_ssh_public_key(public_key: SSHPublicKeyTypes) -> bytes:
    """One-line public key format for OpenSSH"""

SSHCertPrivateKeyTypes: Incomplete

class SSHCertificateBuilder:
    def __init__(self, _public_key: SSHCertPublicKeyTypes | None = None, _serial: int | None = None, _type: SSHCertificateType | None = None, _key_id: bytes | None = None, _valid_principals: typing.List[bytes] = [], _valid_for_all_principals: bool = False, _valid_before: int | None = None, _valid_after: int | None = None, _critical_options: typing.List[typing.Tuple[bytes, bytes]] = [], _extensions: typing.List[typing.Tuple[bytes, bytes]] = []) -> None: ...
    def public_key(self, public_key: SSHCertPublicKeyTypes) -> SSHCertificateBuilder: ...
    def serial(self, serial: int) -> SSHCertificateBuilder: ...
    def type(self, type: SSHCertificateType) -> SSHCertificateBuilder: ...
    def key_id(self, key_id: bytes) -> SSHCertificateBuilder: ...
    def valid_principals(self, valid_principals: typing.List[bytes]) -> SSHCertificateBuilder: ...
    def valid_for_all_principals(self): ...
    def valid_before(self, valid_before: int | float) -> SSHCertificateBuilder: ...
    def valid_after(self, valid_after: int | float) -> SSHCertificateBuilder: ...
    def add_critical_option(self, name: bytes, value: bytes) -> SSHCertificateBuilder: ...
    def add_extension(self, name: bytes, value: bytes) -> SSHCertificateBuilder: ...
    def sign(self, private_key: SSHCertPrivateKeyTypes) -> SSHCertificate: ...
