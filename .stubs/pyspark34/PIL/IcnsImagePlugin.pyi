from . import Image as Image, ImageFile as ImageFile, Jpeg2KImagePlugin as Jpeg2KImagePlugin, PngImagePlugin as PngImagePlugin, features as features
from _typeshed import Incomplete

enable_jpeg2k: Incomplete
MAGIC: bytes
HEADERSIZE: int

def nextheader(fobj): ...
def read_32t(fobj, start_length, size): ...
def read_32(fobj, start_length, size):
    """
    Read a 32bit RGB icon resource.  Seems to be either uncompressed or
    an RLE packbits-like scheme.
    """
def read_mk(fobj, start_length, size): ...
def read_png_or_jpeg2000(fobj, start_length, size): ...

class IcnsFile:
    SIZES: Incomplete
    dct: Incomplete
    fobj: Incomplete
    def __init__(self, fobj) -> None:
        """
        fobj is a file-like object as an icns resource
        """
    def itersizes(self): ...
    def bestsize(self): ...
    def dataforsize(self, size):
        """
        Get an icon resource as {channel: array}.  Note that
        the arrays are bottom-up like windows bitmaps and will likely
        need to be flipped or transposed in some way.
        """
    def getimage(self, size: Incomplete | None = None): ...

class IcnsImageFile(ImageFile.ImageFile):
    """
    PIL image support for Mac OS .icns files.
    Chooses the best resolution, but will possibly load
    a different size image if you mutate the size attribute
    before calling 'load'.

    The info dictionary has a key 'sizes' that is a list
    of sizes that the icns file has.
    """
    format: str
    format_description: str
    @property
    def size(self): ...
    @size.setter
    def size(self, value) -> None: ...
    best_size: Incomplete
    im: Incomplete
    mode: Incomplete
    def load(self): ...
