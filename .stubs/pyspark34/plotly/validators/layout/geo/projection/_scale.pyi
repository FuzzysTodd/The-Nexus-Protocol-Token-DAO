import _plotly_utils.basevalidators

class ScaleValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'scale', parent_name: str = 'layout.geo.projection', **kwargs) -> None: ...
