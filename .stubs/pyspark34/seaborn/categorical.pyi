from _typeshed import Incomplete
from seaborn.relational import _RelationalPlotter

__all__ = ['catplot', 'stripplot', 'swarmplot', 'boxplot', 'violinplot', 'boxenplot', 'pointplot', 'barplot', 'countplot']

class _CategoricalPlotterNew(_RelationalPlotter):
    semantics: Incomplete
    wide_structure: Incomplete
    flat_structure: Incomplete
    plot_data: Incomplete
    orient: Incomplete
    legend: Incomplete
    def __init__(self, data: Incomplete | None = None, variables={}, order: Incomplete | None = None, orient: Incomplete | None = None, require_numeric: bool = False, legend: str = 'auto') -> None: ...
    @property
    def cat_axis(self): ...
    def plot_strips(self, jitter, dodge, color, edgecolor, plot_kws) -> None: ...
    def plot_swarms(self, dodge, color, edgecolor, warn_thresh, plot_kws) -> None: ...

class _CategoricalFacetPlotter(_CategoricalPlotterNew):
    semantics: Incomplete

class _CategoricalPlotter:
    width: float
    default_palette: str
    require_numeric: bool
    orient: Incomplete
    plot_data: Incomplete
    group_label: Incomplete
    value_label: Incomplete
    group_names: Incomplete
    plot_hues: Incomplete
    hue_title: Incomplete
    hue_names: Incomplete
    plot_units: Incomplete
    def establish_variables(self, x: Incomplete | None = None, y: Incomplete | None = None, hue: Incomplete | None = None, data: Incomplete | None = None, orient: Incomplete | None = None, order: Incomplete | None = None, hue_order: Incomplete | None = None, units: Incomplete | None = None) -> None:
        """Convert input specification into a common representation."""
    colors: Incomplete
    gray: Incomplete
    def establish_colors(self, color, palette, saturation) -> None:
        """Get a list of colors for the main component of the plots."""
    @property
    def hue_offsets(self):
        """A list of center positions for plots when hue nesting is used."""
    @property
    def nested_width(self):
        """A float with the width of plot elements when hue nesting is used."""
    def annotate_axes(self, ax) -> None:
        """Add descriptive labels to an Axes object."""
    def add_legend_data(self, ax, color, label) -> None:
        """Add a dummy patch object so we can get legend data."""

class _BoxPlotter(_CategoricalPlotter):
    dodge: Incomplete
    width: Incomplete
    fliersize: Incomplete
    linewidth: Incomplete
    def __init__(self, x, y, hue, data, order, hue_order, orient, color, palette, saturation, width, dodge, fliersize, linewidth) -> None: ...
    def draw_boxplot(self, ax, kws) -> None:
        """Use matplotlib to draw a boxplot on an Axes."""
    def restyle_boxplot(self, artist_dict, color, props) -> None:
        """Take a drawn matplotlib boxplot and make it look nice."""
    def plot(self, ax, boxplot_kws) -> None:
        """Make the plot."""

class _ViolinPlotter(_CategoricalPlotter):
    gridsize: Incomplete
    width: Incomplete
    dodge: Incomplete
    inner: Incomplete
    split: Incomplete
    linewidth: Incomplete
    def __init__(self, x, y, hue, data, order, hue_order, bw, cut, scale, scale_hue, gridsize, width, inner, split, dodge, orient, linewidth, color, palette, saturation) -> None: ...
    support: Incomplete
    density: Incomplete
    def estimate_densities(self, bw, cut, scale, scale_hue, gridsize) -> None:
        """Find the support and density for all of the data."""
    def fit_kde(self, x, bw):
        """Estimate a KDE for a vector of data with flexible bandwidth."""
    def kde_support(self, x, bw, cut, gridsize):
        """Define a grid of support for the violin."""
    def scale_area(self, density, max_density, scale_hue) -> None:
        '''Scale the relative area under the KDE curve.

        This essentially preserves the "standard" KDE scaling, but the
        resulting maximum density will be 1 so that the curve can be
        properly multiplied by the violin width.

        '''
    def scale_width(self, density) -> None:
        """Scale each density curve to the same height."""
    def scale_count(self, density, counts, scale_hue) -> None:
        """Scale each density curve by the number of observations."""
    @property
    def dwidth(self): ...
    def draw_violins(self, ax) -> None:
        """Draw the violins onto `ax`."""
    def draw_single_observation(self, ax, at_group, at_quant, density) -> None:
        """Draw a line to mark a single observation."""
    def draw_box_lines(self, ax, data, center) -> None:
        """Draw boxplot information at center of the density."""
    def draw_quartiles(self, ax, data, support, density, center, split: bool = False) -> None:
        """Draw the quartiles as lines at width of density."""
    def draw_points(self, ax, data, center) -> None:
        """Draw individual observations as points at middle of the violin."""
    def draw_stick_lines(self, ax, data, support, density, center, split: bool = False) -> None:
        """Draw individual observations as sticks at width of density."""
    def draw_to_density(self, ax, center, val, support, density, split, **kws) -> None:
        """Draw a line orthogonal to the value axis at width of density."""
    def plot(self, ax) -> None:
        """Make the violin plot."""

class _CategoricalStatPlotter(_CategoricalPlotter):
    require_numeric: bool
    @property
    def nested_width(self):
        """A float with the width of plot elements when hue nesting is used."""
    statistic: Incomplete
    confint: Incomplete
    def estimate_statistic(self, estimator, errorbar, n_boot, seed) -> None: ...
    def draw_confints(self, ax, at_group, confint, colors, errwidth: Incomplete | None = None, capsize: Incomplete | None = None, **kws) -> None: ...

class _BarPlotter(_CategoricalStatPlotter):
    dodge: Incomplete
    width: Incomplete
    errcolor: Incomplete
    errwidth: Incomplete
    capsize: Incomplete
    def __init__(self, x, y, hue, data, order, hue_order, estimator, errorbar, n_boot, units, seed, orient, color, palette, saturation, width, errcolor, errwidth, capsize, dodge) -> None:
        """Initialize the plotter."""
    def draw_bars(self, ax, kws) -> None:
        """Draw the bars onto `ax`."""
    def plot(self, ax, bar_kws) -> None:
        """Make the plot."""

class _PointPlotter(_CategoricalStatPlotter):
    default_palette: str
    colors: Incomplete
    markers: Incomplete
    linestyles: Incomplete
    dodge: Incomplete
    join: Incomplete
    scale: Incomplete
    errwidth: Incomplete
    capsize: Incomplete
    label: Incomplete
    def __init__(self, x, y, hue, data, order, hue_order, estimator, errorbar, n_boot, units, seed, markers, linestyles, dodge, join, scale, orient, color, palette, errwidth, capsize, label) -> None:
        """Initialize the plotter."""
    @property
    def hue_offsets(self):
        """Offsets relative to the center position for each hue level."""
    def draw_points(self, ax) -> None:
        """Draw the main data components of the plot."""
    def plot(self, ax) -> None:
        """Make the plot."""

class _CountPlotter(_BarPlotter):
    require_numeric: bool

class _LVPlotter(_CategoricalPlotter):
    width: Incomplete
    dodge: Incomplete
    saturation: Incomplete
    k_depth: Incomplete
    linewidth: Incomplete
    scale: Incomplete
    outlier_prop: Incomplete
    trust_alpha: Incomplete
    showfliers: Incomplete
    def __init__(self, x, y, hue, data, order, hue_order, orient, color, palette, saturation, width, dodge, k_depth, linewidth, scale, outlier_prop, trust_alpha, showfliers: bool = True) -> None: ...
    def draw_letter_value_plot(self, ax, box_kws: Incomplete | None = None, flier_kws: Incomplete | None = None, line_kws: Incomplete | None = None) -> None:
        """Use matplotlib to draw a letter value plot on an Axes."""
    def plot(self, ax, box_kws, flier_kws, line_kws) -> None:
        """Make the plot."""

def boxplot(data: Incomplete | None = None, *, x: Incomplete | None = None, y: Incomplete | None = None, hue: Incomplete | None = None, order: Incomplete | None = None, hue_order: Incomplete | None = None, orient: Incomplete | None = None, color: Incomplete | None = None, palette: Incomplete | None = None, saturation: float = 0.75, width: float = 0.8, dodge: bool = True, fliersize: int = 5, linewidth: Incomplete | None = None, whis: float = 1.5, ax: Incomplete | None = None, **kwargs): ...
def violinplot(data: Incomplete | None = None, *, x: Incomplete | None = None, y: Incomplete | None = None, hue: Incomplete | None = None, order: Incomplete | None = None, hue_order: Incomplete | None = None, bw: str = 'scott', cut: int = 2, scale: str = 'area', scale_hue: bool = True, gridsize: int = 100, width: float = 0.8, inner: str = 'box', split: bool = False, dodge: bool = True, orient: Incomplete | None = None, linewidth: Incomplete | None = None, color: Incomplete | None = None, palette: Incomplete | None = None, saturation: float = 0.75, ax: Incomplete | None = None, **kwargs): ...
def boxenplot(data: Incomplete | None = None, *, x: Incomplete | None = None, y: Incomplete | None = None, hue: Incomplete | None = None, order: Incomplete | None = None, hue_order: Incomplete | None = None, orient: Incomplete | None = None, color: Incomplete | None = None, palette: Incomplete | None = None, saturation: float = 0.75, width: float = 0.8, dodge: bool = True, k_depth: str = 'tukey', linewidth: Incomplete | None = None, scale: str = 'exponential', outlier_prop: float = 0.007, trust_alpha: float = 0.05, showfliers: bool = True, ax: Incomplete | None = None, box_kws: Incomplete | None = None, flier_kws: Incomplete | None = None, line_kws: Incomplete | None = None): ...
def stripplot(data: Incomplete | None = None, *, x: Incomplete | None = None, y: Incomplete | None = None, hue: Incomplete | None = None, order: Incomplete | None = None, hue_order: Incomplete | None = None, jitter: bool = True, dodge: bool = False, orient: Incomplete | None = None, color: Incomplete | None = None, palette: Incomplete | None = None, size: int = 5, edgecolor: str = 'gray', linewidth: int = 0, hue_norm: Incomplete | None = None, native_scale: bool = False, formatter: Incomplete | None = None, legend: str = 'auto', ax: Incomplete | None = None, **kwargs): ...
def swarmplot(data: Incomplete | None = None, *, x: Incomplete | None = None, y: Incomplete | None = None, hue: Incomplete | None = None, order: Incomplete | None = None, hue_order: Incomplete | None = None, dodge: bool = False, orient: Incomplete | None = None, color: Incomplete | None = None, palette: Incomplete | None = None, size: int = 5, edgecolor: str = 'gray', linewidth: int = 0, hue_norm: Incomplete | None = None, native_scale: bool = False, formatter: Incomplete | None = None, legend: str = 'auto', warn_thresh: float = 0.05, ax: Incomplete | None = None, **kwargs): ...
def barplot(data: Incomplete | None = None, *, x: Incomplete | None = None, y: Incomplete | None = None, hue: Incomplete | None = None, order: Incomplete | None = None, hue_order: Incomplete | None = None, estimator: str = 'mean', errorbar=('ci', 95), n_boot: int = 1000, units: Incomplete | None = None, seed: Incomplete | None = None, orient: Incomplete | None = None, color: Incomplete | None = None, palette: Incomplete | None = None, saturation: float = 0.75, width: float = 0.8, errcolor: str = '.26', errwidth: Incomplete | None = None, capsize: Incomplete | None = None, dodge: bool = True, ci: str = 'deprecated', ax: Incomplete | None = None, **kwargs): ...
def pointplot(data: Incomplete | None = None, *, x: Incomplete | None = None, y: Incomplete | None = None, hue: Incomplete | None = None, order: Incomplete | None = None, hue_order: Incomplete | None = None, estimator: str = 'mean', errorbar=('ci', 95), n_boot: int = 1000, units: Incomplete | None = None, seed: Incomplete | None = None, markers: str = 'o', linestyles: str = '-', dodge: bool = False, join: bool = True, scale: int = 1, orient: Incomplete | None = None, color: Incomplete | None = None, palette: Incomplete | None = None, errwidth: Incomplete | None = None, ci: str = 'deprecated', capsize: Incomplete | None = None, label: Incomplete | None = None, ax: Incomplete | None = None): ...
def countplot(data: Incomplete | None = None, *, x: Incomplete | None = None, y: Incomplete | None = None, hue: Incomplete | None = None, order: Incomplete | None = None, hue_order: Incomplete | None = None, orient: Incomplete | None = None, color: Incomplete | None = None, palette: Incomplete | None = None, saturation: float = 0.75, width: float = 0.8, dodge: bool = True, ax: Incomplete | None = None, **kwargs): ...
def catplot(data: Incomplete | None = None, *, x: Incomplete | None = None, y: Incomplete | None = None, hue: Incomplete | None = None, row: Incomplete | None = None, col: Incomplete | None = None, col_wrap: Incomplete | None = None, estimator: str = 'mean', errorbar=('ci', 95), n_boot: int = 1000, units: Incomplete | None = None, seed: Incomplete | None = None, order: Incomplete | None = None, hue_order: Incomplete | None = None, row_order: Incomplete | None = None, col_order: Incomplete | None = None, height: int = 5, aspect: int = 1, kind: str = 'strip', native_scale: bool = False, formatter: Incomplete | None = None, orient: Incomplete | None = None, color: Incomplete | None = None, palette: Incomplete | None = None, hue_norm: Incomplete | None = None, legend: str = 'auto', legend_out: bool = True, sharex: bool = True, sharey: bool = True, margin_titles: bool = False, facet_kws: Incomplete | None = None, ci: str = 'deprecated', **kwargs): ...

class Beeswarm:
    """Modifies a scatterplot artist to show a beeswarm plot."""
    orient: Incomplete
    width: Incomplete
    warn_thresh: Incomplete
    def __init__(self, orient: str = 'v', width: float = 0.8, warn_thresh: float = 0.05) -> None: ...
    def __call__(self, points, center) -> None:
        """Swarm `points`, a PathCollection, around the `center` position."""
    def beeswarm(self, orig_xyr):
        """Adjust x position of points to avoid overlaps."""
    def could_overlap(self, xyr_i, swarm):
        """Return a list of all swarm points that could overlap with target."""
    def position_candidates(self, xyr_i, neighbors):
        """Return a list of coordinates that might be valid by adjusting x."""
    def first_non_overlapping_candidate(self, candidates, neighbors):
        """Find the first candidate that does not overlap with the swarm."""
    def add_gutters(self, points, center, log_scale: bool = False):
        """Stop points from extending beyond their territory."""
