import _plotly_utils.basevalidators

class RotationValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'rotation', parent_name: str = 'layout.geo.projection', **kwargs) -> None: ...
