import _plotly_utils.basevalidators

class TokenValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'token', parent_name: str = 'ohlc.stream', **kwargs) -> None: ...
