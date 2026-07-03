import _plotly_utils.basevalidators

class CurrentbinValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'currentbin', parent_name: str = 'histogram.cumulative', **kwargs) -> None: ...
