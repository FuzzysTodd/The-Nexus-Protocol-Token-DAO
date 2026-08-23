import _plotly_utils.basevalidators

class WestValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'west', parent_name: str = 'layout.mapbox.bounds', **kwargs) -> None: ...
