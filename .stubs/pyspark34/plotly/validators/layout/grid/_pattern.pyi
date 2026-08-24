import _plotly_utils.basevalidators

class PatternValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'pattern', parent_name: str = 'layout.grid', **kwargs) -> None: ...
