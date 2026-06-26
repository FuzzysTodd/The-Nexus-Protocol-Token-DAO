import _plotly_utils.basevalidators

class YpadValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'ypad', parent_name: str = 'histogram.marker.colorbar', **kwargs) -> None: ...
