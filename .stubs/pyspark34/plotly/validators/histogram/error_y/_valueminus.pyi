import _plotly_utils.basevalidators

class ValueminusValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'valueminus', parent_name: str = 'histogram.error_y', **kwargs) -> None: ...
