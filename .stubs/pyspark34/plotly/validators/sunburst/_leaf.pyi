import _plotly_utils.basevalidators

class LeafValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'leaf', parent_name: str = 'sunburst', **kwargs) -> None: ...
