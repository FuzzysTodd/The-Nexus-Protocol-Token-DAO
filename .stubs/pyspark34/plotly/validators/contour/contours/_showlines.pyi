import _plotly_utils.basevalidators

class ShowlinesValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showlines', parent_name: str = 'contour.contours', **kwargs) -> None: ...
