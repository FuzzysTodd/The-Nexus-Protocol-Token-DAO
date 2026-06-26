from _typeshed import Incomplete
from fontTools.merge.options import Options as Options

__all__ = ['Options', 'Merger', 'main']

class Merger:
    """Font merger.

    This class merges multiple files into a single OpenType font, taking into
    account complexities such as OpenType layout (``GSUB``/``GPOS``) tables and
    cross-font metrics (e.g. ``hhea.ascent`` is set to the maximum value across
    all the fonts).

    If multiple glyphs map to the same Unicode value, and the glyphs are considered
    sufficiently different (that is, they differ in any of paths, widths, or
    height), then subsequent glyphs are renamed and a lookup in the ``locl``
    feature will be created to disambiguate them. For example, if the arguments
    are an Arabic font and a Latin font and both contain a set of parentheses,
    the Latin glyphs will be renamed to ``parenleft#1`` and ``parenright#1``,
    and a lookup will be inserted into the to ``locl`` feature (creating it if
    necessary) under the ``latn`` script to substitute ``parenleft`` with
    ``parenleft#1`` etc.

    Restrictions:

    - All fonts must have the same units per em.
    - If duplicate glyph disambiguation takes place as described above then the
            fonts must have a ``GSUB`` table.

    Attributes:
            options: Currently unused.
    """
    options: Incomplete
    def __init__(self, options: Incomplete | None = None) -> None: ...
    duplicateGlyphsPerFont: Incomplete
    fonts: Incomplete
    def merge(self, fontfiles):
        """Merges fonts together.

        Args:
                fontfiles: A list of file names to be merged

        Returns:
                A :class:`fontTools.ttLib.TTFont` object. Call the ``save`` method on
                this to write it out to an OTF file.
        """
    def mergeObjects(self, returnTable, logic, tables): ...

def main(args: Incomplete | None = None):
    """Merge multiple fonts into one"""
