from _typeshed import Incomplete

class ContainerIO:
    """
    A file object that provides read access to a part of an existing
    file (for example a TAR file).
    """
    fh: Incomplete
    pos: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, file, offset, length) -> None:
        """
        Create file object.

        :param file: Existing file.
        :param offset: Start of region, in bytes.
        :param length: Size of region, in bytes.
        """
    def isatty(self): ...
    def seek(self, offset, mode=...) -> None:
        """
        Move file pointer.

        :param offset: Offset in bytes.
        :param mode: Starting position. Use 0 for beginning of region, 1
           for current offset, and 2 for end of region.  You cannot move
           the pointer outside the defined region.
        """
    def tell(self):
        """
        Get current file pointer.

        :returns: Offset from start of region, in bytes.
        """
    def read(self, n: int = 0):
        """
        Read data.

        :param n: Number of bytes to read. If omitted or zero,
            read until end of region.
        :returns: An 8-bit string.
        """
    def readline(self):
        """
        Read a line of text.

        :returns: An 8-bit string.
        """
    def readlines(self):
        """
        Read multiple lines of text.

        :returns: A list of 8-bit strings.
        """
