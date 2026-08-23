import _plotly_utils.basevalidators

class PaddingValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'padding', parent_name: str = 'layout.shape.label', **kwargs) -> None: ...
