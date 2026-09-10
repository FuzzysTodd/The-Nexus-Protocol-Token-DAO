import _plotly_utils.basevalidators

class OhlcValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'ohlc', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
