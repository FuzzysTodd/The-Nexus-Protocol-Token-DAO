from . import Image as Image, ImageChops as ImageChops, ImageFile as ImageFile, ImagePalette as ImagePalette, ImageSequence as ImageSequence
from ._binary import o8 as o8
from _typeshed import Incomplete
from enum import IntEnum

class LoadingStrategy(IntEnum):
    """.. versionadded:: 9.1.0"""
    RGB_AFTER_FIRST: int
    RGB_AFTER_DIFFERENT_PALETTE_ONLY: int
    RGB_ALWAYS: int

LOADING_STRATEGY: Incomplete

class GifImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    global_palette: Incomplete
    def data(self): ...
    @property
    def n_frames(self): ...
    @property
    def is_animated(self): ...
    im: Incomplete
    def seek(self, frame) -> None: ...
    mode: Incomplete
    def load_prepare(self) -> None: ...
    def load_end(self) -> None: ...
    def tell(self): ...

RAWMODE: Incomplete

def get_interlace(im): ...
def getheader(im, palette: Incomplete | None = None, info: Incomplete | None = None):
    """
    Legacy Method to get Gif data from image.

    Warning:: May modify image data.

    :param im: Image object
    :param palette: bytes object containing the source palette, or ....
    :param info: encoderinfo
    :returns: tuple of(list of header items, optimized palette)

    """
def getdata(im, offset=(0, 0), **params):
    """
    Legacy Method

    Return a list of strings representing this image.
    The first string is a local image header, the rest contains
    encoded image data.

    To specify duration, add the time in milliseconds,
    e.g. ``getdata(im_frame, duration=1000)``

    :param im: Image object
    :param offset: Tuple of (x, y) pixels. Defaults to (0, 0)
    :param \\**params: e.g. duration or other encoder info parameters
    :returns: List of bytes containing GIF encoded frame data

    """
