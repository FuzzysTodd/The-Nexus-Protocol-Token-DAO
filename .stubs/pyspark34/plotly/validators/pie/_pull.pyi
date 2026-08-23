import _plotly_utils.basevalidators

class PullValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'pull', parent_name: str = 'pie', **kwargs) -> None: ...
