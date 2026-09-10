import _plotly_utils.basevalidators

class XanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'xanchor', parent_name: str = 'scatter.marker.colorbar', **kwargs) -> None: ...
