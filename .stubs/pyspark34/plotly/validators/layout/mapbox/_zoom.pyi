import _plotly_utils.basevalidators

class ZoomValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'zoom', parent_name: str = 'layout.mapbox', **kwargs) -> None: ...
