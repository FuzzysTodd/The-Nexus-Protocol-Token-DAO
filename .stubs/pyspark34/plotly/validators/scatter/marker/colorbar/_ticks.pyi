import _plotly_utils.basevalidators

class TicksValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'ticks', parent_name: str = 'scatter.marker.colorbar', **kwargs) -> None: ...
