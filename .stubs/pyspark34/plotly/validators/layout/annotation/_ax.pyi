import _plotly_utils.basevalidators

class AxValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'ax', parent_name: str = 'layout.annotation', **kwargs) -> None: ...
