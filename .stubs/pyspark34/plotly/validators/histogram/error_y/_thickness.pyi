import _plotly_utils.basevalidators

class ThicknessValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'thickness', parent_name: str = 'histogram.error_y', **kwargs) -> None: ...
