from _typeshed import Incomplete

def check_bar_match(old_bar, new_bar):
    """Check if two bars belong in the same collection (bar chart).

    Positional arguments:
    old_bar -- a previously sorted bar dictionary.
    new_bar -- a new bar dictionary that needs to be sorted.

    """
def check_corners(inner_obj, outer_obj): ...
def convert_dash(mpl_dash):
    """Convert mpl line symbol to plotly line symbol and return symbol."""
def convert_path(path): ...
def convert_symbol(mpl_symbol):
    """Convert mpl marker symbol to plotly symbol and return symbol."""
def hex_to_rgb(value):
    """
    Change a hex color to an rgb tuple

    :param (str|unicode) value: The hex string we want to convert.
    :return: (int, int, int) The red, green, blue int-tuple.

    Example:

        '#FFFFFF' --> (255, 255, 255)

    """
def merge_color_and_opacity(color, opacity):
    """
    Merge hex color with an alpha (opacity) to get an rgba tuple.

    :param (str|unicode) color: A hex color string.
    :param (float|int) opacity: A value [0, 1] for the 'a' in 'rgba'.
    :return: (int, int, int, float) The rgba color and alpha tuple.

    """
def convert_va(mpl_va):
    """Convert mpl vertical alignment word to equivalent HTML word.

    Text alignment specifiers from mpl differ very slightly from those used
    in HTML. See the VA_MAP for more details.

    Positional arguments:
    mpl_va -- vertical mpl text alignment spec.

    """
def convert_x_domain(mpl_plot_bounds, mpl_max_x_bounds):
    """Map x dimension of current plot to plotly's domain space.

    The bbox used to locate an axes object in mpl differs from the
    method used to locate axes in plotly. The mpl version locates each
    axes in the figure so that axes in a single-plot figure might have
    the bounds, [0.125, 0.125, 0.775, 0.775] (x0, y0, width, height),
    in mpl's figure coordinates. However, the axes all share one space in
    plotly such that the domain will always be [0, 0, 1, 1]
    (x0, y0, x1, y1). To convert between the two, the mpl figure bounds
    need to be mapped to a [0, 1] domain for x and y. The margins set
    upon opening a new figure will appropriately match the mpl margins.

    Optionally, setting margins=0 and simply copying the domains from
    mpl to plotly would place axes appropriately. However,
    this would throw off axis and title labeling.

    Positional arguments:
    mpl_plot_bounds -- the (x0, y0, width, height) params for current ax **
    mpl_max_x_bounds -- overall (x0, x1) bounds for all axes **

    ** these are all specified in mpl figure coordinates

    """
def convert_y_domain(mpl_plot_bounds, mpl_max_y_bounds):
    """Map y dimension of current plot to plotly's domain space.

    The bbox used to locate an axes object in mpl differs from the
    method used to locate axes in plotly. The mpl version locates each
    axes in the figure so that axes in a single-plot figure might have
    the bounds, [0.125, 0.125, 0.775, 0.775] (x0, y0, width, height),
    in mpl's figure coordinates. However, the axes all share one space in
    plotly such that the domain will always be [0, 0, 1, 1]
    (x0, y0, x1, y1). To convert between the two, the mpl figure bounds
    need to be mapped to a [0, 1] domain for x and y. The margins set
    upon opening a new figure will appropriately match the mpl margins.

    Optionally, setting margins=0 and simply copying the domains from
    mpl to plotly would place axes appropriately. However,
    this would throw off axis and title labeling.

    Positional arguments:
    mpl_plot_bounds -- the (x0, y0, width, height) params for current ax **
    mpl_max_y_bounds -- overall (y0, y1) bounds for all axes **

    ** these are all specified in mpl figure coordinates

    """
def display_to_paper(x, y, layout):
    """Convert mpl display coordinates to plotly paper coordinates.

    Plotly references object positions with an (x, y) coordinate pair in either
    'data' or 'paper' coordinates which reference actual data in a plot or
    the entire plotly axes space where the bottom-left of the bottom-left
    plot has the location (x, y) = (0, 0) and the top-right of the top-right
    plot has the location (x, y) = (1, 1). Display coordinates in mpl reference
    objects with an (x, y) pair in pixel coordinates, where the bottom-left
    corner is at the location (x, y) = (0, 0) and the top-right corner is at
    the location (x, y) = (figwidth*dpi, figheight*dpi). Here, figwidth and
    figheight are in inches and dpi are the dots per inch resolution.

    """
def get_axes_bounds(fig):
    """Return the entire axes space for figure.

    An axes object in mpl is specified by its relation to the figure where
    (0,0) corresponds to the bottom-left part of the figure and (1,1)
    corresponds to the top-right. Margins exist in matplotlib because axes
    objects normally don't go to the edges of the figure.

    In plotly, the axes area (where all subplots go) is always specified with
    the domain [0,1] for both x and y. This function finds the smallest box,
    specified by two points, that all of the mpl axes objects fit into. This
    box is then used to map mpl axes domains to plotly axes domains.

    """
def get_axis_mirror(main_spine, mirror_spine): ...
def get_bar_gap(bar_starts, bar_ends, tol: float = 1e-10): ...
def convert_rgba_array(color_list): ...
def convert_path_array(path_array): ...
def convert_linewidth_array(width_array): ...
def convert_size_array(size_array): ...
def get_markerstyle_from_collection(props): ...
def get_rect_xmin(data):
    """Find minimum x value from four (x,y) vertices."""
def get_rect_xmax(data):
    """Find maximum x value from four (x,y) vertices."""
def get_rect_ymin(data):
    """Find minimum y value from four (x,y) vertices."""
def get_rect_ymax(data):
    """Find maximum y value from four (x,y) vertices."""
def get_spine_visible(ax, spine_key):
    """Return some spine parameters for the spine, `spine_key`."""
def is_bar(bar_containers, **props):
    """A test to decide whether a path is a bar from a vertical bar chart."""
def make_bar(**props):
    """Make an intermediate bar dictionary.

    This creates a bar dictionary which aids in the comparison of new bars to
    old bars from other bar chart (patch) collections. This is not the
    dictionary that needs to get passed to plotly as a data dictionary. That
    happens in PlotlyRenderer in that class's draw_bar method. In other
    words, this dictionary describes a SINGLE bar, whereas, plotly will
    require a set of bars to be passed in a data dictionary.

    """
def prep_ticks(ax, index, ax_type, props):
    """Prepare axis obj belonging to axes obj.

    positional arguments:
    ax - the mpl axes instance
    index - the index of the axis in `props`
    ax_type - 'x' or 'y' (for now)
    props - an mplexporter poperties dictionary

    """
def prep_xy_axis(ax, props, x_bounds, y_bounds): ...
def mpl_dates_to_datestrings(dates, mpl_formatter):
    '''Convert matplotlib dates to iso-formatted-like time strings.

    Plotly\'s accepted format: "YYYY-MM-DD HH:MM:SS" (e.g., 2001-01-01 00:00:00)

    Info on mpl dates: http://matplotlib.org/api/dates_api.html

    '''

DASH_MAP: Incomplete
PATH_MAP: Incomplete
SYMBOL_MAP: Incomplete
VA_MAP: Incomplete
