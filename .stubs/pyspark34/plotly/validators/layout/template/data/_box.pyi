import _plotly_utils.basevalidators

class BoxValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'box', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
