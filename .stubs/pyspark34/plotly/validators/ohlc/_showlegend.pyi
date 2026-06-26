import _plotly_utils.basevalidators

class ShowlegendValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showlegend', parent_name: str = 'ohlc', **kwargs) -> None: ...
