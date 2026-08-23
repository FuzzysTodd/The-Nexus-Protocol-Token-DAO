from .docutils import doc_subst as doc_subst
from .widget import Widget as Widget
from .widget_box import GridBox as GridBox
from _typeshed import Incomplete
from traitlets import HasTraits

class LayoutProperties(HasTraits):
    """Mixin class for layout templates

    This class handles mainly style attributes (height, grid_gap etc.)

    Parameters
    ----------

    {style_params}


    Note
    ----

    This class is only meant to be used in inheritance as mixin with other
    classes. It will not work, unless `self.layout` attribute is defined.

    """
    grid_gap: Incomplete
    justify_content: Incomplete
    align_items: Incomplete
    width: Incomplete
    height: Incomplete
    def __init__(self, **kwargs) -> None: ...

class AppLayout(GridBox, LayoutProperties):
    """ Define an application like layout of widgets.

    Parameters
    ----------

    header: instance of Widget
    left_sidebar: instance of Widget
    center: instance of Widget
    right_sidebar: instance of Widget
    footer: instance of Widget
        widgets to fill the positions in the layout

    merge: bool
        flag to say whether the empty positions should be automatically merged

    pane_widths: list of numbers/strings
        the fraction of the total layout width each of the central panes should occupy
        (left_sidebar,
        center, right_sidebar)

    pane_heights: list of numbers/strings
        the fraction of the width the vertical space that the panes should occupy
         (left_sidebar, center, right_sidebar)

    {style_params}

    Examples
    --------

    """
    header: Incomplete
    footer: Incomplete
    left_sidebar: Incomplete
    right_sidebar: Incomplete
    center: Incomplete
    pane_widths: Incomplete
    pane_heights: Incomplete
    merge: Incomplete
    def __init__(self, **kwargs) -> None: ...

class GridspecLayout(GridBox, LayoutProperties):
    """ Define a N by M grid layout

    Parameters
    ----------

    n_rows : int
        number of rows in the grid

    n_columns : int
        number of columns in the grid

    {style_params}

    Examples
    --------

    >>> from ipywidgets import GridspecLayout, Button, Layout
    >>> layout = GridspecLayout(n_rows=4, n_columns=2, height='200px')
    >>> layout[:3, 0] = Button(layout=Layout(height='auto', width='auto'))
    >>> layout[1:, 1] = Button(layout=Layout(height='auto', width='auto'))
    >>> layout[-1, 0] = Button(layout=Layout(height='auto', width='auto'))
    >>> layout[0, 1] = Button(layout=Layout(height='auto', width='auto'))
    >>> layout
    """
    n_rows: Incomplete
    n_columns: Incomplete
    def __init__(self, n_rows: Incomplete | None = None, n_columns: Incomplete | None = None, **kwargs) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def __getitem__(self, key): ...

class TwoByTwoLayout(GridBox, LayoutProperties):
    ''' Define a layout with 2x2 regular grid.

    Parameters
    ----------

    top_left: instance of Widget
    top_right: instance of Widget
    bottom_left: instance of Widget
    bottom_right: instance of Widget
        widgets to fill the positions in the layout

    merge: bool
        flag to say whether the empty positions should be automatically merged

    {style_params}

    Examples
    --------

    >>> from ipywidgets import TwoByTwoLayout, Button
    >>> TwoByTwoLayout(top_left=Button(description="Top left"),
    ...                top_right=Button(description="Top right"),
    ...                bottom_left=Button(description="Bottom left"),
    ...                bottom_right=Button(description="Bottom right"))

    '''
    top_left: Incomplete
    top_right: Incomplete
    bottom_left: Incomplete
    bottom_right: Incomplete
    merge: Incomplete
    def __init__(self, **kwargs) -> None: ...
