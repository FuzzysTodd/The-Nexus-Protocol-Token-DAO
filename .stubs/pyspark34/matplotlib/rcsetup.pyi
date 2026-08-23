import ast
from _typeshed import Incomplete
from matplotlib import cbook as cbook
from matplotlib._enums import CapStyle as CapStyle, JoinStyle as JoinStyle
from matplotlib._fontconfig_pattern import parse_fontconfig_pattern as parse_fontconfig_pattern
from matplotlib.cbook import ls_mapper as ls_mapper
from matplotlib.colors import Colormap as Colormap, is_color_like as is_color_like

interactive_bk: Incomplete
non_interactive_bk: Incomplete
all_backends: Incomplete

class ValidateInStrings:
    key: Incomplete
    ignorecase: Incomplete
    valid: Incomplete
    def __init__(self, key, valid, ignorecase: bool = False, *, _deprecated_since: Incomplete | None = None) -> None:
        """*valid* is a list of legal strings."""
    def __call__(self, s): ...

def validate_any(s): ...

validate_anylist: Incomplete

def validate_bool(b):
    """Convert b to ``bool`` or raise."""
def validate_axisbelow(s): ...
def validate_dpi(s):
    """Confirm s is string 'figure' or convert s to float or raise."""

validate_string: Incomplete
validate_string_or_None: Incomplete
validate_stringlist: Incomplete
validate_int: Incomplete
validate_int_or_None: Incomplete
validate_float: Incomplete
validate_float_or_None: Incomplete
validate_floatlist: Incomplete

def validate_fonttype(s):
    """
    Confirm that this is a Postscript or PDF font type that we know how to
    convert to.
    """
def validate_backend(s): ...
def validate_color_or_inherit(s):
    """Return a valid color arg."""
def validate_color_or_auto(s): ...
def validate_color_for_prop_cycle(s): ...
def validate_color(s):
    """Return a valid color arg."""

validate_colorlist: Incomplete

def validate_aspect(s): ...
def validate_fontsize_None(s): ...
def validate_fontsize(s): ...

validate_fontsizelist: Incomplete

def validate_fontweight(s): ...
def validate_fontstretch(s): ...
def validate_font_properties(s): ...
def validate_whiskers(s): ...
def validate_ps_distiller(s): ...

validate_fillstyle: Incomplete
validate_fillstylelist: Incomplete

def validate_markevery(s):
    """
    Validate the markevery property of a Line2D object.

    Parameters
    ----------
    s : None, int, (int, int), slice, float, (float, float), or list[int]

    Returns
    -------
    None, int, (int, int), slice, float, (float, float), or list[int]
    """

validate_markeverylist: Incomplete

def validate_bbox(s): ...
def validate_sketch(s): ...
def validate_hatch(s):
    """
    Validate a hatch pattern.
    A hatch pattern string can have any sequence of the following
    characters: ``\\ / | - + * . x o O``.
    """

validate_hatchlist: Incomplete
validate_dashlist: Incomplete

def cycler(*args, **kwargs):
    """
    Create a `~cycler.Cycler` object much like :func:`cycler.cycler`,
    but includes input validation.

    Call signatures::

      cycler(cycler)
      cycler(label=values[, label2=values2[, ...]])
      cycler(label, values)

    Form 1 copies a given `~cycler.Cycler` object.

    Form 2 creates a `~cycler.Cycler` which cycles over one or more
    properties simultaneously. If multiple properties are given, their
    value lists must have the same length.

    Form 3 creates a `~cycler.Cycler` for a single property. This form
    exists for compatibility with the original cycler. Its use is
    discouraged in favor of the kwarg form, i.e. ``cycler(label=values)``.

    Parameters
    ----------
    cycler : Cycler
        Copy constructor for Cycler.

    label : str
        The property key. Must be a valid `.Artist` property.
        For example, 'color' or 'linestyle'. Aliases are allowed,
        such as 'c' for 'color' and 'lw' for 'linewidth'.

    values : iterable
        Finite-length iterable of the property values. These values
        are validated and will raise a ValueError if invalid.

    Returns
    -------
    Cycler
        A new :class:`~cycler.Cycler` for the given properties.

    Examples
    --------
    Creating a cycler for a single property:

    >>> c = cycler(color=['red', 'green', 'blue'])

    Creating a cycler for simultaneously cycling over multiple properties
    (e.g. red circle, green plus, blue cross):

    >>> c = cycler(color=['red', 'green', 'blue'],
    ...            marker=['o', '+', 'x'])

    """

class _DunderChecker(ast.NodeVisitor):
    def visit_Attribute(self, node) -> None: ...

def validate_cycler(s):
    """Return a Cycler object from a string repr or the object itself."""
def validate_hist_bins(s): ...

class _ignorecase(list):
    """A marker class indicating that a list-of-str is case-insensitive."""
