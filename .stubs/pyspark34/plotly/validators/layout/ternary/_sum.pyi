import _plotly_utils.basevalidators

class SumValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'sum', parent_name: str = 'layout.ternary', **kwargs) -> None: ...
