import _plotly_utils.basevalidators

class CumulativeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'cumulative', parent_name: str = 'histogram', **kwargs) -> None: ...
