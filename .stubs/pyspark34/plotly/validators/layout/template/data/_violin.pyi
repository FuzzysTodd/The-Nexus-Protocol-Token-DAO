import _plotly_utils.basevalidators

class ViolinValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'violin', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
