import _plotly_utils.basevalidators

class LatValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'lat', parent_name: str = 'layout.mapbox.center', **kwargs) -> None: ...
