from ._decorators import share_init_params_with_map as share_init_params_with_map
from .external.version import Version as Version
from .palettes import QUAL_PALETTES as QUAL_PALETTES, color_palette as color_palette
from .utils import get_color_cycle as get_color_cycle, remove_na as remove_na
from _typeshed import Incomplete
from collections import UserString
from collections.abc import Generator

class SemanticMapping:
    """Base class for mapping data values to plot attributes."""
    map_type: Incomplete
    levels: Incomplete
    lookup_table: Incomplete
    plotter: Incomplete
    def __init__(self, plotter) -> None: ...
    def map(cls, plotter, *args, **kwargs): ...
    def __call__(self, key, *args, **kwargs):
        """Get the attribute(s) values for the data key."""

class HueMapping(SemanticMapping):
    """Mapping that sets artist colors according to data values."""
    palette: Incomplete
    norm: Incomplete
    cmap: Incomplete
    map_type: Incomplete
    lookup_table: Incomplete
    levels: Incomplete
    def __init__(self, plotter, palette: Incomplete | None = None, order: Incomplete | None = None, norm: Incomplete | None = None) -> None:
        """Map the levels of the `hue` variable to distinct colors.

        Parameters
        ----------
        # TODO add generic parameters

        """
    def infer_map_type(self, palette, norm, input_format, var_type):
        """Determine how to implement the mapping."""
    def categorical_mapping(self, data, palette, order):
        """Determine colors when the hue mapping is categorical."""
    def numeric_mapping(self, data, palette, norm):
        """Determine colors when the hue variable is quantitative."""

class SizeMapping(SemanticMapping):
    """Mapping that sets artist sizes according to data values."""
    norm: Incomplete
    map_type: Incomplete
    levels: Incomplete
    sizes: Incomplete
    size_range: Incomplete
    lookup_table: Incomplete
    def __init__(self, plotter, sizes: Incomplete | None = None, order: Incomplete | None = None, norm: Incomplete | None = None) -> None:
        """Map the levels of the `size` variable to distinct values.

        Parameters
        ----------
        # TODO add generic parameters

        """
    def infer_map_type(self, norm, sizes, var_type): ...
    def categorical_mapping(self, data, sizes, order): ...
    def numeric_mapping(self, data, sizes, norm): ...

class StyleMapping(SemanticMapping):
    """Mapping that sets artist style according to data values."""
    map_type: str
    levels: Incomplete
    lookup_table: Incomplete
    def __init__(self, plotter, markers: Incomplete | None = None, dashes: Incomplete | None = None, order: Incomplete | None = None) -> None:
        """Map the levels of the `style` variable to distinct values.

        Parameters
        ----------
        # TODO add generic parameters

        """

class VectorPlotter:
    """Base class for objects underlying *plot functions."""
    semantics: Incomplete
    wide_structure: Incomplete
    flat_structure: Incomplete
    def __init__(self, data: Incomplete | None = None, variables={}) -> None: ...
    @classmethod
    def get_semantics(cls, kwargs, semantics: Incomplete | None = None):
        """Subset a dictionary arguments with known semantic variables."""
    @property
    def has_xy_data(self):
        """Return True at least one of x or y is defined."""
    @property
    def var_levels(self):
        """Property interface to ordered list of variables levels.

        Each time it's accessed, it updates the var_levels dictionary with the
        list of levels in the current semantic mappers. But it also allows the
        dictionary to persist, so it can be used to set levels by a key. This is
        used to track the list of col/row levels using an attached FacetGrid
        object, but it's kind of messy and ideally fixed by improving the
        faceting logic so it interfaces better with the modern approach to
        tracking plot variables.

        """
    input_format: str
    plot_data: Incomplete
    variables: Incomplete
    var_types: Incomplete
    def assign_variables(self, data: Incomplete | None = None, variables={}):
        """Define plot variables, optionally using lookup from `data`."""
    def iter_data(self, grouping_vars: Incomplete | None = None, *, reverse: bool = False, from_comp_data: bool = False, by_facet: bool = True, allow_empty: bool = False, dropna: bool = True) -> Generator[Incomplete, None, None]:
        '''Generator for getting subsets of data defined by semantic variables.

        Also injects "col" and "row" into grouping semantics.

        Parameters
        ----------
        grouping_vars : string or list of strings
            Semantic variables that define the subsets of data.
        reverse : bool
            If True, reverse the order of iteration.
        from_comp_data : bool
            If True, use self.comp_data rather than self.plot_data
        by_facet : bool
            If True, add faceting variables to the set of grouping variables.
        allow_empty : bool
            If True, yield an empty dataframe when no observations exist for
            combinations of grouping variables.
        dropna : bool
            If True, remove rows with missing data.

        Yields
        ------
        sub_vars : dict
            Keys are semantic names, values are the level of that semantic.
        sub_data : :class:`pandas.DataFrame`
            Subset of ``plot_data`` for this combination of semantic values.

        '''
    @property
    def comp_data(self):
        """Dataframe with numeric x and y, after unit conversion and log scaling."""
    def scale_native(self, axis, *args, **kwargs) -> None: ...
    def scale_numeric(self, axis, *args, **kwargs) -> None: ...
    def scale_datetime(self, axis, *args, **kwargs) -> None: ...
    def scale_categorical(self, axis, order: Incomplete | None = None, formatter: Incomplete | None = None):
        '''
        Enforce categorical (fixed-scale) rules for the data on given axis.

        Parameters
        ----------
        axis : "x" or "y"
            Axis of the plot to operate on.
        order : list
            Order that unique values should appear in.
        formatter : callable
            Function mapping values to a string representation.

        Returns
        -------
        self

        '''

class VariableType(UserString):
    """
    Prevent comparisons elsewhere in the library from using the wrong name.

    Errors are simple assertions because users should not be able to trigger
    them. If that changes, they should be more verbose.

    """
    allowed: Incomplete
    def __init__(self, data) -> None: ...
    def __eq__(self, other): ...

def variable_type(vector, boolean_type: str = 'numeric'):
    """
    Determine whether a vector contains numeric, categorical, or datetime data.

    This function differs from the pandas typing API in two ways:

    - Python sequences or object-typed PyData objects are considered numeric if
      all of their entries are numeric.
    - String or mixed-type data are considered categorical even if not
      explicitly represented as a :class:`pandas.api.types.CategoricalDtype`.

    Parameters
    ----------
    vector : :func:`pandas.Series`, :func:`numpy.ndarray`, or Python sequence
        Input data to test.
    boolean_type : 'numeric' or 'categorical'
        Type to use for vectors containing only 0s and 1s (and NAs).

    Returns
    -------
    var_type : 'numeric', 'categorical', or 'datetime'
        Name identifying the type of data in the vector.
    """
def infer_orient(x: Incomplete | None = None, y: Incomplete | None = None, orient: Incomplete | None = None, require_numeric: bool = True):
    '''Determine how the plot should be oriented based on the data.

    For historical reasons, the convention is to call a plot "horizontally"
    or "vertically" oriented based on the axis representing its dependent
    variable. Practically, this is used when determining the axis for
    numerical aggregation.

    Parameters
    ----------
    x, y : Vector data or None
        Positional data vectors for the plot.
    orient : string or None
        Specified orientation, which must start with "v" or "h" if not None.
    require_numeric : bool
        If set, raise when the implied dependent variable is not numeric.

    Returns
    -------
    orient : "v" or "h"

    Raises
    ------
    ValueError: When `orient` is not None and does not start with "h" or "v"
    TypeError: When dependent variable is not numeric, with `require_numeric`

    '''
def unique_dashes(n):
    '''Build an arbitrarily long list of unique dash styles for lines.

    Parameters
    ----------
    n : int
        Number of unique dash specs to generate.

    Returns
    -------
    dashes : list of strings or tuples
        Valid arguments for the ``dashes`` parameter on
        :class:`matplotlib.lines.Line2D`. The first spec is a solid
        line (``""``), the remainder are sequences of long and short
        dashes.

    '''
def unique_markers(n):
    """Build an arbitrarily long list of unique marker styles for points.

    Parameters
    ----------
    n : int
        Number of unique marker specs to generate.

    Returns
    -------
    markers : list of string or tuples
        Values for defining :class:`matplotlib.markers.MarkerStyle` objects.
        All markers will be filled.

    """
def categorical_order(vector, order: Incomplete | None = None):
    '''Return a list of unique data values.

    Determine an ordered list of levels in ``values``.

    Parameters
    ----------
    vector : list, array, Categorical, or Series
        Vector of "categorical" values
    order : list-like, optional
        Desired order of category levels to override the order determined
        from the ``values`` object.

    Returns
    -------
    order : list
        Ordered list of category levels not including null values.

    '''
