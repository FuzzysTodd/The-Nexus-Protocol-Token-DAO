from _typeshed import Incomplete
from matplotlib import dviread as dviread
from matplotlib.font_manager import FontProperties as FontProperties, get_font as get_font
from matplotlib.ft2font import LOAD_NO_HINTING as LOAD_NO_HINTING, LOAD_TARGET_LIGHT as LOAD_TARGET_LIGHT
from matplotlib.mathtext import MathTextParser as MathTextParser
from matplotlib.path import Path as Path
from matplotlib.texmanager import TexManager as TexManager
from matplotlib.transforms import Affine2D as Affine2D

class TextToPath:
    """A class that converts strings to paths."""
    FONT_SCALE: float
    DPI: int
    mathtext_parser: Incomplete
    def __init__(self) -> None: ...
    def get_text_width_height_descent(self, s, prop, ismath): ...
    def get_text_path(self, prop, s, ismath: bool = False):
        '''
        Convert text *s* to path (a tuple of vertices and codes for
        matplotlib.path.Path).

        Parameters
        ----------
        prop : `~matplotlib.font_manager.FontProperties`
            The font properties for the text.

        s : str
            The text to be converted.

        ismath : {False, True, "TeX"}
            If True, use mathtext parser.  If "TeX", use tex for rendering.

        Returns
        -------
        verts : list
            A list of numpy arrays containing the x and y coordinates of the
            vertices.

        codes : list
            A list of path codes.

        Examples
        --------
        Create a list of vertices and codes from a text, and create a `.Path`
        from those::

            from matplotlib.path import Path
            from matplotlib.text import TextToPath
            from matplotlib.font_manager import FontProperties

            fp = FontProperties(family="Humor Sans", style="italic")
            verts, codes = TextToPath().get_text_path(fp, "ABC")
            path = Path(verts, codes, closed=False)

        Also see `TextPath` for a more direct way to create a path from a text.
        '''
    def get_glyphs_with_font(self, font, s, glyph_map: Incomplete | None = None, return_new_glyphs_only: bool = False):
        """
        Convert string *s* to vertices and codes using the provided ttf font.
        """
    def get_glyphs_mathtext(self, prop, s, glyph_map: Incomplete | None = None, return_new_glyphs_only: bool = False):
        """
        Parse mathtext string *s* and convert it to a (vertices, codes) pair.
        """
    def get_texmanager(self):
        """Return the cached `~.texmanager.TexManager` instance."""
    def get_glyphs_tex(self, prop, s, glyph_map: Incomplete | None = None, return_new_glyphs_only: bool = False):
        """Convert the string *s* to vertices and codes using usetex mode."""

text_to_path: Incomplete

class TextPath(Path):
    """
    Create a path from the text.
    """
    def __init__(self, xy, s, size: Incomplete | None = None, prop: Incomplete | None = None, _interpolation_steps: int = 1, usetex: bool = False) -> None:
        '''
        Create a path from the text. Note that it simply is a path,
        not an artist. You need to use the `.PathPatch` (or other artists)
        to draw this path onto the canvas.

        Parameters
        ----------
        xy : tuple or array of two float values
            Position of the text. For no offset, use ``xy=(0, 0)``.

        s : str
            The text to convert to a path.

        size : float, optional
            Font size in points. Defaults to the size specified via the font
            properties *prop*.

        prop : `~matplotlib.font_manager.FontProperties`, optional
            Font property. If not provided, will use a default
            `.FontProperties` with parameters from the
            :ref:`rcParams<customizing-with-dynamic-rc-settings>`.

        _interpolation_steps : int, optional
            (Currently ignored)

        usetex : bool, default: False
            Whether to use tex rendering.

        Examples
        --------
        The following creates a path from the string "ABC" with Helvetica
        font face; and another path from the latex fraction 1/2::

            from matplotlib.text import TextPath
            from matplotlib.font_manager import FontProperties

            fp = FontProperties(family="Helvetica", style="italic")
            path1 = TextPath((12, 12), "ABC", size=12, prop=fp)
            path2 = TextPath((0, 0), r"$\\frac{1}{2}$", size=12, usetex=True)

        Also see :doc:`/gallery/text_labels_and_annotations/demo_text_path`.
        '''
    def set_size(self, size) -> None:
        """Set the text size."""
    def get_size(self):
        """Get the text size."""
    @property
    def vertices(self):
        """
        Return the cached path after updating it if necessary.
        """
    @property
    def codes(self):
        """
        Return the codes
        """
