import _plotly_utils.basevalidators

class CloseValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name: str = 'close', parent_name: str = 'candlestick', **kwargs) -> None: ...
