import _plotly_utils.basevalidators

class ShowactiveValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'showactive', parent_name: str = 'layout.updatemenu', **kwargs) -> None: ...
