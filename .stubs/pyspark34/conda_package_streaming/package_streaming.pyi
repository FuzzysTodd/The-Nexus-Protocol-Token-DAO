import tarfile
from _typeshed import Incomplete
from enum import Enum
from typing import Generator

UMASK: Incomplete

class CondaComponent(Enum):
    pkg: str
    info: str

class TarfileNoSameOwner(tarfile.TarFile):
    umask: Incomplete
    def __init__(self, *args, umask=..., **kwargs) -> None:
        """Open an (uncompressed) tar archive `name'. `mode' is either 'r' to
        read from an existing archive, 'a' to append data to an existing
        file or 'w' to create a new file overwriting an existing one. `mode'
        defaults to 'r'.
        If `fileobj' is given, it is used for reading or writing data. If it
        can be determined, `mode' is overridden by `fileobj's mode.
        `fileobj' is not closed, when TarFile is closed.
        """
    def chown(self, tarinfo, targetpath, numeric_owner) -> None:
        """
        Override chown to be a no-op, since we don't want to preserve ownership
        here. (tarfile.TarFile only lets us toggle all of (chown, chmod, mtime))
        """
    def chmod(self, tarinfo, targetpath) -> None:
        """
        Set file permissions of targetpath according to tarinfo, respecting
        umask.
        """

def tar_generator(fileobj, tarfile_open=..., closefd: bool = False) -> Generator[tuple[tarfile.TarFile, tarfile.TarInfo], None, None]:
    """
    Yield (tar, member) from fileobj.
    """
def stream_conda_info(filename, fileobj: Incomplete | None = None) -> Generator[tuple[tarfile.TarFile, tarfile.TarInfo], None, None]:
    """
    Yield members from conda's embedded info/ tarball.

    For .tar.bz2 packages, yield all members.

    Yields (tar, member) tuples. You must only use the current member to
    prevent tar seeks and scans.

    To extract to disk, it's possible to call ``tar.extractall(path)`` on the
    first result and then ignore the rest of this generator. ``extractall`` takes
    care of some directory permissions/mtime issues, compared to ``extract`` or
    writing out the file objects yourself.
    """
def stream_conda_component(filename, fileobj: Incomplete | None = None, component: CondaComponent | str = ...) -> Generator[tuple[tarfile.TarFile, tarfile.TarInfo], None, None]:
    '''
    Yield members from .conda\'s embedded {component}- tarball. "info" or "pkg".

    For .tar.bz2 packages, yield all members.

    Yields (tar, member) tuples. You must only use the current member to
    prevent tar seeks and scans.

    To extract to disk, it\'s possible to call ``tar.extractall(path)`` on the
    first result and then ignore the rest of this generator. ``extractall`` takes
    care of some directory permissions/mtime issues, compared to ``extract`` or
    writing out the file objects yourself.
    '''
