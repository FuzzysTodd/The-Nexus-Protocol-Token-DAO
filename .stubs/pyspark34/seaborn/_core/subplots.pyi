from _typeshed import Incomplete
from collections.abc import Generator
from matplotlib.axes import Axes as Axes
from matplotlib.figure import Figure as Figure, SubFigure as SubFigure
from seaborn._core.plot import FacetSpec as FacetSpec, PairSpec as PairSpec

class Subplots:
    """
    Interface for creating and using matplotlib subplots based on seaborn parameters.

    Parameters
    ----------
    subplot_spec : dict
        Keyword args for :meth:`matplotlib.figure.Figure.subplots`.
    facet_spec : dict
        Parameters that control subplot faceting.
    pair_spec : dict
        Parameters that control subplot pairing.
    data : PlotData
        Data used to define figure setup.

    """
    subplot_spec: Incomplete
    def __init__(self, subplot_spec: dict, facet_spec: FacetSpec, pair_spec: PairSpec) -> None: ...
    def init_figure(self, pair_spec: PairSpec, pyplot: bool = False, figure_kws: dict | None = None, target: Axes | Figure | SubFigure = None) -> Figure:
        """Initialize matplotlib objects and add seaborn-relevant metadata."""
    def __iter__(self) -> Generator[dict, None, None]:
        """Yield each subplot dictionary with Axes object and metadata."""
    def __len__(self) -> int:
        """Return the number of subplots in this figure."""
