import _plotly_utils.basevalidators

class LabelValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name: str = 'label', parent_name: str = 'sankey.node', **kwargs) -> None: ...
