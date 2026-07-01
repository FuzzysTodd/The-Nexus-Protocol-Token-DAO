from _typeshed import Incomplete
from collections.abc import Generator, MutableMapping
from matplotlib._api import MatplotlibDeprecationWarning as MatplotlibDeprecationWarning
from matplotlib.cbook import sanitize_sequence as sanitize_sequence
from matplotlib.rcsetup import cycler as cycler, validate_backend as validate_backend
from typing import NamedTuple

__bibtex__: str

class _VersionInfo(NamedTuple):
    major: Incomplete
    minor: Incomplete
    micro: Incomplete
    releaselevel: Incomplete
    serial: Incomplete

class __getattr__:
    __version__: Incomplete
    __version_info__: Incomplete

def set_loglevel(level) -> None:
    '''
    Configure Matplotlib\'s logging levels.

    Matplotlib uses the standard library `logging` framework under the root
    logger \'matplotlib\'.  This is a helper function to:

    - set Matplotlib\'s root logger level
    - set the root logger handler\'s level, creating the handler
      if it does not exist yet

    Typically, one should call ``set_loglevel("info")`` or
    ``set_loglevel("debug")`` to get additional debugging information.

    Users or applications that are installing their own logging handlers
    may want to directly manipulate ``logging.getLogger(\'matplotlib\')`` rather
    than use this function.

    Parameters
    ----------
    level : {"notset", "debug", "info", "warning", "error", "critical"}
        The log level of the handler.

    Notes
    -----
    The first time this function is called, an additional handler is attached
    to Matplotlib\'s root handler; this handler is reused every time and this
    function simply manipulates the logger and handler\'s level.

    '''

class _ExecInfo(NamedTuple):
    executable: Incomplete
    raw_version: Incomplete
    version: Incomplete

class ExecutableNotFoundError(FileNotFoundError):
    """
    Error raised when an executable that Matplotlib optionally
    depends on can't be found.
    """

def checkdep_usetex(s): ...
def get_configdir():
    """
    Return the string path of the configuration directory.

    The directory is chosen as follows:

    1. If the MPLCONFIGDIR environment variable is supplied, choose that.
    2. On Linux, follow the XDG specification and look first in
       ``$XDG_CONFIG_HOME``, if defined, or ``$HOME/.config``.  On other
       platforms, choose ``$HOME/.matplotlib``.
    3. If the chosen directory exists and is writable, use that as the
       configuration directory.
    4. Else, create a temporary directory, and use it as the configuration
       directory.
    """
def get_cachedir():
    """
    Return the string path of the cache directory.

    The procedure used to find the directory is the same as for
    _get_config_dir, except using ``$XDG_CACHE_HOME``/``$HOME/.cache`` instead.
    """
def get_data_path():
    """Return the path to Matplotlib data."""
def matplotlib_fname():
    """
    Get the location of the config file.

    The file location is determined in the following order

    - ``$PWD/matplotlibrc``
    - ``$MATPLOTLIBRC`` if it is not a directory
    - ``$MATPLOTLIBRC/matplotlibrc``
    - ``$MPLCONFIGDIR/matplotlibrc``
    - On Linux,
        - ``$XDG_CONFIG_HOME/matplotlib/matplotlibrc`` (if ``$XDG_CONFIG_HOME``
          is defined)
        - or ``$HOME/.config/matplotlib/matplotlibrc`` (if ``$XDG_CONFIG_HOME``
          is not defined)
    - On other platforms,
      - ``$HOME/.matplotlib/matplotlibrc`` if ``$HOME`` is defined
    - Lastly, it looks in ``$MATPLOTLIBDATA/matplotlibrc``, which should always
      exist.
    """

class RcParams(MutableMapping, dict):
    """
    A dict-like key-value store for config parameters, including validation.

    Validating functions are defined and associated with rc parameters in
    :mod:`matplotlib.rcsetup`.

    The list of rcParams is:

    %s

    See Also
    --------
    :ref:`customizing-with-matplotlibrc-files`
    """
    validate: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __setitem__(self, key, val) -> None: ...
    def __getitem__(self, key): ...
    def __iter__(self):
        """Yield sorted list of keys."""
    def __len__(self) -> int: ...
    def find_all(self, pattern):
        """
        Return the subset of this RcParams dictionary whose keys match,
        using :func:`re.search`, the given ``pattern``.

        .. note::

            Changes to the returned dictionary are *not* propagated to
            the parent RcParams dictionary.

        """
    def copy(self):
        """Copy this RcParams instance."""

def rc_params(fail_on_error: bool = False):
    """Construct a `RcParams` instance from the default Matplotlib rc file."""
def rc_params_from_file(fname, fail_on_error: bool = False, use_default_template: bool = True):
    """
    Construct a `RcParams` from file *fname*.

    Parameters
    ----------
    fname : str or path-like
        A file with Matplotlib rc settings.
    fail_on_error : bool
        If True, raise an error when the parser fails to convert a parameter.
    use_default_template : bool
        If True, initialize with default parameters before updating with those
        in the given file. If False, the configuration class only contains the
        parameters specified in the file. (Useful for updating dicts.)
    """

rcParamsDefault: Incomplete
rcParams: Incomplete
rcParamsOrig: Incomplete
defaultParams: Incomplete

def rc(group, **kwargs) -> None:
    '''
    Set the current `.rcParams`.  *group* is the grouping for the rc, e.g.,
    for ``lines.linewidth`` the group is ``lines``, for
    ``axes.facecolor``, the group is ``axes``, and so on.  Group may
    also be a list or tuple of group names, e.g., (*xtick*, *ytick*).
    *kwargs* is a dictionary attribute name/value pairs, e.g.,::

      rc(\'lines\', linewidth=2, color=\'r\')

    sets the current `.rcParams` and is equivalent to::

      rcParams[\'lines.linewidth\'] = 2
      rcParams[\'lines.color\'] = \'r\'

    The following aliases are available to save typing for interactive users:

    =====   =================
    Alias   Property
    =====   =================
    \'lw\'    \'linewidth\'
    \'ls\'    \'linestyle\'
    \'c\'     \'color\'
    \'fc\'    \'facecolor\'
    \'ec\'    \'edgecolor\'
    \'mew\'   \'markeredgewidth\'
    \'aa\'    \'antialiased\'
    =====   =================

    Thus you could abbreviate the above call as::

          rc(\'lines\', lw=2, c=\'r\')

    Note you can use python\'s kwargs dictionary facility to store
    dictionaries of default parameters.  e.g., you can customize the
    font rc as follows::

      font = {\'family\' : \'monospace\',
              \'weight\' : \'bold\',
              \'size\'   : \'larger\'}
      rc(\'font\', **font)  # pass in the font dict as kwargs

    This enables you to easily switch between several configurations.  Use
    ``matplotlib.style.use(\'default\')`` or :func:`~matplotlib.rcdefaults` to
    restore the default `.rcParams` after changes.

    Notes
    -----
    Similar functionality is available by using the normal dict interface, i.e.
    ``rcParams.update({"lines.linewidth": 2, ...})`` (but ``rcParams.update``
    does not support abbreviations or grouping).
    '''
def rcdefaults() -> None:
    """
    Restore the `.rcParams` from Matplotlib's internal default style.

    Style-blacklisted `.rcParams` (defined in
    ``matplotlib.style.core.STYLE_BLACKLIST``) are not updated.

    See Also
    --------
    matplotlib.rc_file_defaults
        Restore the `.rcParams` from the rc file originally loaded by
        Matplotlib.
    matplotlib.style.use
        Use a specific style file.  Call ``style.use('default')`` to restore
        the default style.
    """
def rc_file_defaults() -> None:
    """
    Restore the `.rcParams` from the original rc file loaded by Matplotlib.

    Style-blacklisted `.rcParams` (defined in
    ``matplotlib.style.core.STYLE_BLACKLIST``) are not updated.
    """
def rc_file(fname, *, use_default_template: bool = True) -> None:
    """
    Update `.rcParams` from file.

    Style-blacklisted `.rcParams` (defined in
    ``matplotlib.style.core.STYLE_BLACKLIST``) are not updated.

    Parameters
    ----------
    fname : str or path-like
        A file with Matplotlib rc settings.

    use_default_template : bool
        If True, initialize with default parameters before updating with those
        in the given file. If False, the current configuration persists
        and only the parameters specified in the file are updated.
    """
def rc_context(rc: Incomplete | None = None, fname: Incomplete | None = None) -> Generator[None, None, None]:
    """
    Return a context manager for temporarily changing rcParams.

    The :rc:`backend` will not be reset by the context manager.

    rcParams changed both through the context manager invocation and
    in the body of the context will be reset on context exit.

    Parameters
    ----------
    rc : dict
        The rcParams to temporarily set.
    fname : str or path-like
        A file with Matplotlib rc settings. If both *fname* and *rc* are given,
        settings from *rc* take precedence.

    See Also
    --------
    :ref:`customizing-with-matplotlibrc-files`

    Examples
    --------
    Passing explicit values via a dict::

        with mpl.rc_context({'interactive': False}):
            fig, ax = plt.subplots()
            ax.plot(range(3), range(3))
            fig.savefig('example.png')
            plt.close(fig)

    Loading settings from a file::

         with mpl.rc_context(fname='print.rc'):
             plt.plot(x, y)  # uses 'print.rc'

    Setting in the context body::

        with mpl.rc_context():
            # will be reset
            mpl.rcParams['lines.linewidth'] = 5
            plt.plot(x, y)

    """
def use(backend, *, force: bool = True) -> None:
    """
    Select the backend used for rendering and GUI integration.

    If pyplot is already imported, `~matplotlib.pyplot.switch_backend` is used
    and if the new backend is different than the current backend, all Figures
    will be closed.

    Parameters
    ----------
    backend : str
        The backend to switch to.  This can either be one of the standard
        backend names, which are case-insensitive:

        - interactive backends:
          GTK3Agg, GTK3Cairo, GTK4Agg, GTK4Cairo, MacOSX, nbAgg, QtAgg,
          QtCairo, TkAgg, TkCairo, WebAgg, WX, WXAgg, WXCairo, Qt5Agg, Qt5Cairo

        - non-interactive backends:
          agg, cairo, pdf, pgf, ps, svg, template

        or a string of the form: ``module://my.module.name``.

        Switching to an interactive backend is not possible if an unrelated
        event loop has already been started (e.g., switching to GTK3Agg if a
        TkAgg window has already been opened).  Switching to a non-interactive
        backend is always possible.

    force : bool, default: True
        If True (the default), raise an `ImportError` if the backend cannot be
        set up (either because it fails to import, or because an incompatible
        GUI interactive framework is already running); if False, silently
        ignore the failure.

    See Also
    --------
    :ref:`backends`
    matplotlib.get_backend
    matplotlib.pyplot.switch_backend

    """
def get_backend():
    """
    Return the name of the current backend.

    See Also
    --------
    matplotlib.use
    """
def interactive(b) -> None:
    """
    Set whether to redraw after every plotting command (e.g. `.pyplot.xlabel`).
    """
def is_interactive():
    """
    Return whether to redraw after every plotting command.

    .. note::

        This function is only intended for use in backends. End users should
        use `.pyplot.isinteractive` instead.
    """
