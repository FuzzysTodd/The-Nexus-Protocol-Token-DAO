import _plotly_utils.basevalidators

class CategoryorderValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'categoryorder', parent_name: str = 'layout.xaxis', **kwargs) -> None: ...
