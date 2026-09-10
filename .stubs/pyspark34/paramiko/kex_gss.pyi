from _typeshed import Incomplete
from paramiko import util as util
from paramiko.common import DEBUG as DEBUG, byte_chr as byte_chr, byte_mask as byte_mask, byte_ord as byte_ord, max_byte as max_byte, zero_byte as zero_byte
from paramiko.message import Message as Message
from paramiko.ssh_exception import SSHException as SSHException

MSG_KEXGSS_INIT: Incomplete
MSG_KEXGSS_CONTINUE: Incomplete
MSG_KEXGSS_COMPLETE: Incomplete
MSG_KEXGSS_HOSTKEY: Incomplete
MSG_KEXGSS_ERROR: Incomplete
MSG_KEXGSS_GROUPREQ: Incomplete
MSG_KEXGSS_GROUP: Incomplete
c_MSG_KEXGSS_INIT: Incomplete
c_MSG_KEXGSS_CONTINUE: Incomplete
c_MSG_KEXGSS_COMPLETE: Incomplete
c_MSG_KEXGSS_HOSTKEY: Incomplete
c_MSG_KEXGSS_ERROR: Incomplete
c_MSG_KEXGSS_GROUPREQ: Incomplete
c_MSG_KEXGSS_GROUP: Incomplete

class KexGSSGroup1:
    """
    GSS-API / SSPI Authenticated Diffie-Hellman Key Exchange as defined in `RFC
    4462 Section 2 <https://tools.ietf.org/html/rfc4462.html#section-2>`_
    """
    P: int
    G: int
    b7fffffffffffffff: Incomplete
    b0000000000000000: Incomplete
    NAME: str
    transport: Incomplete
    kexgss: Incomplete
    gss_host: Incomplete
    x: int
    e: int
    f: int
    def __init__(self, transport) -> None: ...
    def start_kex(self) -> None:
        """
        Start the GSS-API / SSPI Authenticated Diffie-Hellman Key Exchange.
        """
    def parse_next(self, ptype, m):
        """
        Parse the next packet.

        :param ptype: The (string) type of the incoming packet
        :param `.Message` m: The packet content
        """

class KexGSSGroup14(KexGSSGroup1):
    """
    GSS-API / SSPI Authenticated Diffie-Hellman Group14 Key Exchange as defined
    in `RFC 4462 Section 2
    <https://tools.ietf.org/html/rfc4462.html#section-2>`_
    """
    P: int
    G: int
    NAME: str

class KexGSSGex:
    """
    GSS-API / SSPI Authenticated Diffie-Hellman Group Exchange as defined in
    `RFC 4462 Section 2 <https://tools.ietf.org/html/rfc4462.html#section-2>`_
    """
    NAME: str
    min_bits: int
    max_bits: int
    preferred_bits: int
    transport: Incomplete
    kexgss: Incomplete
    gss_host: Incomplete
    p: Incomplete
    q: Incomplete
    g: Incomplete
    x: Incomplete
    e: Incomplete
    f: Incomplete
    old_style: bool
    def __init__(self, transport) -> None: ...
    def start_kex(self) -> None:
        """
        Start the GSS-API / SSPI Authenticated Diffie-Hellman Group Exchange
        """
    def parse_next(self, ptype, m):
        """
        Parse the next packet.

        :param ptype: The (string) type of the incoming packet
        :param `.Message` m: The packet content
        """

class NullHostKey:
    """
    This class represents the Null Host Key for GSS-API Key Exchange as defined
    in `RFC 4462 Section 5
    <https://tools.ietf.org/html/rfc4462.html#section-5>`_
    """
    key: str
    def __init__(self) -> None: ...
    def get_name(self): ...
