import _plotly_utils.basevalidators

class ComputedValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'computed', parent_name: str = 'layout', **kwargs) -> None: ...
