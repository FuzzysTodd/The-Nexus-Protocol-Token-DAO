import _plotly_utils.basevalidators

class BearingValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'bearing', parent_name: str = 'layout.mapbox', **kwargs) -> None: ...
