import _plotly_utils.basevalidators

class OpacityValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'opacity', parent_name: str = 'layout.activeselection', **kwargs) -> None: ...
