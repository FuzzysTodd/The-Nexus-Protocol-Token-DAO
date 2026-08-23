from . import Image as Image, ImageFile as ImageFile
from _typeshed import Incomplete

class WalImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    im: Incomplete
    def load(self): ...

def open(filename):
    """
    Load texture from a Quake2 WAL texture file.

    By default, a Quake2 standard palette is attached to the texture.
    To override the palette, use the :py:func:`PIL.Image.Image.putpalette()` method.

    :param filename: WAL file name, or an opened file handle.
    :returns: An image instance.
    """

quake2palette: bytes
