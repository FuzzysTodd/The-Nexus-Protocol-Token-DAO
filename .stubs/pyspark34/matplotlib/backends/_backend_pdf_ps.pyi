from .. import font_manager as font_manager, ft2font as ft2font
from .._afm import AFM as AFM
from ..backend_bases import RendererBase as RendererBase
from _typeshed import Incomplete

def get_glyphs_subset(fontfile, characters):
    """
    Subset a TTF font

    Reads the named fontfile and restricts the font to the characters.
    Returns a serialization of the subset font as file-like object.

    Parameters
    ----------
    symbol : str
        Path to the font file
    characters : str
        Continuous set of characters to include in subset
    """

class CharacterTracker:
    """
    Helper for font subsetting by the pdf and ps backends.

    Maintains a mapping of font paths to the set of character codepoints that
    are being used from that font.
    """
    used: Incomplete
    def __init__(self) -> None: ...
    def track(self, font, s) -> None:
        """Record that string *s* is being typeset using font *font*."""
    def track_glyph(self, font, glyph) -> None:
        """Record that codepoint *glyph* is being typeset using font *font*."""

class RendererPDFPSBase(RendererBase):
    width: Incomplete
    height: Incomplete
    def __init__(self, width, height) -> None: ...
    def flipy(self): ...
    def option_scale_image(self): ...
    def option_image_nocomposite(self): ...
    def get_canvas_width_height(self): ...
    def get_text_width_height_descent(self, s, prop, ismath): ...
