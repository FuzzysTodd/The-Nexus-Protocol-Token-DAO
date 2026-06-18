import _plotly_utils.basevalidators

class NodeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'node', parent_name: str = 'sankey', **kwargs) -> None: ...
