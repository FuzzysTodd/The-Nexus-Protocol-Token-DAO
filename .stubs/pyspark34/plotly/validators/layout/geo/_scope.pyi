import _plotly_utils.basevalidators

class ScopeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'scope', parent_name: str = 'layout.geo', **kwargs) -> None: ...
