import _plotly_utils.basevalidators

class TiltValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'tilt', parent_name: str = 'layout.geo.projection', **kwargs) -> None: ...
