import _plotly_utils.basevalidators

class LowValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name: str = 'low', parent_name: str = 'ohlc', **kwargs) -> None: ...
