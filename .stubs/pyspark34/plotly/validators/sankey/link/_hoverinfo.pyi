import _plotly_utils.basevalidators

class HoverinfoValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'hoverinfo', parent_name: str = 'sankey.link', **kwargs) -> None: ...
