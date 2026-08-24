import _plotly_utils.basevalidators

class PointsValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'points', parent_name: str = 'violin', **kwargs) -> None: ...
