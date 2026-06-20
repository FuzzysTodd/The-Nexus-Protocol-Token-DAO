from . import Image as Image
from ._util import is_path as is_path
from _typeshed import Incomplete

MAXBLOCK: int
SAFEBLOCK: Incomplete
LOAD_TRUNCATED_IMAGES: bool
ERRORS: Incomplete

def raise_oserror(error) -> None: ...

class ImageFile(Image.Image):
    """Base class for image file format handlers."""
    custom_mimetype: Incomplete
    tile: Incomplete
    readonly: int
    decoderconfig: Incomplete
    decodermaxblock: Incomplete
    fp: Incomplete
    filename: Incomplete
    def __init__(self, fp: Incomplete | None = None, filename: Incomplete | None = None) -> None: ...
    def get_format_mimetype(self): ...
    def verify(self) -> None:
        """Check file integrity"""
    map: Incomplete
    im: Incomplete
    def load(self):
        """Load image data based on tile list"""
    def load_prepare(self) -> None: ...
    def load_end(self) -> None: ...

class StubImageFile(ImageFile):
    """
    Base class for stub image loaders.

    A stub loader is an image loader that can identify files of a
    certain format, but relies on external code to load the file.
    """
    __class__: Incomplete
    __dict__: Incomplete
    def load(self): ...

class Parser:
    """
    Incremental image parser.  This class implements the standard
    feed/close consumer interface.
    """
    incremental: Incomplete
    image: Incomplete
    data: Incomplete
    decoder: Incomplete
    offset: int
    finished: int
    def reset(self) -> None:
        """
        (Consumer) Reset the parser.  Note that you can only call this
        method immediately after you've created a parser; parser
        instances cannot be reused.
        """
    decode: Incomplete
    def feed(self, data) -> None:
        """
        (Consumer) Feed data to the parser.

        :param data: A string buffer.
        :exception OSError: If the parser failed to parse the image file.
        """
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self):
        """
        (Consumer) Close the stream.

        :returns: An image object.
        :exception OSError: If the parser failed to parse the image file either
                            because it cannot be identified or cannot be
                            decoded.
        """

class PyCodecState:
    xsize: int
    ysize: int
    xoff: int
    yoff: int
    def __init__(self) -> None: ...
    def extents(self): ...

class PyCodec:
    im: Incomplete
    state: Incomplete
    fd: Incomplete
    mode: Incomplete
    def __init__(self, mode, *args) -> None: ...
    args: Incomplete
    def init(self, args) -> None:
        """
        Override to perform codec specific initialization

        :param args: Array of args items from the tile entry
        :returns: None
        """
    def cleanup(self) -> None:
        """
        Override to perform codec specific cleanup

        :returns: None
        """
    def setfd(self, fd) -> None:
        """
        Called from ImageFile to set the Python file-like object

        :param fd: A Python file-like object
        :returns: None
        """
    def setimage(self, im, extents: Incomplete | None = None) -> None:
        """
        Called from ImageFile to set the core output image for the codec

        :param im: A core image object
        :param extents: a 4 tuple of (x0, y0, x1, y1) defining the rectangle
            for this tile
        :returns: None
        """

class PyDecoder(PyCodec):
    """
    Python implementation of a format decoder. Override this class and
    add the decoding logic in the :meth:`decode` method.

    See :ref:`Writing Your Own File Codec in Python<file-codecs-py>`
    """
    @property
    def pulls_fd(self): ...
    def decode(self, buffer) -> None:
        """
        Override to perform the decoding process.

        :param buffer: A bytes object with the data to be decoded.
        :returns: A tuple of ``(bytes consumed, errcode)``.
            If finished with decoding return -1 for the bytes consumed.
            Err codes are from :data:`.ImageFile.ERRORS`.
        """
    def set_as_raw(self, data, rawmode: Incomplete | None = None) -> None:
        """
        Convenience method to set the internal image from a stream of raw data

        :param data: Bytes to be set
        :param rawmode: The rawmode to be used for the decoder.
            If not specified, it will default to the mode of the image
        :returns: None
        """

class PyEncoder(PyCodec):
    """
    Python implementation of a format encoder. Override this class and
    add the decoding logic in the :meth:`encode` method.

    See :ref:`Writing Your Own File Codec in Python<file-codecs-py>`
    """
    @property
    def pushes_fd(self): ...
    def encode(self, bufsize) -> None:
        """
        Override to perform the encoding process.

        :param bufsize: Buffer size.
        :returns: A tuple of ``(bytes encoded, errcode, bytes)``.
            If finished with encoding return 1 for the error code.
            Err codes are from :data:`.ImageFile.ERRORS`.
        """
    def encode_to_pyfd(self):
        """
        If ``pushes_fd`` is ``True``, then this method will be used,
        and ``encode()`` will only be called once.

        :returns: A tuple of ``(bytes consumed, errcode)``.
            Err codes are from :data:`.ImageFile.ERRORS`.
        """
    def encode_to_file(self, fh, bufsize):
        """
        :param fh: File handle.
        :param bufsize: Buffer size.

        :returns: If finished successfully, return 0.
            Otherwise, return an error code. Err codes are from
            :data:`.ImageFile.ERRORS`.
        """
