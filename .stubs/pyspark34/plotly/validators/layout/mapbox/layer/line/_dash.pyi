import _plotly_utils.basevalidators

class DashValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name: str = 'dash', parent_name: str = 'layout.mapbox.layer.line', **kwargs) -> None: ...
