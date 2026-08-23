import _plotly_utils.basevalidators

class BaseValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'base', parent_name: str = 'barpolar', **kwargs) -> None: ...
