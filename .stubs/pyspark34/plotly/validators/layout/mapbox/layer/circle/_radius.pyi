import _plotly_utils.basevalidators

class RadiusValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'radius', parent_name: str = 'layout.mapbox.layer.circle', **kwargs) -> None: ...
