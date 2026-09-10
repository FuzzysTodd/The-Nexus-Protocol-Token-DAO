import _plotly_utils.basevalidators

class BaseframeValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'baseframe', parent_name: str = 'frame', **kwargs) -> None: ...
