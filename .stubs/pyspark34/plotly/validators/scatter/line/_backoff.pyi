import _plotly_utils.basevalidators

class BackoffValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'backoff', parent_name: str = 'scatter.line', **kwargs) -> None: ...
