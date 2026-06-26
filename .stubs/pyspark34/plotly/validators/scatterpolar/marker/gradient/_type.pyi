import _plotly_utils.basevalidators

class TypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'type', parent_name: str = 'scatterpolar.marker.gradient', **kwargs) -> None: ...
