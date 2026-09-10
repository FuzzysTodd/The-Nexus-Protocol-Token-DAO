import _plotly_utils.basevalidators

class PositionValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'position', parent_name: str = 'indicator.delta', **kwargs) -> None: ...
