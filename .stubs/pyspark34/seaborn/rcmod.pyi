from _typeshed import Incomplete

__all__ = ['set_theme', 'set', 'reset_defaults', 'reset_orig', 'axes_style', 'set_style', 'plotting_context', 'set_context', 'set_palette']

def set_theme(context: str = 'notebook', style: str = 'darkgrid', palette: str = 'deep', font: str = 'sans-serif', font_scale: int = 1, color_codes: bool = True, rc: Incomplete | None = None) -> None:
    '''
    Set aspects of the visual theme for all matplotlib and seaborn plots.

    This function changes the global defaults for all plots using the
    matplotlib rcParams system. The themeing is decomposed into several distinct
    sets of parameter values.

    The options are illustrated in the :doc:`aesthetics <../tutorial/aesthetics>`
    and :doc:`color palette <../tutorial/color_palettes>` tutorials.

    Parameters
    ----------
    context : string or dict
        Scaling parameters, see :func:`plotting_context`.
    style : string or dict
        Axes style parameters, see :func:`axes_style`.
    palette : string or sequence
        Color palette, see :func:`color_palette`.
    font : string
        Font family, see matplotlib font manager.
    font_scale : float, optional
        Separate scaling factor to independently scale the size of the
        font elements.
    color_codes : bool
        If ``True`` and ``palette`` is a seaborn palette, remap the shorthand
        color codes (e.g. "b", "g", "r", etc.) to the colors from this palette.
    rc : dict or None
        Dictionary of rc parameter mappings to override the above.

    Examples
    --------

    .. include:: ../docstrings/set_theme.rst

    '''
def set(*args, **kwargs) -> None:
    """
    Alias for :func:`set_theme`, which is the preferred interface.

    This function may be removed in the future.
    """
def reset_defaults() -> None:
    """Restore all RC params to default settings."""
def reset_orig() -> None:
    """Restore all RC params to original settings (respects custom rc)."""
def axes_style(style: Incomplete | None = None, rc: Incomplete | None = None):
    """
    Get the parameters that control the general style of the plots.

    The style parameters control properties like the color of the background and
    whether a grid is enabled by default. This is accomplished using the
    matplotlib rcParams system.

    The options are illustrated in the
    :doc:`aesthetics tutorial <../tutorial/aesthetics>`.

    This function can also be used as a context manager to temporarily
    alter the global defaults. See :func:`set_theme` or :func:`set_style`
    to modify the global defaults for all plots.

    Parameters
    ----------
    style : None, dict, or one of {darkgrid, whitegrid, dark, white, ticks}
        A dictionary of parameters or the name of a preconfigured style.
    rc : dict, optional
        Parameter mappings to override the values in the preset seaborn
        style dictionaries. This only updates parameters that are
        considered part of the style definition.

    Examples
    --------

    .. include:: ../docstrings/axes_style.rst

    """
def set_style(style: Incomplete | None = None, rc: Incomplete | None = None) -> None:
    """
    Set the parameters that control the general style of the plots.

    The style parameters control properties like the color of the background and
    whether a grid is enabled by default. This is accomplished using the
    matplotlib rcParams system.

    The options are illustrated in the
    :doc:`aesthetics tutorial <../tutorial/aesthetics>`.

    See :func:`axes_style` to get the parameter values.

    Parameters
    ----------
    style : dict, or one of {darkgrid, whitegrid, dark, white, ticks}
        A dictionary of parameters or the name of a preconfigured style.
    rc : dict, optional
        Parameter mappings to override the values in the preset seaborn
        style dictionaries. This only updates parameters that are
        considered part of the style definition.

    Examples
    --------

    .. include:: ../docstrings/set_style.rst

    """
def plotting_context(context: Incomplete | None = None, font_scale: int = 1, rc: Incomplete | None = None):
    '''
    Get the parameters that control the scaling of plot elements.

    This affects things like the size of the labels, lines, and other elements
    of the plot, but not the overall style. This is accomplished using the
    matplotlib rcParams system.

    The base context is "notebook", and the other contexts are "paper", "talk",
    and "poster", which are version of the notebook parameters scaled by different
    values. Font elements can also be scaled independently of (but relative to)
    the other values.

    This function can also be used as a context manager to temporarily
    alter the global defaults. See :func:`set_theme` or :func:`set_context`
    to modify the global defaults for all plots.

    Parameters
    ----------
    context : None, dict, or one of {paper, notebook, talk, poster}
        A dictionary of parameters or the name of a preconfigured set.
    font_scale : float, optional
        Separate scaling factor to independently scale the size of the
        font elements.
    rc : dict, optional
        Parameter mappings to override the values in the preset seaborn
        context dictionaries. This only updates parameters that are
        considered part of the context definition.

    Examples
    --------

    .. include:: ../docstrings/plotting_context.rst

    '''
def set_context(context: Incomplete | None = None, font_scale: int = 1, rc: Incomplete | None = None) -> None:
    '''
    Set the parameters that control the scaling of plot elements.

    This affects things like the size of the labels, lines, and other elements
    of the plot, but not the overall style. This is accomplished using the
    matplotlib rcParams system.

    The base context is "notebook", and the other contexts are "paper", "talk",
    and "poster", which are version of the notebook parameters scaled by different
    values. Font elements can also be scaled independently of (but relative to)
    the other values.

    See :func:`plotting_context` to get the parameter values.

    Parameters
    ----------
    context : dict, or one of {paper, notebook, talk, poster}
        A dictionary of parameters or the name of a preconfigured set.
    font_scale : float, optional
        Separate scaling factor to independently scale the size of the
        font elements.
    rc : dict, optional
        Parameter mappings to override the values in the preset seaborn
        context dictionaries. This only updates parameters that are
        considered part of the context definition.

    Examples
    --------

    .. include:: ../docstrings/set_context.rst

    '''

class _RCAesthetics(dict):
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def __call__(self, func): ...

class _AxesStyle(_RCAesthetics):
    """Light wrapper on a dict to set style temporarily."""
class _PlottingContext(_RCAesthetics):
    """Light wrapper on a dict to set context temporarily."""

def set_palette(palette, n_colors: Incomplete | None = None, desat: Incomplete | None = None, color_codes: bool = False) -> None:
    '''Set the matplotlib color cycle using a seaborn palette.

    Parameters
    ----------
    palette : seaborn color paltte | matplotlib colormap | hls | husl
        Palette definition. Should be something :func:`color_palette` can process.
    n_colors : int
        Number of colors in the cycle. The default number of colors will depend
        on the format of ``palette``, see the :func:`color_palette`
        documentation for more information.
    desat : float
        Proportion to desaturate each color by.
    color_codes : bool
        If ``True`` and ``palette`` is a seaborn palette, remap the shorthand
        color codes (e.g. "b", "g", "r", etc.) to the colors from this palette.

    See Also
    --------
    color_palette : build a color palette or set the color cycle temporarily
                    in a ``with`` statement.
    set_context : set parameters to scale plot elements
    set_style : set the default parameters for figure style

    '''
