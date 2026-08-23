import _plotly_utils.basevalidators

class YValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'y', parent_name: str = 'layout.annotation', **kwargs) -> None: ...
