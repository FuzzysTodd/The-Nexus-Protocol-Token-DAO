import _plotly_utils.basevalidators

class YValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'y', parent_name: str = 'surface.contours.z.project', **kwargs) -> None: ...
