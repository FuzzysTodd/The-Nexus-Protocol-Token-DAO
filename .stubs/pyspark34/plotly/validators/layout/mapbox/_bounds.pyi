import _plotly_utils.basevalidators

class BoundsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'bounds', parent_name: str = 'layout.mapbox', **kwargs) -> None: ...
