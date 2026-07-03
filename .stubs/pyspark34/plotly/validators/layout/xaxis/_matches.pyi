import _plotly_utils.basevalidators

class MatchesValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'matches', parent_name: str = 'layout.xaxis', **kwargs) -> None: ...
