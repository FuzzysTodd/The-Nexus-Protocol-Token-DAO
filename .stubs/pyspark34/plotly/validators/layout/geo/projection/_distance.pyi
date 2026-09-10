import _plotly_utils.basevalidators

class DistanceValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'distance', parent_name: str = 'layout.geo.projection', **kwargs) -> None: ...
