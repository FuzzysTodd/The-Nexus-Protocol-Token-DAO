import _plotly_utils.basevalidators

class BaseValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'base', parent_name: str = 'waterfall', **kwargs) -> None: ...
