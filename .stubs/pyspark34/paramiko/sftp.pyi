from _typeshed import Incomplete
from paramiko import util as util
from paramiko.common import DEBUG as DEBUG, byte_chr as byte_chr, byte_ord as byte_ord
from paramiko.message import Message as Message

CMD_INIT: Incomplete
CMD_VERSION: Incomplete
CMD_OPEN: Incomplete
CMD_CLOSE: Incomplete
CMD_READ: Incomplete
CMD_WRITE: Incomplete
CMD_LSTAT: Incomplete
CMD_FSTAT: Incomplete
CMD_SETSTAT: Incomplete
CMD_FSETSTAT: Incomplete
CMD_OPENDIR: Incomplete
CMD_READDIR: Incomplete
CMD_REMOVE: Incomplete
CMD_MKDIR: Incomplete
CMD_RMDIR: Incomplete
CMD_REALPATH: Incomplete
CMD_STAT: Incomplete
CMD_RENAME: Incomplete
CMD_READLINK: Incomplete
CMD_SYMLINK: Incomplete
CMD_STATUS: Incomplete
CMD_HANDLE: Incomplete
CMD_DATA: Incomplete
CMD_NAME: Incomplete
CMD_ATTRS: Incomplete
CMD_EXTENDED: Incomplete
CMD_EXTENDED_REPLY: Incomplete
SFTP_OK: int
SFTP_EOF: Incomplete
SFTP_NO_SUCH_FILE: Incomplete
SFTP_PERMISSION_DENIED: Incomplete
SFTP_FAILURE: Incomplete
SFTP_BAD_MESSAGE: Incomplete
SFTP_NO_CONNECTION: Incomplete
SFTP_CONNECTION_LOST: Incomplete
SFTP_OP_UNSUPPORTED: Incomplete
SFTP_DESC: Incomplete
SFTP_FLAG_READ: int
SFTP_FLAG_WRITE: int
SFTP_FLAG_APPEND: int
SFTP_FLAG_CREATE: int
SFTP_FLAG_TRUNC: int
SFTP_FLAG_EXCL: int
CMD_NAMES: Incomplete

class int64(int): ...
class SFTPError(Exception): ...

class BaseSFTP:
    logger: Incomplete
    sock: Incomplete
    ultra_debug: bool
    def __init__(self) -> None: ...
