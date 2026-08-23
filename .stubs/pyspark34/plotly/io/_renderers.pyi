from _typeshed import Incomplete
from plotly import optional_imports as optional_imports
from plotly.io._base_renderers import AzureRenderer as AzureRenderer, BrowserRenderer as BrowserRenderer, CoCalcRenderer as CoCalcRenderer, ColabRenderer as ColabRenderer, DatabricksRenderer as DatabricksRenderer, ExternalRenderer as ExternalRenderer, IFrameRenderer as IFrameRenderer, JpegRenderer as JpegRenderer, JsonRenderer as JsonRenderer, KaggleRenderer as KaggleRenderer, MimetypeRenderer as MimetypeRenderer, NotebookRenderer as NotebookRenderer, PdfRenderer as PdfRenderer, PlotlyRenderer as PlotlyRenderer, PngRenderer as PngRenderer, SphinxGalleryHtmlRenderer as SphinxGalleryHtmlRenderer, SphinxGalleryOrcaRenderer as SphinxGalleryOrcaRenderer, SvgRenderer as SvgRenderer
from plotly.io._utils import validate_coerce_fig_to_dict as validate_coerce_fig_to_dict
from plotly.io.orca import validate_executable as validate_executable

ipython: Incomplete
ipython_display: Incomplete
nbformat: Incomplete

class RenderersConfig:
    """
    Singleton object containing the current renderer configurations
    """
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, item) -> bool: ...
    def __iter__(self): ...
    def __getitem__(self, item): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def keys(self): ...
    def items(self): ...
    def update(self, d={}, **kwargs) -> None:
        """
        Update one or more renderers from a dict or from input keyword
        arguments.

        Parameters
        ----------
        d: dict
            Dictionary from renderer names to new renderer objects.

        kwargs
            Named argument value pairs where the name is a renderer name
            and the value is a new renderer object
        """
    @property
    def default(self):
        """
        The default renderer, or None if no there is no default

        If not None, the default renderer is used to render
        figures when the `plotly.io.show` function is called on a Figure.

        If `plotly.io.renderers.render_on_display` is True, then the default
        renderer will also be used to display Figures automatically when
        displayed in the Jupyter Notebook

        Multiple renderers may be registered by separating their names with
        '+' characters. For example, to specify rendering compatible with
        the classic Jupyter Notebook, JupyterLab, and PDF export:

        >>> import plotly.io as pio
        >>> pio.renderers.default = 'notebook+jupyterlab+pdf'

        The names of available renderers may be retrieved with:

        >>> import plotly.io as pio
        >>> list(pio.renderers)

        Returns
        -------
        str
        """
    @default.setter
    def default(self, value) -> None: ...
    @property
    def render_on_display(self):
        """
        If True, the default mimetype renderers will be used to render
        figures when they are displayed in an IPython context.

        Returns
        -------
        bool
        """
    @render_on_display.setter
    def render_on_display(self, val) -> None: ...

renderers: Incomplete

def show(fig, renderer: Incomplete | None = None, validate: bool = True, **kwargs) -> None:
    """
    Show a figure using either the default renderer(s) or the renderer(s)
    specified by the renderer argument

    Parameters
    ----------
    fig: dict of Figure
        The Figure object or figure dict to display

    renderer: str or None (default None)
        A string containing the names of one or more registered renderers
        (separated by '+' characters) or None.  If None, then the default
        renderers specified in plotly.io.renderers.default are used.

    validate: bool (default True)
        True if the figure should be validated before being shown,
        False otherwise.

    width: int or float
        An integer or float that determines the number of pixels wide the
        plot is. The default is set in plotly.js.

    height: int or float
        An integer or float that determines the number of pixels wide the
        plot is. The default is set in plotly.js.

    config: dict
        A dict of parameters to configure the figure. The defaults are set
        in plotly.js.

    Returns
    -------
    None
    """

plotly_renderer: Incomplete
config: Incomplete
jpeg_renderer: Incomplete
default_renderer: Incomplete
env_renderer: Incomplete
default_renderer = env_renderer
