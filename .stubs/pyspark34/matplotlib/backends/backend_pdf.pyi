from . import _backend_pdf_ps
from _typeshed import Incomplete
from enum import Enum
from matplotlib import cbook as cbook, dviread as dviread
from matplotlib._afm import AFM as AFM
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase, FigureManagerBase as FigureManagerBase, GraphicsContextBase as GraphicsContextBase, RendererBase as RendererBase, _Backend
from matplotlib.backends.backend_mixed import MixedModeRenderer as MixedModeRenderer
from matplotlib.dates import UTC as UTC
from matplotlib.figure import Figure as Figure
from matplotlib.font_manager import get_font as get_font
from matplotlib.ft2font import FIXED_WIDTH as FIXED_WIDTH, FT2Font as FT2Font, ITALIC as ITALIC, KERNING_UNFITTED as KERNING_UNFITTED, LOAD_NO_HINTING as LOAD_NO_HINTING, LOAD_NO_SCALE as LOAD_NO_SCALE
from matplotlib.path import Path as Path
from matplotlib.transforms import Affine2D as Affine2D, BboxBase as BboxBase

def fill(strings, linelen: int = 75): ...
def pdfRepr(obj):
    """Map Python objects to PDF syntax."""

class Reference:
    """
    PDF reference object.

    Use PdfFile.reserveObject() to create References.
    """
    id: Incomplete
    def __init__(self, id) -> None: ...
    def pdfRepr(self): ...
    def write(self, contents, file) -> None: ...

class Name:
    """PDF name object."""
    name: Incomplete
    def __init__(self, name) -> None: ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self): ...
    @staticmethod
    def hexify(match): ...
    def pdfRepr(self): ...

class Operator:
    op: Incomplete
    def __init__(self, op) -> None: ...
    def pdfRepr(self): ...

class Verbatim:
    """Store verbatim PDF command content for later inclusion in the stream."""
    def __init__(self, x) -> None: ...
    def pdfRepr(self): ...

class Op(Enum):
    """PDF operators (not an exhaustive list)."""
    close_fill_stroke: bytes
    fill_stroke: bytes
    fill: bytes
    closepath: bytes
    close_stroke: bytes
    stroke: bytes
    endpath: bytes
    begin_text: bytes
    end_text: bytes
    curveto: bytes
    rectangle: bytes
    lineto: bytes
    moveto: bytes
    concat_matrix: bytes
    use_xobject: bytes
    setgray_stroke: bytes
    setgray_nonstroke: bytes
    setrgb_stroke: bytes
    setrgb_nonstroke: bytes
    setcolorspace_stroke: bytes
    setcolorspace_nonstroke: bytes
    setcolor_stroke: bytes
    setcolor_nonstroke: bytes
    setdash: bytes
    setlinejoin: bytes
    setlinecap: bytes
    setgstate: bytes
    gsave: bytes
    grestore: bytes
    textpos: bytes
    selectfont: bytes
    textmatrix: bytes
    show: bytes
    showkern: bytes
    setlinewidth: bytes
    clip: bytes
    shading: bytes
    op: Incomplete
    def pdfRepr(self): ...
    @classmethod
    def paint_path(cls, fill, stroke):
        """
        Return the PDF operator to paint a path.

        Parameters
        ----------
        fill : bool
            Fill the path with the fill color.
        stroke : bool
            Stroke the outline of the path with the line color.
        """

class Stream:
    """
    PDF stream object.

    This has no pdfRepr method. Instead, call begin(), then output the
    contents of the stream by calling write(), and finally call end().
    """
    id: Incomplete
    len: Incomplete
    pdfFile: Incomplete
    file: Incomplete
    compressobj: Incomplete
    extra: Incomplete
    pos: Incomplete
    def __init__(self, id, len, file, extra: Incomplete | None = None, png: Incomplete | None = None) -> None:
        """
        Parameters
        ----------
        id : int
            Object id of the stream.
        len : Reference or None
            An unused Reference object for the length of the stream;
            None means to use a memory buffer so the length can be inlined.
        file : PdfFile
            The underlying object to write the stream to.
        extra : dict from Name to anything, or None
            Extra key-value pairs to include in the stream header.
        png : dict or None
            If the data is already png encoded, the decode parameters.
        """
    def end(self) -> None:
        """Finalize stream."""
    def write(self, data) -> None:
        """Write some data on the stream."""

class PdfFile:
    """PDF file object."""
    xrefTable: Incomplete
    passed_in_file_object: bool
    original_file_like: Incomplete
    tell_base: int
    fh: Incomplete
    currentstream: Incomplete
    rootObject: Incomplete
    pagesObject: Incomplete
    pageList: Incomplete
    fontObject: Incomplete
    hatchObject: Incomplete
    gouraudObject: Incomplete
    XObjectObject: Incomplete
    resourceObject: Incomplete
    infoDict: Incomplete
    fontNames: Incomplete
    dviFontInfo: Incomplete
    type1Descriptors: Incomplete
    alphaStates: Incomplete
    hatchPatterns: Incomplete
    gouraudTriangles: Incomplete
    markers: Incomplete
    multi_byte_charprocs: Incomplete
    paths: Incomplete
    pageAnnotations: Incomplete
    def __init__(self, filename, metadata: Incomplete | None = None) -> None:
        """
        Parameters
        ----------
        filename : str or path-like or file-like
            Output target; if a string, a file will be opened for writing.

        metadata : dict from strings to strings and dates
            Information dictionary object (see PDF reference section 10.2.1
            'Document Information Dictionary'), e.g.:
            ``{'Creator': 'My software', 'Author': 'Me', 'Title': 'Awesome'}``.

            The standard keys are 'Title', 'Author', 'Subject', 'Keywords',
            'Creator', 'Producer', 'CreationDate', 'ModDate', and
            'Trapped'. Values have been predefined for 'Creator', 'Producer'
            and 'CreationDate'. They can be removed by setting them to `None`.
        """
    def newPage(self, width, height) -> None: ...
    def newTextnote(self, text, positionRect=[-100, -100, 0, 0]) -> None: ...
    def finalize(self) -> None:
        """Write out the various deferred objects and the pdf end matter."""
    def close(self) -> None:
        """Flush all buffers and free all resources."""
    def write(self, data) -> None: ...
    def output(self, *data) -> None: ...
    def beginStream(self, id, len, extra: Incomplete | None = None, png: Incomplete | None = None) -> None: ...
    def endStream(self) -> None: ...
    def outputStream(self, ref, data, *, extra: Incomplete | None = None) -> None: ...
    def fontName(self, fontprop):
        """
        Select a font based on fontprop and return a name suitable for
        Op.selectfont. If fontprop is a string, it will be interpreted
        as the filename of the font.
        """
    def dviFontName(self, dvifont):
        """
        Given a dvi font object, return a name suitable for Op.selectfont.
        This registers the font information in ``self.dviFontInfo`` if not yet
        registered.
        """
    def writeFonts(self) -> None: ...
    def createType1Descriptor(self, t1font, fontfile): ...
    def embedTTF(self, filename, characters):
        """Embed the TTF font from the named file into the document."""
    def alphaState(self, alpha):
        """Return name of an ExtGState that sets alpha to the given value."""
    def writeExtGSTates(self) -> None: ...
    def hatchPattern(self, hatch_style): ...
    def writeHatches(self) -> None: ...
    def addGouraudTriangles(self, points, colors):
        """
        Add a Gouraud triangle shading.

        Parameters
        ----------
        points : np.ndarray
            Triangle vertices, shape (n, 3, 2)
            where n = number of triangles, 3 = vertices, 2 = x, y.
        colors : np.ndarray
            Vertex colors, shape (n, 3, 1) or (n, 3, 4)
            as with points, but last dimension is either (gray,)
            or (r, g, b, alpha).

        Returns
        -------
        Name, Reference
        """
    def writeGouraudTriangles(self) -> None: ...
    def imageObject(self, image):
        """Return name of an image XObject representing the given image."""
    def writeImages(self) -> None: ...
    def markerObject(self, path, trans, fill, stroke, lw, joinstyle, capstyle):
        """Return name of a marker XObject representing the given path."""
    def writeMarkers(self) -> None: ...
    def pathCollectionObject(self, gc, path, trans, padding, filled, stroked): ...
    def writePathCollectionTemplates(self) -> None: ...
    @staticmethod
    def pathOperations(path, transform, clip: Incomplete | None = None, simplify: Incomplete | None = None, sketch: Incomplete | None = None): ...
    def writePath(self, path, transform, clip: bool = False, sketch: Incomplete | None = None) -> None: ...
    def reserveObject(self, name: str = ''):
        """
        Reserve an ID for an indirect object.

        The name is used for debugging in case we forget to print out
        the object with writeObject.
        """
    def recordXref(self, id) -> None: ...
    def writeObject(self, object, contents) -> None: ...
    startxref: Incomplete
    def writeXref(self) -> None:
        """Write out the xref table."""
    infoObject: Incomplete
    def writeInfoDict(self) -> None:
        """Write out the info dictionary, checking it for good form"""
    def writeTrailer(self) -> None:
        """Write out the PDF trailer."""

class RendererPdf(_backend_pdf_ps.RendererPDFPSBase):
    file: Incomplete
    gc: Incomplete
    image_dpi: Incomplete
    def __init__(self, file, image_dpi, height, width) -> None: ...
    def finalize(self) -> None: ...
    def check_gc(self, gc, fillcolor: Incomplete | None = None) -> None: ...
    def get_image_magnification(self): ...
    def draw_image(self, gc, x, y, im, transform: Incomplete | None = None) -> None: ...
    def draw_path(self, gc, path, transform, rgbFace: Incomplete | None = None) -> None: ...
    def draw_path_collection(self, gc, master_transform, paths, all_transforms, offsets, offset_trans, facecolors, edgecolors, linewidths, linestyles, antialiaseds, urls, offset_position): ...
    def draw_markers(self, gc, marker_path, marker_trans, path, trans, rgbFace: Incomplete | None = None) -> None: ...
    def draw_gouraud_triangle(self, gc, points, colors, trans) -> None: ...
    def draw_gouraud_triangles(self, gc, points, colors, trans) -> None: ...
    def draw_mathtext(self, gc, x, y, s, prop, angle) -> None: ...
    def draw_tex(self, gc, x, y, s, prop, angle, *, mtext: Incomplete | None = None) -> None: ...
    def encode_string(self, s, fonttype): ...
    def draw_text(self, gc, x, y, s, prop, angle, ismath: bool = False, mtext: Incomplete | None = None): ...
    def new_gc(self): ...

class GraphicsContextPdf(GraphicsContextBase):
    file: Incomplete
    parent: Incomplete
    def __init__(self, file) -> None: ...
    def stroke(self):
        """
        Predicate: does the path need to be stroked (its outline drawn)?
        This tests for the various conditions that disable stroking
        the path, in which case it would presumably be filled.
        """
    def fill(self, *args):
        """
        Predicate: does the path need to be filled?

        An optional argument can be used to specify an alternative
        _fillcolor, as needed by RendererPdf.draw_markers.
        """
    def paint(self):
        """
        Return the appropriate pdf operator to cause the path to be
        stroked, filled, or both.
        """
    capstyles: Incomplete
    joinstyles: Incomplete
    def capstyle_cmd(self, style): ...
    def joinstyle_cmd(self, style): ...
    def linewidth_cmd(self, width): ...
    def dash_cmd(self, dashes): ...
    def alpha_cmd(self, alpha, forced, effective_alphas): ...
    def hatch_cmd(self, hatch, hatch_color): ...
    def rgb_cmd(self, rgb): ...
    def fillcolor_cmd(self, rgb): ...
    def push(self): ...
    def pop(self): ...
    def clip_cmd(self, cliprect, clippath):
        """Set clip rectangle. Calls `.pop()` and `.push()`."""
    commands: Incomplete
    def delta(self, other):
        """
        Copy properties of other into self and return PDF commands
        needed to transform *self* into *other*.
        """
    def copy_properties(self, other) -> None:
        """
        Copy properties of other into self.
        """
    def finalize(self):
        """
        Make sure every pushed graphics state is popped.
        """

class PdfPages:
    """
    A multi-page PDF file.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> # Initialize:
    >>> with PdfPages('foo.pdf') as pdf:
    ...     # As many times as you like, create a figure fig and save it:
    ...     fig = plt.figure()
    ...     pdf.savefig(fig)
    ...     # When no figure is specified the current figure is saved
    ...     pdf.savefig()

    Notes
    -----
    In reality `PdfPages` is a thin wrapper around `PdfFile`, in order to avoid
    confusion when using `~.pyplot.savefig` and forgetting the format argument.
    """
    keep_empty: Incomplete
    def __init__(self, filename, keep_empty: bool = True, metadata: Incomplete | None = None) -> None:
        """
        Create a new PdfPages object.

        Parameters
        ----------
        filename : str or path-like or file-like
            Plots using `PdfPages.savefig` will be written to a file at this
            location. The file is opened at once and any older file with the
            same name is overwritten.

        keep_empty : bool, optional
            If set to False, then empty pdf files will be deleted automatically
            when closed.

        metadata : dict, optional
            Information dictionary object (see PDF reference section 10.2.1
            'Document Information Dictionary'), e.g.:
            ``{'Creator': 'My software', 'Author': 'Me', 'Title': 'Awesome'}``.

            The standard keys are 'Title', 'Author', 'Subject', 'Keywords',
            'Creator', 'Producer', 'CreationDate', 'ModDate', and
            'Trapped'. Values have been predefined for 'Creator', 'Producer'
            and 'CreationDate'. They can be removed by setting them to `None`.
        """
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def close(self) -> None:
        """
        Finalize this object, making the underlying file a complete
        PDF file.
        """
    def infodict(self):
        """
        Return a modifiable information dictionary object
        (see PDF reference section 10.2.1 'Document Information
        Dictionary').
        """
    def savefig(self, figure: Incomplete | None = None, **kwargs) -> None:
        """
        Save a `.Figure` to this file as a new page.

        Any other keyword arguments are passed to `~.Figure.savefig`.

        Parameters
        ----------
        figure : `.Figure` or int, default: the active figure
            The figure, or index of the figure, that is saved to the file.
        """
    def get_pagecount(self):
        """Return the current number of pages in the multipage pdf file."""
    def attach_note(self, text, positionRect=[-100, -100, 0, 0]) -> None:
        """
        Add a new text note to the page to be saved next. The optional
        positionRect specifies the position of the new note on the
        page. It is outside the page per default to make sure it is
        invisible on printouts.
        """

class FigureCanvasPdf(FigureCanvasBase):
    fixed_dpi: int
    filetypes: Incomplete
    def get_default_filetype(self): ...
    def print_pdf(self, filename, *, bbox_inches_restore: Incomplete | None = None, metadata: Incomplete | None = None) -> None: ...
    def draw(self): ...
FigureManagerPdf = FigureManagerBase

class _BackendPdf(_Backend):
    FigureCanvas = FigureCanvasPdf
