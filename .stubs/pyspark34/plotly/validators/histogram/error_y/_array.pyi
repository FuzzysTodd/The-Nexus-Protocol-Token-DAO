import _plotly_utils.basevalidators

class ArrayValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name: str = 'array', parent_name: str = 'histogram.error_y', **kwargs) -> None: ...
