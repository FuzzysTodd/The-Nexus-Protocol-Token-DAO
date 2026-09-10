import _plotly_utils.basevalidators

class YValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'y', parent_name: str = 'heatmap.colorbar', **kwargs) -> None: ...
