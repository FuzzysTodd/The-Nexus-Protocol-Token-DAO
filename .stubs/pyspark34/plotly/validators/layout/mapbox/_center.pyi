import _plotly_utils.basevalidators

class CenterValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'center', parent_name: str = 'layout.mapbox', **kwargs) -> None: ...
