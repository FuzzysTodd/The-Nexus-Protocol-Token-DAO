import _plotly_utils.basevalidators

class UsecolormapValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'usecolormap', parent_name: str = 'surface.contours.x', **kwargs) -> None: ...
