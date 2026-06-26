from _typeshed import Incomplete
from paramiko import util as util
from paramiko.common import DEBUG as DEBUG, MSG_NAMES as MSG_NAMES, byte_ord as byte_ord, cr_byte_value as cr_byte_value, linefeed_byte as linefeed_byte, xffffffff as xffffffff, zero_byte as zero_byte
from paramiko.message import Message as Message
from paramiko.ssh_exception import ProxyCommandFailure as ProxyCommandFailure, SSHException as SSHException
from paramiko.util import u as u

def compute_hmac(key, message, digest_class): ...

class NeedRekeyException(Exception):
    """
    Exception indicating a rekey is needed.
    """

def first_arg(e): ...

class Packetizer:
    """
    Implementation of the base SSH packet protocol.
    """
    REKEY_PACKETS: Incomplete
    REKEY_BYTES: Incomplete
    REKEY_PACKETS_OVERFLOW_MAX: Incomplete
    REKEY_BYTES_OVERFLOW_MAX: Incomplete
    def __init__(self, socket) -> None: ...
    @property
    def closed(self): ...
    def set_log(self, log) -> None:
        """
        Set the Python log object to use for logging.
        """
    def set_outbound_cipher(self, block_engine, block_size, mac_engine, mac_size, mac_key, sdctr: bool = False, etm: bool = False) -> None:
        """
        Switch outbound data cipher.
        :param etm: Set encrypt-then-mac from OpenSSH
        """
    def set_inbound_cipher(self, block_engine, block_size, mac_engine, mac_size, mac_key, etm: bool = False) -> None:
        """
        Switch inbound data cipher.
        :param etm: Set encrypt-then-mac from OpenSSH
        """
    def set_outbound_compressor(self, compressor) -> None: ...
    def set_inbound_compressor(self, compressor) -> None: ...
    def close(self) -> None: ...
    def set_hexdump(self, hexdump) -> None: ...
    def get_hexdump(self): ...
    def get_mac_size_in(self): ...
    def get_mac_size_out(self): ...
    def need_rekey(self):
        """
        Returns ``True`` if a new set of keys needs to be negotiated.  This
        will be triggered during a packet read or write, so it should be
        checked after every read or write, or at least after every few.
        """
    def set_keepalive(self, interval, callback) -> None:
        """
        Turn on/off the callback keepalive.  If ``interval`` seconds pass with
        no data read from or written to the socket, the callback will be
        executed and the timer will be reset.
        """
    def read_timer(self) -> None: ...
    def start_handshake(self, timeout) -> None:
        """
        Tells `Packetizer` that the handshake process started.
        Starts a book keeping timer that can signal a timeout in the
        handshake process.

        :param float timeout: amount of seconds to wait before timing out
        """
    def handshake_timed_out(self):
        """
        Checks if the handshake has timed out.

        If `start_handshake` wasn't called before the call to this function,
        the return value will always be `False`. If the handshake completed
        before a timeout was reached, the return value will be `False`

        :return: handshake time out status, as a `bool`
        """
    def complete_handshake(self) -> None:
        """
        Tells `Packetizer` that the handshake has completed.
        """
    def read_all(self, n, check_rekey: bool = False):
        """
        Read as close to N bytes as possible, blocking as long as necessary.

        :param int n: number of bytes to read
        :return: the data read, as a `str`

        :raises:
            ``EOFError`` -- if the socket was closed before all the bytes could
            be read
        """
    def write_all(self, out) -> None: ...
    def readline(self, timeout):
        """
        Read a line from the socket.  We assume no data is pending after the
        line, so it's okay to attempt large reads.
        """
    def send_message(self, data) -> None:
        """
        Write a block of data using the current cipher, as an SSH block.
        """
    def read_message(self):
        """
        Only one thread should ever be in this function (no other locking is
        done).

        :raises: `.SSHException` -- if the packet is mangled
        :raises: `.NeedRekeyException` -- if the transport should rekey
        """
