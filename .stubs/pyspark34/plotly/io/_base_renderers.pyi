from _typeshed import Incomplete
from plotly import optional_imports as optional_imports, utils as utils
from plotly.io import to_image as to_image, to_json as to_json, write_html as write_html, write_image as write_image
from plotly.io._orca import ensure_server as ensure_server
from plotly.io._utils import plotly_cdn_url as plotly_cdn_url
from plotly.offline.offline import get_plotlyjs as get_plotlyjs
from plotly.tools import return_figure_from_figure_or_data as return_figure_from_figure_or_data

ipython_display: Incomplete
IPython: Incomplete

class BaseRenderer:
    """
    Base class for all renderers
    """
    def activate(self) -> None: ...
    def __hash__(self): ...

class MimetypeRenderer(BaseRenderer):
    """
    Base class for all mime type renderers
    """
    def to_mimebundle(self, fig_dict) -> None: ...

class JsonRenderer(MimetypeRenderer):
    """
    Renderer to display figures as JSON hierarchies.  This renderer is
    compatible with JupyterLab and VSCode.

    mime type: 'application/json'
    """
    def to_mimebundle(self, fig_dict): ...

class PlotlyRenderer(MimetypeRenderer):
    """
    Renderer to display figures using the plotly mime type.  This renderer is
    compatible with JupyterLab (using the @jupyterlab/plotly-extension),
    VSCode, and nteract.

    mime type: 'application/vnd.plotly.v1+json'
    """
    config: Incomplete
    def __init__(self, config: Incomplete | None = None) -> None: ...
    def to_mimebundle(self, fig_dict): ...

class ImageRenderer(MimetypeRenderer):
    """
    Base class for all static image renderers
    """
    mime_type: Incomplete
    b64_encode: Incomplete
    format: Incomplete
    width: Incomplete
    height: Incomplete
    scale: Incomplete
    engine: Incomplete
    def __init__(self, mime_type, b64_encode: bool = False, format: Incomplete | None = None, width: Incomplete | None = None, height: Incomplete | None = None, scale: Incomplete | None = None, engine: str = 'auto') -> None: ...
    def to_mimebundle(self, fig_dict): ...

class PngRenderer(ImageRenderer):
    """
    Renderer to display figures as static PNG images.  This renderer requires
    either the kaleido package or the orca command-line utility and is broadly
    compatible across IPython environments (classic Jupyter Notebook, JupyterLab,
    QtConsole, VSCode, PyCharm, etc) and nbconvert targets (HTML, PDF, etc.).

    mime type: 'image/png'
    """
    def __init__(self, width: Incomplete | None = None, height: Incomplete | None = None, scale: Incomplete | None = None, engine: str = 'auto') -> None: ...

class SvgRenderer(ImageRenderer):
    """
    Renderer to display figures as static SVG images.  This renderer requires
    either the kaleido package or the orca command-line utility and is broadly
    compatible across IPython environments (classic Jupyter Notebook, JupyterLab,
    QtConsole, VSCode, PyCharm, etc) and nbconvert targets (HTML, PDF, etc.).

    mime type: 'image/svg+xml'
    """
    def __init__(self, width: Incomplete | None = None, height: Incomplete | None = None, scale: Incomplete | None = None, engine: str = 'auto') -> None: ...

class JpegRenderer(ImageRenderer):
    """
    Renderer to display figures as static JPEG images.  This renderer requires
    either the kaleido package or the orca command-line utility and is broadly
    compatible across IPython environments (classic Jupyter Notebook, JupyterLab,
    QtConsole, VSCode, PyCharm, etc) and nbconvert targets (HTML, PDF, etc.).

    mime type: 'image/jpeg'
    """
    def __init__(self, width: Incomplete | None = None, height: Incomplete | None = None, scale: Incomplete | None = None, engine: str = 'auto') -> None: ...

class PdfRenderer(ImageRenderer):
    """
    Renderer to display figures as static PDF images.  This renderer requires
    either the kaleido package or the orca command-line utility and is compatible
    with JupyterLab and the LaTeX-based nbconvert export to PDF.

    mime type: 'application/pdf'
    """
    def __init__(self, width: Incomplete | None = None, height: Incomplete | None = None, scale: Incomplete | None = None, engine: str = 'auto') -> None: ...

class HtmlRenderer(MimetypeRenderer):
    """
    Base class for all HTML mime type renderers

    mime type: 'text/html'
    """
    config: Incomplete
    auto_play: Incomplete
    connected: Incomplete
    global_init: Incomplete
    requirejs: Incomplete
    full_html: Incomplete
    animation_opts: Incomplete
    post_script: Incomplete
    def __init__(self, connected: bool = False, full_html: bool = False, requirejs: bool = True, global_init: bool = False, config: Incomplete | None = None, auto_play: bool = False, post_script: Incomplete | None = None, animation_opts: Incomplete | None = None) -> None: ...
    def activate(self) -> None: ...
    def to_mimebundle(self, fig_dict): ...

class NotebookRenderer(HtmlRenderer):
    """
    Renderer to display interactive figures in the classic Jupyter Notebook.
    This renderer is also useful for notebooks that will be converted to
    HTML using nbconvert/nbviewer as it will produce standalone HTML files
    that include interactive figures.

    This renderer automatically performs global notebook initialization when
    activated.

    mime type: 'text/html'
    """
    def __init__(self, connected: bool = False, config: Incomplete | None = None, auto_play: bool = False, post_script: Incomplete | None = None, animation_opts: Incomplete | None = None) -> None: ...

class KaggleRenderer(HtmlRenderer):
    """
    Renderer to display interactive figures in Kaggle Notebooks.

    Same as NotebookRenderer but with connected=True so that the plotly.js
    bundle is loaded from a CDN rather than being embedded in the notebook.

    This renderer is enabled by default when running in a Kaggle notebook.

    mime type: 'text/html'
    """
    def __init__(self, config: Incomplete | None = None, auto_play: bool = False, post_script: Incomplete | None = None, animation_opts: Incomplete | None = None) -> None: ...

class AzureRenderer(HtmlRenderer):
    """
    Renderer to display interactive figures in Azure Notebooks.

    Same as NotebookRenderer but with connected=True so that the plotly.js
    bundle is loaded from a CDN rather than being embedded in the notebook.

    This renderer is enabled by default when running in an Azure notebook.

    mime type: 'text/html'
    """
    def __init__(self, config: Incomplete | None = None, auto_play: bool = False, post_script: Incomplete | None = None, animation_opts: Incomplete | None = None) -> None: ...

class ColabRenderer(HtmlRenderer):
    """
    Renderer to display interactive figures in Google Colab Notebooks.

    This renderer is enabled by default when running in a Colab notebook.

    mime type: 'text/html'
    """
    def __init__(self, config: Incomplete | None = None, auto_play: bool = False, post_script: Incomplete | None = None, animation_opts: Incomplete | None = None) -> None: ...

class IFrameRenderer(MimetypeRenderer):
    """
    Renderer to display interactive figures using an IFrame.  HTML
    representations of Figures are saved to an `iframe_figures/` directory and
    iframe HTML elements that reference these files are inserted into the
    notebook.

    With this approach, neither plotly.js nor the figure data are embedded in
    the notebook, so this is a good choice for notebooks that contain so many
    large figures that basic operations (like saving and opening) become
    very slow.

    Notebooks using this renderer will display properly when exported to HTML
    as long as the `iframe_figures/` directory is placed in the same directory
    as the exported html file.

    Note that the HTML files in `iframe_figures/` are numbered according to
    the IPython cell execution count and so they will start being overwritten
    each time the kernel is restarted.  This directory may be deleted whenever
    the kernel is restarted and it will be automatically recreated.

    mime type: 'text/html'
    """
    config: Incomplete
    auto_play: Incomplete
    post_script: Incomplete
    animation_opts: Incomplete
    include_plotlyjs: Incomplete
    html_directory: Incomplete
    def __init__(self, config: Incomplete | None = None, auto_play: bool = False, post_script: Incomplete | None = None, animation_opts: Incomplete | None = None, include_plotlyjs: bool = True, html_directory: str = 'iframe_figures') -> None: ...
    def to_mimebundle(self, fig_dict): ...
    def build_filename(self): ...
    def build_url(self, filename): ...

class CoCalcRenderer(IFrameRenderer):
    def build_filename(self): ...
    def build_url(self, filename): ...

class ExternalRenderer(BaseRenderer):
    """
    Base class for external renderers.  ExternalRenderer subclasses
    do not display figures inline in a notebook environment, but render
    figures by some external means (e.g. a separate browser tab).

    Unlike MimetypeRenderer subclasses, ExternalRenderer subclasses are not
    invoked when a figure is asked to display itself in the notebook.
    Instead, they are invoked when the plotly.io.show function is called
    on a figure.
    """
    def render(self, fig) -> None: ...

def open_html_in_browser(html, using: Incomplete | None = None, new: int = 0, autoraise: bool = True) -> None:
    """
    Display html in a web browser without creating a temp file.

    Instantiates a trivial http server and uses the webbrowser module to
    open a URL to retrieve html from that server.

    Parameters
    ----------
    html: str
        HTML string to display
    using, new, autoraise:
        See docstrings in webbrowser.get and webbrowser.open
    """

class BrowserRenderer(ExternalRenderer):
    """
    Renderer to display interactive figures in an external web browser.
    This renderer will open a new browser window or tab when the
    plotly.io.show function is called on a figure.

    This renderer has no ipython/jupyter dependencies and is a good choice
    for use in environments that do not support the inline display of
    interactive figures.

    mime type: 'text/html'
    """
    config: Incomplete
    auto_play: Incomplete
    using: Incomplete
    new: Incomplete
    autoraise: Incomplete
    post_script: Incomplete
    animation_opts: Incomplete
    def __init__(self, config: Incomplete | None = None, auto_play: bool = False, using: Incomplete | None = None, new: int = 0, autoraise: bool = True, post_script: Incomplete | None = None, animation_opts: Incomplete | None = None) -> None: ...
    def render(self, fig_dict) -> None: ...

class DatabricksRenderer(ExternalRenderer):
    config: Incomplete
    auto_play: Incomplete
    post_script: Incomplete
    animation_opts: Incomplete
    include_plotlyjs: Incomplete
    def __init__(self, config: Incomplete | None = None, auto_play: bool = False, post_script: Incomplete | None = None, animation_opts: Incomplete | None = None, include_plotlyjs: str = 'cdn') -> None: ...
    @property
    def displayHTML(self): ...
    def render(self, fig_dict) -> None: ...

class SphinxGalleryHtmlRenderer(HtmlRenderer):
    def __init__(self, connected: bool = True, config: Incomplete | None = None, auto_play: bool = False, post_script: Incomplete | None = None, animation_opts: Incomplete | None = None) -> None: ...
    def to_mimebundle(self, fig_dict): ...

class SphinxGalleryOrcaRenderer(ExternalRenderer):
    def render(self, fig_dict) -> None: ...
