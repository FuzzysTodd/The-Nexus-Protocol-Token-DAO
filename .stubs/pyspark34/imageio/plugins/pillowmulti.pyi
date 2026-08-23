from .pillow_legacy import PillowFormat as PillowFormat, image_as_uint as image_as_uint, ndarray_to_pil as ndarray_to_pil
from _typeshed import Incomplete

logger: Incomplete
NeuQuant: Incomplete

class TIFFFormat(PillowFormat): ...

class GIFFormat(PillowFormat):
    """See :mod:`imageio.plugins.pillow_legacy`"""
    class Writer(PillowFormat.Writer): ...

def intToBin(i): ...

class GifWriter:
    """Class that for helping write the animated GIF file. This is based on
    code from images2gif.py (part of visvis). The version here is modified
    to allow streamed writing.
    """
    fp: Incomplete
    opt_subrectangle: Incomplete
    opt_loop: Incomplete
    opt_quantizer: Incomplete
    opt_palette_size: Incomplete
    getdata: Incomplete
    def __init__(self, file, opt_subrectangle: bool = True, opt_loop: int = 0, opt_quantizer: int = 0, opt_palette_size: int = 256) -> None: ...
    def add_image(self, im, duration, dispose) -> None: ...
    def write_header(self, im, globalPalette, loop) -> None: ...
    def close(self) -> None: ...
    def write_image(self, im, palette, rect, duration, dispose) -> None: ...
    def getheaderAnim(self, im):
        """Get animation header. To replace PILs getheader()[0]"""
    def getImageDescriptor(self, im, xy: Incomplete | None = None):
        """Used for the local color table properties per image.
        Otherwise global color table applies to all frames irrespective of
        whether additional colors comes in play that require a redefined
        palette. Still a maximum of 256 color per frame, obviously.

        Written by Ant1 on 2010-08-22
        Modified by Alex Robinson in Janurari 2011 to implement subrectangles.
        """
    def getAppExt(self, loop):
        """Application extension. This part specifies the amount of loops.
        If loop is 0 or inf, it goes on infinitely.
        """
    def getGraphicsControlExt(self, duration: float = 0.1, dispose: int = 2):
        """Graphics Control Extension. A sort of header at the start of
        each image. Specifies duration and transparancy.

        Dispose
        -------
          * 0 - No disposal specified.
          * 1 - Do not dispose. The graphic is to be left in place.
          * 2 - Restore to background color. The area used by the graphic
            must be restored to the background color.
          * 3 - Restore to previous. The decoder is required to restore the
            area overwritten by the graphic with what was there prior to
            rendering the graphic.
          * 4-7 -To be defined.
        """
    def getSubRectangle(self, im):
        """Calculate the minimal rectangle that need updating. Returns
        a two-element tuple containing the cropped image and an x-y tuple.

        Calculating the subrectangles takes extra time, obviously. However,
        if the image sizes were reduced, the actual writing of the GIF
        goes faster. In some cases applying this method produces a GIF faster.
        """
    def converToPIL(self, im, quantizer, palette_size: int = 256):
        """Convert image to Paletted PIL image.

        PIL used to not do a very good job at quantization, but I guess
        this has improved a lot (at least in Pillow). I don't think we need
        neuqant (and we can add it later if we really want).
        """
