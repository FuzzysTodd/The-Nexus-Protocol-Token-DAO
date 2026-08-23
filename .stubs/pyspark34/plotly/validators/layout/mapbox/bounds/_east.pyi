import _plotly_utils.basevalidators

class EastValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'east', parent_name: str = 'layout.mapbox.bounds', **kwargs) -> None: ...
