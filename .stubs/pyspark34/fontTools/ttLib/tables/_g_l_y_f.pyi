from . import DefaultTable as DefaultTable, ttProgram as ttProgram
from _typeshed import Incomplete
from enum import IntFlag as IntFlag
from fontTools import ttLib as ttLib, version as version
from fontTools.misc import sstruct as sstruct, xmlWriter as xmlWriter
from fontTools.misc.arrayTools import pointInRect as pointInRect, updateBounds as updateBounds
from fontTools.misc.bezierTools import calcQuadraticBounds as calcQuadraticBounds
from fontTools.misc.filenames import userNameToFileName as userNameToFileName
from fontTools.misc.loggingTools import deprecateFunction as deprecateFunction
from fontTools.misc.roundTools import noRound as noRound, otRound as otRound
from fontTools.misc.textTools import pad as pad, safeEval as safeEval, tostr as tostr
from fontTools.misc.transform import DecomposedTransform as DecomposedTransform
from fontTools.misc.vector import Vector as Vector
from typing import NamedTuple, Set

log: Incomplete
SCALE_COMPONENT_OFFSET_DEFAULT: int

class table__g_l_y_f(DefaultTable.DefaultTable):
    '''Glyph Data Table

    This class represents the `glyf <https://docs.microsoft.com/en-us/typography/opentype/spec/glyf>`_
    table, which contains outlines for glyphs in TrueType format. In many cases,
    it is easier to access and manipulate glyph outlines through the ``GlyphSet``
    object returned from :py:meth:`fontTools.ttLib.ttFont.getGlyphSet`::

                    >> from fontTools.pens.boundsPen import BoundsPen
                    >> glyphset = font.getGlyphSet()
                    >> bp = BoundsPen(glyphset)
                    >> glyphset["A"].draw(bp)
                    >> bp.bounds
                    (19, 0, 633, 716)

    However, this class can be used for low-level access to the ``glyf`` table data.
    Objects of this class support dictionary-like access, mapping glyph names to
    :py:class:`Glyph` objects::

                    >> glyf = font["glyf"]
                    >> len(glyf["Aacute"].components)
                    2

    Note that when adding glyphs to the font via low-level access to the ``glyf``
    table, the new glyphs must also be added to the ``hmtx``/``vmtx`` table::

                    >> font["glyf"]["divisionslash"] = Glyph()
                    >> font["hmtx"]["divisionslash"] = (640, 0)

    '''
    dependencies: Incomplete
    padding: int
    axisTags: Incomplete
    glyphs: Incomplete
    glyphOrder: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    def ensureDecompiled(self, recurse: bool = False) -> None: ...
    def compile(self, ttFont): ...
    def toXML(self, writer, ttFont, splitGlyphs: bool = False) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
    def setGlyphOrder(self, glyphOrder) -> None:
        """Sets the glyph order

        Args:
                glyphOrder ([str]): List of glyph names in order.
        """
    def getGlyphName(self, glyphID):
        """Returns the name for the glyph with the given ID.

        Raises a ``KeyError`` if the glyph name is not found in the font.
        """
    def getGlyphID(self, glyphName):
        """Returns the ID of the glyph with the given name.

        Raises a ``ValueError`` if the glyph is not found in the font.
        """
    def removeHinting(self) -> None:
        """Removes TrueType hints from all glyphs in the glyphset.

        See :py:meth:`Glyph.removeHinting`.
        """
    def keys(self): ...
    def has_key(self, glyphName): ...
    __contains__ = has_key
    def get(self, glyphName, default: Incomplete | None = None): ...
    def __getitem__(self, glyphName): ...
    def __setitem__(self, glyphName, glyph) -> None: ...
    def __delitem__(self, glyphName) -> None: ...
    def __len__(self) -> int: ...
    def getPhantomPoints(self, glyphName, ttFont, defaultVerticalOrigin: Incomplete | None = None):
        """Old public name for self._getPhantomPoints().
        See: https://github.com/fonttools/fonttools/pull/2266"""
    def getCoordinatesAndControls(self, glyphName, ttFont, defaultVerticalOrigin: Incomplete | None = None):
        """Old public name for self._getCoordinatesAndControls().
        See: https://github.com/fonttools/fonttools/pull/2266"""
    def setCoordinates(self, glyphName, ttFont) -> None:
        """Old public name for self._setCoordinates().
        See: https://github.com/fonttools/fonttools/pull/2266"""

class _GlyphControls(NamedTuple):
    numberOfContours: Incomplete
    endPts: Incomplete
    flags: Incomplete
    components: Incomplete

glyphHeaderFormat: str
flagOnCurve: int
flagXShort: int
flagYShort: int
flagRepeat: int
flagXsame: int
flagYsame: int
flagOverlapSimple: int
flagCubic: int
keepFlags: Incomplete

def flagBest(x, y, onCurve):
    """For a given x,y delta pair, returns the flag that packs this pair
    most efficiently, as well as the number of byte cost of such flag."""
def flagFits(newFlag, oldFlag, mask): ...
def flagSupports(newFlag, oldFlag): ...
def flagEncodeCoord(flag, mask, coord, coordBytes) -> None: ...
def flagEncodeCoords(flag, x, y, xBytes, yBytes) -> None: ...

ARG_1_AND_2_ARE_WORDS: int
ARGS_ARE_XY_VALUES: int
ROUND_XY_TO_GRID: int
WE_HAVE_A_SCALE: int
NON_OVERLAPPING: int
MORE_COMPONENTS: int
WE_HAVE_AN_X_AND_Y_SCALE: int
WE_HAVE_A_TWO_BY_TWO: int
WE_HAVE_INSTRUCTIONS: int
USE_MY_METRICS: int
OVERLAP_COMPOUND: int
SCALED_COMPONENT_OFFSET: int
UNSCALED_COMPONENT_OFFSET: int

class CompositeMaxpValues(NamedTuple):
    nPoints: Incomplete
    nContours: Incomplete
    maxComponentDepth: Incomplete

class Glyph:
    '''This class represents an individual TrueType glyph.

    TrueType glyph objects come in two flavours: simple and composite. Simple
    glyph objects contain contours, represented via the ``.coordinates``,
    ``.flags``, ``.numberOfContours``, and ``.endPtsOfContours`` attributes;
    composite glyphs contain components, available through the ``.components``
    attributes.

    Because the ``.coordinates`` attribute (and other simple glyph attributes mentioned
    above) is only set on simple glyphs and the ``.components`` attribute is only
    set on composite glyphs, it is necessary to use the :py:meth:`isComposite`
    method to test whether a glyph is simple or composite before attempting to
    access its data.

    For a composite glyph, the components can also be accessed via array-like access::

            >> assert(font["glyf"]["Aacute"].isComposite())
            >> font["glyf"]["Aacute"][0]
            <fontTools.ttLib.tables._g_l_y_f.GlyphComponent at 0x1027b2ee0>

    '''
    numberOfContours: int
    data: Incomplete
    def __init__(self, data: bytes = b'') -> None: ...
    def compact(self, glyfTable, recalcBBoxes: bool = True) -> None: ...
    def expand(self, glyfTable) -> None: ...
    def compile(self, glyfTable, recalcBBoxes: bool = True, *, boundsDone: Incomplete | None = None): ...
    def toXML(self, writer, ttFont) -> None: ...
    coordinates: Incomplete
    flags: Incomplete
    endPtsOfContours: Incomplete
    components: Incomplete
    program: Incomplete
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
    def getCompositeMaxpValues(self, glyfTable, maxComponentDepth: int = 1): ...
    def getMaxpValues(self): ...
    def decompileComponents(self, data, glyfTable) -> None: ...
    def decompileCoordinates(self, data) -> None: ...
    def decompileCoordinatesRaw(self, nCoordinates, data, pos: int = 0): ...
    def compileComponents(self, glyfTable): ...
    def compileCoordinates(self): ...
    def compileDeltasGreedy(self, flags, deltas): ...
    def compileDeltasOptimal(self, flags, deltas): ...
    def recalcBounds(self, glyfTable, *, boundsDone: Incomplete | None = None) -> None:
        """Recalculates the bounds of the glyph.

        Each glyph object stores its bounding box in the
        ``xMin``/``yMin``/``xMax``/``yMax`` attributes. These bounds must be
        recomputed when the ``coordinates`` change. The ``table__g_l_y_f`` bounds
        must be provided to resolve component bounds.
        """
    def tryRecalcBoundsComposite(self, glyfTable, *, boundsDone: Incomplete | None = None):
        """Try recalculating the bounds of a composite glyph that has
        certain constrained properties. Namely, none of the components
        have a transform other than an integer translate, and none
        uses the anchor points.

        Each glyph object stores its bounding box in the
        ``xMin``/``yMin``/``xMax``/``yMax`` attributes. These bounds must be
        recomputed when the ``coordinates`` change. The ``table__g_l_y_f`` bounds
        must be provided to resolve component bounds.

        Return True if bounds were calculated, False otherwise.
        """
    def isComposite(self):
        """Test whether a glyph has components"""
    def getCoordinates(self, glyfTable):
        '''Return the coordinates, end points and flags

        This method returns three values: A :py:class:`GlyphCoordinates` object,
        a list of the indexes of the final points of each contour (allowing you
        to split up the coordinates list into contours) and a list of flags.

        On simple glyphs, this method returns information from the glyph\'s own
        contours; on composite glyphs, it "flattens" all components recursively
        to return a list of coordinates representing all the components involved
        in the glyph.

        To interpret the flags for each point, see the "Simple Glyph Flags"
        section of the `glyf table specification <https://docs.microsoft.com/en-us/typography/opentype/spec/glyf#simple-glyph-description>`.
        '''
    def getComponentNames(self, glyfTable):
        """Returns a list of names of component glyphs used in this glyph

        This method can be used on simple glyphs (in which case it returns an
        empty list) or composite glyphs.
        """
    def trim(self, remove_hinting: bool = False) -> None:
        """Remove padding and, if requested, hinting, from a glyph.
        This works on both expanded and compacted glyphs, without
        expanding it."""
    def removeHinting(self) -> None:
        """Removes TrueType hinting instructions from the glyph."""
    def draw(self, pen, glyfTable, offset: int = 0):
        """Draws the glyph using the supplied pen object.

        Arguments:
                pen: An object conforming to the pen protocol.
                glyfTable: A :py:class:`table__g_l_y_f` object, to resolve components.
                offset (int): A horizontal offset. If provided, all coordinates are
                        translated by this offset.
        """
    def drawPoints(self, pen, glyfTable, offset: int = 0) -> None:
        """Draw the glyph using the supplied pointPen. As opposed to Glyph.draw(),
        this will not change the point indices.
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...

def dropImpliedOnCurvePoints(*interpolatable_glyphs: Glyph) -> Set[int]:
    """Drop impliable on-curve points from the (simple) glyph or glyphs.

    In TrueType glyf outlines, on-curve points can be implied when they are located at
    the midpoint of the line connecting two consecutive off-curve points.

    If more than one glyphs are passed, these are assumed to be interpolatable masters
    of the same glyph impliable, and thus only the on-curve points that are impliable
    for all of them will actually be implied.
    Composite glyphs or empty glyphs are skipped, only simple glyphs with 1 or more
    contours are considered.
    The input glyph(s) is/are modified in-place.

    Args:
        interpolatable_glyphs: The glyph or glyphs to modify in-place.

    Returns:
        The set of point indices that were dropped if any.

    Raises:
        ValueError if simple glyphs are not in fact interpolatable because they have
        different point flags or number of contours.

    Reference:
    https://developer.apple.com/fonts/TrueType-Reference-Manual/RM01/Chap1.html
    """

class GlyphComponent:
    '''Represents a component within a composite glyph.

    The component is represented internally with four attributes: ``glyphName``,
    ``x``, ``y`` and ``transform``. If there is no "two-by-two" matrix (i.e
    no scaling, reflection, or rotation; only translation), the ``transform``
    attribute is not present.
    '''
    def __init__(self) -> None: ...
    def getComponentInfo(self):
        """Return information about the component

        This method returns a tuple of two values: the glyph name of the component's
        base glyph, and a transformation matrix. As opposed to accessing the attributes
        directly, ``getComponentInfo`` always returns a six-element tuple of the
        component's transformation matrix, even when the two-by-two ``.transform``
        matrix is not present.
        """
    flags: Incomplete
    glyphName: Incomplete
    transform: Incomplete
    def decompile(self, data, glyfTable): ...
    def compile(self, more, haveInstructions, glyfTable): ...
    def toXML(self, writer, ttFont) -> None: ...
    firstPt: Incomplete
    secondPt: Incomplete
    x: Incomplete
    y: Incomplete
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class GlyphCoordinates:
    """A list of glyph coordinates.

    Unlike an ordinary list, this is a numpy-like matrix object which supports
    matrix addition, scalar multiplication and other operations described below.
    """
    def __init__(self, iterable=[]) -> None: ...
    @property
    def array(self):
        """Returns the underlying array of coordinates"""
    @staticmethod
    def zeros(count):
        """Creates a new ``GlyphCoordinates`` object with all coordinates set to (0,0)"""
    def copy(self):
        """Creates a new ``GlyphCoordinates`` object which is a copy of the current one."""
    def __len__(self) -> int:
        """Returns the number of coordinates in the array."""
    def __getitem__(self, k):
        """Returns a two element tuple (x,y)"""
    def __setitem__(self, k, v) -> None:
        """Sets a point's coordinates to a two element tuple (x,y)"""
    def __delitem__(self, i) -> None:
        """Removes a point from the list"""
    def append(self, p) -> None: ...
    def extend(self, iterable) -> None: ...
    def toInt(self, *, round=...) -> None: ...
    def calcBounds(self): ...
    def calcIntBounds(self, round=...): ...
    def relativeToAbsolute(self) -> None: ...
    def absoluteToRelative(self) -> None: ...
    def translate(self, p) -> None:
        """
        >>> GlyphCoordinates([(1,2)]).translate((.5,0))
        """
    def scale(self, p) -> None:
        """
        >>> GlyphCoordinates([(1,2)]).scale((.5,0))
        """
    def transform(self, t) -> None:
        """
        >>> GlyphCoordinates([(1,2)]).transform(((.5,0),(.2,.5)))
        """
    def __eq__(self, other):
        """
        >>> g = GlyphCoordinates([(1,2)])
        >>> g2 = GlyphCoordinates([(1.0,2)])
        >>> g3 = GlyphCoordinates([(1.5,2)])
        >>> g == g2
        True
        >>> g == g3
        False
        >>> g2 == g3
        False
        """
    def __ne__(self, other):
        """
        >>> g = GlyphCoordinates([(1,2)])
        >>> g2 = GlyphCoordinates([(1.0,2)])
        >>> g3 = GlyphCoordinates([(1.5,2)])
        >>> g != g2
        False
        >>> g != g3
        True
        >>> g2 != g3
        True
        """
    def __pos__(self):
        """
        >>> g = GlyphCoordinates([(1,2)])
        >>> g
        GlyphCoordinates([(1, 2)])
        >>> g2 = +g
        >>> g2
        GlyphCoordinates([(1, 2)])
        >>> g2.translate((1,0))
        >>> g2
        GlyphCoordinates([(2, 2)])
        >>> g
        GlyphCoordinates([(1, 2)])
        """
    def __neg__(self):
        """
        >>> g = GlyphCoordinates([(1,2)])
        >>> g
        GlyphCoordinates([(1, 2)])
        >>> g2 = -g
        >>> g2
        GlyphCoordinates([(-1, -2)])
        >>> g
        GlyphCoordinates([(1, 2)])
        """
    def __round__(self, *, round=...): ...
    def __add__(self, other): ...
    def __sub__(self, other): ...
    def __mul__(self, other): ...
    def __truediv__(self, other): ...
    __radd__ = __add__
    __rmul__ = __mul__
    def __rsub__(self, other): ...
    def __iadd__(self, other):
        """
        >>> g = GlyphCoordinates([(1,2)])
        >>> g += (.5,0)
        >>> g
        GlyphCoordinates([(1.5, 2)])
        >>> g2 = GlyphCoordinates([(3,4)])
        >>> g += g2
        >>> g
        GlyphCoordinates([(4.5, 6)])
        """
    def __isub__(self, other):
        """
        >>> g = GlyphCoordinates([(1,2)])
        >>> g -= (.5,0)
        >>> g
        GlyphCoordinates([(0.5, 2)])
        >>> g2 = GlyphCoordinates([(3,4)])
        >>> g -= g2
        >>> g
        GlyphCoordinates([(-2.5, -2)])
        """
    def __imul__(self, other):
        """
        >>> g = GlyphCoordinates([(1,2)])
        >>> g *= (2,.5)
        >>> g *= 2
        >>> g
        GlyphCoordinates([(4, 2)])
        >>> g = GlyphCoordinates([(1,2)])
        >>> g *= 2
        >>> g
        GlyphCoordinates([(2, 4)])
        """
    def __itruediv__(self, other):
        """
        >>> g = GlyphCoordinates([(1,3)])
        >>> g /= (.5,1.5)
        >>> g /= 2
        >>> g
        GlyphCoordinates([(1, 1)])
        """
    def __bool__(self) -> bool:
        """
        >>> g = GlyphCoordinates([])
        >>> bool(g)
        False
        >>> g = GlyphCoordinates([(0,0), (0.,0)])
        >>> bool(g)
        True
        >>> g = GlyphCoordinates([(0,0), (1,0)])
        >>> bool(g)
        True
        >>> g = GlyphCoordinates([(0,.5), (0,0)])
        >>> bool(g)
        True
        """
    __nonzero__ = __bool__
