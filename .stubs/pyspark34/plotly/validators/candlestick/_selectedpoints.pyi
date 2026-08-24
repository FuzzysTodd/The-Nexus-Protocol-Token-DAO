import _plotly_utils.basevalidators

class SelectedpointsValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'selectedpoints', parent_name: str = 'candlestick', **kwargs) -> None: ...
