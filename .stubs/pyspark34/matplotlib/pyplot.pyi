from .ticker import AutoLocator as AutoLocator, FixedFormatter as FixedFormatter, FixedLocator as FixedLocator, FormatStrFormatter as FormatStrFormatter, Formatter as Formatter, FuncFormatter as FuncFormatter, IndexLocator as IndexLocator, LinearLocator as LinearLocator, Locator as Locator, LogFormatter as LogFormatter, LogFormatterExponent as LogFormatterExponent, LogFormatterMathtext as LogFormatterMathtext, LogLocator as LogLocator, MaxNLocator as MaxNLocator, MultipleLocator as MultipleLocator, NullFormatter as NullFormatter, NullLocator as NullLocator, ScalarFormatter as ScalarFormatter, TickHelper as TickHelper
from _typeshed import Incomplete
from cycler import cycler as cycler
from matplotlib import cbook as cbook, cm as cm, get_backend as get_backend, interactive as interactive, mlab as mlab, rcParams as rcParams, rcParamsDefault as rcParamsDefault, rcParamsOrig as rcParamsOrig, rcsetup as rcsetup, style as style
from matplotlib.artist import Artist as Artist
from matplotlib.axes import Axes as Axes, Subplot as Subplot
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase, FigureManagerBase as FigureManagerBase, MouseButton as MouseButton
from matplotlib.cm import register_cmap as register_cmap
from matplotlib.colors import Normalize as Normalize
from matplotlib.figure import Figure as Figure, FigureBase as FigureBase, figaspect as figaspect
from matplotlib.gridspec import GridSpec as GridSpec, SubplotSpec as SubplotSpec
from matplotlib.lines import Line2D as Line2D
from matplotlib.patches import Arrow as Arrow, Circle as Circle, Polygon as Polygon, Rectangle as Rectangle
from matplotlib.projections import PolarAxes as PolarAxes
from matplotlib.scale import get_scale_names as get_scale_names
from matplotlib.text import Annotation as Annotation, Text as Text
from matplotlib.widgets import Button as Button, Slider as Slider, Widget as Widget
from numbers import Number as Number

def install_repl_displayhook() -> None:
    """
    Connect to the display hook of the current shell.

    The display hook gets called when the read-evaluate-print-loop (REPL) of
    the shell has finished the execution of a command. We use this callback
    to be able to automatically update a figure in interactive mode.

    This works both with IPython and with vanilla python shells.
    """
def uninstall_repl_displayhook() -> None:
    """Disconnect from the display hook of the current shell."""

draw_all: Incomplete

def set_loglevel(*args, **kwargs): ...
def findobj(o: Incomplete | None = None, match: Incomplete | None = None, include_self: bool = True): ...
def switch_backend(newbackend):
    """
    Set the pyplot backend.

    Switching to an interactive backend is possible only if no event loop for
    another interactive backend has started.  Switching to and from
    non-interactive backends is always possible.

    If the new backend is different than the current backend then all open
    Figures will be closed via ``plt.close('all')``.

    Parameters
    ----------
    newbackend : str
        The case-insensitive name of the backend to use.

    """
def new_figure_manager(*args, **kwargs):
    """Create a new figure manager instance."""
def draw_if_interactive(*args, **kwargs):
    """
    Redraw the current figure if in interactive mode.

    .. warning::

        End users will typically not have to call this function because the
        the interactive mode takes care of this.
    """
def show(*args, **kwargs):
    """
    Display all open figures.

    Parameters
    ----------
    block : bool, optional
        Whether to wait for all figures to be closed before returning.

        If `True` block and run the GUI main loop until all figure windows
        are closed.

        If `False` ensure that all figure windows are displayed and return
        immediately.  In this case, you are responsible for ensuring
        that the event loop is running to have responsive figures.

        Defaults to True in non-interactive mode and to False in interactive
        mode (see `.pyplot.isinteractive`).

    See Also
    --------
    ion : Enable interactive mode, which shows / updates the figure after
          every plotting command, so that calling ``show()`` is not necessary.
    ioff : Disable interactive mode.
    savefig : Save the figure to an image file instead of showing it on screen.

    Notes
    -----
    **Saving figures to file and showing a window at the same time**

    If you want an image file as well as a user interface window, use
    `.pyplot.savefig` before `.pyplot.show`. At the end of (a blocking)
    ``show()`` the figure is closed and thus unregistered from pyplot. Calling
    `.pyplot.savefig` afterwards would save a new and thus empty figure. This
    limitation of command order does not apply if the show is non-blocking or
    if you keep a reference to the figure and use `.Figure.savefig`.

    **Auto-show in jupyter notebooks**

    The jupyter backends (activated via ``%matplotlib inline``,
    ``%matplotlib notebook``, or ``%matplotlib widget``), call ``show()`` at
    the end of every cell by default. Thus, you usually don't have to call it
    explicitly there.
    """
def isinteractive():
    """
    Return whether plots are updated after every plotting command.

    The interactive mode is mainly useful if you build plots from the command
    line and want to see the effect of each command while you are building the
    figure.

    In interactive mode:

    - newly created figures will be shown immediately;
    - figures will automatically redraw on change;
    - `.pyplot.show` will not block by default.

    In non-interactive mode:

    - newly created figures and changes to figures will not be reflected until
      explicitly asked to be;
    - `.pyplot.show` will block by default.

    See Also
    --------
    ion : Enable interactive mode.
    ioff : Disable interactive mode.
    show : Show all figures (and maybe block).
    pause : Show all figures, and block for a time.
    """
def ioff():
    """
    Disable interactive mode.

    See `.pyplot.isinteractive` for more details.

    See Also
    --------
    ion : Enable interactive mode.
    isinteractive : Whether interactive mode is enabled.
    show : Show all figures (and maybe block).
    pause : Show all figures, and block for a time.

    Notes
    -----
    For a temporary change, this can be used as a context manager::

        # if interactive mode is on
        # then figures will be shown on creation
        plt.ion()
        # This figure will be shown immediately
        fig = plt.figure()

        with plt.ioff():
            # interactive mode will be off
            # figures will not automatically be shown
            fig2 = plt.figure()
            # ...

    To enable optional usage as a context manager, this function returns a
    `~contextlib.ExitStack` object, which is not intended to be stored or
    accessed by the user.
    """
def ion():
    """
    Enable interactive mode.

    See `.pyplot.isinteractive` for more details.

    See Also
    --------
    ioff : Disable interactive mode.
    isinteractive : Whether interactive mode is enabled.
    show : Show all figures (and maybe block).
    pause : Show all figures, and block for a time.

    Notes
    -----
    For a temporary change, this can be used as a context manager::

        # if interactive mode is off
        # then figures will not be shown on creation
        plt.ioff()
        # This figure will not be shown immediately
        fig = plt.figure()

        with plt.ion():
            # interactive mode will be on
            # figures will automatically be shown
            fig2 = plt.figure()
            # ...

    To enable optional usage as a context manager, this function returns a
    `~contextlib.ExitStack` object, which is not intended to be stored or
    accessed by the user.
    """
def pause(interval) -> None:
    """
    Run the GUI event loop for *interval* seconds.

    If there is an active figure, it will be updated and displayed before the
    pause, and the GUI event loop (if any) will run during the pause.

    This can be used for crude animation.  For more complex animation use
    :mod:`matplotlib.animation`.

    If there is no active figure, sleep for *interval* seconds instead.

    See Also
    --------
    matplotlib.animation : Proper animations
    show : Show all figures and optional block until all figures are closed.
    """
def rc(group, **kwargs) -> None: ...
def rc_context(rc: Incomplete | None = None, fname: Incomplete | None = None): ...
def rcdefaults() -> None: ...
def getp(obj, *args, **kwargs): ...
def get(obj, *args, **kwargs): ...
def setp(obj, *args, **kwargs): ...
def xkcd(scale: int = 1, length: int = 100, randomness: int = 2):
    '''
    Turn on `xkcd <https://xkcd.com/>`_ sketch-style drawing mode.  This will
    only have effect on things drawn after this function is called.

    For best results, the "Humor Sans" font should be installed: it is
    not included with Matplotlib.

    Parameters
    ----------
    scale : float, optional
        The amplitude of the wiggle perpendicular to the source line.
    length : float, optional
        The length of the wiggle along the line.
    randomness : float, optional
        The scale factor by which the length is shrunken or expanded.

    Notes
    -----
    This function works by a number of rcParams, so it will probably
    override others you have set before.

    If you want the effects of this function to be temporary, it can
    be used as a context manager, for example::

        with plt.xkcd():
            # This figure will be in XKCD-style
            fig1 = plt.figure()
            # ...

        # This figure will be in regular style
        fig2 = plt.figure()
    '''
def figure(num: Incomplete | None = None, figsize: Incomplete | None = None, dpi: Incomplete | None = None, facecolor: Incomplete | None = None, edgecolor: Incomplete | None = None, frameon: bool = True, FigureClass=..., clear: bool = False, **kwargs):
    """
    Create a new figure, or activate an existing figure.

    Parameters
    ----------
    num : int or str or `.Figure` or `.SubFigure`, optional
        A unique identifier for the figure.

        If a figure with that identifier already exists, this figure is made
        active and returned. An integer refers to the ``Figure.number``
        attribute, a string refers to the figure label.

        If there is no figure with the identifier or *num* is not given, a new
        figure is created, made active and returned.  If *num* is an int, it
        will be used for the ``Figure.number`` attribute, otherwise, an
        auto-generated integer value is used (starting at 1 and incremented
        for each new figure). If *num* is a string, the figure label and the
        window title is set to this value.  If num is a ``SubFigure``, its
        parent ``Figure`` is activated.

    figsize : (float, float), default: :rc:`figure.figsize`
        Width, height in inches.

    dpi : float, default: :rc:`figure.dpi`
        The resolution of the figure in dots-per-inch.

    facecolor : color, default: :rc:`figure.facecolor`
        The background color.

    edgecolor : color, default: :rc:`figure.edgecolor`
        The border color.

    frameon : bool, default: True
        If False, suppress drawing the figure frame.

    FigureClass : subclass of `~matplotlib.figure.Figure`
        If set, an instance of this subclass will be created, rather than a
        plain `.Figure`.

    clear : bool, default: False
        If True and the figure already exists, then it is cleared.

    layout : {'constrained', 'compressed', 'tight', 'none', `.LayoutEngine`, None}, default: None
        The layout mechanism for positioning of plot elements to avoid
        overlapping Axes decorations (labels, ticks, etc). Note that layout
        managers can measurably slow down figure display.

        - 'constrained': The constrained layout solver adjusts axes sizes
          to avoid overlapping axes decorations.  Can handle complex plot
          layouts and colorbars, and is thus recommended.

          See :doc:`/tutorials/intermediate/constrainedlayout_guide`
          for examples.

        - 'compressed': uses the same algorithm as 'constrained', but
          removes extra space between fixed-aspect-ratio Axes.  Best for
          simple grids of axes.

        - 'tight': Use the tight layout mechanism. This is a relatively
          simple algorithm that adjusts the subplot parameters so that
          decorations do not overlap. See `.Figure.set_tight_layout` for
          further details.

        - 'none': Do not use a layout engine.

        - A `.LayoutEngine` instance. Builtin layout classes are
          `.ConstrainedLayoutEngine` and `.TightLayoutEngine`, more easily
          accessible by 'constrained' and 'tight'.  Passing an instance
          allows third parties to provide their own layout engine.

        If not given, fall back to using the parameters *tight_layout* and
        *constrained_layout*, including their config defaults
        :rc:`figure.autolayout` and :rc:`figure.constrained_layout.use`.

    **kwargs
        Additional keyword arguments are passed to the `.Figure` constructor.

    Returns
    -------
    `~matplotlib.figure.Figure`

    Notes
    -----
    A newly created figure is passed to the `~.FigureCanvasBase.new_manager`
    method or the `new_figure_manager` function provided by the current
    backend, which install a canvas and a manager on the figure.

    Once this is done, :rc:`figure.hooks` are called, one at a time, on the
    figure; these hooks allow arbitrary customization of the figure (e.g.,
    attaching callbacks) or of associated elements (e.g., modifying the
    toolbar).  See :doc:`/gallery/user_interfaces/mplcvd` for an example of
    toolbar customization.

    If you are creating many figures, make sure you explicitly call
    `.pyplot.close` on the figures you are not using, because this will
    enable pyplot to properly clean up the memory.

    `~matplotlib.rcParams` defines the default values, which can be modified
    in the matplotlibrc file.
    """
def gcf():
    """
    Get the current figure.

    If there is currently no figure on the pyplot figure stack, a new one is
    created using `~.pyplot.figure()`.  (To test whether there is currently a
    figure on the pyplot figure stack, check whether `~.pyplot.get_fignums()`
    is empty.)
    """
def fignum_exists(num):
    """Return whether the figure with the given id exists."""
def get_fignums():
    """Return a list of existing figure numbers."""
def get_figlabels():
    """Return a list of existing figure labels."""
def get_current_fig_manager():
    """
    Return the figure manager of the current figure.

    The figure manager is a container for the actual backend-depended window
    that displays the figure on screen.

    If no current figure exists, a new one is created, and its figure
    manager is returned.

    Returns
    -------
    `.FigureManagerBase` or backend-dependent subclass thereof
    """
def connect(s, func): ...
def disconnect(cid): ...
def close(fig: Incomplete | None = None) -> None:
    """
    Close a figure window.

    Parameters
    ----------
    fig : None or int or str or `.Figure`
        The figure to close. There are a number of ways to specify this:

        - *None*: the current figure
        - `.Figure`: the given `.Figure` instance
        - ``int``: a figure number
        - ``str``: a figure name
        - 'all': all figures

    """
def clf() -> None:
    """Clear the current figure."""
def draw() -> None:
    '''
    Redraw the current figure.

    This is used to update a figure that has been altered, but not
    automatically re-drawn.  If interactive mode is on (via `.ion()`), this
    should be only rarely needed, but there may be ways to modify the state of
    a figure without marking it as "stale".  Please report these cases as bugs.

    This is equivalent to calling ``fig.canvas.draw_idle()``, where ``fig`` is
    the current figure.

    See Also
    --------
    .FigureCanvasBase.draw_idle
    .FigureCanvasBase.draw
    '''
def savefig(*args, **kwargs): ...
def figlegend(*args, **kwargs): ...
def axes(arg: Incomplete | None = None, **kwargs):
    """
    Add an Axes to the current figure and make it the current Axes.

    Call signatures::

        plt.axes()
        plt.axes(rect, projection=None, polar=False, **kwargs)
        plt.axes(ax)

    Parameters
    ----------
    arg : None or 4-tuple
        The exact behavior of this function depends on the type:

        - *None*: A new full window Axes is added using
          ``subplot(**kwargs)``.
        - 4-tuple of floats *rect* = ``[left, bottom, width, height]``.
          A new Axes is added with dimensions *rect* in normalized
          (0, 1) units using `~.Figure.add_axes` on the current figure.

    projection : {None, 'aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear', str}, optional
        The projection type of the `~.axes.Axes`. *str* is the name of
        a custom projection, see `~matplotlib.projections`. The default
        None results in a 'rectilinear' projection.

    polar : bool, default: False
        If True, equivalent to projection='polar'.

    sharex, sharey : `~matplotlib.axes.Axes`, optional
        Share the x or y `~matplotlib.axis` with sharex and/or sharey.
        The axis will have the same limits, ticks, and scale as the axis
        of the shared Axes.

    label : str
        A label for the returned Axes.

    Returns
    -------
    `~.axes.Axes`, or a subclass of `~.axes.Axes`
        The returned axes class depends on the projection used. It is
        `~.axes.Axes` if rectilinear projection is used and
        `.projections.polar.PolarAxes` if polar projection is used.

    Other Parameters
    ----------------
    **kwargs
        This method also takes the keyword arguments for
        the returned Axes class. The keyword arguments for the
        rectilinear Axes class `~.axes.Axes` can be found in
        the following table but there might also be other keyword
        arguments if another projection is used, see the actual Axes
        class.

        %(Axes:kwdoc)s

    See Also
    --------
    .Figure.add_axes
    .pyplot.subplot
    .Figure.add_subplot
    .Figure.subplots
    .pyplot.subplots

    Examples
    --------
    ::

        # Creating a new full window Axes
        plt.axes()

        # Creating a new Axes with specified dimensions and a grey background
        plt.axes((left, bottom, width, height), facecolor='grey')
    """
def delaxes(ax: Incomplete | None = None) -> None:
    """
    Remove an `~.axes.Axes` (defaulting to the current axes) from its figure.
    """
def sca(ax) -> None:
    """
    Set the current Axes to *ax* and the current Figure to the parent of *ax*.
    """
def cla():
    """Clear the current axes."""
def subplot(*args, **kwargs):
    '''
    Add an Axes to the current figure or retrieve an existing Axes.

    This is a wrapper of `.Figure.add_subplot` which provides additional
    behavior when working with the implicit API (see the notes section).

    Call signatures::

       subplot(nrows, ncols, index, **kwargs)
       subplot(pos, **kwargs)
       subplot(**kwargs)
       subplot(ax)

    Parameters
    ----------
    *args : int, (int, int, *index*), or `.SubplotSpec`, default: (1, 1, 1)
        The position of the subplot described by one of

        - Three integers (*nrows*, *ncols*, *index*). The subplot will take the
          *index* position on a grid with *nrows* rows and *ncols* columns.
          *index* starts at 1 in the upper left corner and increases to the
          right. *index* can also be a two-tuple specifying the (*first*,
          *last*) indices (1-based, and including *last*) of the subplot, e.g.,
          ``fig.add_subplot(3, 1, (1, 2))`` makes a subplot that spans the
          upper 2/3 of the figure.
        - A 3-digit integer. The digits are interpreted as if given separately
          as three single-digit integers, i.e. ``fig.add_subplot(235)`` is the
          same as ``fig.add_subplot(2, 3, 5)``. Note that this can only be used
          if there are no more than 9 subplots.
        - A `.SubplotSpec`.

    projection : {None, \'aitoff\', \'hammer\', \'lambert\', \'mollweide\', \'polar\', \'rectilinear\', str}, optional
        The projection type of the subplot (`~.axes.Axes`). *str* is the name
        of a custom projection, see `~matplotlib.projections`. The default
        None results in a \'rectilinear\' projection.

    polar : bool, default: False
        If True, equivalent to projection=\'polar\'.

    sharex, sharey : `~matplotlib.axes.Axes`, optional
        Share the x or y `~matplotlib.axis` with sharex and/or sharey. The
        axis will have the same limits, ticks, and scale as the axis of the
        shared axes.

    label : str
        A label for the returned axes.

    Returns
    -------
    `~.axes.Axes`

        The Axes of the subplot. The returned Axes can actually be an instance
        of a subclass, such as `.projections.polar.PolarAxes` for polar
        projections.

    Other Parameters
    ----------------
    **kwargs
        This method also takes the keyword arguments for the returned axes
        base class; except for the *figure* argument. The keyword arguments
        for the rectilinear base class `~.axes.Axes` can be found in
        the following table but there might also be other keyword
        arguments if another projection is used.

        %(Axes:kwdoc)s

    Notes
    -----
    Creating a new Axes will delete any preexisting Axes that
    overlaps with it beyond sharing a boundary::

        import matplotlib.pyplot as plt
        # plot a line, implicitly creating a subplot(111)
        plt.plot([1, 2, 3])
        # now create a subplot which represents the top plot of a grid
        # with 2 rows and 1 column. Since this subplot will overlap the
        # first, the plot (and its axes) previously created, will be removed
        plt.subplot(211)

    If you do not want this behavior, use the `.Figure.add_subplot` method
    or the `.pyplot.axes` function instead.

    If no *kwargs* are passed and there exists an Axes in the location
    specified by *args* then that Axes will be returned rather than a new
    Axes being created.

    If *kwargs* are passed and there exists an Axes in the location
    specified by *args*, the projection type is the same, and the
    *kwargs* match with the existing Axes, then the existing Axes is
    returned.  Otherwise a new Axes is created with the specified
    parameters.  We save a reference to the *kwargs* which we use
    for this comparison.  If any of the values in *kwargs* are
    mutable we will not detect the case where they are mutated.
    In these cases we suggest using `.Figure.add_subplot` and the
    explicit Axes API rather than the implicit pyplot API.

    See Also
    --------
    .Figure.add_subplot
    .pyplot.subplots
    .pyplot.axes
    .Figure.subplots

    Examples
    --------
    ::

        plt.subplot(221)

        # equivalent but more general
        ax1 = plt.subplot(2, 2, 1)

        # add a subplot with no frame
        ax2 = plt.subplot(222, frameon=False)

        # add a polar subplot
        plt.subplot(223, projection=\'polar\')

        # add a red subplot that shares the x-axis with ax1
        plt.subplot(224, sharex=ax1, facecolor=\'red\')

        # delete ax2 from the figure
        plt.delaxes(ax2)

        # add ax2 to the figure again
        plt.subplot(ax2)

        # make the first axes "current" again
        plt.subplot(221)

    '''
def subplots(nrows: int = 1, ncols: int = 1, *, sharex: bool = False, sharey: bool = False, squeeze: bool = True, width_ratios: Incomplete | None = None, height_ratios: Incomplete | None = None, subplot_kw: Incomplete | None = None, gridspec_kw: Incomplete | None = None, **fig_kw):
    '''
    Create a figure and a set of subplots.

    This utility wrapper makes it convenient to create common layouts of
    subplots, including the enclosing figure object, in a single call.

    Parameters
    ----------
    nrows, ncols : int, default: 1
        Number of rows/columns of the subplot grid.

    sharex, sharey : bool or {\'none\', \'all\', \'row\', \'col\'}, default: False
        Controls sharing of properties among x (*sharex*) or y (*sharey*)
        axes:

        - True or \'all\': x- or y-axis will be shared among all subplots.
        - False or \'none\': each subplot x- or y-axis will be independent.
        - \'row\': each subplot row will share an x- or y-axis.
        - \'col\': each subplot column will share an x- or y-axis.

        When subplots have a shared x-axis along a column, only the x tick
        labels of the bottom subplot are created. Similarly, when subplots
        have a shared y-axis along a row, only the y tick labels of the first
        column subplot are created. To later turn other subplots\' ticklabels
        on, use `~matplotlib.axes.Axes.tick_params`.

        When subplots have a shared axis that has units, calling
        `~matplotlib.axis.Axis.set_units` will update each axis with the
        new units.

    squeeze : bool, default: True
        - If True, extra dimensions are squeezed out from the returned
          array of `~matplotlib.axes.Axes`:

          - if only one subplot is constructed (nrows=ncols=1), the
            resulting single Axes object is returned as a scalar.
          - for Nx1 or 1xM subplots, the returned object is a 1D numpy
            object array of Axes objects.
          - for NxM, subplots with N>1 and M>1 are returned as a 2D array.

        - If False, no squeezing at all is done: the returned Axes object is
          always a 2D array containing Axes instances, even if it ends up
          being 1x1.

    width_ratios : array-like of length *ncols*, optional
        Defines the relative widths of the columns. Each column gets a
        relative width of ``width_ratios[i] / sum(width_ratios)``.
        If not given, all columns will have the same width.  Equivalent
        to ``gridspec_kw={\'width_ratios\': [...]}``.

    height_ratios : array-like of length *nrows*, optional
        Defines the relative heights of the rows. Each row gets a
        relative height of ``height_ratios[i] / sum(height_ratios)``.
        If not given, all rows will have the same height. Convenience
        for ``gridspec_kw={\'height_ratios\': [...]}``.

    subplot_kw : dict, optional
        Dict with keywords passed to the
        `~matplotlib.figure.Figure.add_subplot` call used to create each
        subplot.

    gridspec_kw : dict, optional
        Dict with keywords passed to the `~matplotlib.gridspec.GridSpec`
        constructor used to create the grid the subplots are placed on.

    **fig_kw
        All additional keyword arguments are passed to the
        `.pyplot.figure` call.

    Returns
    -------
    fig : `.Figure`

    ax : `~matplotlib.axes.Axes` or array of Axes
        *ax* can be either a single `~.axes.Axes` object, or an array of Axes
        objects if more than one subplot was created.  The dimensions of the
        resulting array can be controlled with the squeeze keyword, see above.

        Typical idioms for handling the return value are::

            # using the variable ax for single a Axes
            fig, ax = plt.subplots()

            # using the variable axs for multiple Axes
            fig, axs = plt.subplots(2, 2)

            # using tuple unpacking for multiple Axes
            fig, (ax1, ax2) = plt.subplots(1, 2)
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

        The names ``ax`` and pluralized ``axs`` are preferred over ``axes``
        because for the latter it\'s not clear if it refers to a single
        `~.axes.Axes` instance or a collection of these.

    See Also
    --------
    .pyplot.figure
    .pyplot.subplot
    .pyplot.axes
    .Figure.subplots
    .Figure.add_subplot

    Examples
    --------
    ::

        # First create some toy data:
        x = np.linspace(0, 2*np.pi, 400)
        y = np.sin(x**2)

        # Create just a figure and only one subplot
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(\'Simple plot\')

        # Create two subplots and unpack the output array immediately
        f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
        ax1.plot(x, y)
        ax1.set_title(\'Sharing Y axis\')
        ax2.scatter(x, y)

        # Create four polar axes and access them through the returned array
        fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
        axs[0, 0].plot(x, y)
        axs[1, 1].scatter(x, y)

        # Share a X axis with each column of subplots
        plt.subplots(2, 2, sharex=\'col\')

        # Share a Y axis with each row of subplots
        plt.subplots(2, 2, sharey=\'row\')

        # Share both X and Y axes with all subplots
        plt.subplots(2, 2, sharex=\'all\', sharey=\'all\')

        # Note that this is the same as
        plt.subplots(2, 2, sharex=True, sharey=True)

        # Create figure number 10 with a single subplot
        # and clears it if it already exists.
        fig, ax = plt.subplots(num=10, clear=True)

    '''
def subplot_mosaic(mosaic, *, sharex: bool = False, sharey: bool = False, width_ratios: Incomplete | None = None, height_ratios: Incomplete | None = None, empty_sentinel: str = '.', subplot_kw: Incomplete | None = None, gridspec_kw: Incomplete | None = None, per_subplot_kw: Incomplete | None = None, **fig_kw):
    '''
    Build a layout of Axes based on ASCII art or nested lists.

    This is a helper function to build complex GridSpec layouts visually.

    See :doc:`/gallery/subplots_axes_and_figures/mosaic`
    for an example and full API documentation

    Parameters
    ----------
    mosaic : list of list of {hashable or nested} or str

        A visual layout of how you want your Axes to be arranged
        labeled as strings.  For example ::

           x = [[\'A panel\', \'A panel\', \'edge\'],
                [\'C panel\', \'.\',       \'edge\']]

        produces 4 axes:

        - \'A panel\' which is 1 row high and spans the first two columns
        - \'edge\' which is 2 rows high and is on the right edge
        - \'C panel\' which in 1 row and 1 column wide in the bottom left
        - a blank space 1 row and 1 column wide in the bottom center

        Any of the entries in the layout can be a list of lists
        of the same form to create nested layouts.

        If input is a str, then it must be of the form ::

          \'\'\'
          AAE
          C.E
          \'\'\'

        where each character is a column and each line is a row.
        This only allows only single character Axes labels and does
        not allow nesting but is very terse.

    sharex, sharey : bool, default: False
        If True, the x-axis (*sharex*) or y-axis (*sharey*) will be shared
        among all subplots.  In that case, tick label visibility and axis units
        behave as for `subplots`.  If False, each subplot\'s x- or y-axis will
        be independent.

    width_ratios : array-like of length *ncols*, optional
        Defines the relative widths of the columns. Each column gets a
        relative width of ``width_ratios[i] / sum(width_ratios)``.
        If not given, all columns will have the same width.  Convenience
        for ``gridspec_kw={\'width_ratios\': [...]}``.

    height_ratios : array-like of length *nrows*, optional
        Defines the relative heights of the rows. Each row gets a
        relative height of ``height_ratios[i] / sum(height_ratios)``.
        If not given, all rows will have the same height. Convenience
        for ``gridspec_kw={\'height_ratios\': [...]}``.

    empty_sentinel : object, optional
        Entry in the layout to mean "leave this space empty".  Defaults
        to ``\'.\'``. Note, if *layout* is a string, it is processed via
        `inspect.cleandoc` to remove leading white space, which may
        interfere with using white-space as the empty sentinel.

    subplot_kw : dict, optional
        Dictionary with keywords passed to the `.Figure.add_subplot` call
        used to create each subplot.  These values may be overridden by
        values in *per_subplot_kw*.

    per_subplot_kw : dict, optional
        A dictionary mapping the Axes identifiers or tuples of identifiers
        to a dictionary of keyword arguments to be passed to the
        `.Figure.add_subplot` call used to create each subplot.  The values
        in these dictionaries have precedence over the values in
        *subplot_kw*.

        If *mosaic* is a string, and thus all keys are single characters,
        it is possible to use a single string instead of a tuple as keys;
        i.e. ``"AB"`` is equivalent to ``("A", "B")``.

        .. versionadded:: 3.7

    gridspec_kw : dict, optional
        Dictionary with keywords passed to the `.GridSpec` constructor used
        to create the grid the subplots are placed on.

    **fig_kw
        All additional keyword arguments are passed to the
        `.pyplot.figure` call.

    Returns
    -------
    fig : `.Figure`
       The new figure

    dict[label, Axes]
       A dictionary mapping the labels to the Axes objects.  The order of
       the axes is left-to-right and top-to-bottom of their position in the
       total layout.

    '''
def subplot2grid(shape, loc, rowspan: int = 1, colspan: int = 1, fig: Incomplete | None = None, **kwargs):
    """
    Create a subplot at a specific location inside a regular grid.

    Parameters
    ----------
    shape : (int, int)
        Number of rows and of columns of the grid in which to place axis.
    loc : (int, int)
        Row number and column number of the axis location within the grid.
    rowspan : int, default: 1
        Number of rows for the axis to span downwards.
    colspan : int, default: 1
        Number of columns for the axis to span to the right.
    fig : `.Figure`, optional
        Figure to place the subplot in. Defaults to the current figure.
    **kwargs
        Additional keyword arguments are handed to `~.Figure.add_subplot`.

    Returns
    -------
    `~.axes.Axes`

        The Axes of the subplot. The returned Axes can actually be an instance
        of a subclass, such as `.projections.polar.PolarAxes` for polar
        projections.

    Notes
    -----
    The following call ::

        ax = subplot2grid((nrows, ncols), (row, col), rowspan, colspan)

    is identical to ::

        fig = gcf()
        gs = fig.add_gridspec(nrows, ncols)
        ax = fig.add_subplot(gs[row:row+rowspan, col:col+colspan])
    """
def twinx(ax: Incomplete | None = None):
    """
    Make and return a second axes that shares the *x*-axis.  The new axes will
    overlay *ax* (or the current axes if *ax* is *None*), and its ticks will be
    on the right.

    Examples
    --------
    :doc:`/gallery/subplots_axes_and_figures/two_scales`
    """
def twiny(ax: Incomplete | None = None):
    """
    Make and return a second axes that shares the *y*-axis.  The new axes will
    overlay *ax* (or the current axes if *ax* is *None*), and its ticks will be
    on the top.

    Examples
    --------
    :doc:`/gallery/subplots_axes_and_figures/two_scales`
    """
def subplot_tool(targetfig: Incomplete | None = None):
    """
    Launch a subplot tool window for a figure.

    Returns
    -------
    `matplotlib.widgets.SubplotTool`
    """
def box(on: Incomplete | None = None) -> None:
    """
    Turn the axes box on or off on the current axes.

    Parameters
    ----------
    on : bool or None
        The new `~matplotlib.axes.Axes` box state. If ``None``, toggle
        the state.

    See Also
    --------
    :meth:`matplotlib.axes.Axes.set_frame_on`
    :meth:`matplotlib.axes.Axes.get_frame_on`
    """
def xlim(*args, **kwargs):
    """
    Get or set the x limits of the current axes.

    Call signatures::

        left, right = xlim()  # return the current xlim
        xlim((left, right))   # set the xlim to left, right
        xlim(left, right)     # set the xlim to left, right

    If you do not specify args, you can pass *left* or *right* as kwargs,
    i.e.::

        xlim(right=3)  # adjust the right leaving left unchanged
        xlim(left=1)  # adjust the left leaving right unchanged

    Setting limits turns autoscaling off for the x-axis.

    Returns
    -------
    left, right
        A tuple of the new x-axis limits.

    Notes
    -----
    Calling this function with no arguments (e.g. ``xlim()``) is the pyplot
    equivalent of calling `~.Axes.get_xlim` on the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_xlim` on the current axes. All arguments are passed though.
    """
def ylim(*args, **kwargs):
    """
    Get or set the y-limits of the current axes.

    Call signatures::

        bottom, top = ylim()  # return the current ylim
        ylim((bottom, top))   # set the ylim to bottom, top
        ylim(bottom, top)     # set the ylim to bottom, top

    If you do not specify args, you can alternatively pass *bottom* or
    *top* as kwargs, i.e.::

        ylim(top=3)  # adjust the top leaving bottom unchanged
        ylim(bottom=1)  # adjust the bottom leaving top unchanged

    Setting limits turns autoscaling off for the y-axis.

    Returns
    -------
    bottom, top
        A tuple of the new y-axis limits.

    Notes
    -----
    Calling this function with no arguments (e.g. ``ylim()``) is the pyplot
    equivalent of calling `~.Axes.get_ylim` on the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_ylim` on the current axes. All arguments are passed though.
    """
def xticks(ticks: Incomplete | None = None, labels: Incomplete | None = None, *, minor: bool = False, **kwargs):
    """
    Get or set the current tick locations and labels of the x-axis.

    Pass no arguments to return the current values without modifying them.

    Parameters
    ----------
    ticks : array-like, optional
        The list of xtick locations.  Passing an empty list removes all xticks.
    labels : array-like, optional
        The labels to place at the given *ticks* locations.  This argument can
        only be passed if *ticks* is passed as well.
    minor : bool, default: False
        If ``False``, get/set the major ticks/labels; if ``True``, the minor
        ticks/labels.
    **kwargs
        `.Text` properties can be used to control the appearance of the labels.

    Returns
    -------
    locs
        The list of xtick locations.
    labels
        The list of xlabel `.Text` objects.

    Notes
    -----
    Calling this function with no arguments (e.g. ``xticks()``) is the pyplot
    equivalent of calling `~.Axes.get_xticks` and `~.Axes.get_xticklabels` on
    the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_xticks` and `~.Axes.set_xticklabels` on the current axes.

    Examples
    --------
    >>> locs, labels = xticks()  # Get the current locations and labels.
    >>> xticks(np.arange(0, 1, step=0.2))  # Set label locations.
    >>> xticks(np.arange(3), ['Tom', 'Dick', 'Sue'])  # Set text labels.
    >>> xticks([0, 1, 2], ['January', 'February', 'March'],
    ...        rotation=20)  # Set text labels and properties.
    >>> xticks([])  # Disable xticks.
    """
def yticks(ticks: Incomplete | None = None, labels: Incomplete | None = None, *, minor: bool = False, **kwargs):
    """
    Get or set the current tick locations and labels of the y-axis.

    Pass no arguments to return the current values without modifying them.

    Parameters
    ----------
    ticks : array-like, optional
        The list of ytick locations.  Passing an empty list removes all yticks.
    labels : array-like, optional
        The labels to place at the given *ticks* locations.  This argument can
        only be passed if *ticks* is passed as well.
    minor : bool, default: False
        If ``False``, get/set the major ticks/labels; if ``True``, the minor
        ticks/labels.
    **kwargs
        `.Text` properties can be used to control the appearance of the labels.

    Returns
    -------
    locs
        The list of ytick locations.
    labels
        The list of ylabel `.Text` objects.

    Notes
    -----
    Calling this function with no arguments (e.g. ``yticks()``) is the pyplot
    equivalent of calling `~.Axes.get_yticks` and `~.Axes.get_yticklabels` on
    the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_yticks` and `~.Axes.set_yticklabels` on the current axes.

    Examples
    --------
    >>> locs, labels = yticks()  # Get the current locations and labels.
    >>> yticks(np.arange(0, 1, step=0.2))  # Set label locations.
    >>> yticks(np.arange(3), ['Tom', 'Dick', 'Sue'])  # Set text labels.
    >>> yticks([0, 1, 2], ['January', 'February', 'March'],
    ...        rotation=45)  # Set text labels and properties.
    >>> yticks([])  # Disable yticks.
    """
def rgrids(radii: Incomplete | None = None, labels: Incomplete | None = None, angle: Incomplete | None = None, fmt: Incomplete | None = None, **kwargs):
    """
    Get or set the radial gridlines on the current polar plot.

    Call signatures::

     lines, labels = rgrids()
     lines, labels = rgrids(radii, labels=None, angle=22.5, fmt=None, **kwargs)

    When called with no arguments, `.rgrids` simply returns the tuple
    (*lines*, *labels*). When called with arguments, the labels will
    appear at the specified radial distances and angle.

    Parameters
    ----------
    radii : tuple with floats
        The radii for the radial gridlines

    labels : tuple with strings or None
        The labels to use at each radial gridline. The
        `matplotlib.ticker.ScalarFormatter` will be used if None.

    angle : float
        The angular position of the radius labels in degrees.

    fmt : str or None
        Format string used in `matplotlib.ticker.FormatStrFormatter`.
        For example '%f'.

    Returns
    -------
    lines : list of `.lines.Line2D`
        The radial gridlines.

    labels : list of `.text.Text`
        The tick labels.

    Other Parameters
    ----------------
    **kwargs
        *kwargs* are optional `.Text` properties for the labels.

    See Also
    --------
    .pyplot.thetagrids
    .projections.polar.PolarAxes.set_rgrids
    .Axis.get_gridlines
    .Axis.get_ticklabels

    Examples
    --------
    ::

      # set the locations of the radial gridlines
      lines, labels = rgrids( (0.25, 0.5, 1.0) )

      # set the locations and labels of the radial gridlines
      lines, labels = rgrids( (0.25, 0.5, 1.0), ('Tom', 'Dick', 'Harry' ))
    """
def thetagrids(angles: Incomplete | None = None, labels: Incomplete | None = None, fmt: Incomplete | None = None, **kwargs):
    """
    Get or set the theta gridlines on the current polar plot.

    Call signatures::

     lines, labels = thetagrids()
     lines, labels = thetagrids(angles, labels=None, fmt=None, **kwargs)

    When called with no arguments, `.thetagrids` simply returns the tuple
    (*lines*, *labels*). When called with arguments, the labels will
    appear at the specified angles.

    Parameters
    ----------
    angles : tuple with floats, degrees
        The angles of the theta gridlines.

    labels : tuple with strings or None
        The labels to use at each radial gridline. The
        `.projections.polar.ThetaFormatter` will be used if None.

    fmt : str or None
        Format string used in `matplotlib.ticker.FormatStrFormatter`.
        For example '%f'. Note that the angle in radians will be used.

    Returns
    -------
    lines : list of `.lines.Line2D`
        The theta gridlines.

    labels : list of `.text.Text`
        The tick labels.

    Other Parameters
    ----------------
    **kwargs
        *kwargs* are optional `.Text` properties for the labels.

    See Also
    --------
    .pyplot.rgrids
    .projections.polar.PolarAxes.set_thetagrids
    .Axis.get_gridlines
    .Axis.get_ticklabels

    Examples
    --------
    ::

      # set the locations of the angular gridlines
      lines, labels = thetagrids(range(45, 360, 90))

      # set the locations and labels of the angular gridlines
      lines, labels = thetagrids(range(45, 360, 90), ('NE', 'NW', 'SW', 'SE'))
    """
def get_plot_commands():
    """
    Get a sorted list of all of the plotting commands.
    """
def colorbar(mappable: Incomplete | None = None, cax: Incomplete | None = None, ax: Incomplete | None = None, **kwargs): ...
def clim(vmin: Incomplete | None = None, vmax: Incomplete | None = None) -> None:
    """
    Set the color limits of the current image.

    If either *vmin* or *vmax* is None, the image min/max respectively
    will be used for color scaling.

    If you want to set the clim of multiple images, use
    `~.ScalarMappable.set_clim` on every image, for example::

      for im in gca().get_images():
          im.set_clim(0, 0.5)

    """
def get_cmap(name: Incomplete | None = None, lut: Incomplete | None = None): ...
def set_cmap(cmap) -> None:
    """
    Set the default colormap, and applies it to the current image if any.

    Parameters
    ----------
    cmap : `~matplotlib.colors.Colormap` or str
        A colormap instance or the name of a registered colormap.

    See Also
    --------
    colormaps
    matplotlib.cm.register_cmap
    matplotlib.cm.get_cmap
    """
def imread(fname, format: Incomplete | None = None): ...
def imsave(fname, arr, **kwargs): ...
def matshow(A, fignum: Incomplete | None = None, **kwargs):
    """
    Display an array as a matrix in a new figure window.

    The origin is set at the upper left hand corner and rows (first
    dimension of the array) are displayed horizontally.  The aspect
    ratio of the figure window is that of the array, unless this would
    make an excessively short or narrow figure.

    Tick labels for the xaxis are placed on top.

    Parameters
    ----------
    A : 2D array-like
        The matrix to be displayed.

    fignum : None or int or False
        If *None*, create a new figure window with automatic numbering.

        If a nonzero integer, draw into the figure with the given number
        (create it if it does not exist).

        If 0, use the current axes (or create one if it does not exist).

        .. note::

           Because of how `.Axes.matshow` tries to set the figure aspect
           ratio to be the one of the array, strange things may happen if you
           reuse an existing figure.

    Returns
    -------
    `~matplotlib.image.AxesImage`

    Other Parameters
    ----------------
    **kwargs : `~matplotlib.axes.Axes.imshow` arguments

    """
def polar(*args, **kwargs):
    """
    Make a polar plot.

    call signature::

      polar(theta, r, **kwargs)

    Multiple *theta*, *r* arguments are supported, with format strings, as in
    `plot`.
    """
def figimage(X, xo: int = 0, yo: int = 0, alpha: Incomplete | None = None, norm: Incomplete | None = None, cmap: Incomplete | None = None, vmin: Incomplete | None = None, vmax: Incomplete | None = None, origin: Incomplete | None = None, resize: bool = False, **kwargs): ...
def figtext(x, y, s, fontdict: Incomplete | None = None, **kwargs): ...
def gca(): ...
def gci(): ...
def ginput(n: int = 1, timeout: int = 30, show_clicks: bool = True, mouse_add=..., mouse_pop=..., mouse_stop=...): ...
def subplots_adjust(left: Incomplete | None = None, bottom: Incomplete | None = None, right: Incomplete | None = None, top: Incomplete | None = None, wspace: Incomplete | None = None, hspace: Incomplete | None = None): ...
def suptitle(t, **kwargs): ...
def tight_layout(*, pad: float = 1.08, h_pad: Incomplete | None = None, w_pad: Incomplete | None = None, rect: Incomplete | None = None): ...
def waitforbuttonpress(timeout: int = -1): ...
def acorr(x, *, data: Incomplete | None = None, **kwargs): ...
def angle_spectrum(x, Fs: Incomplete | None = None, Fc: Incomplete | None = None, window: Incomplete | None = None, pad_to: Incomplete | None = None, sides: Incomplete | None = None, *, data: Incomplete | None = None, **kwargs): ...
def annotate(text, xy, xytext: Incomplete | None = None, xycoords: str = 'data', textcoords: Incomplete | None = None, arrowprops: Incomplete | None = None, annotation_clip: Incomplete | None = None, **kwargs): ...
def arrow(x, y, dx, dy, **kwargs): ...
def autoscale(enable: bool = True, axis: str = 'both', tight: Incomplete | None = None): ...
def axhline(y: int = 0, xmin: int = 0, xmax: int = 1, **kwargs): ...
def axhspan(ymin, ymax, xmin: int = 0, xmax: int = 1, **kwargs): ...
def axis(arg: Incomplete | None = None, *, emit: bool = True, **kwargs): ...
def axline(xy1, xy2: Incomplete | None = None, *, slope: Incomplete | None = None, **kwargs): ...
def axvline(x: int = 0, ymin: int = 0, ymax: int = 1, **kwargs): ...
def axvspan(xmin, xmax, ymin: int = 0, ymax: int = 1, **kwargs): ...
def bar(x, height, width: float = 0.8, bottom: Incomplete | None = None, *, align: str = 'center', data: Incomplete | None = None, **kwargs): ...
def barbs(*args, data: Incomplete | None = None, **kwargs): ...
def barh(y, width, height: float = 0.8, left: Incomplete | None = None, *, align: str = 'center', data: Incomplete | None = None, **kwargs): ...
def bar_label(container, labels: Incomplete | None = None, *, fmt: str = '%g', label_type: str = 'edge', padding: int = 0, **kwargs): ...
def boxplot(x, notch: Incomplete | None = None, sym: Incomplete | None = None, vert: Incomplete | None = None, whis: Incomplete | None = None, positions: Incomplete | None = None, widths: Incomplete | None = None, patch_artist: Incomplete | None = None, bootstrap: Incomplete | None = None, usermedians: Incomplete | None = None, conf_intervals: Incomplete | None = None, meanline: Incomplete | None = None, showmeans: Incomplete | None = None, showcaps: Incomplete | None = None, showbox: Incomplete | None = None, showfliers: Incomplete | None = None, boxprops: Incomplete | None = None, labels: Incomplete | None = None, flierprops: Incomplete | None = None, medianprops: Incomplete | None = None, meanprops: Incomplete | None = None, capprops: Incomplete | None = None, whiskerprops: Incomplete | None = None, manage_ticks: bool = True, autorange: bool = False, zorder: Incomplete | None = None, capwidths: Incomplete | None = None, *, data: Incomplete | None = None): ...
def broken_barh(xranges, yrange, *, data: Incomplete | None = None, **kwargs): ...
def clabel(CS, levels: Incomplete | None = None, **kwargs): ...
def cohere(x, y, NFFT: int = 256, Fs: int = 2, Fc: int = 0, detrend=..., window=..., noverlap: int = 0, pad_to: Incomplete | None = None, sides: str = 'default', scale_by_freq: Incomplete | None = None, *, data: Incomplete | None = None, **kwargs): ...
def contour(*args, data: Incomplete | None = None, **kwargs): ...
def contourf(*args, data: Incomplete | None = None, **kwargs): ...
def csd(x, y, NFFT: Incomplete | None = None, Fs: Incomplete | None = None, Fc: Incomplete | None = None, detrend: Incomplete | None = None, window: Incomplete | None = None, noverlap: Incomplete | None = None, pad_to: Incomplete | None = None, sides: Incomplete | None = None, scale_by_freq: Incomplete | None = None, return_line: Incomplete | None = None, *, data: Incomplete | None = None, **kwargs): ...
def errorbar(x, y, yerr: Incomplete | None = None, xerr: Incomplete | None = None, fmt: str = '', ecolor: Incomplete | None = None, elinewidth: Incomplete | None = None, capsize: Incomplete | None = None, barsabove: bool = False, lolims: bool = False, uplims: bool = False, xlolims: bool = False, xuplims: bool = False, errorevery: int = 1, capthick: Incomplete | None = None, *, data: Incomplete | None = None, **kwargs): ...
def eventplot(positions, orientation: str = 'horizontal', lineoffsets: int = 1, linelengths: int = 1, linewidths: Incomplete | None = None, colors: Incomplete | None = None, alpha: Incomplete | None = None, linestyles: str = 'solid', *, data: Incomplete | None = None, **kwargs): ...
def fill(*args, data: Incomplete | None = None, **kwargs): ...
def fill_between(x, y1, y2: int = 0, where: Incomplete | None = None, interpolate: bool = False, step: Incomplete | None = None, *, data: Incomplete | None = None, **kwargs): ...
def fill_betweenx(y, x1, x2: int = 0, where: Incomplete | None = None, step: Incomplete | None = None, interpolate: bool = False, *, data: Incomplete | None = None, **kwargs): ...
def grid(visible: Incomplete | None = None, which: str = 'major', axis: str = 'both', **kwargs): ...
def hexbin(x, y, C: Incomplete | None = None, gridsize: int = 100, bins: Incomplete | None = None, xscale: str = 'linear', yscale: str = 'linear', extent: Incomplete | None = None, cmap: Incomplete | None = None, norm: Incomplete | None = None, vmin: Incomplete | None = None, vmax: Incomplete | None = None, alpha: Incomplete | None = None, linewidths: Incomplete | None = None, edgecolors: str = 'face', reduce_C_function=..., mincnt: Incomplete | None = None, marginals: bool = False, *, data: Incomplete | None = None, **kwargs): ...
def hist(x, bins: Incomplete | None = None, range: Incomplete | None = None, density: bool = False, weights: Incomplete | None = None, cumulative: bool = False, bottom: Incomplete | None = None, histtype: str = 'bar', align: str = 'mid', orientation: str = 'vertical', rwidth: Incomplete | None = None, log: bool = False, color: Incomplete | None = None, label: Incomplete | None = None, stacked: bool = False, *, data: Incomplete | None = None, **kwargs): ...
def stairs(values, edges: Incomplete | None = None, *, orientation: str = 'vertical', baseline: int = 0, fill: bool = False, data: Incomplete | None = None, **kwargs): ...
def hist2d(x, y, bins: int = 10, range: Incomplete | None = None, density: bool = False, weights: Incomplete | None = None, cmin: Incomplete | None = None, cmax: Incomplete | None = None, *, data: Incomplete | None = None, **kwargs): ...
def hlines(y, xmin, xmax, colors: Incomplete | None = None, linestyles: str = 'solid', label: str = '', *, data: Incomplete | None = None, **kwargs): ...
def imshow(X, cmap: Incomplete | None = None, norm: Incomplete | None = None, *, aspect: Incomplete | None = None, interpolation: Incomplete | None = None, alpha: Incomplete | None = None, vmin: Incomplete | None = None, vmax: Incomplete | None = None, origin: Incomplete | None = None, extent: Incomplete | None = None, interpolation_stage: Incomplete | None = None, filternorm: bool = True, filterrad: float = 4.0, resample: Incomplete | None = None, url: Incomplete | None = None, data: Incomplete | None = None, **kwargs): ...
def legend(*args, **kwargs): ...
def locator_params(axis: str = 'both', tight: Incomplete | None = None, **kwargs): ...
def loglog(*args, **kwargs): ...
def magnitude_spectrum(x, Fs: Incomplete | None = None, Fc: Incomplete | None = None, window: Incomplete | None = None, pad_to: Incomplete | None = None, sides: Incomplete | None = None, scale: Incomplete | None = None, *, data: Incomplete | None = None, **kwargs): ...
def margins(*margins, x: Incomplete | None = None, y: Incomplete | None = None, tight: bool = True): ...
def minorticks_off(): ...
def minorticks_on(): ...
def pcolor(*args, shading: Incomplete | None = None, alpha: Incomplete | None = None, norm: Incomplete | None = None, cmap: Incomplete | None = None, vmin: Incomplete | None = None, vmax: Incomplete | None = None, data: Incomplete | None = None, **kwargs): ...
def pcolormesh(*args, alpha: Incomplete | None = None, norm: Incomplete | None = None, cmap: Incomplete | None = None, vmin: Incomplete | None = None, vmax: Incomplete | None = None, shading: Incomplete | None = None, antialiased: bool = False, data: Incomplete | None = None, **kwargs): ...
def phase_spectrum(x, Fs: Incomplete | None = None, Fc: Incomplete | None = None, window: Incomplete | None = None, pad_to: Incomplete | None = None, sides: Incomplete | None = None, *, data: Incomplete | None = None, **kwargs): ...
def pie(x, explode: Incomplete | None = None, labels: Incomplete | None = None, colors: Incomplete | None = None, autopct: Incomplete | None = None, pctdistance: float = 0.6, shadow: bool = False, labeldistance: float = 1.1, startangle: int = 0, radius: int = 1, counterclock: bool = True, wedgeprops: Incomplete | None = None, textprops: Incomplete | None = None, center=(0, 0), frame: bool = False, rotatelabels: bool = False, *, normalize: bool = True, hatch: Incomplete | None = None, data: Incomplete | None = None): ...
def plot(*args, scalex: bool = True, scaley: bool = True, data: Incomplete | None = None, **kwargs): ...
def plot_date(x, y, fmt: str = 'o', tz: Incomplete | None = None, xdate: bool = True, ydate: bool = False, *, data: Incomplete | None = None, **kwargs): ...
def psd(x, NFFT: Incomplete | None = None, Fs: Incomplete | None = None, Fc: Incomplete | None = None, detrend: Incomplete | None = None, window: Incomplete | None = None, noverlap: Incomplete | None = None, pad_to: Incomplete | None = None, sides: Incomplete | None = None, scale_by_freq: Incomplete | None = None, return_line: Incomplete | None = None, *, data: Incomplete | None = None, **kwargs): ...
def quiver(*args, data: Incomplete | None = None, **kwargs): ...
def quiverkey(Q, X, Y, U, label, **kwargs): ...
def scatter(x, y, s: Incomplete | None = None, c: Incomplete | None = None, marker: Incomplete | None = None, cmap: Incomplete | None = None, norm: Incomplete | None = None, vmin: Incomplete | None = None, vmax: Incomplete | None = None, alpha: Incomplete | None = None, linewidths: Incomplete | None = None, *, edgecolors: Incomplete | None = None, plotnonfinite: bool = False, data: Incomplete | None = None, **kwargs): ...
def semilogx(*args, **kwargs): ...
def semilogy(*args, **kwargs): ...
def specgram(x, NFFT: Incomplete | None = None, Fs: Incomplete | None = None, Fc: Incomplete | None = None, detrend: Incomplete | None = None, window: Incomplete | None = None, noverlap: Incomplete | None = None, cmap: Incomplete | None = None, xextent: Incomplete | None = None, pad_to: Incomplete | None = None, sides: Incomplete | None = None, scale_by_freq: Incomplete | None = None, mode: Incomplete | None = None, scale: Incomplete | None = None, vmin: Incomplete | None = None, vmax: Incomplete | None = None, *, data: Incomplete | None = None, **kwargs): ...
def spy(Z, precision: int = 0, marker: Incomplete | None = None, markersize: Incomplete | None = None, aspect: str = 'equal', origin: str = 'upper', **kwargs): ...
def stackplot(x, *args, labels=(), colors: Incomplete | None = None, baseline: str = 'zero', data: Incomplete | None = None, **kwargs): ...
def stem(*args, linefmt: Incomplete | None = None, markerfmt: Incomplete | None = None, basefmt: Incomplete | None = None, bottom: int = 0, label: Incomplete | None = None, use_line_collection=..., orientation: str = 'vertical', data: Incomplete | None = None): ...
def step(x, y, *args, where: str = 'pre', data: Incomplete | None = None, **kwargs): ...
def streamplot(x, y, u, v, density: int = 1, linewidth: Incomplete | None = None, color: Incomplete | None = None, cmap: Incomplete | None = None, norm: Incomplete | None = None, arrowsize: int = 1, arrowstyle: str = '-|>', minlength: float = 0.1, transform: Incomplete | None = None, zorder: Incomplete | None = None, start_points: Incomplete | None = None, maxlength: float = 4.0, integration_direction: str = 'both', broken_streamlines: bool = True, *, data: Incomplete | None = None): ...
def table(cellText: Incomplete | None = None, cellColours: Incomplete | None = None, cellLoc: str = 'right', colWidths: Incomplete | None = None, rowLabels: Incomplete | None = None, rowColours: Incomplete | None = None, rowLoc: str = 'left', colLabels: Incomplete | None = None, colColours: Incomplete | None = None, colLoc: str = 'center', loc: str = 'bottom', bbox: Incomplete | None = None, edges: str = 'closed', **kwargs): ...
def text(x, y, s, fontdict: Incomplete | None = None, **kwargs): ...
def tick_params(axis: str = 'both', **kwargs): ...
def ticklabel_format(*, axis: str = 'both', style: str = '', scilimits: Incomplete | None = None, useOffset: Incomplete | None = None, useLocale: Incomplete | None = None, useMathText: Incomplete | None = None): ...
def tricontour(*args, **kwargs): ...
def tricontourf(*args, **kwargs): ...
def tripcolor(*args, alpha: float = 1.0, norm: Incomplete | None = None, cmap: Incomplete | None = None, vmin: Incomplete | None = None, vmax: Incomplete | None = None, shading: str = 'flat', facecolors: Incomplete | None = None, **kwargs): ...
def triplot(*args, **kwargs): ...
def violinplot(dataset, positions: Incomplete | None = None, vert: bool = True, widths: float = 0.5, showmeans: bool = False, showextrema: bool = True, showmedians: bool = False, quantiles: Incomplete | None = None, points: int = 100, bw_method: Incomplete | None = None, *, data: Incomplete | None = None): ...
def vlines(x, ymin, ymax, colors: Incomplete | None = None, linestyles: str = 'solid', label: str = '', *, data: Incomplete | None = None, **kwargs): ...
def xcorr(x, y, normed: bool = True, detrend=..., usevlines: bool = True, maxlags: int = 10, *, data: Incomplete | None = None, **kwargs): ...
def sci(im): ...
def title(label, fontdict: Incomplete | None = None, loc: Incomplete | None = None, pad: Incomplete | None = None, *, y: Incomplete | None = None, **kwargs): ...
def xlabel(xlabel, fontdict: Incomplete | None = None, labelpad: Incomplete | None = None, *, loc: Incomplete | None = None, **kwargs): ...
def ylabel(ylabel, fontdict: Incomplete | None = None, labelpad: Incomplete | None = None, *, loc: Incomplete | None = None, **kwargs): ...
def xscale(value, **kwargs): ...
def yscale(value, **kwargs): ...
def autumn() -> None:
    """
    Set the colormap to 'autumn'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def bone() -> None:
    """
    Set the colormap to 'bone'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def cool() -> None:
    """
    Set the colormap to 'cool'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def copper() -> None:
    """
    Set the colormap to 'copper'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def flag() -> None:
    """
    Set the colormap to 'flag'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def gray() -> None:
    """
    Set the colormap to 'gray'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def hot() -> None:
    """
    Set the colormap to 'hot'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def hsv() -> None:
    """
    Set the colormap to 'hsv'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def jet() -> None:
    """
    Set the colormap to 'jet'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def pink() -> None:
    """
    Set the colormap to 'pink'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def prism() -> None:
    """
    Set the colormap to 'prism'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def spring() -> None:
    """
    Set the colormap to 'spring'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def summer() -> None:
    """
    Set the colormap to 'summer'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def winter() -> None:
    """
    Set the colormap to 'winter'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def magma() -> None:
    """
    Set the colormap to 'magma'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def inferno() -> None:
    """
    Set the colormap to 'inferno'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def plasma() -> None:
    """
    Set the colormap to 'plasma'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def viridis() -> None:
    """
    Set the colormap to 'viridis'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
def nipy_spectral() -> None:
    """
    Set the colormap to 'nipy_spectral'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.
    """
