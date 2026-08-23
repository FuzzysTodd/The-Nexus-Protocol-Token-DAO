import _plotly_utils.basevalidators

class AyValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name: str = 'ay', parent_name: str = 'layout.annotation', **kwargs) -> None: ...
