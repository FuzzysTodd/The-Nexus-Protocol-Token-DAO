import _plotly_utils.basevalidators

class SelectionsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'selections', parent_name: str = 'layout', **kwargs) -> None: ...
