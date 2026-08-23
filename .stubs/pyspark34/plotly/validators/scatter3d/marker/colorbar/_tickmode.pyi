import _plotly_utils.basevalidators

class TickmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'tickmode', parent_name: str = 'scatter3d.marker.colorbar', **kwargs) -> None: ...
