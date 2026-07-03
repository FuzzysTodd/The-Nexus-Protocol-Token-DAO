import _plotly_utils.basevalidators

class DxValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'dx', parent_name: str = 'heatmapgl', **kwargs) -> None: ...
