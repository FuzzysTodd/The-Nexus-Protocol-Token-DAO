from fontTools.ttLib import ttFont
from typing import Iterable

__all__ = ['removeOverlaps']

class RemoveOverlapsError(Exception): ...

def removeOverlaps(font: ttFont.TTFont, glyphNames: Iterable[str] | None = None, removeHinting: bool = True, ignoreErrors: bool = False, *, removeUnusedSubroutines: bool = True) -> None:
    """Simplify glyphs in TTFont by merging overlapping contours.

    Overlapping components are first decomposed to simple contours, then merged.

    Currently this only works for fonts with 'glyf' or 'CFF ' tables.
    Raises NotImplementedError if 'glyf' or 'CFF ' tables are absent.

    Note that removing overlaps invalidates the hinting. By default we drop hinting
    from all glyphs whether or not overlaps are removed from a given one, as it would
    look weird if only some glyphs are left (un)hinted.

    Args:
        font: input TTFont object, modified in place.
        glyphNames: optional iterable of glyph names (str) to remove overlaps from.
            By default, all glyphs in the font are processed.
        removeHinting (bool): set to False to keep hinting for unmodified glyphs.
        ignoreErrors (bool): set to True to ignore errors while removing overlaps,
            thus keeping the tricky glyphs unchanged (fonttools/fonttools#2363).
        removeUnusedSubroutines (bool): set to False to keep unused subroutines
            in CFF table after removing overlaps. Default is to remove them if
            any glyphs are modified.
    """
