import _plotly_utils.basevalidators

class CountsValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'counts', parent_name: str = 'parcats', **kwargs) -> None: ...
