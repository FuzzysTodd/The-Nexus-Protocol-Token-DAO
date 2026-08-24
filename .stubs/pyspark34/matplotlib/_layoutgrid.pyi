from _typeshed import Incomplete
from matplotlib.transforms import Bbox as Bbox

class LayoutGrid:
    """
    Analogous to a gridspec, and contained in another LayoutGrid.
    """
    parent_pos: Incomplete
    parent_inner: Incomplete
    name: Incomplete
    nrows: Incomplete
    ncols: Incomplete
    height_ratios: Incomplete
    width_ratios: Incomplete
    solver: Incomplete
    artists: Incomplete
    children: Incomplete
    margins: Incomplete
    margin_vals: Incomplete
    lefts: Incomplete
    rights: Incomplete
    bottoms: Incomplete
    tops: Incomplete
    h_pad: Incomplete
    w_pad: Incomplete
    def __init__(self, parent: Incomplete | None = None, parent_pos=(0, 0), parent_inner: bool = False, name: str = '', ncols: int = 1, nrows: int = 1, h_pad: Incomplete | None = None, w_pad: Incomplete | None = None, width_ratios: Incomplete | None = None, height_ratios: Incomplete | None = None) -> None: ...
    def reset_margins(self) -> None:
        """
        Reset all the margins to zero.  Must do this after changing
        figure size, for instance, because the relative size of the
        axes labels etc changes.
        """
    def add_constraints(self, parent) -> None: ...
    def hard_constraints(self) -> None:
        """
        These are the redundant constraints, plus ones that make the
        rest of the code easier.
        """
    def add_child(self, child, i: int = 0, j: int = 0) -> None: ...
    def parent_constraints(self, parent) -> None: ...
    def grid_constraints(self) -> None: ...
    def edit_margin(self, todo, size, cell) -> None:
        """
        Change the size of the margin for one cell.

        Parameters
        ----------
        todo : string (one of 'left', 'right', 'bottom', 'top')
            margin to alter.

        size : float
            Size of the margin.  If it is larger than the existing minimum it
            updates the margin size. Fraction of figure size.

        cell : int
            Cell column or row to edit.
        """
    def edit_margin_min(self, todo, size, cell: int = 0) -> None:
        """
        Change the minimum size of the margin for one cell.

        Parameters
        ----------
        todo : string (one of 'left', 'right', 'bottom', 'top')
            margin to alter.

        size : float
            Minimum size of the margin .  If it is larger than the
            existing minimum it updates the margin size. Fraction of
            figure size.

        cell : int
            Cell column or row to edit.
        """
    def edit_margins(self, todo, size) -> None:
        """
        Change the size of all the margin of all the cells in the layout grid.

        Parameters
        ----------
        todo : string (one of 'left', 'right', 'bottom', 'top')
            margin to alter.

        size : float
            Size to set the margins.  Fraction of figure size.
        """
    def edit_all_margins_min(self, todo, size) -> None:
        """
        Change the minimum size of all the margin of all
        the cells in the layout grid.

        Parameters
        ----------
        todo : {'left', 'right', 'bottom', 'top'}
            The margin to alter.

        size : float
            Minimum size of the margin.  If it is larger than the
            existing minimum it updates the margin size. Fraction of
            figure size.
        """
    def edit_outer_margin_mins(self, margin, ss) -> None:
        """
        Edit all four margin minimums in one statement.

        Parameters
        ----------
        margin : dict
            size of margins in a dict with keys 'left', 'right', 'bottom',
            'top'

        ss : SubplotSpec
            defines the subplotspec these margins should be applied to
        """
    def get_margins(self, todo, col):
        """Return the margin at this position"""
    def get_outer_bbox(self, rows: int = 0, cols: int = 0):
        """
        Return the outer bounding box of the subplot specs
        given by rows and cols.  rows and cols can be spans.
        """
    def get_inner_bbox(self, rows: int = 0, cols: int = 0):
        """
        Return the inner bounding box of the subplot specs
        given by rows and cols.  rows and cols can be spans.
        """
    def get_bbox_for_cb(self, rows: int = 0, cols: int = 0):
        """
        Return the bounding box that includes the
        decorations but, *not* the colorbar...
        """
    def get_left_margin_bbox(self, rows: int = 0, cols: int = 0):
        """
        Return the left margin bounding box of the subplot specs
        given by rows and cols.  rows and cols can be spans.
        """
    def get_bottom_margin_bbox(self, rows: int = 0, cols: int = 0):
        """
        Return the left margin bounding box of the subplot specs
        given by rows and cols.  rows and cols can be spans.
        """
    def get_right_margin_bbox(self, rows: int = 0, cols: int = 0):
        """
        Return the left margin bounding box of the subplot specs
        given by rows and cols.  rows and cols can be spans.
        """
    def get_top_margin_bbox(self, rows: int = 0, cols: int = 0):
        """
        Return the left margin bounding box of the subplot specs
        given by rows and cols.  rows and cols can be spans.
        """
    def update_variables(self) -> None:
        """
        Update the variables for the solver attached to this layoutgrid.
        """

def seq_id():
    """Generate a short sequential id for layoutbox objects."""
def plot_children(fig, lg: Incomplete | None = None, level: int = 0) -> None:
    """Simple plotting to show where boxes are."""
