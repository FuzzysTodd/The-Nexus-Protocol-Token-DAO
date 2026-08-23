import _plotly_utils.basevalidators

class RotationValidator(_plotly_utils.basevalidators.AngleValidator):
    def __init__(self, plotly_name: str = 'rotation', parent_name: str = 'layout.polar.angularaxis', **kwargs) -> None: ...
