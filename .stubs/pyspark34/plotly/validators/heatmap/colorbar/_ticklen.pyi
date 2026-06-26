import _plotly_utils.basevalidators

class TicklenValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'ticklen', parent_name: str = 'heatmap.colorbar', **kwargs) -> None: ...
