from _typeshed import Incomplete
from matplotlib.offsetbox import AnchoredOffsetbox

__all__ = ['AnchoredDrawingArea', 'AnchoredAuxTransformBox', 'AnchoredEllipse', 'AnchoredSizeBar', 'AnchoredDirectionArrows']

class AnchoredDrawingArea(AnchoredOffsetbox):
    da: Incomplete
    drawing_area: Incomplete
    def __init__(self, width, height, xdescent, ydescent, loc, pad: float = 0.4, borderpad: float = 0.5, prop: Incomplete | None = None, frameon: bool = True, **kwargs) -> None:
        '''
        An anchored container with a fixed size and fillable `.DrawingArea`.

        Artists added to the *drawing_area* will have their coordinates
        interpreted as pixels. Any transformations set on the artists will be
        overridden.

        Parameters
        ----------
        width, height : float
            Width and height of the container, in pixels.
        xdescent, ydescent : float
            Descent of the container in the x- and y- direction, in pixels.
        loc : str
            Location of this artist.  Valid locations are
            \'upper left\', \'upper center\', \'upper right\',
            \'center left\', \'center\', \'center right\',
            \'lower left\', \'lower center\', \'lower right\'.
            For backward compatibility, numeric values are accepted as well.
            See the parameter *loc* of `.Legend` for details.
        pad : float, default: 0.4
            Padding around the child objects, in fraction of the font size.
        borderpad : float, default: 0.5
            Border padding, in fraction of the font size.
        prop : `~matplotlib.font_manager.FontProperties`, optional
            Font property used as a reference for paddings.
        frameon : bool, default: True
            If True, draw a box around this artist.
        **kwargs
            Keyword arguments forwarded to `.AnchoredOffsetbox`.

        Attributes
        ----------
        drawing_area : `~matplotlib.offsetbox.DrawingArea`
            A container for artists to display.

        Examples
        --------
        To display blue and red circles of different sizes in the upper right
        of an Axes *ax*:

        >>> ada = AnchoredDrawingArea(20, 20, 0, 0,
        ...                           loc=\'upper right\', frameon=False)
        >>> ada.drawing_area.add_artist(Circle((10, 10), 10, fc="b"))
        >>> ada.drawing_area.add_artist(Circle((30, 10), 5, fc="r"))
        >>> ax.add_artist(ada)
        '''

class AnchoredAuxTransformBox(AnchoredOffsetbox):
    drawing_area: Incomplete
    def __init__(self, transform, loc, pad: float = 0.4, borderpad: float = 0.5, prop: Incomplete | None = None, frameon: bool = True, **kwargs) -> None:
        """
        An anchored container with transformed coordinates.

        Artists added to the *drawing_area* are scaled according to the
        coordinates of the transformation used. The dimensions of this artist
        will scale to contain the artists added.

        Parameters
        ----------
        transform : `~matplotlib.transforms.Transform`
            The transformation object for the coordinate system in use, i.e.,
            :attr:`matplotlib.axes.Axes.transData`.
        loc : str
            Location of this artist.  Valid locations are
            'upper left', 'upper center', 'upper right',
            'center left', 'center', 'center right',
            'lower left', 'lower center', 'lower right'.
            For backward compatibility, numeric values are accepted as well.
            See the parameter *loc* of `.Legend` for details.
        pad : float, default: 0.4
            Padding around the child objects, in fraction of the font size.
        borderpad : float, default: 0.5
            Border padding, in fraction of the font size.
        prop : `~matplotlib.font_manager.FontProperties`, optional
            Font property used as a reference for paddings.
        frameon : bool, default: True
            If True, draw a box around this artist.
        **kwargs
            Keyword arguments forwarded to `.AnchoredOffsetbox`.

        Attributes
        ----------
        drawing_area : `~matplotlib.offsetbox.AuxTransformBox`
            A container for artists to display.

        Examples
        --------
        To display an ellipse in the upper left, with a width of 0.1 and
        height of 0.4 in data coordinates:

        >>> box = AnchoredAuxTransformBox(ax.transData, loc='upper left')
        >>> el = Ellipse((0, 0), width=0.1, height=0.4, angle=30)
        >>> box.drawing_area.add_artist(el)
        >>> ax.add_artist(box)
        """

class AnchoredEllipse(AnchoredOffsetbox):
    ellipse: Incomplete
    def __init__(self, transform, width, height, angle, loc, pad: float = 0.1, borderpad: float = 0.1, prop: Incomplete | None = None, frameon: bool = True, **kwargs) -> None:
        """
        Draw an anchored ellipse of a given size.

        Parameters
        ----------
        transform : `~matplotlib.transforms.Transform`
            The transformation object for the coordinate system in use, i.e.,
            :attr:`matplotlib.axes.Axes.transData`.
        width, height : float
            Width and height of the ellipse, given in coordinates of
            *transform*.
        angle : float
            Rotation of the ellipse, in degrees, anti-clockwise.
        loc : str
            Location of the ellipse.  Valid locations are
            'upper left', 'upper center', 'upper right',
            'center left', 'center', 'center right',
            'lower left', 'lower center', 'lower right'.
            For backward compatibility, numeric values are accepted as well.
            See the parameter *loc* of `.Legend` for details.
        pad : float, default: 0.1
            Padding around the ellipse, in fraction of the font size.
        borderpad : float, default: 0.1
            Border padding, in fraction of the font size.
        frameon : bool, default: True
            If True, draw a box around the ellipse.
        prop : `~matplotlib.font_manager.FontProperties`, optional
            Font property used as a reference for paddings.
        **kwargs
            Keyword arguments forwarded to `.AnchoredOffsetbox`.

        Attributes
        ----------
        ellipse : `~matplotlib.patches.Ellipse`
            Ellipse patch drawn.
        """

class AnchoredSizeBar(AnchoredOffsetbox):
    size_bar: Incomplete
    txt_label: Incomplete
    def __init__(self, transform, size, label, loc, pad: float = 0.1, borderpad: float = 0.1, sep: int = 2, frameon: bool = True, size_vertical: int = 0, color: str = 'black', label_top: bool = False, fontproperties: Incomplete | None = None, fill_bar: Incomplete | None = None, **kwargs) -> None:
        """
        Draw a horizontal scale bar with a center-aligned label underneath.

        Parameters
        ----------
        transform : `~matplotlib.transforms.Transform`
            The transformation object for the coordinate system in use, i.e.,
            :attr:`matplotlib.axes.Axes.transData`.
        size : float
            Horizontal length of the size bar, given in coordinates of
            *transform*.
        label : str
            Label to display.
        loc : str
            Location of the size bar.  Valid locations are
            'upper left', 'upper center', 'upper right',
            'center left', 'center', 'center right',
            'lower left', 'lower center', 'lower right'.
            For backward compatibility, numeric values are accepted as well.
            See the parameter *loc* of `.Legend` for details.
        pad : float, default: 0.1
            Padding around the label and size bar, in fraction of the font
            size.
        borderpad : float, default: 0.1
            Border padding, in fraction of the font size.
        sep : float, default: 2
            Separation between the label and the size bar, in points.
        frameon : bool, default: True
            If True, draw a box around the horizontal bar and label.
        size_vertical : float, default: 0
            Vertical length of the size bar, given in coordinates of
            *transform*.
        color : str, default: 'black'
            Color for the size bar and label.
        label_top : bool, default: False
            If True, the label will be over the size bar.
        fontproperties : `~matplotlib.font_manager.FontProperties`, optional
            Font properties for the label text.
        fill_bar : bool, optional
            If True and if *size_vertical* is nonzero, the size bar will
            be filled in with the color specified by the size bar.
            Defaults to True if *size_vertical* is greater than
            zero and False otherwise.
        **kwargs
            Keyword arguments forwarded to `.AnchoredOffsetbox`.

        Attributes
        ----------
        size_bar : `~matplotlib.offsetbox.AuxTransformBox`
            Container for the size bar.
        txt_label : `~matplotlib.offsetbox.TextArea`
            Container for the label of the size bar.

        Notes
        -----
        If *prop* is passed as a keyword argument, but *fontproperties* is
        not, then *prop* is assumed to be the intended *fontproperties*.
        Using both *prop* and *fontproperties* is not supported.

        Examples
        --------
        >>> import matplotlib.pyplot as plt
        >>> import numpy as np
        >>> from mpl_toolkits.axes_grid1.anchored_artists import (
        ...     AnchoredSizeBar)
        >>> fig, ax = plt.subplots()
        >>> ax.imshow(np.random.random((10, 10)))
        >>> bar = AnchoredSizeBar(ax.transData, 3, '3 data units', 4)
        >>> ax.add_artist(bar)
        >>> fig.show()

        Using all the optional parameters

        >>> import matplotlib.font_manager as fm
        >>> fontprops = fm.FontProperties(size=14, family='monospace')
        >>> bar = AnchoredSizeBar(ax.transData, 3, '3 units', 4, pad=0.5,
        ...                       sep=5, borderpad=0.5, frameon=False,
        ...                       size_vertical=0.5, color='white',
        ...                       fontproperties=fontprops)
        """

class AnchoredDirectionArrows(AnchoredOffsetbox):
    box: Incomplete
    arrow_x: Incomplete
    arrow_y: Incomplete
    p_x: Incomplete
    p_y: Incomplete
    def __init__(self, transform, label_x, label_y, length: float = 0.15, fontsize: float = 0.08, loc: str = 'upper left', angle: int = 0, aspect_ratio: int = 1, pad: float = 0.4, borderpad: float = 0.4, frameon: bool = False, color: str = 'w', alpha: int = 1, sep_x: float = 0.01, sep_y: int = 0, fontproperties: Incomplete | None = None, back_length: float = 0.15, head_width: int = 10, head_length: int = 15, tail_width: int = 2, text_props: Incomplete | None = None, arrow_props: Incomplete | None = None, **kwargs) -> None:
        """
        Draw two perpendicular arrows to indicate directions.

        Parameters
        ----------
        transform : `~matplotlib.transforms.Transform`
            The transformation object for the coordinate system in use, i.e.,
            :attr:`matplotlib.axes.Axes.transAxes`.
        label_x, label_y : str
            Label text for the x and y arrows
        length : float, default: 0.15
            Length of the arrow, given in coordinates of *transform*.
        fontsize : float, default: 0.08
            Size of label strings, given in coordinates of *transform*.
        loc : str, default: 'upper left'
            Location of the arrow.  Valid locations are
            'upper left', 'upper center', 'upper right',
            'center left', 'center', 'center right',
            'lower left', 'lower center', 'lower right'.
            For backward compatibility, numeric values are accepted as well.
            See the parameter *loc* of `.Legend` for details.
        angle : float, default: 0
            The angle of the arrows in degrees.
        aspect_ratio : float, default: 1
            The ratio of the length of arrow_x and arrow_y.
            Negative numbers can be used to change the direction.
        pad : float, default: 0.4
            Padding around the labels and arrows, in fraction of the font size.
        borderpad : float, default: 0.4
            Border padding, in fraction of the font size.
        frameon : bool, default: False
            If True, draw a box around the arrows and labels.
        color : str, default: 'white'
            Color for the arrows and labels.
        alpha : float, default: 1
            Alpha values of the arrows and labels
        sep_x, sep_y : float, default: 0.01 and 0 respectively
            Separation between the arrows and labels in coordinates of
            *transform*.
        fontproperties : `~matplotlib.font_manager.FontProperties`, optional
            Font properties for the label text.
        back_length : float, default: 0.15
            Fraction of the arrow behind the arrow crossing.
        head_width : float, default: 10
            Width of arrow head, sent to `.ArrowStyle`.
        head_length : float, default: 15
            Length of arrow head, sent to `.ArrowStyle`.
        tail_width : float, default: 2
            Width of arrow tail, sent to `.ArrowStyle`.
        text_props, arrow_props : dict
            Properties of the text and arrows, passed to `.TextPath` and
            `.FancyArrowPatch`.
        **kwargs
            Keyword arguments forwarded to `.AnchoredOffsetbox`.

        Attributes
        ----------
        arrow_x, arrow_y : `~matplotlib.patches.FancyArrowPatch`
            Arrow x and y
        text_path_x, text_path_y : `~matplotlib.text.TextPath`
            Path for arrow labels
        p_x, p_y : `~matplotlib.patches.PathPatch`
            Patch for arrow labels
        box : `~matplotlib.offsetbox.AuxTransformBox`
            Container for the arrows and labels.

        Notes
        -----
        If *prop* is passed as a keyword argument, but *fontproperties* is
        not, then *prop* is assumed to be the intended *fontproperties*.
        Using both *prop* and *fontproperties* is not supported.

        Examples
        --------
        >>> import matplotlib.pyplot as plt
        >>> import numpy as np
        >>> from mpl_toolkits.axes_grid1.anchored_artists import (
        ...     AnchoredDirectionArrows)
        >>> fig, ax = plt.subplots()
        >>> ax.imshow(np.random.random((10, 10)))
        >>> arrows = AnchoredDirectionArrows(ax.transAxes, '111', '110')
        >>> ax.add_artist(arrows)
        >>> fig.show()

        Using several of the optional parameters, creating downward pointing
        arrow and high contrast text labels.

        >>> import matplotlib.font_manager as fm
        >>> fontprops = fm.FontProperties(family='monospace')
        >>> arrows = AnchoredDirectionArrows(ax.transAxes, 'East', 'South',
        ...                                  loc='lower left', color='k',
        ...                                  aspect_ratio=-1, sep_x=0.02,
        ...                                  sep_y=-0.01,
        ...                                  text_props={'ec':'w', 'fc':'k'},
        ...                                  fontproperties=fontprops)
        """
