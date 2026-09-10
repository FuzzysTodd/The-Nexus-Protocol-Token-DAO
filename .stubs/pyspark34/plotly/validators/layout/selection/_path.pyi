import _plotly_utils.basevalidators

class PathValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name: str = 'path', parent_name: str = 'layout.selection', **kwargs) -> None: ...
