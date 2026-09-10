import _plotly_utils.basevalidators

class OrientationValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'orientation', parent_name: str = 'funnel.marker.colorbar', **kwargs) -> None: ...
