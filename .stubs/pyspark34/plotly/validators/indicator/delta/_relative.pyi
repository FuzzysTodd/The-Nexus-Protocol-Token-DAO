import _plotly_utils.basevalidators

class RelativeValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'relative', parent_name: str = 'indicator.delta', **kwargs) -> None: ...
