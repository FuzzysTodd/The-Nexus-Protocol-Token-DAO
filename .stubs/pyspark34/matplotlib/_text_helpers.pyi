from .ft2font import KERNING_DEFAULT as KERNING_DEFAULT, LOAD_NO_HINTING as LOAD_NO_HINTING
from _typeshed import Incomplete
from collections.abc import Generator

LayoutItem: Incomplete

def warn_on_missing_glyph(codepoint) -> None: ...
def layout(string, font, *, kern_mode=...) -> Generator[Incomplete, None, None]:
    """
    Render *string* with *font*.  For each character in *string*, yield a
    (glyph-index, x-position) pair.  When such a pair is yielded, the font's
    glyph is set to the corresponding character.

    Parameters
    ----------
    string : str
        The string to be rendered.
    font : FT2Font
        The font.
    kern_mode : int
        A FreeType kerning mode.

    Yields
    ------
    glyph_index : int
    x_position : float
    """
