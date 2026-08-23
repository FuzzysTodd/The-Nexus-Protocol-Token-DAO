import _plotly_utils.basevalidators

class NorthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'north', parent_name: str = 'layout.mapbox.bounds', **kwargs) -> None: ...
