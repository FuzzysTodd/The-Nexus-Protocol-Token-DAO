import _plotly_utils.basevalidators

class DecreasingValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'decreasing', parent_name: str = 'ohlc', **kwargs) -> None: ...
