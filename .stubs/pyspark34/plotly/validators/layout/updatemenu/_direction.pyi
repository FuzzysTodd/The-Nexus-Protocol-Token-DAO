import _plotly_utils.basevalidators

class DirectionValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name: str = 'direction', parent_name: str = 'layout.updatemenu', **kwargs) -> None: ...
