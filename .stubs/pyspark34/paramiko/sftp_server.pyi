from _typeshed import Incomplete
from paramiko import util as util
from paramiko.common import DEBUG as DEBUG
from paramiko.server import SubsystemHandler as SubsystemHandler
from paramiko.sftp import BaseSFTP as BaseSFTP, CMD_ATTRS as CMD_ATTRS, CMD_CLOSE as CMD_CLOSE, CMD_DATA as CMD_DATA, CMD_EXTENDED as CMD_EXTENDED, CMD_EXTENDED_REPLY as CMD_EXTENDED_REPLY, CMD_FSETSTAT as CMD_FSETSTAT, CMD_FSTAT as CMD_FSTAT, CMD_HANDLE as CMD_HANDLE, CMD_LSTAT as CMD_LSTAT, CMD_MKDIR as CMD_MKDIR, CMD_NAME as CMD_NAME, CMD_NAMES as CMD_NAMES, CMD_OPEN as CMD_OPEN, CMD_OPENDIR as CMD_OPENDIR, CMD_READ as CMD_READ, CMD_READDIR as CMD_READDIR, CMD_READLINK as CMD_READLINK, CMD_REALPATH as CMD_REALPATH, CMD_REMOVE as CMD_REMOVE, CMD_RENAME as CMD_RENAME, CMD_RMDIR as CMD_RMDIR, CMD_SETSTAT as CMD_SETSTAT, CMD_STAT as CMD_STAT, CMD_STATUS as CMD_STATUS, CMD_SYMLINK as CMD_SYMLINK, CMD_WRITE as CMD_WRITE, Message as Message, SFTP_BAD_MESSAGE as SFTP_BAD_MESSAGE, SFTP_DESC as SFTP_DESC, SFTP_EOF as SFTP_EOF, SFTP_FAILURE as SFTP_FAILURE, SFTP_FLAG_APPEND as SFTP_FLAG_APPEND, SFTP_FLAG_CREATE as SFTP_FLAG_CREATE, SFTP_FLAG_EXCL as SFTP_FLAG_EXCL, SFTP_FLAG_READ as SFTP_FLAG_READ, SFTP_FLAG_TRUNC as SFTP_FLAG_TRUNC, SFTP_FLAG_WRITE as SFTP_FLAG_WRITE, SFTP_NO_SUCH_FILE as SFTP_NO_SUCH_FILE, SFTP_OK as SFTP_OK, SFTP_OP_UNSUPPORTED as SFTP_OP_UNSUPPORTED, SFTP_PERMISSION_DENIED as SFTP_PERMISSION_DENIED, int64 as int64
from paramiko.sftp_attr import SFTPAttributes as SFTPAttributes
from paramiko.sftp_handle import SFTPHandle as SFTPHandle
from paramiko.sftp_si import SFTPServerInterface as SFTPServerInterface
from paramiko.util import b as b

class SFTPServer(BaseSFTP, SubsystemHandler):
    '''
    Server-side SFTP subsystem support.  Since this is a `.SubsystemHandler`,
    it can be (and is meant to be) set as the handler for ``"sftp"`` requests.
    Use `.Transport.set_subsystem_handler` to activate this class.
    '''
    logger: Incomplete
    ultra_debug: Incomplete
    next_handle: int
    file_table: Incomplete
    folder_table: Incomplete
    server: Incomplete
    def __init__(self, channel, name, server, sftp_si=..., *args, **kwargs) -> None:
        """
        The constructor for SFTPServer is meant to be called from within the
        `.Transport` as a subsystem handler.  ``server`` and any additional
        parameters or keyword parameters are passed from the original call to
        `.Transport.set_subsystem_handler`.

        :param .Channel channel: channel passed from the `.Transport`.
        :param str name: name of the requested subsystem.
        :param .ServerInterface server:
            the server object associated with this channel and subsystem
        :param sftp_si:
            a subclass of `.SFTPServerInterface` to use for handling individual
            requests.
        """
    sock: Incomplete
    def start_subsystem(self, name, transport, channel) -> None: ...
    def finish_subsystem(self) -> None: ...
    @staticmethod
    def convert_errno(e):
        """
        Convert an errno value (as from an ``OSError`` or ``IOError``) into a
        standard SFTP result code.  This is a convenience function for trapping
        exceptions in server code and returning an appropriate result.

        :param int e: an errno code, as from ``OSError.errno``.
        :return: an `int` SFTP error code like ``SFTP_NO_SUCH_FILE``.
        """
    @staticmethod
    def set_file_attr(filename, attr) -> None:
        """
        Change a file's attributes on the local filesystem.  The contents of
        ``attr`` are used to change the permissions, owner, group ownership,
        and/or modification & access time of the file, depending on which
        attributes are present in ``attr``.

        This is meant to be a handy helper function for translating SFTP file
        requests into local file operations.

        :param str filename:
            name of the file to alter (should usually be an absolute path).
        :param .SFTPAttributes attr: attributes to change.
        """
