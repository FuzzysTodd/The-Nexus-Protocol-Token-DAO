import _plotly_utils.basevalidators

class CoordinatesValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'coordinates', parent_name: str = 'layout.mapbox.layer', **kwargs) -> None: ...
