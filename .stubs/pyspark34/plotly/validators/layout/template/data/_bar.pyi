import _plotly_utils.basevalidators

class BarValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'bar', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
