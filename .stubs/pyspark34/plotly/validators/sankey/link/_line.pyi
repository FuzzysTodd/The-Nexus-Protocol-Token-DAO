import _plotly_utils.basevalidators

class LineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'line', parent_name: str = 'sankey.link', **kwargs) -> None: ...
