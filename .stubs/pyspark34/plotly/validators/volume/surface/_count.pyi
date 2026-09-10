import _plotly_utils.basevalidators

class CountValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name: str = 'count', parent_name: str = 'volume.surface', **kwargs) -> None: ...
