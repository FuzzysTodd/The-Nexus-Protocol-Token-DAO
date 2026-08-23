import _plotly_utils.basevalidators

class OpenValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name: str = 'open', parent_name: str = 'ohlc', **kwargs) -> None: ...
