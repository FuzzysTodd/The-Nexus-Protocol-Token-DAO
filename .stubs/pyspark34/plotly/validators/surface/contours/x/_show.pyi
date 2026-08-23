import _plotly_utils.basevalidators

class ShowValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'show', parent_name: str = 'surface.contours.x', **kwargs) -> None: ...
