import _plotly_utils.basevalidators

class XValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'x', parent_name: str = 'layout.image', **kwargs) -> None: ...
