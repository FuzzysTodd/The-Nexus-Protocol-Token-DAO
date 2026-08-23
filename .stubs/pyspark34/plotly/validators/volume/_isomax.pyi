import _plotly_utils.basevalidators

class IsomaxValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name: str = 'isomax', parent_name: str = 'volume', **kwargs) -> None: ...
