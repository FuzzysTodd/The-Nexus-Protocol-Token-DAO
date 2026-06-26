import _plotly_utils.basevalidators

class StartValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'start', parent_name: str = 'surface.contours.y', **kwargs) -> None: ...
