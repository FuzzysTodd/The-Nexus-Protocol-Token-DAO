import _plotly_utils.basevalidators

class SankeyValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name: str = 'sankey', parent_name: str = 'layout.template.data', **kwargs) -> None: ...
