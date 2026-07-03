from paramiko.common import DEBUG as DEBUG, byte_chr as byte_chr, byte_ord as byte_ord, max_byte as max_byte, xffffffff as xffffffff, zero_byte as zero_byte
from paramiko.config import SSHConfig as SSHConfig

def inflate_long(s, always_positive: bool = False):
    """turns a normalized byte string into a long-int
    (adapted from Crypto.Util.number)"""
def deflate_long(n, add_sign_padding: bool = True):
    """turns a long-int into a normalized byte string
    (adapted from Crypto.Util.number)"""
def format_binary(data, prefix: str = ''): ...
def format_binary_line(data): ...
def safe_string(s): ...
def bit_length(n): ...
def tb_strings(): ...
def generate_key_bytes(hash_alg, salt, key, nbytes):
    """
    Given a password, passphrase, or other human-source key, scramble it
    through a secure hash into some keyworthy bytes.  This specific algorithm
    is used for encrypting/decrypting private key files.

    :param function hash_alg: A function which creates a new hash object, such
        as ``hashlib.sha256``.
    :param salt: data to salt the hash with.
    :type bytes salt: Hash salt bytes.
    :param str key: human-entered password or passphrase.
    :param int nbytes: number of bytes to generate.
    :return: Key data, as `bytes`.
    """
def load_host_keys(filename):
    '''
    Read a file of known SSH host keys, in the format used by openssh, and
    return a compound dict of ``hostname -> keytype ->`` `PKey
    <paramiko.pkey.PKey>`. The hostname may be an IP address or DNS name.  The
    keytype will be either ``"ssh-rsa"`` or ``"ssh-dss"``.

    This type of file unfortunately doesn\'t exist on Windows, but on posix,
    it will usually be stored in ``os.path.expanduser("~/.ssh/known_hosts")``.

    Since 1.5.3, this is just a wrapper around `.HostKeys`.

    :param str filename: name of the file to read host keys from
    :return:
        nested dict of `.PKey` objects, indexed by hostname and then keytype
    '''
def parse_ssh_config(file_obj):
    """
    Provided only as a backward-compatible wrapper around `.SSHConfig`.

    .. deprecated:: 2.7
        Use `SSHConfig.from_file` instead.
    """
def lookup_ssh_host_config(hostname, config):
    """
    Provided only as a backward-compatible wrapper around `.SSHConfig`.
    """
def mod_inverse(x, m): ...
def get_thread_id(): ...
def log_to_file(filename, level=...) -> None:
    """send paramiko logs to a logfile,
    if they're not already going somewhere"""

class PFilter:
    def filter(self, record): ...

def get_logger(name): ...
def constant_time_bytes_eq(a, b): ...

class ClosingContextManager:
    def __enter__(self): ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def clamp_value(minimum, val, maximum): ...
def asbytes(s):
    """
    Coerce to bytes if possible or return unchanged.
    """
def b(s, encoding: str = 'utf8'):
    """cast unicode or bytes to bytes"""
def u(s, encoding: str = 'utf8'):
    """cast bytes or unicode to unicode"""
