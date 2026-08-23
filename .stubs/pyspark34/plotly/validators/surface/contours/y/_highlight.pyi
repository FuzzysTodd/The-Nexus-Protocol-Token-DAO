import _plotly_utils.basevalidators

class HighlightValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'highlight', parent_name: str = 'surface.contours.y', **kwargs) -> None: ...
