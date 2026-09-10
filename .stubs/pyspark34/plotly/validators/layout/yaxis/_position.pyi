import _plotly_utils.basevalidators

class PositionValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'position', parent_name: str = 'layout.yaxis', **kwargs) -> None: ...
