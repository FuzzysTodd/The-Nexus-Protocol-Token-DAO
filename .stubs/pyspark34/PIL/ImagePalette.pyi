from . import GimpGradientFile as GimpGradientFile, GimpPaletteFile as GimpPaletteFile, ImageColor as ImageColor, PaletteFile as PaletteFile
from _typeshed import Incomplete

class ImagePalette:
    '''
    Color palette for palette mapped images

    :param mode: The mode to use for the palette. See:
        :ref:`concept-modes`. Defaults to "RGB"
    :param palette: An optional palette. If given, it must be a bytearray,
        an array or a list of ints between 0-255. The list must consist of
        all channels for one color followed by the next color (e.g. RGBRGBRGB).
        Defaults to an empty palette.
    '''
    mode: Incomplete
    rawmode: Incomplete
    dirty: Incomplete
    def __init__(self, mode: str = 'RGB', palette: Incomplete | None = None) -> None: ...
    @property
    def palette(self): ...
    @palette.setter
    def palette(self, palette) -> None: ...
    @property
    def colors(self): ...
    @colors.setter
    def colors(self, colors) -> None: ...
    def copy(self): ...
    def getdata(self):
        """
        Get palette contents in format suitable for the low-level
        ``im.putpalette`` primitive.

        .. warning:: This method is experimental.
        """
    def tobytes(self):
        """Convert palette to bytes.

        .. warning:: This method is experimental.
        """
    tostring = tobytes
    def getcolor(self, color, image: Incomplete | None = None):
        """Given an rgb tuple, allocate palette entry.

        .. warning:: This method is experimental.
        """
    def save(self, fp) -> None:
        """Save palette to text file.

        .. warning:: This method is experimental.
        """

def raw(rawmode, data): ...
def make_linear_lut(black, white): ...
def make_gamma_lut(exp): ...
def negative(mode: str = 'RGB'): ...
def random(mode: str = 'RGB'): ...
def sepia(white: str = '#fff0c0'): ...
def wedge(mode: str = 'RGB'): ...
def load(filename): ...
