import _plotly_utils.basevalidators

class MaxzoomValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'maxzoom', parent_name: str = 'layout.mapbox.layer', **kwargs) -> None: ...
