import _plotly_utils.basevalidators

class SimplifyValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'simplify', parent_name: str = 'scatter.line', **kwargs) -> None: ...
