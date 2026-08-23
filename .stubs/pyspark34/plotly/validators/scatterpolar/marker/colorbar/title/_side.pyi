import _plotly_utils.basevalidators

class SideValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'side', parent_name: str = 'scatterpolar.marker.colorbar.title', **kwargs) -> None: ...
