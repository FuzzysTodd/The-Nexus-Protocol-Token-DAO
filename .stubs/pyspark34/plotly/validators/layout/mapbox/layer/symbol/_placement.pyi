import _plotly_utils.basevalidators

class PlacementValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'placement', parent_name: str = 'layout.mapbox.layer.symbol', **kwargs) -> None: ...
