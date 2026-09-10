from plotly import exceptions as exceptions
from plotly.colors import DEFAULT_PLOTLY_COLORS as DEFAULT_PLOTLY_COLORS, PLOTLY_SCALES as PLOTLY_SCALES, color_parser as color_parser, colorscale_to_colors as colorscale_to_colors, colorscale_to_scale as colorscale_to_scale, convert_to_RGB_255 as convert_to_RGB_255, find_intermediate_color as find_intermediate_color, hex_to_rgb as hex_to_rgb, label_rgb as label_rgb, n_colors as n_colors, unconvert_from_RGB_255 as unconvert_from_RGB_255, unlabel_rgb as unlabel_rgb, validate_colors as validate_colors, validate_colors_dict as validate_colors_dict, validate_colorscale as validate_colorscale, validate_scale_values as validate_scale_values

def is_sequence(obj): ...
def validate_index(index_vals) -> None:
    """
    Validates if a list contains all numbers or all strings

    :raises: (PlotlyError) If there are any two items in the list whose
        types differ
    """
def validate_dataframe(array) -> None:
    """
    Validates all strings or numbers in each dataframe column

    :raises: (PlotlyError) If there are any two items in any list whose
        types differ
    """
def validate_equal_length(*args) -> None:
    """
    Validates that data lists or ndarrays are the same length.

    :raises: (PlotlyError) If any data lists are not the same length.
    """
def validate_positive_scalars(**kwargs) -> None:
    """
    Validates that all values given in key/val pairs are positive.

    Accepts kwargs to improve Exception messages.

    :raises: (PlotlyError) If any value is < 0 or raises.
    """
def flatten(array):
    """
    Uses list comprehension to flatten array

    :param (array): An iterable to flatten
    :raises (PlotlyError): If iterable is not nested.
    :rtype (list): The flattened list.
    """
def endpts_to_intervals(endpts):
    """
    Returns a list of intervals for categorical colormaps

    Accepts a list or tuple of sequentially increasing numbers and returns
    a list representation of the mathematical intervals with these numbers
    as endpoints. For example, [1, 6] returns [[-inf, 1], [1, 6], [6, inf]]

    :raises: (PlotlyError) If input is not a list or tuple
    :raises: (PlotlyError) If the input contains a string
    :raises: (PlotlyError) If any number does not increase after the
        previous one in the sequence
    """
def annotation_dict_for_label(text, lane, num_of_lanes, subplot_spacing, row_col: str = 'col', flipped: bool = True, right_side: bool = True, text_color: str = '#0f0f0f'):
    """
    Returns annotation dict for label of n labels of a 1xn or nx1 subplot.

    :param (str) text: the text for a label.
    :param (int) lane: the label number for text. From 1 to n inclusive.
    :param (int) num_of_lanes: the number 'n' of rows or columns in subplot.
    :param (float) subplot_spacing: the value for the horizontal_spacing and
        vertical_spacing params in your plotly.tools.make_subplots() call.
    :param (str) row_col: choose whether labels are placed along rows or
        columns.
    :param (bool) flipped: flips text by 90 degrees. Text is printed
        horizontally if set to True and row_col='row', or if False and
        row_col='col'.
    :param (bool) right_side: only applicable if row_col is set to 'row'.
    :param (str) text_color: color of the text.
    """
def list_of_options(iterable, conj: str = 'and', period: bool = True):
    """
    Returns an English listing of objects seperated by commas ','

    For example, ['foo', 'bar', 'baz'] becomes 'foo, bar and baz'
    if the conjunction 'and' is selected.
    """
