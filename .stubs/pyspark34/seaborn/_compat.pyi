from _typeshed import Incomplete
from seaborn.external.version import Version as Version

def MarkerStyle(marker: Incomplete | None = None, fillstyle: Incomplete | None = None):
    """
    Allow MarkerStyle to accept a MarkerStyle object as parameter.

    Supports matplotlib < 3.3.0
    https://github.com/matplotlib/matplotlib/pull/16692

    """
def norm_from_scale(scale, norm):
    """Produce a Normalize object given a Scale and min/max domain limits."""
def scale_factory(scale, axis, **kwargs):
    """
    Backwards compatability for creation of independent scales.

    Matplotlib scales require an Axis object for instantiation on < 3.4.
    But the axis is not used, aside from extraction of the axis_name in LogScale.

    """
def set_scale_obj(ax, axis, scale) -> None:
    """Handle backwards compatability with setting matplotlib scale."""
def get_colormap(name):
    """Handle changes to matplotlib colormap interface in 3.6."""
def register_colormap(name, cmap) -> None:
    """Handle changes to matplotlib colormap interface in 3.6."""
def set_layout_engine(fig, engine) -> None:
    """Handle changes to auto layout engine interface in 3.6"""
def share_axis(ax0, ax1, which) -> None:
    """Handle changes to post-hoc axis sharing."""
