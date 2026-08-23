import _plotly_utils.basevalidators

class OhlcValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'ohlc', parent_name: str = '', **kwargs) -> None: ...
