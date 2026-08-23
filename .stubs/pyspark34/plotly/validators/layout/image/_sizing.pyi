import _plotly_utils.basevalidators

class SizingValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'sizing', parent_name: str = 'layout.image', **kwargs) -> None: ...
