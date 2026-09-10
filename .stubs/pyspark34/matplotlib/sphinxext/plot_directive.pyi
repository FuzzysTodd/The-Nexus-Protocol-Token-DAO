from _typeshed import Incomplete
from docutils.parsers.rst import Directive
from matplotlib import cbook as cbook
from matplotlib.backend_bases import FigureManagerBase as FigureManagerBase

__version__: int

def mark_plot_labels(app, document) -> None:
    '''
    To make plots referenceable, we need to move the reference from the
    "htmlonly" (or "latexonly") node to the actual figure node itself.
    '''

class PlotDirective(Directive):
    """The ``.. plot::`` directive, as documented in the module's docstring."""
    has_content: bool
    required_arguments: int
    optional_arguments: int
    final_argument_whitespace: bool
    option_spec: Incomplete
    def run(self):
        """Run the plot directive."""

def setup(app): ...
def contains_doctest(text): ...

TEMPLATE: str
exception_template: str
plot_context: Incomplete

class ImageFile:
    basename: Incomplete
    dirname: Incomplete
    formats: Incomplete
    def __init__(self, basename, dirname) -> None: ...
    def filename(self, format): ...
    def filenames(self): ...

def out_of_date(original, derived, includes: Incomplete | None = None):
    """
    Return whether *derived* is out-of-date relative to *original* or any of
    the RST files included in it using the RST include directive (*includes*).
    *derived* and *original* are full paths, and *includes* is optionally a
    list of full paths which may have been included in the *original*.
    """

class PlotError(RuntimeError): ...

def clear_state(plot_rcparams, close: bool = True) -> None: ...
def get_plot_formats(config): ...
def render_figures(code, code_path, output_dir, output_base, context, function_name, config, context_reset: bool = False, close_figs: bool = False, code_includes: Incomplete | None = None):
    """
    Run a pyplot script and save the images in *output_dir*.

    Save the images under *output_dir* with file names derived from
    *output_base*
    """
def run(arguments, content, options, state_machine, state, lineno): ...
