import _plotly_utils.basevalidators

class LayersValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'layers', parent_name: str = 'layout.mapbox', **kwargs) -> None: ...
