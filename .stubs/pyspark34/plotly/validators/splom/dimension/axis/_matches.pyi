import _plotly_utils.basevalidators

class MatchesValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name: str = 'matches', parent_name: str = 'splom.dimension.axis', **kwargs) -> None: ...
