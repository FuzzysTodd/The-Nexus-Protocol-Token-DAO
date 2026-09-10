import _plotly_utils.basevalidators

class ShiftValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'shift', parent_name: str = 'layout.yaxis', **kwargs) -> None: ...
