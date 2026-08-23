import _plotly_utils.basevalidators

class SplitValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'split', parent_name: str = 'ohlc.hoverlabel', **kwargs) -> None: ...
