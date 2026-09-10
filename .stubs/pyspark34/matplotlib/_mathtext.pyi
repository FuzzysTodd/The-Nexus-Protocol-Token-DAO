import enum
from . import cbook as cbook
from ._mathtext_data import latex_to_bakoma as latex_to_bakoma, stix_glyph_fixes as stix_glyph_fixes, stix_virtual_fonts as stix_virtual_fonts, tex2uni as tex2uni
from .font_manager import FontProperties as FontProperties, findfont as findfont, get_font as get_font
from .ft2font import FT2Image as FT2Image, KERNING_DEFAULT as KERNING_DEFAULT
from _typeshed import Incomplete
from typing import NamedTuple

def get_unicode_index(symbol, math: bool = False):
    """
    Return the integer index (from the Unicode table) of *symbol*.

    Parameters
    ----------
    symbol : str
        A single (Unicode) character, a TeX command (e.g. r'\\pi') or a Type1
        symbol name (e.g. 'phi').
    math : bool, default: False
        If True (deprecated), replace ASCII hyphen-minus by Unicode minus.
    """

class VectorParse(NamedTuple):
    width: Incomplete
    height: Incomplete
    depth: Incomplete
    glyphs: Incomplete
    rects: Incomplete

class RasterParse(NamedTuple):
    ox: Incomplete
    oy: Incomplete
    width: Incomplete
    height: Incomplete
    depth: Incomplete
    image: Incomplete

class Output:
    """
    Result of `ship`\\ping a box: lists of positioned glyphs and rectangles.

    This class is not exposed to end users, but converted to a `VectorParse` or
    a `RasterParse` by `.MathTextParser.parse`.
    """
    box: Incomplete
    glyphs: Incomplete
    rects: Incomplete
    def __init__(self, box) -> None: ...
    def to_vector(self): ...
    def to_raster(self): ...

class Fonts:
    """
    An abstract base class for a system of fonts to use for mathtext.

    The class must be able to take symbol keys and font file names and
    return the character metrics.  It also delegates to a backend class
    to do the actual drawing.
    """
    default_font_prop: Incomplete
    load_glyph_flags: Incomplete
    def __init__(self, default_font_prop, load_glyph_flags) -> None:
        """
        Parameters
        ----------
        default_font_prop : `~.font_manager.FontProperties`
            The default non-math font, or the base font for Unicode (generic)
            font rendering.
        load_glyph_flags : int
            Flags passed to the glyph loader (e.g. ``FT_Load_Glyph`` and
            ``FT_Load_Char`` for FreeType-based fonts).
        """
    def get_kern(self, font1, fontclass1, sym1, fontsize1, font2, fontclass2, sym2, fontsize2, dpi):
        """
        Get the kerning distance for font between *sym1* and *sym2*.

        See `~.Fonts.get_metrics` for a detailed description of the parameters.
        """
    def get_metrics(self, font, font_class, sym, fontsize, dpi):
        '''
        Parameters
        ----------
        font : str
            One of the TeX font names: "tt", "it", "rm", "cal", "sf", "bf",
            "default", "regular", "bb", "frak", "scr".  "default" and "regular"
            are synonyms and use the non-math font.
        font_class : str
            One of the TeX font names (as for *font*), but **not** "bb",
            "frak", or "scr".  This is used to combine two font classes.  The
            only supported combination currently is ``get_metrics("frak", "bf",
            ...)``.
        sym : str
            A symbol in raw TeX form, e.g., "1", "x", or "\\sigma".
        fontsize : float
            Font size in points.
        dpi : float
            Rendering dots-per-inch.

        Returns
        -------
        object

            The returned object has the following attributes (all floats,
            except *slanted*):

            - *advance*: The advance distance (in points) of the glyph.
            - *height*: The height of the glyph in points.
            - *width*: The width of the glyph in points.
            - *xmin*, *xmax*, *ymin*, *ymax*: The ink rectangle of the glyph
            - *iceberg*: The distance from the baseline to the top of the
              glyph.  (This corresponds to TeX\'s definition of "height".)
            - *slanted*: Whether the glyph should be considered as "slanted"
              (currently used for kerning sub/superscripts).
        '''
    def render_glyph(self, output, ox, oy, font, font_class, sym, fontsize, dpi) -> None:
        """
        At position (*ox*, *oy*), draw the glyph specified by the remaining
        parameters (see `get_metrics` for their detailed description).
        """
    def render_rect_filled(self, output, x1, y1, x2, y2) -> None:
        """
        Draw a filled rectangle from (*x1*, *y1*) to (*x2*, *y2*).
        """
    def get_xheight(self, font, fontsize, dpi) -> None:
        """
        Get the xheight for the given *font* and *fontsize*.
        """
    def get_underline_thickness(self, font, fontsize, dpi) -> None:
        """
        Get the line thickness that matches the given font.  Used as a
        base unit for drawing lines such as in a fraction or radical.
        """
    def get_used_characters(self):
        """
        Get the set of characters that were used in the math
        expression.  Used by backends that need to subset fonts so
        they know which glyphs to include.
        """
    def get_sized_alternatives_for_symbol(self, fontname, sym):
        """
        Override if your font provides multiple sizes of the same
        symbol.  Should return a list of symbols matching *sym* in
        various sizes.  The expression renderer will select the most
        appropriate size for a given situation from this list.
        """

class TruetypeFonts(Fonts):
    """
    A generic base class for all font setups that use Truetype fonts
    (through FT2Font).
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def get_xheight(self, fontname, fontsize, dpi): ...
    def get_underline_thickness(self, font, fontsize, dpi): ...
    def get_kern(self, font1, fontclass1, sym1, fontsize1, font2, fontclass2, sym2, fontsize2, dpi): ...

class BakomaFonts(TruetypeFonts):
    """
    Use the Bakoma TrueType fonts for rendering.

    Symbols are strewn about a number of font files, each of which has
    its own proprietary 8-bit encoding.
    """
    fontmap: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def get_sized_alternatives_for_symbol(self, fontname, sym): ...

class UnicodeFonts(TruetypeFonts):
    '''
    An abstract base class for handling Unicode fonts.

    While some reasonably complete Unicode fonts (such as DejaVu) may
    work in some situations, the only Unicode font I\'m aware of with a
    complete set of math symbols is STIX.

    This class will "fallback" on the Bakoma fonts when a required
    symbol can not be found in the font.
    '''
    fontmap: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def get_sized_alternatives_for_symbol(self, fontname, sym): ...

class DejaVuFonts(UnicodeFonts):
    bakoma: Incomplete
    fontmap: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class DejaVuSerifFonts(DejaVuFonts):
    """
    A font handling class for the DejaVu Serif fonts

    If a glyph is not found it will fallback to Stix Serif
    """
class DejaVuSansFonts(DejaVuFonts):
    """
    A font handling class for the DejaVu Sans fonts

    If a glyph is not found it will fallback to Stix Sans
    """

class StixFonts(UnicodeFonts):
    '''
    A font handling class for the STIX fonts.

    In addition to what UnicodeFonts provides, this class:

    - supports "virtual fonts" which are complete alpha numeric
      character sets with different font styles at special Unicode
      code points, such as "Blackboard".

    - handles sized alternative characters for the STIXSizeX fonts.
    '''
    fontmap: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def get_sized_alternatives_for_symbol(self, fontname, sym): ...

class StixSansFonts(StixFonts):
    """
    A font handling class for the STIX fonts (that uses sans-serif
    characters by default).
    """

SHRINK_FACTOR: float
NUM_SIZE_LEVELS: int

class FontConstantsBase:
    """
    A set of constants that controls how certain things, such as sub-
    and superscripts are laid out.  These are all metrics that can't
    be reliably retrieved from the font metrics in the font itself.
    """
    script_space: float
    subdrop: float
    sup1: float
    sub1: float
    sub2: float
    delta: float
    delta_slanted: float
    delta_integral: float

class ComputerModernFontConstants(FontConstantsBase):
    script_space: float
    subdrop: float
    sup1: float
    sub1: float
    sub2: float
    delta: float
    delta_slanted: float
    delta_integral: float

class STIXFontConstants(FontConstantsBase):
    script_space: float
    sup1: float
    sub2: float
    delta: float
    delta_slanted: float
    delta_integral: float

class STIXSansFontConstants(FontConstantsBase):
    script_space: float
    sup1: float
    delta_slanted: float
    delta_integral: float

class DejaVuSerifFontConstants(FontConstantsBase): ...
class DejaVuSansFontConstants(FontConstantsBase): ...

class Node:
    """A node in the TeX box model."""
    size: int
    def __init__(self) -> None: ...
    def get_kerning(self, next): ...
    def shrink(self) -> None:
        """
        Shrinks one level smaller.  There are only three levels of
        sizes, after which things will no longer get smaller.
        """
    def render(self, output, x, y) -> None:
        """Render this node."""

class Box(Node):
    """A node with a physical location."""
    width: Incomplete
    height: Incomplete
    depth: Incomplete
    def __init__(self, width, height, depth) -> None: ...
    def shrink(self) -> None: ...
    def render(self, output, x1, y1, x2, y2) -> None: ...

class Vbox(Box):
    """A box with only height (zero width)."""
    def __init__(self, height, depth) -> None: ...

class Hbox(Box):
    """A box with only width (zero height and depth)."""
    def __init__(self, width) -> None: ...

class Char(Node):
    """
    A single character.

    Unlike TeX, the font information and metrics are stored with each `Char`
    to make it easier to lookup the font metrics when needed.  Note that TeX
    boxes have a width, height, and depth, unlike Type1 and TrueType which use
    a full bounding box and an advance in the x-direction.  The metrics must
    be converted to the TeX model, and the advance (if different from width)
    must be converted into a `Kern` node when the `Char` is added to its parent
    `Hlist`.
    """
    c: Incomplete
    fontset: Incomplete
    font: Incomplete
    font_class: Incomplete
    fontsize: Incomplete
    dpi: Incomplete
    def __init__(self, c, state) -> None: ...
    def is_slanted(self): ...
    def get_kerning(self, next):
        """
        Return the amount of kerning between this and the given character.

        This method is called when characters are strung together into `Hlist`
        to create `Kern` nodes.
        """
    def render(self, output, x, y) -> None: ...
    def shrink(self) -> None: ...

class Accent(Char):
    """
    The font metrics need to be dealt with differently for accents,
    since they are already offset correctly from the baseline in
    TrueType fonts.
    """
    def shrink(self) -> None: ...
    def render(self, output, x, y) -> None: ...

class List(Box):
    """A list of nodes (either horizontal or vertical)."""
    shift_amount: float
    children: Incomplete
    glue_set: float
    glue_sign: int
    glue_order: int
    def __init__(self, elements) -> None: ...
    def shrink(self) -> None: ...

class Hlist(List):
    """A horizontal list of boxes."""
    def __init__(self, elements, w: float = 0.0, m: str = 'additional', do_kern: bool = True) -> None: ...
    children: Incomplete
    def kern(self) -> None:
        """
        Insert `Kern` nodes between `Char` nodes to set kerning.

        The `Char` nodes themselves determine the amount of kerning they need
        (in `~Char.get_kerning`), and this function just creates the correct
        linked list.
        """
    height: Incomplete
    depth: Incomplete
    width: Incomplete
    glue_sign: int
    glue_order: int
    glue_ratio: float
    def hpack(self, w: float = 0.0, m: str = 'additional') -> None:
        """
        Compute the dimensions of the resulting boxes, and adjust the glue if
        one of those dimensions is pre-specified.  The computed sizes normally
        enclose all of the material inside the new box; but some items may
        stick out if negative glue is used, if the box is overfull, or if a
        ``\\vbox`` includes other boxes that have been shifted left.

        Parameters
        ----------
        w : float, default: 0
            A width.
        m : {'exactly', 'additional'}, default: 'additional'
            Whether to produce a box whose width is 'exactly' *w*; or a box
            with the natural width of the contents, plus *w* ('additional').

        Notes
        -----
        The defaults produce a box with the natural width of the contents.
        """

class Vlist(List):
    """A vertical list of boxes."""
    def __init__(self, elements, h: float = 0.0, m: str = 'additional') -> None: ...
    width: Incomplete
    depth: Incomplete
    height: Incomplete
    glue_sign: int
    glue_order: int
    glue_ratio: float
    def vpack(self, h: float = 0.0, m: str = 'additional', l=...) -> None:
        """
        Compute the dimensions of the resulting boxes, and to adjust the glue
        if one of those dimensions is pre-specified.

        Parameters
        ----------
        h : float, default: 0
            A height.
        m : {'exactly', 'additional'}, default: 'additional'
            Whether to produce a box whose height is 'exactly' *h*; or a box
            with the natural height of the contents, plus *h* ('additional').
        l : float, default: np.inf
            The maximum height.

        Notes
        -----
        The defaults produce a box with the natural height of the contents.
        """

class Rule(Box):
    '''
    A solid black rectangle.

    It has *width*, *depth*, and *height* fields just as in an `Hlist`.
    However, if any of these dimensions is inf, the actual value will be
    determined by running the rule up to the boundary of the innermost
    enclosing box.  This is called a "running dimension".  The width is never
    running in an `Hlist`; the height and depth are never running in a `Vlist`.
    '''
    fontset: Incomplete
    def __init__(self, width, height, depth, state) -> None: ...
    def render(self, output, x, y, w, h) -> None: ...

class Hrule(Rule):
    """Convenience class to create a horizontal rule."""
    def __init__(self, state, thickness: Incomplete | None = None) -> None: ...

class Vrule(Rule):
    """Convenience class to create a vertical rule."""
    def __init__(self, state) -> None: ...

class _GlueSpec(NamedTuple):
    width: Incomplete
    stretch: Incomplete
    stretch_order: Incomplete
    shrink: Incomplete
    shrink_order: Incomplete

class Glue(Node):
    """
    Most of the information in this object is stored in the underlying
    ``_GlueSpec`` class, which is shared between multiple glue objects.
    (This is a memory optimization which probably doesn't matter anymore, but
    it's easier to stick to what TeX does.)
    """
    glue_spec: Incomplete
    def __init__(self, glue_type) -> None: ...
    def shrink(self) -> None: ...

class HCentered(Hlist):
    """
    A convenience class to create an `Hlist` whose contents are
    centered within its enclosing box.
    """
    def __init__(self, elements) -> None: ...

class VCentered(Vlist):
    """
    A convenience class to create a `Vlist` whose contents are
    centered within its enclosing box.
    """
    def __init__(self, elements) -> None: ...

class Kern(Node):
    """
    A `Kern` node has a width field to specify a (normally
    negative) amount of spacing. This spacing correction appears in
    horizontal lists between letters like A and V when the font
    designer said that it looks better to move them closer together or
    further apart. A kern node can also appear in a vertical list,
    when its *width* denotes additional spacing in the vertical
    direction.
    """
    height: int
    depth: int
    width: Incomplete
    def __init__(self, width) -> None: ...
    def shrink(self) -> None: ...

class AutoHeightChar(Hlist):
    """
    A character as close to the given height and depth as possible.

    When using a font with multiple height versions of some characters (such as
    the BaKoMa fonts), the correct glyph will be selected, otherwise this will
    always just return a scaled version of the glyph.
    """
    shift_amount: Incomplete
    def __init__(self, c, height, depth, state, always: bool = False, factor: Incomplete | None = None) -> None: ...

class AutoWidthChar(Hlist):
    """
    A character as close to the given width as possible.

    When using a font with multiple width versions of some characters (such as
    the BaKoMa fonts), the correct glyph will be selected, otherwise this will
    always just return a scaled version of the glyph.
    """
    width: Incomplete
    def __init__(self, c, width, state, always: bool = False, char_class=...) -> None: ...

def ship(box, xy=(0, 0)):
    """
    Ship out *box* at offset *xy*, converting it to an `Output`.

    Since boxes can be inside of boxes inside of boxes, the main work of `ship`
    is done by two mutually recursive routines, `hlist_out` and `vlist_out`,
    which traverse the `Hlist` nodes and `Vlist` nodes inside of horizontal
    and vertical boxes.  The global variables used in TeX to store state as it
    processes have become local variables here.
    """
def Error(msg):
    """Helper class to raise parser errors."""

class ParserState:
    '''
    Parser state.

    States are pushed and popped from a stack as necessary, and the "current"
    state is always at the top of the stack.

    Upon entering and leaving a group { } or math/non-math, the stack is pushed
    and popped accordingly.
    '''
    fontset: Incomplete
    font_class: Incomplete
    fontsize: Incomplete
    dpi: Incomplete
    def __init__(self, fontset, font, font_class, fontsize, dpi) -> None: ...
    def copy(self): ...
    @property
    def font(self): ...
    @font.setter
    def font(self, name) -> None: ...
    def get_current_underline_thickness(self):
        """Return the underline thickness for this state."""

def cmd(expr, args):
    '''
    Helper to define TeX commands.

    ``cmd("\\cmd", args)`` is equivalent to
    ``"\\cmd" - (args | Error("Expected \\cmd{arg}{...}"))`` where the names in
    the error message are taken from element names in *args*.  If *expr*
    already includes arguments (e.g. "\\cmd{arg}{...}"), then they are stripped
    when constructing the parse element, but kept (and *expr* is used as is) in
    the error message.
    '''

class Parser:
    """
    A pyparsing-based parser for strings containing math expressions.

    Raw text may also appear outside of pairs of ``$``.

    The grammar is based directly on that in TeX, though it cuts a few corners.
    """
    class _MathStyle(enum.Enum):
        DISPLAYSTYLE: int
        TEXTSTYLE: int
        SCRIPTSTYLE: int
        SCRIPTSCRIPTSTYLE: int
    def __init__(self) -> None: ...
    def parse(self, s, fonts_object, fontsize, dpi):
        """
        Parse expression *s* using the given *fonts_object* for
        output, at the given *fontsize* and *dpi*.

        Returns the parse tree of `Node` instances.
        """
    def get_state(self):
        """Get the current `State` of the parser."""
    def pop_state(self) -> None:
        """Pop a `State` off of the stack."""
    def push_state(self) -> None:
        """Push a new `State` onto the stack, copying the current state."""
    def main(self, s, loc, toks): ...
    def math_string(self, s, loc, toks): ...
    def math(self, s, loc, toks): ...
    def non_math(self, s, loc, toks): ...
    float_literal: Incomplete
    def space(self, s, loc, toks): ...
    def customspace(self, s, loc, toks): ...
    def symbol(self, s, loc, toks): ...
    def unknown_symbol(self, s, loc, toks) -> None: ...
    def accent(self, s, loc, toks): ...
    def function(self, s, loc, toks): ...
    def operatorname(self, s, loc, toks): ...
    def start_group(self, s, loc, toks): ...
    def group(self, s, loc, toks): ...
    def required_group(self, s, loc, toks): ...
    optional_group = required_group
    def end_group(self, s, loc, toks): ...
    def font(self, s, loc, toks): ...
    def is_overunder(self, nucleus): ...
    def is_dropsub(self, nucleus): ...
    def is_slanted(self, nucleus): ...
    def is_between_brackets(self, s, loc): ...
    def subsuper(self, s, loc, toks): ...
    def style_literal(self, s, loc, toks): ...
    def genfrac(self, s, loc, toks): ...
    def frac(self, s, loc, toks): ...
    def dfrac(self, s, loc, toks): ...
    def binom(self, s, loc, toks): ...
    overset: Incomplete
    underset: Incomplete
    def sqrt(self, s, loc, toks): ...
    def overline(self, s, loc, toks): ...
    def auto_delim(self, s, loc, toks): ...
