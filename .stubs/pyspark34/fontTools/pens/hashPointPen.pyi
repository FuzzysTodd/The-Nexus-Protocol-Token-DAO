from _typeshed import Incomplete
from fontTools.pens.basePen import MissingComponentError as MissingComponentError
from fontTools.pens.pointPen import AbstractPointPen as AbstractPointPen

class HashPointPen(AbstractPointPen):
    '''
    This pen can be used to check if a glyph\'s contents (outlines plus
    components) have changed.

    Components are added as the original outline plus each composite\'s
    transformation.

    Example: You have some TrueType hinting code for a glyph which you want to
    compile. The hinting code specifies a hash value computed with HashPointPen
    that was valid for the glyph\'s outlines at the time the hinting code was
    written. Now you can calculate the hash for the glyph\'s current outlines to
    check if the outlines have changed, which would probably make the hinting
    code invalid.

    > glyph = ufo[name]
    > hash_pen = HashPointPen(glyph.width, ufo)
    > glyph.drawPoints(hash_pen)
    > ttdata = glyph.lib.get("public.truetype.instructions", None)
    > stored_hash = ttdata.get("id", None)  # The hash is stored in the "id" key
    > if stored_hash is None or stored_hash != hash_pen.hash:
    >    logger.error(f"Glyph hash mismatch, glyph \'{name}\' will have no instructions in font.")
    > else:
    >    # The hash values are identical, the outline has not changed.
    >    # Compile the hinting code ...
    >    pass

    If you want to compare a glyph from a source format which supports floating point
    coordinates and transformations against a glyph from a format which has restrictions
    on the precision of floats, e.g. UFO vs. TTF, you must use an appropriate rounding
    function to make the values comparable. For TTF fonts with composites, this
    construct can be used to make the transform values conform to F2Dot14:

    > ttf_hash_pen = HashPointPen(ttf_glyph_width, ttFont.getGlyphSet())
    > ttf_round_pen = RoundingPointPen(ttf_hash_pen, transformRoundFunc=partial(floatToFixedToFloat, precisionBits=14))
    > ufo_hash_pen = HashPointPen(ufo_glyph.width, ufo)
    > ttf_glyph.drawPoints(ttf_round_pen, ttFont["glyf"])
    > ufo_round_pen = RoundingPointPen(ufo_hash_pen, transformRoundFunc=partial(floatToFixedToFloat, precisionBits=14))
    > ufo_glyph.drawPoints(ufo_round_pen)
    > assert ttf_hash_pen.hash == ufo_hash_pen.hash
    '''
    glyphset: Incomplete
    data: Incomplete
    def __init__(self, glyphWidth: int = 0, glyphSet: Incomplete | None = None) -> None: ...
    @property
    def hash(self): ...
    def beginPath(self, identifier: Incomplete | None = None, **kwargs) -> None: ...
    def endPath(self) -> None: ...
    def addPoint(self, pt, segmentType: Incomplete | None = None, smooth: bool = False, name: Incomplete | None = None, identifier: Incomplete | None = None, **kwargs) -> None: ...
    def addComponent(self, baseGlyphName, transformation, identifier: Incomplete | None = None, **kwargs) -> None: ...
