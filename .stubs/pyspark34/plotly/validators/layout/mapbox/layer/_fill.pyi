import _plotly_utils.basevalidators

class FillValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'fill', parent_name: str = 'layout.mapbox.layer', **kwargs) -> None: ...
