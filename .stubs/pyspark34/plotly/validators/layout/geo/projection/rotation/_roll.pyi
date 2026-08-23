import _plotly_utils.basevalidators

class RollValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'roll', parent_name: str = 'layout.geo.projection.rotation', **kwargs) -> None: ...
