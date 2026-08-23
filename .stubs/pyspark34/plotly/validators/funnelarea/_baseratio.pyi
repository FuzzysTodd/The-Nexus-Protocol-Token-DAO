import _plotly_utils.basevalidators

class BaseratioValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'baseratio', parent_name: str = 'funnelarea', **kwargs) -> None: ...
