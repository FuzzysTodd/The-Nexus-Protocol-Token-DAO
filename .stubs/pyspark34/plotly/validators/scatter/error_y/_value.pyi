import _plotly_utils.basevalidators

class ValueValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'value', parent_name: str = 'scatter.error_y', **kwargs) -> None: ...
