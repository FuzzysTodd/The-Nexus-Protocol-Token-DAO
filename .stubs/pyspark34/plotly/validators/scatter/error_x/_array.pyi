import _plotly_utils.basevalidators

class ArrayValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name: str = 'array', parent_name: str = 'scatter.error_x', **kwargs) -> None: ...
