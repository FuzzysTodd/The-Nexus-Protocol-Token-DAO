import _plotly_utils.basevalidators

class XsideValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'xside', parent_name: str = 'layout.grid', **kwargs) -> None: ...
