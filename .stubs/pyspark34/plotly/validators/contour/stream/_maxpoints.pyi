import _plotly_utils.basevalidators

class MaxpointsValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'maxpoints', parent_name: str = 'contour.stream', **kwargs) -> None: ...
