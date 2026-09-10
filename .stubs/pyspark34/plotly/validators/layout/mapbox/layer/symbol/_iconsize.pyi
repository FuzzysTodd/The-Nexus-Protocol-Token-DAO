import _plotly_utils.basevalidators

class IconsizeValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'iconsize', parent_name: str = 'layout.mapbox.layer.symbol', **kwargs) -> None: ...
