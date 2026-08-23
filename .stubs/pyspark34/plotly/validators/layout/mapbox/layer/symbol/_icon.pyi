import _plotly_utils.basevalidators

class IconValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'icon', parent_name: str = 'layout.mapbox.layer.symbol', **kwargs) -> None: ...
