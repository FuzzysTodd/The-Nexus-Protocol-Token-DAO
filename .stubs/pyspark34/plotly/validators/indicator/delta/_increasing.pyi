import _plotly_utils.basevalidators

class IncreasingValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name: str = 'increasing', parent_name: str = 'indicator.delta', **kwargs) -> None: ...
