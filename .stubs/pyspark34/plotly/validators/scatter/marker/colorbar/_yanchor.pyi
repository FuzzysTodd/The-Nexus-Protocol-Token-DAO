import _plotly_utils.basevalidators

class YanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'yanchor', parent_name: str = 'scatter.marker.colorbar', **kwargs) -> None: ...
