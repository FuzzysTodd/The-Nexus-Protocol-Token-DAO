from . import legend_handler as legend_handler
from _typeshed import Incomplete
from matplotlib import colors as colors, offsetbox as offsetbox
from matplotlib.artist import Artist as Artist, allow_rasterization as allow_rasterization
from matplotlib.cbook import silent_list as silent_list
from matplotlib.collections import CircleCollection as CircleCollection, Collection as Collection, LineCollection as LineCollection, PathCollection as PathCollection, PolyCollection as PolyCollection, RegularPolyCollection as RegularPolyCollection
from matplotlib.container import BarContainer as BarContainer, ErrorbarContainer as ErrorbarContainer, StemContainer as StemContainer
from matplotlib.font_manager import FontProperties as FontProperties
from matplotlib.lines import Line2D as Line2D
from matplotlib.offsetbox import AnchoredOffsetbox as AnchoredOffsetbox, DraggableOffsetBox as DraggableOffsetBox, DrawingArea as DrawingArea, HPacker as HPacker, TextArea as TextArea, VPacker as VPacker
from matplotlib.patches import FancyBboxPatch as FancyBboxPatch, Patch as Patch, Rectangle as Rectangle, Shadow as Shadow, StepPatch as StepPatch
from matplotlib.text import Text as Text
from matplotlib.transforms import Bbox as Bbox, BboxBase as BboxBase, BboxTransformFrom as BboxTransformFrom, BboxTransformTo as BboxTransformTo, TransformedBbox as TransformedBbox

class DraggableLegend(DraggableOffsetBox):
    legend: Incomplete
    def __init__(self, legend, use_blit: bool = False, update: str = 'loc') -> None:
        '''
        Wrapper around a `.Legend` to support mouse dragging.

        Parameters
        ----------
        legend : `.Legend`
            The `.Legend` instance to wrap.
        use_blit : bool, optional
            Use blitting for faster image composition. For details see
            :ref:`func-animation`.
        update : {\'loc\', \'bbox\'}, optional
            If "loc", update the *loc* parameter of the legend upon finalizing.
            If "bbox", update the *bbox_to_anchor* parameter.
        '''
    def finalize_offset(self) -> None: ...

class Legend(Artist):
    """
    Place a legend on the figure/axes.
    """
    codes: Incomplete
    zorder: int
    prop: Incomplete
    texts: Incomplete
    legend_handles: Incomplete
    numpoints: Incomplete
    markerscale: Incomplete
    scatterpoints: Incomplete
    borderpad: Incomplete
    labelspacing: Incomplete
    handlelength: Incomplete
    handleheight: Incomplete
    handletextpad: Incomplete
    borderaxespad: Incomplete
    columnspacing: Incomplete
    shadow: Incomplete
    isaxes: bool
    axes: Incomplete
    parent: Incomplete
    legendPatch: Incomplete
    def __init__(self, parent, handles, labels, loc: Incomplete | None = None, numpoints: Incomplete | None = None, markerscale: Incomplete | None = None, markerfirst: bool = True, reverse: bool = False, scatterpoints: Incomplete | None = None, scatteryoffsets: Incomplete | None = None, prop: Incomplete | None = None, fontsize: Incomplete | None = None, labelcolor: Incomplete | None = None, borderpad: Incomplete | None = None, labelspacing: Incomplete | None = None, handlelength: Incomplete | None = None, handleheight: Incomplete | None = None, handletextpad: Incomplete | None = None, borderaxespad: Incomplete | None = None, columnspacing: Incomplete | None = None, ncols: int = 1, mode: Incomplete | None = None, fancybox: Incomplete | None = None, shadow: Incomplete | None = None, title: Incomplete | None = None, title_fontsize: Incomplete | None = None, framealpha: Incomplete | None = None, edgecolor: Incomplete | None = None, facecolor: Incomplete | None = None, bbox_to_anchor: Incomplete | None = None, bbox_transform: Incomplete | None = None, frameon: Incomplete | None = None, handler_map: Incomplete | None = None, title_fontproperties: Incomplete | None = None, alignment: str = 'center', *, ncol: int = 1, draggable: bool = False) -> None:
        """
        Parameters
        ----------
        parent : `~matplotlib.axes.Axes` or `.Figure`
            The artist that contains the legend.

        handles : list of `.Artist`
            A list of Artists (lines, patches) to be added to the legend.

        labels : list of str
            A list of labels to show next to the artists. The length of handles
            and labels should be the same. If they are not, they are truncated
            to the length of the shorter list.

        Other Parameters
        ----------------
        %(_legend_kw_doc)s

        Attributes
        ----------
        legend_handles
            List of `.Artist` objects added as legend entries.

            .. versionadded:: 3.7
        """
    legendHandles: Incomplete
    def set_ncols(self, ncols) -> None:
        """Set the number of columns."""
    stale: bool
    def draw(self, renderer) -> None: ...
    @classmethod
    def get_default_handler_map(cls):
        """Return the global default handler map, shared by all legends."""
    @classmethod
    def set_default_handler_map(cls, handler_map) -> None:
        """Set the global default handler map, shared by all legends."""
    @classmethod
    def update_default_handler_map(cls, handler_map) -> None:
        """Update the global default handler map, shared by all legends."""
    def get_legend_handler_map(self):
        """Return this legend instance's handler map."""
    @staticmethod
    def get_legend_handler(legend_handler_map, orig_handle):
        """
        Return a legend handler from *legend_handler_map* that
        corresponds to *orig_handler*.

        *legend_handler_map* should be a dictionary object (that is
        returned by the get_legend_handler_map method).

        It first checks if the *orig_handle* itself is a key in the
        *legend_handler_map* and return the associated value.
        Otherwise, it checks for each of the classes in its
        method-resolution-order. If no matching key is found, it
        returns ``None``.
        """
    def get_children(self): ...
    def get_frame(self):
        """Return the `~.patches.Rectangle` used to frame the legend."""
    def get_lines(self):
        """Return the list of `~.lines.Line2D`\\s in the legend."""
    def get_patches(self):
        """Return the list of `~.patches.Patch`\\s in the legend."""
    def get_texts(self):
        """Return the list of `~.text.Text`\\s in the legend."""
    def set_alignment(self, alignment) -> None:
        """
        Set the alignment of the legend title and the box of entries.

        The entries are aligned as a single block, so that markers always
        lined up.

        Parameters
        ----------
        alignment : {'center', 'left', 'right'}.

        """
    def get_alignment(self):
        """Get the alignment value of the legend box"""
    def set_title(self, title, prop: Incomplete | None = None) -> None:
        """
        Set legend title and title style.

        Parameters
        ----------
        title : str
            The legend title.

        prop : `.font_manager.FontProperties` or `str` or `pathlib.Path`
            The font properties of the legend title.
            If a `str`, it is interpreted as a fontconfig pattern parsed by
            `.FontProperties`.  If a `pathlib.Path`, it is interpreted as the
            absolute path to a font file.

        """
    def get_title(self):
        """Return the `.Text` instance for the legend title."""
    def get_window_extent(self, renderer: Incomplete | None = None): ...
    def get_tightbbox(self, renderer: Incomplete | None = None): ...
    def get_frame_on(self):
        """Get whether the legend box patch is drawn."""
    def set_frame_on(self, b) -> None:
        """
        Set whether the legend box patch is drawn.

        Parameters
        ----------
        b : bool
        """
    draw_frame = set_frame_on
    def get_bbox_to_anchor(self):
        """Return the bbox that the legend will be anchored to."""
    def set_bbox_to_anchor(self, bbox, transform: Incomplete | None = None) -> None:
        """
        Set the bbox that the legend will be anchored to.

        Parameters
        ----------
        bbox : `~matplotlib.transforms.BboxBase` or tuple
            The bounding box can be specified in the following ways:

            - A `.BboxBase` instance
            - A tuple of ``(left, bottom, width, height)`` in the given
              transform (normalized axes coordinate if None)
            - A tuple of ``(left, bottom)`` where the width and height will be
              assumed to be zero.
            - *None*, to remove the bbox anchoring, and use the parent bbox.

        transform : `~matplotlib.transforms.Transform`, optional
            A transform to apply to the bounding box. If not specified, this
            will use a transform to the bounding box of the parent.
        """
    def contains(self, event): ...
    def set_draggable(self, state, use_blit: bool = False, update: str = 'loc'):
        """
        Enable or disable mouse dragging support of the legend.

        Parameters
        ----------
        state : bool
            Whether mouse dragging is enabled.
        use_blit : bool, optional
            Use blitting for faster image composition. For details see
            :ref:`func-animation`.
        update : {'loc', 'bbox'}, optional
            The legend parameter to be changed when dragged:

            - 'loc': update the *loc* parameter of the legend
            - 'bbox': update the *bbox_to_anchor* parameter of the legend

        Returns
        -------
        `.DraggableLegend` or *None*
            If *state* is ``True`` this returns the `.DraggableLegend` helper
            instance. Otherwise this returns *None*.
        """
    def get_draggable(self):
        """Return ``True`` if the legend is draggable, ``False`` otherwise."""
