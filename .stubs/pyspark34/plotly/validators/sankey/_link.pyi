import _plotly_utils.basevalidators

class LinkValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'link', parent_name: str = 'sankey', **kwargs) -> None: ...
