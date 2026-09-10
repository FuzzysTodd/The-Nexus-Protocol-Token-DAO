import _plotly_utils.basevalidators

class MinzoomValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'minzoom', parent_name: str = 'layout.mapbox.layer', **kwargs) -> None: ...
