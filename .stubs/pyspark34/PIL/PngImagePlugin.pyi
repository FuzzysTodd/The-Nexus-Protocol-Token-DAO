from . import Image as Image, ImageChops as ImageChops, ImageFile as ImageFile, ImagePalette as ImagePalette, ImageSequence as ImageSequence
from ._binary import o8 as o8
from _typeshed import Incomplete
from enum import IntEnum

logger: Incomplete
is_cid: Incomplete
MAX_TEXT_CHUNK: Incomplete
MAX_TEXT_MEMORY: Incomplete

class Disposal(IntEnum):
    OP_NONE: int
    OP_BACKGROUND: int
    OP_PREVIOUS: int

class Blend(IntEnum):
    OP_SOURCE: int
    OP_OVER: int

class ChunkStream:
    fp: Incomplete
    queue: Incomplete
    def __init__(self, fp) -> None: ...
    def read(self):
        """Fetch a new chunk. Returns header information."""
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self) -> None: ...
    def push(self, cid, pos, length) -> None: ...
    def call(self, cid, pos, length):
        """Call the appropriate chunk handler"""
    def crc(self, cid, data) -> None:
        """Read and verify checksum"""
    def crc_skip(self, cid, data) -> None:
        """Read checksum"""
    def verify(self, endchunk: bytes = b'IEND'): ...

class iTXt(str):
    """
    Subclass of string to allow iTXt chunks to look like strings while
    keeping their extra information

    """
    lang: Incomplete
    tkey: Incomplete
    @staticmethod
    def __new__(cls, text, lang: Incomplete | None = None, tkey: Incomplete | None = None):
        """
        :param cls: the class to use when creating the instance
        :param text: value for this key
        :param lang: language code
        :param tkey: UTF-8 version of the key name
        """

class PngInfo:
    """
    PNG chunk container (for use with save(pnginfo=))

    """
    chunks: Incomplete
    def __init__(self) -> None: ...
    def add(self, cid, data, after_idat: bool = False) -> None:
        """Appends an arbitrary chunk. Use with caution.

        :param cid: a byte string, 4 bytes long.
        :param data: a byte string of the encoded data
        :param after_idat: for use with private chunks. Whether the chunk
                           should be written after IDAT

        """
    def add_itxt(self, key, value, lang: str = '', tkey: str = '', zip: bool = False) -> None:
        """Appends an iTXt chunk.

        :param key: latin-1 encodable text key name
        :param value: value for this key
        :param lang: language code
        :param tkey: UTF-8 version of the key name
        :param zip: compression flag

        """
    def add_text(self, key, value, zip: bool = False):
        """Appends a text chunk.

        :param key: latin-1 encodable text key name
        :param value: value for this key, text or an
           :py:class:`PIL.PngImagePlugin.iTXt` instance
        :param zip: compression flag

        """

class PngStream(ChunkStream):
    im_info: Incomplete
    im_text: Incomplete
    im_size: Incomplete
    im_mode: Incomplete
    im_tile: Incomplete
    im_palette: Incomplete
    im_custom_mimetype: Incomplete
    im_n_frames: Incomplete
    rewind_state: Incomplete
    text_memory: int
    def __init__(self, fp) -> None: ...
    def check_text_memory(self, chunklen) -> None: ...
    def save_rewind(self) -> None: ...
    def rewind(self) -> None: ...
    def chunk_iCCP(self, pos, length): ...
    def chunk_IHDR(self, pos, length): ...
    im_idat: Incomplete
    def chunk_IDAT(self, pos, length) -> None: ...
    def chunk_IEND(self, pos, length) -> None: ...
    def chunk_PLTE(self, pos, length): ...
    def chunk_tRNS(self, pos, length): ...
    def chunk_gAMA(self, pos, length): ...
    def chunk_cHRM(self, pos, length): ...
    def chunk_sRGB(self, pos, length): ...
    def chunk_pHYs(self, pos, length): ...
    def chunk_tEXt(self, pos, length): ...
    def chunk_zTXt(self, pos, length): ...
    def chunk_iTXt(self, pos, length): ...
    def chunk_eXIf(self, pos, length): ...
    def chunk_acTL(self, pos, length): ...
    def chunk_fcTL(self, pos, length): ...
    def chunk_fdAT(self, pos, length): ...

class PngImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    @property
    def text(self): ...
    fp: Incomplete
    def verify(self) -> None:
        """Verify PNG file"""
    def seek(self, frame) -> None: ...
    def tell(self): ...
    decoderconfig: Incomplete
    def load_prepare(self) -> None:
        """internal: prepare to read PNG file"""
    def load_read(self, read_bytes):
        """internal: read more image data"""
    png: Incomplete
    im: Incomplete
    pyaccess: Incomplete
    def load_end(self) -> None:
        """internal: finished reading image data"""
    def getexif(self): ...
    def getxmp(self):
        """
        Returns a dictionary containing the XMP tags.
        Requires defusedxml to be installed.

        :returns: XMP tags in a dictionary.
        """

def putchunk(fp, cid, *data) -> None:
    """Write a PNG chunk (including CRC field)"""

class _idat:
    fp: Incomplete
    chunk: Incomplete
    def __init__(self, fp, chunk) -> None: ...
    def write(self, data) -> None: ...

class _fdat:
    fp: Incomplete
    chunk: Incomplete
    seq_num: Incomplete
    def __init__(self, fp, chunk, seq_num) -> None: ...
    def write(self, data) -> None: ...

def getchunks(im, **params):
    """Return a list of PNG chunks representing this image."""
