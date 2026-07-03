from . import cbook as cbook
from ._enums import CapStyle as CapStyle, JoinStyle as JoinStyle
from .path import Path as Path
from .transforms import Affine2D as Affine2D, IdentityTransform as IdentityTransform
from _typeshed import Incomplete

TICKLEFT: Incomplete
TICKRIGHT: Incomplete
TICKUP: Incomplete
TICKDOWN: Incomplete
CARETLEFT: Incomplete
CARETRIGHT: Incomplete
CARETUP: Incomplete
CARETDOWN: Incomplete
CARETLEFTBASE: Incomplete
CARETRIGHTBASE: Incomplete
CARETUPBASE: Incomplete
CARETDOWNBASE: Incomplete

class MarkerStyle:
    """
    A class representing marker types.

    Instances are immutable. If you need to change anything, create a new
    instance.

    Attributes
    ----------
    markers : list
        All known markers.
    filled_markers : list
        All known filled markers. This is a subset of *markers*.
    fillstyles : list
        The supported fillstyles.
    """
    markers: Incomplete
    filled_markers: Incomplete
    fillstyles: Incomplete
    def __init__(self, marker=..., fillstyle: Incomplete | None = None, transform: Incomplete | None = None, capstyle: Incomplete | None = None, joinstyle: Incomplete | None = None) -> None:
        """
        Parameters
        ----------
        marker : str, array-like, Path, MarkerStyle, or None
            - Another instance of *MarkerStyle* copies the details of that
              ``marker``.
            - *None* means no marker.  This is the deprecated default.
            - For other possible marker values, see the module docstring
              `matplotlib.markers`.

        fillstyle : str, default: :rc:`markers.fillstyle`
            One of 'full', 'left', 'right', 'bottom', 'top', 'none'.

        transform : transforms.Transform, default: None
            Transform that will be combined with the native transform of the
            marker.

        capstyle : CapStyle, default: None
            Cap style that will override the default cap style of the marker.

        joinstyle : JoinStyle, default: None
            Join style that will override the default join style of the marker.
        """
    def __bool__(self) -> bool: ...
    def is_filled(self): ...
    def get_fillstyle(self): ...
    def get_joinstyle(self): ...
    def get_capstyle(self): ...
    def get_marker(self): ...
    def get_path(self):
        """
        Return a `.Path` for the primary part of the marker.

        For unfilled markers this is the whole marker, for filled markers,
        this is the area to be drawn with *markerfacecolor*.
        """
    def get_transform(self):
        """
        Return the transform to be applied to the `.Path` from
        `MarkerStyle.get_path()`.
        """
    def get_alt_path(self):
        """
        Return a `.Path` for the alternate part of the marker.

        For unfilled markers, this is *None*; for filled markers, this is the
        area to be drawn with *markerfacecoloralt*.
        """
    def get_alt_transform(self):
        """
        Return the transform to be applied to the `.Path` from
        `MarkerStyle.get_alt_path()`.
        """
    def get_snap_threshold(self): ...
    def get_user_transform(self):
        """Return user supplied part of marker transform."""
    def transformed(self, transform: Affine2D):
        """
        Return a new version of this marker with the transform applied.

        Parameters
        ----------
        transform : Affine2D, default: None
            Transform will be combined with current user supplied transform.
        """
    def rotated(self, *, deg: Incomplete | None = None, rad: Incomplete | None = None):
        """
        Return a new version of this marker rotated by specified angle.

        Parameters
        ----------
        deg : float, default: None
            Rotation angle in degrees.

        rad : float, default: None
            Rotation angle in radians.

        .. note:: You must specify exactly one of deg or rad.
        """
    def scaled(self, sx, sy: Incomplete | None = None):
        """
        Return new marker scaled by specified scale factors.

        If *sy* is None, the same scale is applied in both the *x*- and
        *y*-directions.

        Parameters
        ----------
        sx : float
            *X*-direction scaling factor.
        sy : float, default: None
            *Y*-direction scaling factor.
        """
