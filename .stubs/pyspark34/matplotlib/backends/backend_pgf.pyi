from _typeshed import Incomplete
from matplotlib import cbook as cbook
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase, FigureManagerBase as FigureManagerBase, RendererBase as RendererBase, _Backend
from matplotlib.backends.backend_mixed import MixedModeRenderer as MixedModeRenderer
from matplotlib.figure import Figure as Figure
from matplotlib.path import Path as Path

class __getattr__:
    NO_ESCAPE: Incomplete
    re_mathsep: Incomplete

def get_fontspec():
    """Build fontspec preamble from rc."""
def get_preamble():
    """Get LaTeX preamble from rc."""

latex_pt_to_in: Incomplete
latex_in_to_pt: Incomplete
mpl_pt_to_in: Incomplete
mpl_in_to_pt: Incomplete

def common_texification(text): ...
def writeln(fh, line): ...
def make_pdf_to_png_converter():
    """Return a function that converts a pdf file to a png file."""

class LatexError(Exception):
    latex_output: Incomplete
    def __init__(self, message, latex_output: str = '') -> None: ...

class LatexManager:
    """
    The LatexManager opens an instance of the LaTeX application for
    determining the metrics of text elements. The LaTeX environment can be
    modified by setting fonts and/or a custom preamble in `.rcParams`.
    """
    tmpdir: Incomplete
    latex: Incomplete
    def __init__(self) -> None: ...
    texcommand: Incomplete
    latex_header: Incomplete
    def get_width_height_descent(self, text, prop):
        """
        Get the width, total height, and descent (in TeX points) for a text
        typeset by the current LaTeX environment.
        """

class RendererPgf(RendererBase):
    dpi: Incomplete
    fh: Incomplete
    figure: Incomplete
    image_counter: int
    def __init__(self, figure, fh) -> None:
        """
        Create a new PGF renderer that translates any drawing instruction
        into text commands to be interpreted in a latex pgfpicture environment.

        Attributes
        ----------
        figure : `~matplotlib.figure.Figure`
            Matplotlib figure to initialize height, width and dpi from.
        fh : file-like
            File handle for the output of the drawing commands.
        """
    def draw_markers(self, gc, marker_path, marker_trans, path, trans, rgbFace: Incomplete | None = None) -> None: ...
    def draw_path(self, gc, path, transform, rgbFace: Incomplete | None = None) -> None: ...
    def option_scale_image(self): ...
    def option_image_nocomposite(self): ...
    def draw_image(self, gc, x, y, im, transform: Incomplete | None = None) -> None: ...
    def draw_tex(self, gc, x, y, s, prop, angle, *, mtext: Incomplete | None = None) -> None: ...
    def draw_text(self, gc, x, y, s, prop, angle, ismath: bool = False, mtext: Incomplete | None = None) -> None: ...
    def get_text_width_height_descent(self, s, prop, ismath): ...
    def flipy(self): ...
    def get_canvas_width_height(self): ...
    def points_to_pixels(self, points): ...

class FigureCanvasPgf(FigureCanvasBase):
    filetypes: Incomplete
    def get_default_filetype(self): ...
    def print_pgf(self, fname_or_fh, **kwargs) -> None:
        """
        Output pgf macros for drawing the figure so it can be included and
        rendered in latex documents.
        """
    def print_pdf(self, fname_or_fh, *, metadata: Incomplete | None = None, **kwargs) -> None:
        """Use LaTeX to compile a pgf generated figure to pdf."""
    def print_png(self, fname_or_fh, **kwargs) -> None:
        """Use LaTeX to compile a pgf figure to pdf and convert it to png."""
    def get_renderer(self): ...
    def draw(self): ...
FigureManagerPgf = FigureManagerBase

class _BackendPgf(_Backend):
    FigureCanvas = FigureCanvasPgf

class PdfPages:
    """
    A multi-page PDF file using the pgf backend

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
    """
    keep_empty: Incomplete
    def __init__(self, filename, *, keep_empty: bool = True, metadata: Incomplete | None = None) -> None:
        """
        Create a new PdfPages object.

        Parameters
        ----------
        filename : str or path-like
            Plots using `PdfPages.savefig` will be written to a file at this
            location. Any older file with the same name is overwritten.

        keep_empty : bool, default: True
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

            Note that some versions of LaTeX engines may ignore the 'Producer'
            key and set it to themselves.
        """
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def close(self) -> None:
        """
        Finalize this object, running LaTeX in a temporary directory
        and moving the final pdf file to *filename*.
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
