import _plotly_utils.basevalidators

class LonValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'lon', parent_name: str = 'layout.mapbox.center', **kwargs) -> None: ...
