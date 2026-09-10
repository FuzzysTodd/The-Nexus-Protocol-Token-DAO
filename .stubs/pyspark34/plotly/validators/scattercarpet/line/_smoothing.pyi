import _plotly_utils.basevalidators

class SmoothingValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'smoothing', parent_name: str = 'scattercarpet.line', **kwargs) -> None: ...
