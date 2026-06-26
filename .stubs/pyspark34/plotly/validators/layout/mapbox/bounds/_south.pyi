import _plotly_utils.basevalidators

class SouthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'south', parent_name: str = 'layout.mapbox.bounds', **kwargs) -> None: ...
