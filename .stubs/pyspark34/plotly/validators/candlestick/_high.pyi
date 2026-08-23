import _plotly_utils.basevalidators

class HighValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name: str = 'high', parent_name: str = 'candlestick', **kwargs) -> None: ...
