from .mpl_axes import Axes as Axes
from _typeshed import Incomplete

class ParasiteAxesBase:
    transAux: Incomplete
    def __init__(self, parent_axes, aux_transform: Incomplete | None = None, *, viewlim_mode: Incomplete | None = None, **kwargs) -> None: ...
    def clear(self) -> None: ...
    def pick(self, mouseevent) -> None: ...
    def set_viewlim_mode(self, mode) -> None: ...
    def get_viewlim_mode(self): ...

parasite_axes_class_factory: Incomplete
ParasiteAxes: Incomplete

class HostAxesBase:
    parasites: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def get_aux_axes(self, tr: Incomplete | None = None, viewlim_mode: str = 'equal', axes_class: Incomplete | None = None, **kwargs):
        '''
        Add a parasite axes to this host.

        Despite this method\'s name, this should actually be thought of as an
        ``add_parasite_axes`` method.

        .. versionchanged:: 3.7
           Defaults to same base axes class as host axes.

        Parameters
        ----------
        tr : `~matplotlib.transforms.Transform` or None, default: None
            If a `.Transform`, the following relation will hold:
            ``parasite.transData = tr + host.transData``.
            If None, the parasite\'s and the host\'s ``transData`` are unrelated.
        viewlim_mode : {"equal", "transform", None}, default: "equal"
            How the parasite\'s view limits are set: directly equal to the
            parent axes ("equal"), equal after application of *tr*
            ("transform"), or independently (None).
        axes_class : subclass type of `~matplotlib.axes.Axes`, optional
            The `~.axes.Axes` subclass that is instantiated.  If None, the base
            class of the host axes is used.
        kwargs
            Other parameters are forwarded to the parasite axes constructor.
        '''
    def draw(self, renderer) -> None: ...
    def clear(self) -> None: ...
    def pick(self, mouseevent) -> None: ...
    def twinx(self, axes_class: Incomplete | None = None):
        """
        Create a twin of Axes with a shared x-axis but independent y-axis.

        The y-axis of self will have ticks on the left and the returned axes
        will have ticks on the right.
        """
    def twiny(self, axes_class: Incomplete | None = None):
        """
        Create a twin of Axes with a shared y-axis but independent x-axis.

        The x-axis of self will have ticks on the bottom and the returned axes
        will have ticks on the top.
        """
    def twin(self, aux_trans: Incomplete | None = None, axes_class: Incomplete | None = None):
        """
        Create a twin of Axes with no shared axis.

        While self will have ticks on the left and bottom axis, the returned
        axes will have ticks on the top and right axis.
        """
    def get_tightbbox(self, renderer: Incomplete | None = None, call_axes_locator: bool = True, bbox_extra_artists: Incomplete | None = None): ...

host_axes_class_factory: Incomplete

host_subplot_class_factory: Incomplete
HostAxes: Incomplete
SubplotHost: Incomplete

def host_axes(*args, axes_class=..., figure: Incomplete | None = None, **kwargs):
    """
    Create axes that can act as a hosts to parasitic axes.

    Parameters
    ----------
    figure : `~matplotlib.figure.Figure`
        Figure to which the axes will be added. Defaults to the current figure
        `.pyplot.gcf()`.

    *args, **kwargs
        Will be passed on to the underlying `~.axes.Axes` object creation.
    """
host_subplot = host_axes
