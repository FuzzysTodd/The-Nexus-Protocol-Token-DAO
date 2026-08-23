import _plotly_utils.basevalidators

class MapboxValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'mapbox', parent_name: str = 'layout', **kwargs) -> None: ...
