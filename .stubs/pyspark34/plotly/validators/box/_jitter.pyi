import _plotly_utils.basevalidators

class JitterValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'jitter', parent_name: str = 'box', **kwargs) -> None: ...
