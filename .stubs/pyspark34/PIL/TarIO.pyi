from . import ContainerIO as ContainerIO
from _typeshed import Incomplete

class TarIO(ContainerIO.ContainerIO):
    """A file object that provides read access to a given member of a TAR file."""
    fh: Incomplete
    def __init__(self, tarfile, file) -> None:
        """
        Create file object.

        :param tarfile: Name of TAR file.
        :param file: Name of member file.
        """
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self) -> None: ...
