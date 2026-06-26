import _plotly_utils.basevalidators

class MinValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'min', parent_name: str = 'layout.ternary.baxis', **kwargs) -> None: ...
