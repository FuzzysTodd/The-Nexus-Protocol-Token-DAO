import _plotly_utils.basevalidators

class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'visible', parent_name: str = 'scatter3d.error_z', **kwargs) -> None: ...
