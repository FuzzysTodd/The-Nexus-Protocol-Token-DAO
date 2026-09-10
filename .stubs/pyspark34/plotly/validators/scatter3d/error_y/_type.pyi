import _plotly_utils.basevalidators

class TypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'type', parent_name: str = 'scatter3d.error_y', **kwargs) -> None: ...
