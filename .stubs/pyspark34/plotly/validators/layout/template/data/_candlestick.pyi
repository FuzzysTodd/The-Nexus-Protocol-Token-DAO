import _plotly_utils.basevalidators

class CandlestickValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'candlestick', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
