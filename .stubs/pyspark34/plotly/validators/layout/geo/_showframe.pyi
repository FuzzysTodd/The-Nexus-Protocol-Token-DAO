import _plotly_utils.basevalidators

class ShowframeValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showframe', parent_name: str = 'layout.geo', **kwargs) -> None: ...
