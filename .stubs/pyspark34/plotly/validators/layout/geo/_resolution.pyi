import _plotly_utils.basevalidators

class ResolutionValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'resolution', parent_name: str = 'layout.geo', **kwargs) -> None: ...
